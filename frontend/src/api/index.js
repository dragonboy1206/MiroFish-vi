import axios from 'axios'
import i18n from '../i18n'

// 创建axios实例
const service = axios.create({
  baseURL: import.meta.env.VITE_API_BASE_URL || 'http://localhost:5001',
  timeout: 300000, // 5分钟超时（本体生成可能需要较长时间）
  headers: {
    'Content-Type': 'application/json'
  }
})

// 请求拦截器
service.interceptors.request.use(
  config => {
    config.headers['Accept-Language'] = i18n.global.locale.value
    console.log(`[API Request] ${config.method?.toUpperCase()} ${config.url}`)
    return config
  },
  error => {
    console.error('[API Request Error]', error)
    return Promise.reject(error)
  }
)

// 响应拦截器（容错重试机制）
service.interceptors.response.use(
  response => {
    const res = response.data
    console.log(`[API Response] ${response.status} ${response.config.url}`)
    
    // 如果返回的状态码不是success，则抛出错误
    if (!res.success && res.success !== undefined) {
      console.error('[API Error]', res.error || res.message || 'Unknown error')
      return Promise.reject(new Error(res.error || res.message || 'Error'))
    }
    
    return res
  },
  error => {
    console.error('[API Response Error]', error.message)
    
    // 处理超时
    if (error.code === 'ECONNABORTED' && error.message.includes('timeout')) {
      console.error('[API Timeout] Request timeout - server may be processing')
    }
    
    // 处理网络错误
    if (error.message === 'Network Error') {
      console.error('[API Network Error] Possible causes:')
      console.error('  1. Backend server not running')
      console.error('  2. CORS issue')
      console.error('  3. Network connectivity issue')
      console.error('  4. Server crashed')
    }
    
    // 处理连接拒绝
    if (error.message?.includes('ECONNREFUSED')) {
      console.error('[API Connection Refused] Backend server may not be running')
    }
    
    return Promise.reject(error)
  }
)

// 带重试的请求函数
export const requestWithRetry = async (requestFn, maxRetries = 3, delay = 2000) => {
  let lastError = null
  
  for (let i = 0; i < maxRetries; i++) {
    try {
      console.log(`[Retry] Attempt ${i + 1}/${maxRetries}`)
      const result = await requestFn()
      console.log(`[Retry] Success on attempt ${i + 1}`)
      return result
    } catch (error) {
      lastError = error
      console.warn(`[Retry] Attempt ${i + 1} failed: ${error.message}`)
      
      if (i < maxRetries - 1) {
        const waitTime = delay * Math.pow(2, i)
        console.log(`[Retry] Waiting ${waitTime}ms before retry...`)
        await new Promise(resolve => setTimeout(resolve, waitTime))
      }
    }
  }
  
  console.error(`[Retry] All ${maxRetries} attempts failed`)
  throw lastError
}

export default service

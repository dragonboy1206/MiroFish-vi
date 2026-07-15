"""
LLM客户端封装
统一使用OpenAI格式调用
"""

import json
import re
import time
import logging
from typing import Optional, Dict, Any, List
from openai import OpenAI, APIConnectionError, APITimeoutError, RateLimitError

from ..config import Config

logger = logging.getLogger(__name__)


class LLMClient:
    """LLM客户端"""
    
    def __init__(
        self,
        api_key: Optional[str] = None,
        base_url: Optional[str] = None,
        model: Optional[str] = None
    ):
        self.api_key = api_key or Config.LLM_API_KEY
        self.base_url = base_url or Config.LLM_BASE_URL
        self.model = model or Config.LLM_MODEL_NAME
        
        if not self.api_key:
            raise ValueError("LLM_API_KEY 未配置")
        
        logger.info(f"LLM Client initialized: model={self.model}, base_url={self.base_url}")
        
        self.client = OpenAI(
            api_key=self.api_key,
            base_url=self.base_url,
            timeout=120.0,  # 2分钟超时
            max_retries=2   # 自动重试2次
        )
    
    def chat(
        self,
        messages: List[Dict[str, str]],
        temperature: float = 0.7,
        max_tokens: int = 4096,
        response_format: Optional[Dict] = None,
        max_retries: int = 3
    ) -> str:
        """
        发送聊天请求
        
        Args:
            messages: 消息列表
            temperature: 温度参数
            max_tokens: 最大token数
            response_format: 响应格式（如JSON模式）
            max_retries: 最大重试次数
            
        Returns:
            模型响应文本
        """
        kwargs = {
            "model": self.model,
            "messages": messages,
            "temperature": temperature,
            "max_tokens": max_tokens,
        }
        
        if response_format:
            kwargs["response_format"] = response_format
        
        last_error = None
        
        for attempt in range(max_retries):
            try:
                logger.debug(f"LLM request attempt {attempt + 1}/{max_retries}: model={self.model}, messages={len(messages)}")
                response = self.client.chat.completions.create(**kwargs)
                content = response.choices[0].message.content
                logger.debug(f"LLM response: {len(content)} chars")
                # 部分模型（如MiniMax M2.5）会在content中包含<think>思考内容，需要移除
                content = re.sub(r'<think>[\s\S]*?</think>', '', content).strip()
                return content
                
            except APIConnectionError as e:
                last_error = e
                logger.warning(f"LLM connection error (attempt {attempt + 1}/{max_retries}): {str(e)}")
                if attempt < max_retries - 1:
                    wait_time = 2 ** attempt  # Exponential backoff
                    logger.info(f"Waiting {wait_time}s before retry...")
                    time.sleep(wait_time)
                    
            except APITimeoutError as e:
                last_error = e
                logger.warning(f"LLM timeout (attempt {attempt + 1}/{max_retries}): {str(e)}")
                if attempt < max_retries - 1:
                    wait_time = 2 ** attempt
                    logger.info(f"Waiting {wait_time}s before retry...")
                    time.sleep(wait_time)
                    
            except RateLimitError as e:
                last_error = e
                logger.warning(f"LLM rate limit (attempt {attempt + 1}/{max_retries}): {str(e)}")
                if attempt < max_retries - 1:
                    wait_time = 5  # Wait longer for rate limits
                    logger.info(f"Waiting {wait_time}s before retry...")
                    time.sleep(wait_time)
                    
            except Exception as e:
                last_error = e
                logger.error(f"LLM request failed (attempt {attempt + 1}/{max_retries}): {type(e).__name__}: {str(e)}")
                if attempt < max_retries - 1:
                    time.sleep(1)
        
        logger.error(f"LLM request failed after {max_retries} attempts")
        raise last_error
    
    def chat_json(
        self,
        messages: List[Dict[str, str]],
        temperature: float = 0.3,
        max_tokens: int = 4096
    ) -> Dict[str, Any]:
        """
        发送聊天请求并返回JSON
        
        Args:
            messages: 消息列表
            temperature: 温度参数
            max_tokens: 最大token数
            
        Returns:
            解析后的JSON对象
        """
        response = self.chat(
            messages=messages,
            temperature=temperature,
            max_tokens=max_tokens,
            response_format={"type": "json_object"}
        )
        # 清理markdown代码块标记
        cleaned_response = response.strip()
        cleaned_response = re.sub(r'^```(?:json)?\s*\n?', '', cleaned_response, flags=re.IGNORECASE)
        cleaned_response = re.sub(r'\n?```\s*$', '', cleaned_response)
        cleaned_response = cleaned_response.strip()

        try:
            return json.loads(cleaned_response)
        except json.JSONDecodeError:
            raise ValueError(f"LLM返回的JSON格式无效: {cleaned_response}")


<div align="center">

<img src="./static/image/MiroFish_logo_compressed.jpeg" alt="MiroFish Logo" width="75%"/>

Công cụ trí tuệ tập thể gọn nhẹ & đa năng, Dự đoán mọi thứ
</br>
<em>A Simple and Universal Swarm Intelligence Engine, Predicting Anything</em>

[![GitHub Stars](https://img.shields.io/github/stars/dragonboy1206/MiroFish-vi?style=flat-square&color=DAA520)](https://github.com/dragonboy1206/MiroFish-vi/stargazers)
[![GitHub Watchers](https://img.shields.io/github/watchers/dragonboy1206/MiroFish-vi?style=flat-square)](https://github.com/dragonboy1206/MiroFish-vi/watchers)
[![GitHub Forks](https://img.shields.io/github/forks/dragonboy1206/MiroFish-vi?style=flat-square)](https://github.com/dragonboy1206/MiroFish-vi/network)
[![Docker](https://img.shields.io/badge/Docker-Build-2496ED?style=flat-square&logo=docker&logoColor=white)](https://hub.docker.com/)

[Tiếng Việt](./README-VI.md) | [English](./README.md) | [中文文档](./README-ZH.md)

</div>

## ⚡ Tổng quan

**MiroFish** là công cụ dự đoán AI thế hệ mới được xây dựng trên công nghệ đa agent. Bằng cách trích xuất thông tin hạt giống từ thế giới thực (như tin tức nóng, dự thảo chính sách, hoặc tín hiệu tài chính), hệ thống tự động xây dựng một thế giới số song song có độ chân thực cao. Trong không gian này, hàng nghìn agent thông minh với tính cách độc lập, ký ức dài hạn và logic hành vi tự do tương tác và trải qua quá trình tiến hóa xã hội. Bạn có thể tiêm biến từ "góc nhìn thượng đế" để suy luận chính xác quỹ đạo tương lai — **diễn tập tương lai trong sandbox số, và chiến thắng quyết định sau vô số lần mô phỏng**.

> Bạn chỉ cần: Tải lên tài liệu hạt giống (báo cáo phân tích dữ liệu hoặc câu chuyện tiểu thuyết thú vị) và mô tả yêu cầu dự đoán bằng ngôn ngữ tự nhiên</br>
> MiroFish sẽ trả về: Một báo cáo dự đoán chi tiết và một thế giới số có độ chân thực cao với khả năng tương tác sâu

### Tầm nhìn của chúng tôi

MiroFish致力于 tạo ra một bản sao trí tuệ tập thể ánh xạ hiện thực. Bằng cách nắm bắt sự xuất hiện tập thể được kích hoạt bởi tương tác cá nhân, chúng tôi vượt qua giới hạn của dự đoán truyền thống:

- **Ở cấp độ vĩ mô**: Chúng tôi là phòng thí nghiệm diễn tập cho người ra quyết định, cho phép thử nghiệm chính sách và quan hệ công chúng với rủi ro bằng không
- **Ở cấp độ vi mô**: Chúng tôi là sandbox sáng tạo cho người dùng cá nhân — dù là suy luận kết thúc tiểu thuyết hay khám phá kịch bản tưởng tượng, mọi thứ đều có thể thú vị, vui nhộn và dễ tiếp cận

Từ dự đoán nghiêm túc đến mô phỏng giải trí, chúng tôi để mỗi "điều gì sẽ xảy ra nếu" thấy kết quả của nó, làm cho việc dự đoán mọi thứ trở nên khả thi.

## 🌐 Demo trực tuyến

Chào mừng bạn truy cập môi trường demo trực tuyến của chúng tôi và trải nghiệm mô phỏng dự đoán về các sự kiện dư luận nóng mà chúng tôi đã chuẩn bị: [mirofish-live-demo](https://666ghj.github.io/mirofish-demo/)

## 📸 Ảnh chụp màn hình

<div align="center">
<table>
<tr>
<td><img src="./static/image/Screenshot/运行截图1.png" alt="Screenshot 1" width="100%"/></td>
<td><img src="./static/image/Screenshot/运行截图2.png" alt="Screenshot 2" width="100%"/></td>
</tr>
<tr>
<td><img src="./static/image/Screenshot/运行截图3.png" alt="Screenshot 3" width="100%"/></td>
<td><img src="./static/image/Screenshot/运行截图4.png" alt="Screenshot 4" width="100%"/></td>
</tr>
<tr>
<td><img src="./static/image/Screenshot/运行截图5.png" alt="Screenshot 5" width="100%"/></td>
<td><img src="./static/image/Screenshot/运行截图6.png" alt="Screenshot 6" width="100%"/></td>
</tr>
</table>
</div>

## 🔄 Quy trình làm việc

1. **Xây dựng đồ thị**: Trích xuất hạt giống & Tiêm ký ức cá nhân/tập thể & Xây dựng GraphRAG
2. **Thiết lập môi trường**: Trích xuất quan hệ thực thể & Tạo hồ sơ agent & Cấu hình Agent
3. **Mô phỏng**: Mô phỏng song song hai nền tảng & Tự động phân tích yêu cầu dự đoán & Cập nhật ký ức thời gian thực
4. **Tạo báo cáo**: ReportAgent với bộ công cụ phong phú để tương tác sâu với môi trường sau mô phỏng
5. **Tương tác sâu**: Trò chuyện với bất kỳ agent nào trong thế giới mô phỏng & Tương tác với ReportAgent

## 🚀 Bắt đầu nhanh

### Phương án 1: Triển khai từ mã nguồn (Khuyến nghị)

#### Yêu cầu tiên quyết

| Công cụ | Phiên bản | Mô tả | Kiểm tra cài đặt |
|---------|-----------|-------|-----------------|
| **Node.js** | 18+ | Runtime frontend, bao gồm npm | `node -v` |
| **Python** | ≥3.11, ≤3.12 | Runtime backend | `python --version` |
| **uv** | Mới nhất | Trình quản lý gói Python | `uv --version` |

#### 1. Cấu hình biến môi trường

```bash
# Sao chép tệp cấu hình mẫu
cp .env.example .env

# Chỉnh sửa tệp .env và điền các khóa API cần thiết
```

**Biến môi trường bắt buộc:**

```env
# Cấu hình LLM API (hỗ trợ bất kỳ LLM API nào với định dạng OpenAI SDK)
# Khuyến nghị: Mô hình Alibaba Qwen-plus qua nền tảng Bailian: https://bailian.console.aliyun.com/
# Tiêu thụ lớn, thử mô phỏng với ít hơn 40 vòng trước
LLM_API_KEY=your_api_key
LLM_BASE_URL=https://dashscope.aliyuncs.com/compatible-mode/v1
LLM_MODEL_NAME=qwen-plus

# Cấu hình Zep Cloud
# Dung lượng miễn phí hàng tháng đủ cho sử dụng đơn giản: https://app.getzep.com/
ZEP_API_KEY=your_zep_api_key
```

#### 2. Cài đặt phụ thuộc

```bash
# Cài đặt tất cả phụ thuộc một chạm (root + frontend + backend)
npm run setup:all
```

Hoặc cài đặt từng bước:

```bash
# Cài đặt phụ thuộc Node (root + frontend)
npm run setup

# Cài đặt phụ thuộc Python (backend, tự động tạo môi trường ảo)
npm run setup:backend
```

#### 3. Khởi động dịch vụ

```bash
# Khởi động cả frontend và backend (chạy từ thư mục gốc)
npm run dev
```

**URL dịch vụ:**
- Frontend: `http://localhost:3000`
- Backend API: `http://localhost:5001`

**Khởi động riêng lẻ:**

```bash
npm run backend   # Chỉ khởi động backend
npm run frontend  # Chỉ khởi động frontend
```

### Phương án 2: Triển khai Docker

```bash
# 1. Cấu hình biến môi trường (giống triển khai mã nguồn)
cp .env.example .env

# 2. Kéo ảnh và khởi động
docker compose up -d
```

Mặc định đọc `.env` từ thư mục gốc, ánh xạ cổng `3000 (frontend) / 5001 (backend)`

> Địa chỉ mirror để kéo nhanh hơn được cung cấp dưới dạng comment trong `docker-compose.yml`, thay thế nếu cần.

## 🌐 Hỗ trợ đa ngôn ngữ

MiroFish hỗ trợ đa ngôn ngữ với giao diện tiếng Việt đầy đủ:

- **Tiếng Việt**: Giao diện và AI trả lời hoàn toàn bằng tiếng Việt
- **English**: Full English interface and AI responses
- **中文**: 完整的中文界面和AI回复

### Cách chuyển đổi ngôn ngữ:
1. Nhấp vào dropdown chuyển đổi ngôn ngữ ở góc phải trên cùng
2. Chọn ngôn ngữ bạn muốn sử dụng
3. Toàn bộ giao diện và AI sẽ chuyển sang ngôn ngữ đã chọn

## 🔄 Tính năng làm lại (Retry)

MiroFish cho phép làm lại từng bước khi hệ thống bị lỗi hoặc kết quả chưa vừa ý:

- **Bước 1 (Xây dựng đồ thị)**: Làm lại tạo Ontology hoặc xây dựng GraphRAG
- **Bước 2 (Thiết lập môi trường)**: Làm lại chuẩn bị mô phỏng
- **Bước 3 (Chạy mô phỏng)**: Làm lại chạy mô phỏng
- **Bước 4 (Tạo báo cáo)**: Làm lại toàn bộ báo cáo hoặc từng chương riêng lẻ

### Cách sử dụng:
1. Khi một bước bị lỗi hoặc muốn làm lại, nhấp vào nút "Làm lại bước này"
2. Xác nhận dialog để bắt đầu làm lại
3. Hệ thống sẽ tự động reset trạng thái và chạy lại bước đó

## 📬 Tham gia cộng đồng

Đội ngũ MiroFish đang tuyển dụng vị trí toàn thời gian/thực tập. Nếu bạn quan tâm đến mô phỏng đa agent và ứng dụng LLM, hãy gửi CV đến: **mirofish@shanda.com**

## 📄 Lời cảm ơn

**MiroFish đã nhận được hỗ trợ chiến lược và ươm mầm từ Tập đoàn Shanda!**

Công cụ mô phỏng của MiroFish được xây dựng dựa trên **[OASIS (Open Agent Social Interaction Simulations)](https://github.com/camel-ai/oasis)**, Chúng tôi chân thành cảm ơn đội ngũ CAMEL-AI vì những đóng góp mã nguồn mở của họ!

## 📈 Thống kê dự án

<a href="https://www.star-history.com/#dragonboy1206/MiroFish-vi&type=date&legend=top-left">
 <picture>
   <source media="(prefers-color-scheme: dark)" srcset="https://api.star-history.com/svg?repos=dragonboy1206/MiroFish-vi&type=date&theme=dark&legend=top-left" />
   <source media="(prefers-color-scheme: light)" srcset="https://api.star-history.com/svg?repos=dragonboy1206/MiroFish-vi&type=date&legend=top-left" />
   <img alt="Star History Chart" src="https://api.star-history.com/svg?repos=dragonboy1206/MiroFish-vi&type=date&legend=top-left" />
 </picture>
</a>

---

<div align="center">

**Được tạo với ❤️ bởi đội ngũ MiroFish Việt Nam**

</div>

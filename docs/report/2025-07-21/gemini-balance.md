# gemini-balance by snailyp

## 概要
gemini-balance 是一款基於 Python FastAPI 的代理與負載均衡服務，專為 Google Gemini API 設計，並兼容 OpenAI API 標準。可集中管理多組 API Key，自動輪詢、錯誤重試與失效禁用，同時支援圖文聊天、影像生成、網頁搜尋、狀態監控與可視化管理後台，並提供 Docker 化部署方案。

## 關鍵特色
- 多 Key 負載均衡：自動輪詢多個 Gemini API Key，並在達到最大重試或失敗次數後禁用失效 Key。  
- 雙協定兼容：原生支援 Gemini v1beta 與 OpenAI（HF 兼容與標準）格式，統一 Base URL 代理呼叫。  
- 實時可視化配置：管理後台調整配置即時生效，免重啟。  
- 圖文聊天與影像編輯：透過自定義 IMAGE_MODELS 實現影像生成與編輯。  
- 網頁搜尋整合：配置 SEARCH_MODELS 即可調用搜尋功能，並在回應中顯示結果連結。  
- Key 狀態監控頁面：內建 `/keys_status` 頁面，顯示每支 API Key 的健康狀態、請求統計。  
- 詳細日誌與追蹤：請求/錯誤日誌分級管理，支援自動刪除舊日誌。  
- 彈性 Proxy 支援：可設置 HTTP/SOCKS5 代理轉發。  
- Docker 支持：提供 AMD 與 ARM 架構映像，並附 docker-compose 範例。

## 技術棧
- 語言與框架：Python 3.9+、FastAPI、Uvicorn  
- 資料庫：MySQL 或 SQLite（依環境設定）  
- 定時任務：APScheduler  
- 模板與靜態：Jinja2、內建簡易前端頁面  
- 部署：Docker、Docker Compose  

## 專案結構（精簡）
- app/config：配置管理  
- app/core：FastAPI 實例與中介層  
- app/database：ORM 模型與連線  
- app/router：Gemini、OpenAI、狀態頁面路由  
- app/service：核心業務邏輯（聊天、Key 管理、統計）  
- app/scheduler：Key 狀態檢查等排程任務  
- app/static / app/templates：前端資源與 HTML 樣板  
- app/utils：通用工具函式  

## 核心模組
- 輪詢與重試機制：依 `MAX_RETRIES`、`MAX_FAILURES` 自動重試並標記失效 Key  
- 模型清單同步：定期從 Gemini 與 OpenAI 拉取最新模型列表  
- 圖像上傳：支援 SM.MS、PicGo、CloudFlare-ImgBed 三種上傳方式  
- 日誌管理：可設置保留天數，自動清理過期日誌  
- 管理後台：可視化編輯 API_KEYS、ALLOWED_TOKENS、模型白名單/黑名單等  

## 主要配置項
- API_KEYS / ALLOWED_TOKENS：核心功能所需  
- IMAGE_MODELS / SEARCH_MODELS / FILTERED_MODELS  
- MAX_FAILURES、MAX_RETRIES、CHECK_INTERVAL_HOURS  
- PROXIES、TIME_OUT  
- 日誌級別與自動清理策略  
- 圖像生成模型、上傳服務提供者設定  

## 部署方式
1. Docker Compose：下載 `docker-compose.yml`，編輯 `.env`，執行 `docker-compose up -d`  
2. 單容器模式：`docker run -d -p 8000:8000 --env-file .env ghcr.io/snailyp/gemini-balance:latest`  
3. 原生開發：`pip install -r requirements.txt`，`uvicorn app.main:app --reload`  

## API 介面
- Gemini 格式：`GET /gemini/v1beta/models`、`POST /gemini/v1beta/models/{model}:generateContent`、串流接口  
- OpenAI HF：`GET /hf/v1/models`、`POST /hf/v1/chat/completions`、`/embeddings`、`/images/generations`  
- OpenAI 標準：`GET /openai/v1/models`、`POST /openai/v1/chat/completions` 等  

## 授權與使用限制
- 授權：CC BY-NC 4.0（非商用）  
- 嚴禁商業轉售，作者未在任何平台銷售，若有販售請勿受騙。  

## 小結
gemini-balance 以輕量、可擴充的架構，集中解決多 Key 管理、負載平衡、協議兼容、影像與搜尋功能，並提供完善的監控與日誌機制，是快速搭建自有 AI 代理服務的利器。
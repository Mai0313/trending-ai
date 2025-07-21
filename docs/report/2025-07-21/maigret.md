# maigret by soxoj

## 概覽
maigret 是一款用於 OSINT（開放來源情報）調查的命令列工具，僅需提供目標使用者名稱，即可自動化地在數千個網站（包含主流社群平台、論壇、暗網站點等）上搜尋並彙整所有相關帳號與個人資訊。此專案為著名工具 Sherlock 的強化分支，基於 Python 3.10+ 開發，並提供不限 API Key、免註冊即可使用的便捷性。

## 核心功能
- 帳號存在性檢測：支援 3,000+ 站點（預設篩選 500 個熱門網站），可依類別（社群、約會、區域等）或國別標籤選擇性搜尋
- 頁面解析與資訊萃取：自動抓取並解析個人檔案頁，提取用戶名、連結、個人簡介等多種結構化資料
- 遞迴搜尋：基於新發現的使用者名稱或其他 ID，自動擴展搜索範圍，形成「蛛網式」調查流程
- 報告產出：支援生成 HTML、PDF、XMind 等多種格式，並提供圖形化界面（Web UI）與可下載報表
- 抗 CSRF/CAPTCHA 檢測：自動偵測並跳過觸發驗證機制的站點，提升搜索穩定性
- 重試機制：內建請求失敗重試功能，確保關鍵網站的搜尋不因單次錯誤而中斷

## 特色亮點
- 無需 API 金鑰、帳號或密碼即可全自動執行
- 支援暗網站點（Tor、I2P）及透過 DNS 解析的域名檢測
- 一鍵生成全格式報告並可視化呈現搜尋結果圖譜
- 提供官方 Telegram Bot（@osint_maigret_bot），免安裝即能線上使用
- Docker、Cloud Shell、Repl.it、Colab、Binder 等多種部署方式

## 安裝與使用
- Pip 安裝：`pip3 install maigret`（需 Python ≥3.10）
- Windows Standalone：官方 Release 提供 EXE 二進位檔
- Docker：官方映像 `soxoj/maigret:latest` 或自行編譯
- Web 介面：`maigret --web <port>` 啟動後於瀏覽器操作
- 常見指令示例（無需示範程式碼區塊，請參考 README 幫助文件）

## 社群與授權
- 開源授權：MIT
- Issue、Discussion、Pull Request 歡迎貢獻
- 文檔與開發說明：https://maigret.readthedocs.io
- 兼容與衍生：該工具亦被多個商業 OSINT 平台（如 Social Links API、Crimewall、UserSearch.ai）採用

---

**注意**：請僅於合法合規範疇內使用此工具，並遵守各地隱私與資料保護法規。
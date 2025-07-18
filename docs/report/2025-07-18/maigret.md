# maigret by soxoj

## 專案概述
Maigret 是一個以「使用者名稱」為唯一輸入，針對超過 3,000 個網站（預設 500 個最受歡迎站點）進行搜尋的開源 OSINT 工具。它是 Sherlock 的強化版，不需任何 API 金鑰，就能自動檢測社群帳號並擷取公開資訊，並可輸出多種格式的報告（HTML、PDF、XMind）。

## 核心功能
- 支援超過 3,000 個網站（含 Tor、I2P 節點與 DNS 解析域名），預設依流量排序查詢前 500 名  
- 個人頁面深度解析：自動擷取使用者資訊、個人照片、其他連結與聯絡方式  
- 遞迴搜尋：對從頁面解析出的新帳號或 ID 自動進行二次搜尋  
- 標籤篩選：可依網站分類（如相片、約會）、國家（如 US）快速篩選目標平台  
- 偵測封鎖、驗證碼挑戰，並具備重試機制提高搜尋成功率  
- 多種報告輸出：純文字、HTML、PDF、XMind 8，並提供可互動的網頁介面  

## 技術架構與環境
- 語言：Python 3.10+（推薦 3.11）  
- 依賴：requests、BeautifulSoup 等常用網頁擷取與解析套件  
- 串接方式：純網頁爬蟲，不需第三方 API 金鑰  
- Web 介面：內建輕量 Flask 服務，可視化搜尋圖譜並下載報告  

## 安裝與部署
- 官方 Telegram Bot：使用者可直接透過 @osint_maigret_bot 進行查詢  
- Windows：提供獨立 EXE，免安裝套件  
- Python Pip：`pip3 install maigret`  
- Docker：`docker pull soxoj/maigret` 或自行編譯映像  
- 雲端服務：支援 Google Cloud Shell、Repl.it、Colab、Binder  

## 使用範例
- 對單一使用者輸出 HTML 報告  
  - maigret username --html  
- 同時查詢多個帳號  
  - maigret user1 user2 user3 -a  
- 針對「相片」與「約會」類別網站搜尋  
  - maigret user --tags photo,dating  
- 啟動 Web 介面  
  - maigret --web 5000  

## 應用場景
- OSINT 調查：快速蒐集目標在各大社群平台的公開足跡  
- 資安紅隊/藍隊：分析潛在威脅者使用者習慣與社群互動  
- 社群分析：履歷審查、背景調查，或品牌監控  

## 貢獻與授權
- 開源授權：MIT License  
- 歡迎提交網站條目至 `data.json` 或 Pull Request 改進程式碼  
- 詳見開發文件與討論區，參與社群維護與功能擴充  

---

Maigret 以其高擴充性與易用性，讓安全研究者、調查人員及社群分析師能迅速掌握目標在網路上的各種公開資料，適合教育及合法範疇下的各種調查需求。
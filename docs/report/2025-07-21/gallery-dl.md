# gallery-dl by mikf

## 專案概覽  
- 語言：Python  
- 功能：命令列工具，用於從多種圖床與社群平台下載圖庫、影集及影片  
- Stars：14,252；Forks：1,139；Open Issues：1,041  
- 建立時間：2014-10-12；最近更新：2025-07-20  
- 主分支：master；檔案大小：約14.7 MB  

## 核心特色  
- 支援超過數十種網站與服務，包括 Pixiv、DeviantArt、Flickr、Tumblr、Twitter、Patreon、Instagram、Danbooru、MangaDex 等  
- 強大且靈活的檔名與目錄結構格式化機制，透過 Jinja 模板或內建參數自訂輸出  
- 多元認證方式：OAuth／帳號密碼／瀏覽器 Cookie，突破私密相簿與驗證牆  
- 可整合 yt-dlp／youtube-dl 以下載 HLS/DASH 影片，並支援 FFmpeg 與 mkvmerge 進行後處理（Pixiv Ugoira 動圖轉檔）  
- 內建 URL 篩選與強制指定抽取器機制，能過濾足球範圍、章節編號、語言標籤等條件  

## 安裝與部署  
- 官方發佈：PyPI 套件、跨平台執行檔（Windows .exe、Linux .bin）  
- 套件管理：pip、Snap、Chocolatey、Scoop、Homebrew、MacPorts、Nix  
- 容器化：提供 Dockerfile，可直接建置或從 Docker Hub、GitHub Container Registry 拉取映像  

## 相依項目與可選擴充  
- 必要：Python 3.8+、Requests  
- 可選增效：  
  • yt-dlp / youtube-dl：影片串流下載  
  • FFmpeg、mkvmerge：影像／動圖轉檔  
  • PySocks：SOCKS Proxy 支援  
  • brotli / brotlicffi、zstandard：壓縮演算法  
  • PyYAML、toml：額外組態格式  
  • SecretStorage：GNOME 金鑰圈 Cookie  
  • Psycopg：PostgreSQL 存檔  
  • truststore：系統憑證  
  • Jinja：進階模板化  

## 組態與擴充性  
- 組態檔路徑多樣，支援 JSON、YAML、TOML，多重檔案合併覆蓋  
- per-extractor 自訂選項：下載目錄、檔名格式、認證資訊、過濾規則、並行數量  
- 官方文件詳盡，包含支援網站列表、命令行選項、格式化參考、實例範例  

## 社群與維護狀況  
- 積極開發：每月活躍 commit 與合併請求，Issue 回應迅速  
- CI／測試流程：GitHub Actions 自動化測試  
- 貢獻指引：歡迎透過 Issue 回報、Pull Request、Gitter 聊天室交流與支援  
- 熱門主題標籤：danbooru、deviantart、pixiv、mangadex、twitter、tumblr、downloader 等  

此工具已成為圖庫批量下載領域的經典利器，具備高度彈性與可擴充性，適合從研究、收藏到自動化工作流程的一切需求。
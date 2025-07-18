# sherlock by sherlock-project

## 摘要
sherlock 是一個以 Python 開發的命令列工具，用於根據指定使用者名稱，在全球超過 400 個社交網路和網站上尋找對應帳號。此專案具備高度可擴充性與客製化能力，廣泛應用於資安情報蒐集（OSINT）、滲透測試、紅隊作業與電子取證場景。

## 主要功能
- 多達 400+ 社交平台的使用者帳號搜尋  
- 支援單一或多筆使用者名稱批次查詢  
- 輸出格式：純文字、CSV、XLSX、JSON  
- 支援 Tor 與代理伺服器請求，保障匿名性  
- 可限制查詢特定站點或自定義站點列表  
- 友善的 CLI 介面並顯示命令行參數與說明  
- 支援瀏覽器自動開啟搜尋結果

## 技術特色
- Python 3.x 編寫，易於擴展與維護  
- 內建 JSON 資料檔，方便本地化與離線使用  
- 可透過 pipx、pip、Docker、或發行版套件安裝  
- 內建 debug/verbose 模式，便於問題排查與效能量測  
- 支援 NSFW 內容站點的選擇性查詢  
- 可與 Apify 平台無縫整合，提供雲端 Actor 版本

## 安裝與部署
- 標準方式：`pipx install sherlock-project`（亦可使用 pip）  
- Docker：`docker run -it --rm sherlock/sherlock`  
- 社群維護套件：Debian、Ubuntu、Homebrew、Kali、BlackArch 等  
- 官方文件提供詳細安裝指引與替代方案

## 使用說明
- 單一使用者搜尋：執行 `sherlock 使用者名稱`  
- 多使用者搜尋：執行 `sherlock user1 user2 user3`  
- 常見選項：
  - `--tor` / `--unique-tor`：透過 Tor 網路執行  
  - `--proxy`：設定自訂代理伺服器  
  - `--csv` / `--xlsx`：產生不同格式報表  
  - `--site`：僅針對特定網站查詢  
  - `--print-all` / `--print-found`：自訂顯示結果  
  - `--browse`：於預設瀏覽器開啟所有搜尋結果

## 社群與貢獻
- GitHub Stars：67,000+；Forks：7,600+；Open Issues：230+  
- 原始作者：Siddharth Dushantha（sdushantha）  
- 活躍維護者與貢獻者社群，定期更新數據與修正問題  
- 支援 Hacktoberfest、對安全研究者友好  
- 採用 MIT 授權，鼓勵自由使用與修改

## 應用場景
- OSINT 調查與企業資安防禦  
- 滲透測試中帳號橫向搜尋  
- 數位鑑識與法證案例蒐證  
- 品牌保護與假冒帳號偵測  
- 學術研究使用者行為分析

## 小結
sherlock 以其豐富的網站支援清單、靈活的輸出格式、匿名化請求機制，以及與雲端服務的深度整合，成為資訊安全領域與侦察作業中不可或缺的利器。無論是安全研究員、駭客或品牌監控人員，都能透過此工具快速獲取目標使用者在各大社交平台的帳號分布情形。
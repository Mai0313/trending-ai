# ai-hedge-fund by virattt

## 一、專案概述
- AI Hedge Fund 是一個以多種大型語言模型 (LLM) 驅動的量化交易概念驗證（Proof of Concept），透過擬真多位知名投資大師的投資思維，對股票進行決策支援與回測分析。  
- 完全以教育與研究為目的，**不進行真實下單交易**，並明確附有免責聲明。

## 二、基本資訊
- 語言               : Python  
- 熱門度             : ★38287 ⭐  
- 派生分支 (forks)   : 6733  
- 開放議題數         : 40  
- 建立時間           : 2024-11-29  
- 最後更新時間       : 2025-07-21  
- 主分支             : main  

## 三、核心功能與特色
1. 多智能體架構  
   - 模擬 11 位傳奇投資人（如 Warren Buffett、Michael Burry、Cathie Wood 等）各自的投資策略  
   - 另設 Valuation、Sentiment、Fundamentals、Technicals、Risk Manager、Portfolio Manager 等專責模組，綜合產出最終交易建議  
2. 指令列與網頁介面雙模式  
   - CLI：以 Poetry 或 Docker 執行，支援自訂股票代號、日期區間、是否顯示推理過程等  
   - Web App：前後端整合，一鍵安裝依賴並自動開啟瀏覽器，適合不熟 CLI 的使用者  
3. 回測引擎  
   - 提供歷史資料回測（Backtester），驗證模型決策於不同期間的表現  
4. 彈性支援多種 LLM  
   - OpenAI (GPT-4o 等)、Groq (DeepSeek、Llama3)、Anthropic 等  
   - 可切換至本地模型（Ollama）以降低雲端 API 耗費  

## 四、系統架構與模組
- Aswath Damodaran Agent：價值評估大師，結合故事與數據  
- Ben Graham Agent：價值型投資之父，注重安全邊際  
- Bill Ackman Agent：積極主義者，勇於發聲  
- Cathie Wood Agent：創新成長派，擅長科技與顛覆式機會  
- Charlie Munger Agent：優質企業擁護者，只買優秀企業  
- Michael Burry Agent：反向思考者，尋找深度價值  
- Peter Lynch Agent：日常商機獵手，找出「十倍股」  
- Phil Fisher Agent：深入產業調研，精細化成長研究  
- Rakesh Jhunjhunwala Agent：印度市場看多風向球  
- Stanley Druckenmiller Agent：宏觀大師，追求非對稱機會  
- Warren Buffett Agent：伯克夏之王，長期價值佈局  
- Valuation Agent：計算內在價值並產生交易信號  
- Sentiment Agent：分析市場情緒  
- Fundamentals Agent：檢視財務基本面  
- Technicals Agent：技術指標篩選訊號  
- Risk Manager：控管風險指標與倉位上限  
- Portfolio Manager：整合訊號、下達最終委單  

## 五、使用流程
1. 取得原始碼：`git clone https://github.com/virattt/ai-hedge-fund.git`  
2. 設定環境變數：複製 `.env.example` 並填入 OpenAI/Groq/Financial Data API Key  
3. 安裝套件  
   - Poetry：`poetry install`  
   - Docker：`./run.sh build` (Linux/macOS) 或 `run.bat build` (Windows)  
4. 執行主程式  
   - CLI：`poetry run python src/main.py --ticker AAPL,MSFT --start-date 2024-01-01 --end-date 2024-06-30 --show-reasoning`  
   - Docker：`./run.sh --ticker AAPL,MSFT main`  
   - Web App：於 `app/` 目錄執行 `./run.sh` (macOS/Linux) 或 `run.bat` (Windows)  

## 六、亮點與優勢
- 多角度決策：集合傳奇大師與量化模組的投資觀點  
- 高度彈性：可調整 LLM 平台、回測時間、顯示推理等參數  
- 雙介面支持：CLI for power users、Web UI for 視覺化分析  
- 開放原始碼：MIT 授權，鼓勵 Fork、Issue 回報與 PR 貢獻  
- 教育導向：完整流程示範，適合想學習 AI 金融應用者  

## 七、使用注意與免責
- **僅供學術/研究，不做真實交易**  
- 不提供任何投資建議，不保證績效  
- 自行承擔使用風險，請諮詢專業顧問  
- 歷史表現不代表未來結果  

---

以上為 ai-hedge-fund 專案之重點摘要與技術報告。歡迎參考並在教育或研究場景中深入探討 AI 與量化投資之應用。
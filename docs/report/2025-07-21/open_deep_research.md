# open_deep_research by langchain-ai

## 一、專案概述
open_deep_research 是一個完全開源、可高度配置的深度研究代理（Deep Research Agent），整合多種語言模型供應商、搜尋工具與 MCP（Model Context Protocol）伺服器，協助用戶自動化搜尋、摘要、反思與最終報告撰寫流程。專案重點在於模組化、可視化與易擴充，並提供直觀的 Web UI（LangGraph Studio）以進行交互式操作。

## 二、關鍵亮點
- 完整開源：所有流程、工具呼叫與模型配置均公開，社群可自由擴展與客製化  
- 多模型協同：依研究步驟分工使用不同規模與功能的模型（Summarization、Research、Compression、Final Report）  
- 高度配置：可透過 .env、Web UI 或程式碼調整研究單元併發數、搜尋 API、重試次數等參數  
- MCP 支援：同時支援本地檔案系統與遠端分散式 MCP 伺服器，方便讀寫文件、擴充第三方工具  
- 視覺化界面：LangGraph Studio 提供流程圖模式的編排視覺化與即時 API Docs  

## 三、快速上手
1. 下載專案並啟動虛擬環境  
2. 依照需求安裝相依套件  
3. 複製並修改 .env 範本，設定模型 API 金鑰、搜尋服務與並行參數  
4. 啟動 LangGraph 伺服器，開啟 Studio UI 進行互動式測試  
5. 在 messages 欄位輸入問題，點擊 Submit 即可觀察深度研究流程運行結果  

## 四、主要功能模組
### 1. 研究流程配置
- 研究者迭代次數（Max Researcher Iterations）  
- 研究單元併發數（Max Concurrent Research Units）  
- 工具呼叫重試次數（Max React Tool Calls）  
- 是否允許啟動前澄清（Allow Clarification）  

### 2. 搜尋 API 整合
- 支援 Tavily（跨模型）、OpenAI Web Search、Anthropic Web Search  
- 可自由選擇或停用搜尋功能  
- 模型必須支援對應搜尋 API  

### 3. 多階段模型任務
- Summarization Model：整理搜尋結果  
- Research Model：核心研究與初步分析  
- Compression Model：壓縮子代理回傳內容  
- Final Report Model：生成最終報告  

### 4. MCP 伺服器擴充
- 本地 FileSystem MCP：限制根目錄內之檔案存取與管理  
- 遠端 MCP 伺服器：支援多租戶、JWT 驗證與 HTTP 串流  

### 5. 評估系統
- 多維度評分，0–1 分等級  
- 支援批次化測試與 LangSmith 資料集  
- 主要檔案：run_evaluate.py、evaluators.py、prompts.py  

## 五、部署與使用場景
- LangGraph 本地部署：快速啟動測試與流程可視化  
- LangGraph 平台托管：分分鐘推上雲端，省去基礎架構維運  
- Open Agent Platform（OAP）整合：讓非技術用戶透過 GUI 建構與調整 Deep Researcher  
- 可部署自有 OAP 實例，並將自訂代理對外提供服務  

## 六、過去實現與對比
legacy/ 目錄提供兩套舊版實現：
- Workflow Implementation：以人機協作計劃-執行流程為主，強調可控與精準  
- Multi-Agent Implementation：多研究員並行，加速報告生成，並擴充 MCP 支援  

## 七、社群與延伸
- 官方部落格文章與介紹影片提供完整概念說明  
- Issues 與 PR 區開放 Model Provider 或本地化設置討論  
- 未來可擴充更多自訂工具呼叫、多語言支援與進階評估維度  

---

open_deep_research 透過高度模組化與視覺化流程打造了一套可擴展、可定制的自動化深度研究解決方案，適用於知識管理、學術研究、商業情報等多種場景，具有極高的靈活性與可維護性。
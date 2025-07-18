# open_deep_research by langchain-ai

## 簡介  
open_deep_research 是一個完全開源、可高度自訂的「深度研究」人工智慧代理（agent）框架，旨在自動化複雜研究流程。它整合多家模型服務商、搜尋工具以及 MCP（Model Context Protocol）伺服器，提供從資料蒐集、分析、壓縮到最終報告撰寫的全流程解決方案。

## 核心亮點  
- 完全開源、無鎖定任何商業服務  
- 多模型分工：彙整、研究、壓縮、報告撰寫各司其職  
- 支援結構化輸出與工具呼叫（Tool Calling）  
- 多種搜尋 API：Tavily、OpenAI Native Web Search、Anthropic Native Web Search  
- 可並行執行多個研究單位以加速資料蒐集  
- 附帶完善的批次評估系統與多維度評分  

## 主要功能  
- Research Supervisor 與多個子代理（sub-agents）協同工作  
- 動態設定：可經由環境變數、Web UI（LangGraph Studio）或程式碼直接調整參數  
- 多家模型供應商支援：OpenAI、Anthropic、Google Vertex AI、Ollama 等  
- 可連接本地或遠端 MCP 伺服器，擴充資料存取與分散式協同能力  
- 內建衡量品質的評估模組，支援自訂評分維度與測試資料集  

## 架構與設計  
- 核心流程  
  1. 問題澄清（可選）  
  2. 搜尋工具取回初步資料  
  3. Summarization 模型摘要搜尋結果  
  4. Research 模型深入分析  
  5. Compression 模型壓縮研究成果  
  6. Final Report 模型撰寫完整報告  
- Legacy 實現可供參考：  
  - Workflow Implementation（計劃與執行、逐段生成、反覆審視）  
  - Multi-Agent Implementation（Supervisor-Researcher 架構、平行處理與 MCP 支援）  

## 快速上手  
1. 下載原始碼並啟動虛擬環境  
2. 安裝相依套件  
3. 複製並編輯 `.env`，設定模型金鑰、搜尋 API、MCP 端點等  
4. 啟動 LangGraph 開發伺服器，透過瀏覽器開啟 Studio UI  

## 組態選項  
- 全域設定：最大結構化輸出重試次數、是否允許澄清問題、最大並行研究單位數  
- 研究流程：搜尋 API 類型、研究迭代次數、單步工具呼叫上限  
- 模型設定：  
  - Summarization（預設 openai:gpt-4.1-nano）  
  - Research（預設 openai:gpt-4.1）  
  - Compression（預設 openai:gpt-4.1-mini）  
  - Final Report（預設 openai:gpt-4.1）  
- 模型必須支援結構化輸出與工具呼叫；部分搜尋 API（Anthropic／OpenAI Native）需對應具備網路搜尋能力之模型  

## MCP 伺服器  
- 本地 MCP：Filesystem MCP Server，提供安全的檔案系統操作與存取控制  
- 遠端 MCP：支援多租戶、JWT 驗證，可接受多種工具列表與 HTTP 串流請求  
- 範例：Arcade MCP Server，只需設定 URL 與可用工具即可接入  

## 評估系統  
- 支援批次資料集測試，並以多維度（Accuracy、Completeness、Relevance 等）進行 0–1 分制評分  
- 提供可擴充的 evaluator 函式與自訂 prompts  
- 主要程式位於 tests/ 目錄，可用於自動化比對與基準測試  

## 部署與應用  
- 本地部署：透過 LangGraph Studio 進行互動式測試  
- 雲端部署：發布至 LangGraph Platform  
- Open Agent Platform（OAP）整合：為非技術用戶提供圖形化代理組態與管理介面，可直接體驗 Deep Researcher  

## 備註：Legacy Implementations  
- Workflow Implementation：以人腦互動規劃為核心，強調逐段生成與審查  
- Multi-Agent Implementation：採用平行子代理架構，強化速度與 MCP 支援  

---  
整體而言，open_deep_research 提供了一套靈活且可擴展的深度研究代理解決方案，適合需要大量資料蒐集與分析、自動化報告撰寫的場景，並透過多種配置與外掛機制，滿足不同模型服務商與基礎建設需求。
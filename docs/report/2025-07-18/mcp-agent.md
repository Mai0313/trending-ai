# mcp-agent by lastmile-ai

## 專案概述
mcp-agent 是一個輕量且可組合的 Python 框架，基於 Anthropic 推出的 Model Context Protocol（MCP）與 Building Effective Agents 模式，提供標準化的介面與開箱即用的工作流程（workflows），讓開發者能輕鬆建立具備工具呼叫、跨服務協作與多代理編排的 AI 應用。

## 主要特色
- MCP 協議整合：自動管理 MCP 伺服器的啟動、連線與關閉，並以 `MCPApp` 統一配置。  
- Agent 與增強型 LLM：以 `Agent` 抽象出具備工具(callable tools) 的智慧體，並透過 `AugmentedLLM` 把各種 MCP 工具及記憶模組注入大型模型。  
- 完整實作 Anthropic 工作流程：  
  - Augmented LLM  
  - Parallel（扇出扇入）  
  - Router 與 Intent Classifier（路由與意圖分類）  
  - Evaluator-Optimizer（評估與優化迭代）  
  - Orchestrator-Workers（規劃與分工）  
- 支援 OpenAI Swarm：模型無關的多代理協作參考實現，內建上下文變數管理與人機互動。  
- 多種範例應用：基本檔案與網路讀寫、Claude Desktop 插件、Streamlit Gmail Agent / RAG 聊天機器人、Marimo 筆記本、CLI Swarm 示例。  
- 人機互動與訊號化：工作流程可在任務中途透過 `__human_input__` 或自訂 callback 暫停並等待使用者輸入。  
- 可作為 MCP Server：將整個 Agent 應用封裝成一個「伺服器的伺服器」（`MCPAggregator`），讓任何 MCP 客戶端都能呼叫。

## 核心元件
- MCPApp：全域狀態與設定管理，統一記憶、日誌與伺服器設定。  
- MCPConnectionManager / gen_client：以非同步上下文管理器方式啟動／重用 MCP 伺服器連線。  
- Agent：定義名稱、指令（instruction）與可存取的 MCP 伺服器列表，並將其工具暴露給 LLM。  
- AugmentedLLM：增強型 LLM 基底，支援多輪互動、工具呼叫、結構化輸出與記憶機制。  
- Workflow 模組：每個工作流程如 Parallel、Router、Evaluator-Optimizer、Orchestrator、Swarm 均為 `AugmentedLLM`，可相互嵌套與串接。

## 使用方式與範例
- 安裝：  
  - pip install mcp-agent  
  - 或使用 uv 套件管理 `uv add "mcp-agent"`  
- 基本範例：結合 fetch 與 filesystem 伺服器與 OpenAI LLM，多輪查檔、擷取網頁、摘要推文。  
- 進階應用：  
  - 在 Claude Desktop 內部當作 MCP server 提供動態定義的多代理並行評估工作流程。  
  - 以 Streamlit 打造 Gmail 智能助理以及基於 Qdrant 的 RAG 聊天機器人。  
  - 在 Marimo Notebook 中即時執行 Agent。  
  - Python CLI 版 Swarm 多代理客服示例。

## 未來規劃與社群貢獻
- Durable Execution（持久化暫停／重啟流程），計畫整合 Temporal。  
- 長期記憶 (Long-Term Memory) 與 Streaming 輸出。  
- 擴展 MCP 協議能力：資源管理、提示庫、通知機制等。  
- 歡迎依據 CONTRIBUTING 指南提出 PR、issue 或範例貢獻。  

## 社群與統計資訊
- Stars: 6574  
- Forks: 646  
- Open Issues: 74  
- Topics: agents, ai, ai-agents, llm, mcp, python  
- 主要貢獻者：Shaun Smith (@evalstate)、Jerron Lim (@StreetLamb)、Jason Summer (@jasonsum)  
- 授權：開源許可（License）  

mcp-agent 致力於打造統一、可擴充且易用的 AI Agent 開發框架，讓開發者能專注在商業邏輯，並無縫整合來自任何 MCP 伺服器的工具與服務。
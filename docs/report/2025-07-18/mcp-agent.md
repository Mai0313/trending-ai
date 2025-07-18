# mcp-agent by lastmile-ai

## 簡介

`mcp-agent` 是由 lastmile-ai 開發的一個框架，這個框架旨在使用 Model Context Protocol（MCP）來構建高效能的 AI 代理組件。該項目採用簡單且可組合的工作流程模式，能夠方便地管理AI應用中的代理。

## 關鍵特色

- **Model Context Protocol（MCP）**：提供了一種標準化的介面，使得任何軟體皆可透過 MCP 伺服器供 AI 助手訪問。

- **工作流程模式**：實現多種生產級別的 AI 代理模式，這些模式可組合以創建複雜的代理應用。支持如 OpenAI Swarm 等多代理協作模式，並且不依賴於特定模型。

- **擴展性與輕量化**：`mcp-agent` 由於其採用了輕量化設計，所以更像是一個代理模式庫而非全功能框架，同時因應 MCP 現代化協定，它能夠與其他 MCP 服務完美集成。

- **易用性**：設計上強調簡易安裝與使用，不僅管理 MCP 伺服器連接，還實現了所有 "Building Effective Agents" 所描述的模式，並以範例提供使用。

## 功能模組

- **MCPApp**：全局狀態及應用配置的管理。
- **MCP伺服器管理**：通過 `gen_client` 和 `MCPConnectionManager` 實現對 MCP 伺服器的輕鬆連接和管理。
- **代理（Agent）**：作為一個具名和目的（指令）單位，能夠接入 MCP 伺服器，從而使其工具集成到 LLM 使用中。
- **增強型大模型（AugmentedLLM）**：讓 LLM 集成 MCP 伺服器功能，提供更多應用空間。

## 案例應用

### Claude Desktop
將 mcp-agent 應用集成到 Claude Desktop 中，提供多代理評估任務能力。

### Streamlit
可以在 Streamlit 上部署的 Gmail Agent，支持對 Gmail 的各類操作。

### Python 腳本
能撰寫為 Python 腳本或 Jupyter notebook 使用，如 Swarm 工作流程演示。

## 開始使用

1. 推薦使用 `uv` 管理 Python 專案。
2. 使用簡單指令安裝並運行。

## 開放源碼與社群貢獻

mcp-agent 在 GitHub 開放源碼，歡迎各類貢獻以推動此項目的進一步改進與發展。包括提供更多樣例、拓展功能，或基於更大範圍的 MCP 服務器的兼容能力。

此框架正在初期發展階段，提供了一個標準化和高集成度的方式來構建 AI 應用，並且預計此通訊協定在未來的AI工具開發中將會得到廣泛的應用。
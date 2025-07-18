# autogen by microsoft

## 概述
autogen 是由 Microsoft 發起的多代理（multi-agent）AI 開發框架，旨在協助使用者快速構建具備自主行動或與人類協同作業能力的智能代理系統。該專案自 2023 年 8 月成立以來，迅速累積超過 47,000 顆 ⭐，並在社群內提供豐富的教學資源及開發工具。

## 主要特色
- 支援多語言生態  
  - Python（主力開發）  
  - .NET（官方 .NET 套件，涵蓋 Contracts、Core、gRPC 等）  
- 多層次、可擴充架構  
  - Core API：實作訊息傳遞、事件驅動、分散式執行等核心功能  
  - AgentChat API：在 Core 之上提供「兩者對話」或「多方群聊」等具體模式  
  - Extensions API：支援第三方擴充（如 OpenAI、Azure OpenAI、Code execution、Web browsing）  
- 豐富的開發者工具  
  - AutoGen Studio：無程式碼 GUI 平台，用於原型開發與流程編排  
  - AutoGen Bench：基準測試工具，評估代理效能與任務完成度  
- 生態系統與社群  
  - Discord 實時交流  
  - 定期 Office Hour 與線上直播  
  - GitHub Discussions、Blog、FAQ 文檔等多樣支援管道  

## 核心功能
1. **自主代理（Autonomous Agents）**  
   - 可設定不同角色（AssistantAgent、UserProxyAgent、WebSurfer 等）  
   - 自動切換角色執行任務，並根據條件（如文字關鍵字）終止對話  
2. **多代理協作**  
   - RoundRobinGroupChat、SeqChain 等模式，實現代理間輪替或流程串接  
   - 支援人機互動，由 UserProxyAgent 替使用者在每步輸入  
3. **擴充能力**  
   - 內建對接 OpenAI / AzureOpenAI API  
   - 實現瀏覽器模擬（Playwright）、檔案操作、程式碼執行等  
4. **跨語言與分散式執行**  
   - .NET 客戶端透過 gRPC 與 Python 核心通信  
   - 本地與雲端皆可部署，滿足不同規模與場域需求  

## 使用場景
- 客製化 AI 助手：快速建置具備長期任務管理與多步驟對話能力的虛擬助理  
- 自動化網頁爬取與資訊摘要：結合 WebSurfer 多媒體瀏覽代理，自動收集並生成報告  
- 多代理團隊協作：將不同專長的代理（如資料分析、語言翻譯、程式碼撰寫）組合成一個工作流  
- AI 教學與研究：透過 AutoGen Bench 進行代理性能評估與策略優化  

## 入門與開發流程
1. 安裝需求  
   - Python 3.10 以上  
   - pip 安裝 `autogen-agentchat` 與相應擴充模組  
2. 建立 Agent  
   - 選擇內建的 AssistantAgent 或延伸代碼自定義 Agent  
3. 設計對話或工作流  
   - RoundRobinGroupChat、条件終止（TextMentionTermination）  
4. 執行與監控  
   - Console 介面串流輸出結果  
   - AutoGen Studio GUI 版快速原型  

## 社群與貢獻
- 官方文件、範例程式碼與教學影片定期更新  
- GitHub Issues / Discussions 提問，或加入 Discord 獲得即時協助  
- 歡迎透過 Pull Request 提供 bug 修正、新功能或文件改進  

## 法律與授權
- 文件內容採用 Creative Commons Attribution 4.0 國際授權  
- 原始碼依 MIT License 發佈  
- 不授權使用 Microsoft 商標，詳見專案 LICENSE  

---

autogen 作為領先的多代理 AI 框架，集結了核心 API、豐富的擴充套件及無程式碼開發平台，適合需要快速原型與規模化部署的 AI 團隊與研究者使用。
# ART by OpenPipe

## 簡介
ART（Agent Reinforcement Trainer）是一套開源的強化學習框架，專為大型語言模型（LLM）在真實任務中進行多步驟代理訓練而設計。核心機制採用 GRPO（Generalized Reinforcement Policy Optimization），並結合零樣本獎勵生成「RULER」，省去繁瑣的獎勵函數工程，讓模型能夠 on-the-job 學習。

## 關鍵特色
- RULER（Relative Universal LLM-Elicited Rewards）  
  • 利用 LLM 自動評分代理軌跡，無需標註資料或人工設計獎勵  
  • 2–3 倍開發速度提升，通用於各類任務  
  • 在多個基準上達到或超越手工設計獎勵的效能  
- GRPO 強化學習  
  • 針對大規模語言模型的多步驟決策場景優化  
  • LoRA 微調架構，減少訓練與部署成本  
- 模組化客戶端/伺服器架構  
  • 客戶端模擬 OpenAI API，伺服器負責推論與訓練  
  • 支援本地或雲端（GPU）運行  
- 易整合  
  • 原生對接 vLLM、HuggingFace Transformers  
  • 提供 W&B、Langfuse、OpenPipe 等監控與除錯工具  

## 架構與工作流程
1. 推論階段  
   - 客戶端透過 ART SDK 發送多條並行 Agentic Rollouts  
   - 伺服器在 vLLM 中載入最新 LoRA，執行推論並收錄對話序列（Trajectory）  
   - 每條回合結束後，依據人工設計或 RULER 生成的分數標定獎勵  
2. 訓練階段  
   - 收集好的 Trajectories 分批送回伺服器  
   - 伺服器使用 GRPO 演算法進行微調，更新 LoRA 權重  
   - 保存並重新載入新 LoRA，推論自動繼續  

## 範例與效能
- Notebook 範例涵蓋：  
  • Email 搜尋代理（Qwen 2.5 7B + RULER）  
  • 2048 遊戲（Qwen 2.5 3B）  
  • Tic Tac Toe、Codenames、Temporal Clue 等  
- 每個範例均附訓練過程可視化曲線與基準比較報告  

## 支援模型與整合
- 相容大部分 vLLM/HuggingFace Transformers 兼容之因果語言模型  
- 已驗證支援 Qwen2.5、Qwen3、Llama、Kimi 等主流程式  
- 與 Unsloth 模型庫深度整合，並持續擴增支援名單  
- W&B、Langfuse、OpenPipe 等生態系監控插件  

## 安裝與使用
- Python 套件：`openpipe-art`  
- 安裝指令：pip install openpipe-art  
- 無縫啟動本地或雲端 GPU 服務，透過客戶端調用即刻開始強化訓練  

## 貢獻與授權
- 採用 Apache-2.0 開源許可  
- 歡迎透過 GitHub Issues、Pull Requests 或在 Discord 社群交流討論  
- 詳細文件與範例請見：https://art.openpipe.ai  

## 結論
ART 為 LLM 在複雜任務中進行強化學習提供了一條高效、模組化且低門檻的道路。結合 RULER 的零樣本獎勵生成和 GRPO 的強化策略優化，開發者能更快速地構建可靠的多步驟代理系統，並享有完整的監控、除錯與雲端執行生態支援。
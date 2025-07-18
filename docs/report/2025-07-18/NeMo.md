# NeMo by NVIDIA

## 簡介

NeMo 是由 NVIDIA 開發的一個可擴展及雲原生的生成式 AI 框架，專為大型語言模型（LLMs）、多模態模型、語音識別（ASR）、文字轉語音（TTS）以及電腦視覺（CV）領域的研究人員和開發者設計。此框架便於開發者高效地創建、定制和部署新生成式模型。

## 關鍵特點

- **大型語言模型和多模態模型**：NeMo 支援最新技術，如 SteerLM, 直接偏好優化（DPO），以及來自人類反饋的強化學習（RLHF）等。
- **尺度和效能**：框架支援在數千個 GPU 上進行大規模訓練，並使用 NVIDIA Transformer Engine 在 NVIDIA Hopper GPUs 上進行 FP8 訓練。
- **語音 AI**：NeMo 的 ASR 和 TTS 模型可使用 NVIDIA Riva 進行優化和部署。

## 最新消息

1. **版本更新與技術支持**
   - **NeMo 2.0**：新版提升模組性和易用性，支持 Python-based 配置，兼容 PyTorch Lightning 的模組抽象。
   - **新模型支持**：包括 Llama 4、Flux、Hyena 等模型。
   
2. **多模態生成式 AI**
   - **NVIDIA Cosmos 世界模型平台**：加速物理 AI 系統的世界模型開發，可生成真實合成視頻，適用於高級動作機器人模擬和自動駕駛模型。
   
3. **語音識別**
   - 以高效推理加速 CTC、RNN-T 和 TDT 模型，達到高達 10 倍的速度提升。

## 使用與部署

- **快速啟動引導**：可參考 NeMo Framework 使用指南進行本地和 Slurm 叢集上的實驗。
- **模型部署與優化**：LLMs 和 MMs 可通過 NVIDIA NeMo 微服務進行部署。
- **持續改進與技術支援**：未來版本將持續支持更多的 ASR 和 TTS 模型訓練。

## 社區與貢獻

- **開放源碼貢獻**：歡迎社區參與貢獻，請參閱專案的 CONRIBUTING.md。
- **討論區和常見問題**：NeMo 在 GitHub 上的討論區提供 FAQ 和開放提問的空間。
  
NeMo 框架針對生成式 AI 的開發，提供了完整且強大的模組化支持，並可在雲端環境中高效執行大規模探索和實驗。NVIDIA 不斷升級 NeMo，也展示了生成式 AI 領域的技術突破和未來方向。
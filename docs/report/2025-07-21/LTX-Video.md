# LTX-Video by Lightricks

## 專案概述
LTX-Video 是由 Lightricks 發布的第一款基於 DiT（Diffusion Transformer）的即時視訊生成模型，能以近乎即時的速度產出高品質影片。模型支援多種生成模式，包括文字到影片（Text-to-Video）、影像到影片（Image-to-Video）、關鍵幀動畫、影片延伸（Forward/Backward）、以及影片到影片轉換，使創作者可在多種應用場景中靈活運用。

## 關鍵特色
- 實時生產：在 NVIDIA H100 GPU 上可達 30 FPS、1216×704 的解析度，生成速度超越觀賞速度。
- 多模態條件：同時支援文字提示、影像、影片片段做為生成條件，並可設定多種條件強度。
- 多階段生成管線：提供全尺寸模型（13B）、精簡知識蒸餾模型（2B／13B distilled）及量化版本（FP8 / 8-bit），實現速度、品質與資源消耗之間的平衡。
- 控制模型（LoRA）：深度（Depth）、姿勢（Pose）、Canny 邊緣三大控制 LoRA，可精確引導影片內容與動態。
- 開放原始碼訓練腳本：LTX-Video-Trainer 支援完整微調與 LoRA 微調，便於用戶訓練自定義控制模型與特效。

## 技術細節
- 核心架構：基於 Transformer 的潛空間擴散模型（Latent Diffusion），結合 Spatio-Temporal Guidance（STG）強化時序一致性。
- 推理選項：
  - Config 檔案驅動：多個 YAML 配置檔定義不同模型及多尺度渲染流程。
  - ComfyUI 整合：官方提供範例 Workflow，便於視覺化串接、調參與流程展示。
  - Hugging Face Diffusers：原生支援 LTX-Video Pipeline，並包含 8-bit 量化版本。
- 硬體需求：13B 模型推薦 H100 或同級別 GPU；2B 蒸餾模型可在較輕量 GPU 上以低 VRAM 運行。

## 使用指南
- 線上 Demo：  
  - LTX-Studio、Fal.ai、Replicate 等平台即時體驗影像到影片生成功能。
- 本地化安裝：
  - Python 3.10+、CUDA 12.2、PyTorch ≥2.1.2（macOS MPS 支援 PyTorch 2.3+）。
  - 可選安裝 FP8 核心以進一步提速（Ada 系列 GPU）。
- 基本推理：
  - 提供 CLI 參數接收提示（prompt）、條件媒體路徑、影格數、解析度及配置檔。
  - Python 函式庫方式直接調用 `infer` API。

## 模型版本與更新
- 0.9.0 ~ 0.9.8 系列持續迭代，重點包含：
  - 解析度與影格數倍數支援（128x、32 整除，8＋1 影格制約）。
  - 蒸餾模型提升迭代速度，無需 Classifier-Free Guidance 及 STG。
  - FP8／8-bit 量化版本達到 2–3× 加速且無明顯質量損失。
  - 新增長片段生成（最高支援 60 秒）、多尺度混合渲染、Prompt 增強、控制 LoRA 細節器（Detailer）等。

## 社群與生態整合
- ComfyUI-LTXVideo：官方推薦的介面化工作流程庫，含多款範例 JSON。
- 社群專案：
  - ComfyUI-LTXTricks：延伸節點（RF-Inversion、FlowEdit、RF-Edit、Frame 插值等）。
  - LTX-VideoQ8：8-bit 加速版本，針對 Ada 架構 GPU 最佳化。
  - TeaCache4LTX-Video：無需訓練的緩存策略，最高可達 2× 推理加速。
- Hugging Face Hub：模型、量化權重、控制 LoRA 均在 HF 平台公開管理，並附授權（OpenRail-M）允許商業使用。

## 訓練與擴充
- LTX-Video-Trainer 提供完整訓練框架，支援：
  - 13B／2B 全量微調。
  - 控制 LoRA 與效果 LoRA 微調。
  - 自定義資料集與特效模型訓練流程。
- 官方論文發表於 arXiv（2501.00103），詳述模型架構、訓練細節與實驗結果，歡迎引用與交流。

## 小結
LTX-Video 以其創新的 DiT 潛空間擴散架構、即時生成性能與豐富的生態整合，為影像 AI 創作領域帶來顛覆性進展。從高品質 13B 模型到輕量蒸餾版本、再到社群驅動的加速與控制專案，LTX-Video 已形成完整生態圈，並持續以快速迭代推動影片生成技術落地。
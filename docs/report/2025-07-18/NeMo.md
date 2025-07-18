# NeMo by NVIDIA

## 一、專案概述
NeMo 是 NVIDIA 推出的可擴展生成式 AI 框架，整合大語言模型（LLM）、多模態（MM）、自動語音辨識（ASR）、文字轉語音（TTS）及電腦視覺（CV）領域。透過 PyTorch Lightning 模組化抽象、Python 配置，以及雲端原生工具，研究人員與開發者可輕鬆地建立、微調與部署各式生成與語音 AI 模型。

## 二、重點特色
- Python 為基礎的組態系統  
  取代傳統 YAML，提供高度可程式化的配置靈活度。  
- 模組化架構  
  採用 PyTorch Lightning，降低實驗與元件替換的門檻。  
- 大規模分散式訓練  
  支援張量平行（TP）、管線平行（PP）、Fully Sharded Data Parallel（FSDP）、Mixture-of-Experts（MoE）等策略，並結合 BFloat16/FP8 混合精度。  
- Day-0 支援 Hugging Face 模型  
  透過 AutoModel 快速使用及微調 CausalLM、Image-Text-To-Text 等熱門模型。  
- 世界模型（Cosmos）完整生態  
  提供從視訊資料蒐集、Curator 處理到擴散與自回歸後訓練的端到端流程。  
- Jetson、Blackwell、GB200、B200 等多硬體優化  
  官方公布多項性能基準與 GPU 調優指南。

## 三、近期更新與亮點
- NeMo 2.0 正式推出  
  強化模組化與易用性，並推出全新實驗啟動工具 NeMo-Run。  
- 新增大型模型支援  
  Llama 4、Flux、Hyena & Evo2、Qwen2-VL、Qwen2.5、Gemma3 及 Qwen3-30B/32B 等。  
- MLPerf Training v4.0 創新紀錄  
  雙 H100 GPU 線性擴充至 11,616 張卡，並刷新 LLM 預訓練與微調性能。  
- 分散式雲端部署  
  支援 Amazon EKS、Google Kubernetes Engine、Slurm 叢集的一鍵起跑範例與 Playbooks。

## 四、安裝與容器化
- Pip／Conda 方式：`nemo_toolkit[all]`  
- NGC PyTorch Container：基於 `nvcr.io/nvidia/pytorch`，手動安裝 NeMo。  
- NGC NeMo Container：即用型映像，整合 LLM、MM、ASR、TTS 全域功能。

## 五、文件與社群資源
- 官方使用者手冊（ReadTheDocs）  
- Playbooks、Tutorials、Examples 程式範例  
- GitHub Discussions 問答社群  
- Contributing 指南與論文、部落格彙整  

## 六、應用場景
- 生成式文字與影像服務  
- 多模態輸入輸出工作流程  
- 即時語音辨識與高品質文字轉語音  
- 自動駕駛、機器人世界模型訓練  

---

NeMo 提供研究者與企業完整的訓練、微調與部署解決方案，透過可擴展、高效能的架構，為生成式 AI 與語音 AI 應用帶來全新可能。
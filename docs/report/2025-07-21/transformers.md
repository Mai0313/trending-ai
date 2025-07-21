# transformers by huggingface

## 簡介  
Hugging Face 的 transformers 是目前最主流的深度學習模型定義框架，支援文本、影像、語音及多模態模型的訓練與推理。透過統一的模型定義，使用者可以跨 PyTorch、TensorFlow、Flax 等多種訓練框架，也能整合各種推理引擎與外部工具（如 DeepSpeed、vLLM、llama.cpp 等），大幅簡化從模型設計到生產部署的流程。

## 主要亮點  
- 支援多種模態：文字（NLP）、影像、語音、自訂多模態任務皆可一站式呼叫  
- 統一 API：只需學習少量抽象類別（如 Pipeline、Model、Tokenizer），即可操控所有預訓練模型  
- 豐富模型庫：Hugging Face Hub 上超過 1 百萬個 Transformers 相關檢查點，涵蓋大型語言模型、 專業視覺/聲音模型與多模態模型  
- 跨框架兼容：同一份模型定義可於 PyTorch、TensorFlow、Flax 之間自由切換，並搭配 Accelerate、DeepSpeed、FSDP 等加速工具  
- 社群生態：開源活躍、文檔齊全，提供眾多範例與範本，並且每年都有多達數千次提交和大量活躍 Issue

## 功能與架構  
- Model 定義：集中管理各大論文中的最先進架構（如 BERT、GPT、T5、Whisper、SAM、BLIP、LayoutLM、Emu3 等）  
- Pipeline：高階推理介面，自動處理前處理、模型推論與後處理；支援文本生成、聊天、影像分類、語音辨識、視覺問答等多種任務  
- Tokenizer、Feature Extractor：統一前處理工具，依模型自動選擇最適切的切詞與特徵抽取方式  
- Trainer / TFTrainer：封裝訓練迴圈，支援分散式訓練、混合精度、動態批次等機制  
- Hub 集成：直接從 Hugging Face Hub 加載或推送模型、權重與配置，無縫整合線上模型管理與分享

## 安裝與快速上手  
transformers 需要 Python 3.9+，並可搭配 PyTorch 2.1+、TensorFlow 2.6+ 或 Flax 0.4.1+ 使用。  
安裝方式：  
- 使用 pip 安裝：pip install "transformers[torch]"  
- 從原始碼安裝：git clone https://github.com/huggingface/transformers.git，cd transformers，pip install .[torch]

使用 Pipeline 執行文字生成示例：  
- 從 transformers import pipeline  
- pipeline(task="text-generation", model="Qwen/Qwen2.5-1.5B")  
- pipeline("要生成的文字提示")

## 支援模型及應用場景  
- 文本：GPT、Llama、BART、T5、Gemma、Mixtral 等生成與理解任務  
- 影像：DINO v2、SAM、OneFormer、VideoMAE 等分類、分割、視覺問答與影片分析  
- 語音：Whisper、自動語音辨識、關鍵字偵測、語音生成等  
- 多模態：BLIP、Qwen-VL、LayoutLM、Emu3、Kosmos-2 等跨模態理解與生成

## 社群與生態  
- GitHub Stars 超過 147k、Forks 約 30k，社群貢獻度高  
- 官方文件提供十餘種語言版本，並持續更新範例與教學  
- 每年舉辦 Hacktoberfest、釋出新模型與版本，並與大型企業及學術單位合作  
- 豐富的衍生專案與第三方整合（如 PyTorch-Lightning、DeepSpeed、llama.cpp、vLLM 等）

## 結語  
transformers 已成為 NLP 及多模態領域最重要的開源基礎建設，對於想快速部署最先進模型、進行研究或打造產線服務的使用者而言，皆能提供高度靈活與可擴展的解決方案。無論是學術研究、企業研發或個人專案，都能透過 Hugging Face Hub 與 Transformers 套件快速起步並持續成長。
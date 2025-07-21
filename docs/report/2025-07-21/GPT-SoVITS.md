# GPT-SoVITS by RVC-Boss

## 簡介  
GPT-SoVITS 是一套結合 GPT 與 SoVITS 模型，針對少量語音樣本（1 分鐘以下）即可實現高品質文字轉語音（TTS）與語音克隆的 WebUI 平台。利用少量微調或零樣本推理，快速生成具備擬真度與情感的多語言語音。

## 亮點  
- 少樣本語音克隆：1 分鐘訓練資料即可得到目標語者高度相似的合成語音  
- 零樣本 TTS：輸入 5 秒參考音，即可立即產生對應聲線的語音輸出  
- 跨語言支援：內建中、英、日、韓、粵語語音模型，可在非母語文本上做推理  
- 一體化 WebUI 工具：語音分離、數據切片、自動標註、ASR 校稿等輔助模組，簡化訓練流程  
- 高速推理：RTX 4060Ti 約 0.028 RTF，RTX 4090 約 0.014 RTF，CPU 也能離線推理  

## 核心功能  
- Zero-shot TTS：以極短語音樣本驅動即時合成  
- Few-shot TTS：1 分鐘微調，提升語者相似度與自然度  
- 多語種前端：整合拼音、G2PW、Roformer 等文本前處理，支援中、日、英、韓、粵語  
- 一站式數據管理：語音伴奏分離（UVR5）、音檔切片、降噪、ASR 自動校正、標註輔助  
- Docker/Conda 雙重環境：支援 CUDA 12.6/12.8、ROCm、MPS（Apple Silicon）、CPU  

## 系統架構  
1. 文本前端：文本正則化 → G2PW 音素轉換 → 拼音對齊  
2. GPT 模型：生成 SoVITS 相容的語音單元序列  
3. SoVITS Base+Vocoder：將單元序列合成 Waveform  
4. 可選工具：UVR5（語音/伴奏分離）、ASR（Faster-Whisper、FunASR）、音訊切割  

## 安裝與使用  
安裝前需準備 Conda 或 Docker 環境  
- Conda 方式  
  1. conda create -n GPTSoVits python=3.10  
  2. conda activate GPTSoVits  
  3. install.sh 指定裝置與來源（CUDA/MPS/CPU + HF 或鏡像）  
- Docker 方式  
  1. 選擇對應 cuda 版本之 gpt-sovits 映像  
  2. docker compose run --service-ports <服務名稱>  
- Windows 一鍵包：下載後雙擊 go-webui.bat 即可啟動  

## 版本與演進  
- V1 → V2：擴充語種、優化文前、預訓練資料量由 2k 小時提升至 5k 小時  
- V3 → V4：提升音色相似度、情感生成穩定度；V4 原生輸出 48k 音頻、去除金屬感  
- V2Pro：在 v2 基礎上優化推理速度與合成品質的進階版本  

## 線上資源  
- Colab Train：即點即用訓練筆記本  
- Hugging Face Demo：免費線上體驗  
- 多語言文件：中文、English、日本語、한국어、Türkçe  
- Change Log、Issue 追蹤、貢獻者名單均公開於 GitHub  

## 授權與致謝  
- 授權：MIT License  
- 致謝：感謝 ar-vits、VITS、BigVGAN、eresnetv2、FunASR、Faster-Whisper 等開源項目及所有貢獻者  
- 特別感謝 Naozumi520 提供粵語數據集與知識指導  
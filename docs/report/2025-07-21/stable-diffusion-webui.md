# stable-diffusion-webui by AUTOMATIC1111

## 一、專案概述
stable-diffusion-webui 是一個基於 Gradio 的網頁介面，旨在為 Stable Diffusion 模型提供完整的互動式使用體驗。此專案彙集了從文字生成影像（txt2img）、影像到影像（img2img）到高階自定義腳本等多種功能，並支援多種硬體平台（NVidia、AMD、Intel、Ascend NPU、Apple Silicon）與各式擴充套件。  
- GitHub 熱門度：★ 154,690，Forks 28,726，Open Issues 2,415  
- 創建時間：2022-08-22，最近更新：2025-07-21  

## 二、主要特色與亮點
1. **多種生成模式**  
   - txt2img（文字→影像）、img2img（影像→影像）、inpainting（修補）、outpainting（延展）  
   - 高解析度修補（Highres Fix）、循環迴圈處理（Loopback）、Prompt Matrix、Prompt Editing  

2. **進階提示與注意力控制**  
   - 局部加強注意力語法：`((keyword))`、`(keyword:1.21)`  
   - 快捷鍵調整權重（Ctrl/Command + Up/Down）  
   - 無字元上限的長提示，支援多重提示合成（AND、權重標記）  

3. **嵌入式訓練與文字反演（Textual Inversion）**  
   - 自訂 embeddings、超網絡（Hypernetworks）、LoRAs  
   - 8GB VRAM 以上即可訓練嵌入，精度可達 16-bit  

4. **影像增強與復原工具（Extras Tab）**  
   - GFPGAN、CodeFormer（人臉修復）  
   - RealESRGAN、ESRGAN、SwinIR、LDSR（超解析度放大）  
   - DeepDanbooru、CLIP Interrogator（反向標註）  

5. **使用者介面與配置**  
   - 即時預覽、進度指示、參數儲存（PNG chunk、EXIF）、參數回讀  
   - 自訂佈局、滑桿範圍、提示長度驗證  
   - Tiling（拼貼紋理）、Batch Processing、API 支援  

6. **擴充與社群生態**  
   - 社群腳本與擴充：History Tab、Aesthetic Gradients、Composable Diffusion  
   - 支援 Stability AI、Alt-Diffusion、Segmind 等多款模型、safetensors 格式  
   - xformers 加速、跨平臺硬體支援教學，並提供線上服務列表  

## 三、架構與技術棧
- 核心語言：Python  
- 深度學習框架：PyTorch、k-diffusion  
- 前端介面：Gradio  
- 第三方工具：xformers、GFPGAN、CodeFormer、RealESRGAN、SwinIR、LDSR  
- 模型管理：Checkpoint、VAE、Hypernetwork、LoRA、Textual Inversion embeddings  
- 配置與自動化：bash/PowerShell 腳本、一鍵安裝、參數檔  

## 四、安裝與執行
1. 依據硬體平台選擇相應安裝說明（NVidia、AMD、Intel、Ascend、Apple Silicon）  
2. 克隆或下載 release package  
3. 執行更新腳本（update.bat 或 webui.sh）並啟動（run.bat 或 webui-user.sh）  
4. 可選擇額外參數：`--xformers`、`--allow-code` 等  

## 五、社群與貢獻
- Wiki 文件：功能、依賴、擴充教學、開發指南  
- Issue 與 Discussion：活躍討論、Bug 回報、功能需求  
- Pull Requests：社群自發擴充腳本、優化策略、跨平台支援  
- 授權條款：MIT License，並在介面中提供第三方原始碼授權聲明  

## 六、結論
stable-diffusion-webui 已成為 Stable Diffusion 使用者的重要入口，憑藉其豐富的功能、靈活的擴充機制與廣泛的社群支持，無論對於創作者還是研究者，都能在此平台上快速實驗、調校與生產高品質的 AI 生成影像。其持續演進的開發與維護，亦確保能跟上最前沿的模型與最佳化技術。
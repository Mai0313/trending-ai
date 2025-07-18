# localGPT by PromtEngineer

## 簡介
LocalGPT 是一個專注於「本機化」、「隱私保護」的開源專案，允許使用者在自己的設備上對文件進行問答，確保所有資料和運算皆留在本地，無須任何網路傳輸。

## 主要功能亮點
- **100% 本機化與私密性**  
  所有文件解析、嵌入向量計算及推論皆在本地執行，無資料外洩風險。  
- **多種模型與量化格式支援**  
  無縫整合 HuggingFace、GPTQ、GGML、GGUF 等各類開放原始碼模型，可依硬體條件選擇最適方案。  
- **彈性嵌入方案與向量庫**  
  採用 InstructorEmbeddings 建置向量，並以 ChromaDB 作為本地檔案式向量存儲庫，可累積多次文件聚合。  
- **重複使用已下載模型**  
  模型只需下載一次，後續可重複使用，不需頻繁拉取。  
- **對話上下文管理**  
  支援單次執行的聊天歷史 (session) 串接，並可匯出為 CSV 進行紀錄與分析。  
- **多介面支援**  
  提供 CLI、REST API 以及基於 Streamlit 的圖形化介面，讓開發者與終端使用者都能輕鬆上手。  
- **跨平台硬體適配**  
  兼容 NVIDIA CUDA、Apple MPS、Intel HPU (Gaudi®) 及純 CPU 運算，實現多元部署可能性。

## 系統架構概覽
- **資料預處理 (ingest.py)**  
  利用 LangChain 解析 .pdf/.txt/.md/.csv/.xls/.docx… 等多種格式，產生對應向量並儲存於本地 ChromaDB。  
- **問答推論 (run_localGPT.py)**  
  以向量檢索獲取最相關語料片段，並呼叫本地 LLM 進行生成，呈現於 CLI 或供 API/GUI 調用。  
- **圖形化與 API (run_localGPT_API.py、localGPTUI.py)**  
  提供後端服務與前端頁面，實現網頁式交互，並可自行定制界面或整合至現有系統。  
- **配置機制**  
  透過 constants.py 設定 MODEL_ID、MODEL_BASENAME 及裝置類型 (device_type)，快速切換模型、量化格式與運算裝置。

## 文件格式支援
- 文本檔：.txt、.md、.py  
- PDF：.pdf  
- 試算表：.csv、.xls、.xlsx  
- Word 文件：.doc、.docx  

## 硬體與系統需求
- Python 3.10 以上  
- VRAM 視 LLM 大小與量化方式而定，範圍約 3.5GB 至 260.8GB，另需為嵌入模型預留 2GB–7GB。  
- 支援 GPU (CUDA/cuBLAS)、Apple M1/M2 (Metal)、Intel Gaudi HPU 及純 CPU 執行。  
- 可選擇使用 Conda 環境或 Docker 容器一鍵部署。

## 主要相依套件
- LangChain：資料連接與向量化流程  
- HuggingFace Transformers：LLM 介面與模型管理  
- InstructorEmbeddings：本地嵌入生成  
- llama-cpp-python：GGML/GGUF 模型推論  
- ChromaDB：本地向量資料庫  
- Streamlit：輕量級圖形化界面  

## 專案現況與社群
- GitHub Stars: 21.4K ；Forks: 2.3K  
- 開放 MIT 授權，Issue 與 PR 積極維護中  
- 豐富教學影片與文件，包含模型切換、硬體優化、Chat History、圖形化操作等範例  
- 受 privateGPT 啟發，旨在實現完全本地化的 RAG（Retrieval-Augmented Generation）解決方案  

## 總結
LocalGPT 提供了一條「隱私至上」的本地化問答研發途徑，結合多款開放原始碼 LLM、向量庫與前後端介面，適合對資料安全要求高或無法使用雲端服務的場景，並具備良好的擴展性與靈活度。
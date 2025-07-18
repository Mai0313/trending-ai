# LocalGPT by PromtEngineer

## 簡介

LocalGPT 是一個開源計畫，提供使用 GPT 模型在本地設備上與文件進行交互的解決方案，確保所有數據均不離開您的設備，以保障 100% 的隱私。此項目讓用戶能安全地在本地環境中與多種格式的文件進行對話，適用於不希望其數據離開設備的情況。

## 關鍵特點

- **高度隱私保護**：所有數據均留在本地設備上，確保最高的安全性。
- **多樣化模型支持**：能夠無縫整合如 HF、GPTQ、GGML、GGUF 等多種開源模型。
- **多重嵌入選擇**：可以選擇多種開源嵌入選項。
- **重用大型語言模型 (LLM)**：下載後可多次使用，無需重複下載。
- **聊天歷史記錄**：能夠記住用戶之前的交談記錄，以便於後續會話。
- **API 支持**：LocalGPT 提供 API，可搭建檢索增強生成 (RAG) 應用。
- **圖形化介面**：LocalGPT 配有兩種圖形介面，分別基於 API 和獨立版本（基於 Streamlit）。
- **多平台支持**：支持 `CUDA`、`CPU`、`HPU (Intel® Gaudi®)` 、`MPS` 等平台。

## 技術細節

LocalGPT 利用 LangChain 和本地模型的力量，能夠在本地運行整個 RAG 流程，無需讓任何數據離開用戶環境，在性能上也相當合理。

- `ingest.py` 使用 LangChain 工具解析文件並通過 `InstructorEmbeddings` 創建嵌入，結果存儲在本地的矢量數據庫中（使用 Chroma 矢量存儲）。
- `run_localGPT.py` 則使用本地 LLM 理解問題並生成答案，通過向量存儲進行相似度搜索，提取出生成答案所需的上下文。
- 本地 LLM 可替換為任何 HuggingFace 上的 LLM，請確保所選 LLM 為 HF 格式。

## 使用技術

LocalGPT 利用了以下技術：

- LangChain
- HuggingFace LLMs
- InstructorEmbeddings
- LLAMACPP
- ChromaDB
- Streamlit

## 統計數據

截至報告撰寫時，LocalGPT 擁有 21,467 個星星（Stargazers）和 2,362 個 Forks，並有 9 個開放議題。

## 結論

LocalGPT 是一個提供在本地環境中安全與文件交互的卓越方案，合乎對隱私保護需求的用戶。其眾多特性及支持多種模型和平台，使其在用戶中相當受歡迎，特別適合需要高度隱私的環境中操作。
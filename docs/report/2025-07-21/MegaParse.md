# MegaParse by QuivrHQ

## 一、專案概述
MegaParse 是一個開源的通用文件解析器，專為大型語言模型（LLM）餵入資料所優化，宣稱在解析過程中達到「無資訊遺失」的目標。支援多種文件格式（PDF、Word、PowerPoint、Excel、CSV、純文字等），並以速度與效能為核心設計理念。

## 二、主要功能
- 全格式支援：PDF、Docx、PPTx、Excel、CSV、純文字檔等  
- 完整內容萃取：表格、目錄（TOC）、章節標題、頁首／頁尾、內嵌圖片  
- 無資訊遺失：強化檢查機制，確保解析結果與原始文件一致  
- 高效能：優化解析流程與資源使用，適合批量文件處理  
- 視覺解析：結合 OCR 與多模態 LLM（如 GPT-4o、Claude 3.5/4）進行影像文件解析  

## 三、技術特色
- Python 3.11+ 開發，使用者可透過 `pip install megaparse` 直接安裝  
- 內部整合 Poppler、Tesseract、libmagic（macOS）等第三方工具以處理 PDF 與影像  
- 提供 RESTful API，使用 Makefile 快速啟動開發伺服器（`make dev`）  
- LangChain 兼容性，支援直接呼叫 LLM 進行語義強化或後處理  
- 模組化設計：未來將增設多項「檢查器」以實現結構化輸出與自訂後處理流程  

## 四、系統架構與流程
1. 前處理：文件偵測格式並安裝必要依賴（Poppler、Tesseract、libmagic）  
2. 解析核心：針對文字、表格、圖片分別應用最適演算法  
3. 視覺解析（可選）：使用 MegaParse Vision 模組呼叫多模態 LLM 以處理複雜影像內容  
4. 結果整合：將各類元素重組成統一的 JSON 或文本塊，並提供結構化或半結構化輸出  
5. API 服務：FastAPI 提供線上解析，並在 `/docs` 自動生成 Swagger 文件  

## 五、使用方式
- 安裝：`pip install megaparse`  
- 環境設定：  
  - 設置 OpenAI/Anthropic API Key  
  - 安裝系統依賴：Poppler、Tesseract、macOS 下需 libmagic  
- 程式調用或透過 HTTP API 上傳文件並獲取解析結果  
- 可選擇啟用 MegaParse Vision 以利用多模態 LLM 處理掃描或含圖文件  

## 六、效能與評測
- 內建基準測試指出 MegaParse Vision 的相似度指標達到 0.87，高於其他常見解析器  
- 用戶可於 `evaluations/script.py` 中新增自訂配置，進行對比實驗並貢獻 PR  
- 持續改善 table checker，並計畫引入更多後處理模組以提升結構化精度  

## 七、未來規劃
- 強化表格檢測與校正能力  
- 擴展模組化檢查器，支持用戶自定義後處理流程  
- 開發純結構化輸出模式，使解析結果更易於程式化存取與系統整合  
- 持續豐富對多模態 LLM 的支援，提升影像及掃描文件的解析品質  

---

MegaParse 致力於成為 LLM 生態中最全面、精準且高效的檔案解析方案，適合開發者、研究者與企業在大規模文件處理與知識管理場景中使用。
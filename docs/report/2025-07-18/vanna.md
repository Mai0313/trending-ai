# vanna by vanna-ai

## 總覽
vanna 是一個開源 MIT 許可的 Python RAG（Retrieval-Augmented Generation）框架，專注於透過大型語言模型（LLM）與檢索增強技術，自動生成並執行 SQL 查詢，實現以自然語言與資料庫互動。

## 主要特色
- Chat with your SQL database：以對話方式向資料庫提問，並自動生成正確的 SQL  
- RAG 架構：結合向量檢索與大模型生成，提升複雜查詢的正確率  
- 多介面支援：Jupyter、Streamlit、Flask、Slack 等多種前端範例  
- 安全私密：資料內容不會傳送到外部 LLM 或向量庫，所有 SQL 執行皆在本地環境  

## 工作流程
1. Train RAG「模型」  
   - 輸入 DDL、業務文件、既有 SQL 查詢等進行向量化與索引  
2. Ask questions  
   - 以自然語言提問  
   - 後端檢索相關知識，並由 LLM 生成符合資料結構的 SQL  
   - 可選擇自動執行並回傳查詢結果與可視化圖表  

## 支援的 LLM
- OpenAI (GPT 系列)  
- Anthropic  
- Google Gemini Chat  
- HuggingFace  
- AWS Bedrock  
- Ollama  
- Qianwen、Qianfan  
- ZhipuAI  

## 支援的向量庫 (VectorStores)
- AzureSearch、Opensearch  
- PgVector、Pinecone  
- ChromaDB、FAISS  
- Marqo、Milvus  
- Qdrant、Weaviate  
- Oracle  

## 支援的資料庫
- PostgreSQL、MySQL  
- PrestoDB、Apache Hive  
- ClickHouse、Snowflake  
- Oracle、Microsoft SQL Server  
- BigQuery、SQLite、DuckDB  

## RAG vs. Fine-Tuning
- RAG：跨 LLM 遷移性佳、成本低、資料可即時移除  
- Fine-Tuning：適合極端 prompt 最小化需求，但訓練與運行成本較高  

## 為什麼選擇 Vanna
- 高精準度：模型能力完全由訓練資料決定，大量且多元的知識可提升大規模資料集執行複雜查詢的正確率  
- 自我學習：可於 Jupyter Notebook 中自動從成功執行的查詢中擷取問答對，或透過 UI 讓使用者回饋，持續優化模型  
- 完整可擴充：提供抽象基底類別，可自行整合或開發新的 LLM 與向量庫  
- 任意前端：可快速嵌入 Slack、Streamlit、Flask、客製化 Web 應用或 BI 平台  

## 擴充與客製化
- VannaBase 抽象基底定義核心訓練與查詢流程  
- 已實作範例：OpenAI + ChromaDB  
- 使用者可依照需求繼承相應類別，自行整合第三方 LLM、向量庫或資料庫連線  

---  
更多資源  
- 文件：https://vanna.ai/docs/  
- 官方網站：https://vanna.ai  
- Discord 支援群組：discord.gg/qUZYKHremx
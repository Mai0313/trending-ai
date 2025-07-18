# Vanna by Vanna-AI

## 簡介

Vanna 是由 Vanna-AI 開發的一款開源的 Python 框架，目標是利用檢索增強生成（RAG）技術，實現準確的文本到 SQL 的轉換功能。透過此工具，使用者可以透過自然語言的查詢與 SQL 資料庫進行互動，並自動生成和執行 SQL 查詢。

## 核心功能

- **RAG 模型訓練與查詢**：使用者只需透過簡單的兩個步驟來運作 Vanna：先用自己的資料訓練 RAG 模型，再透過問答的方式取得 SQL 查詢，並在資料庫中自動執行。
- **支援多樣化的界面**：提供多種使用者界面供選擇，如 Jupyter Notebook、Streamlit、Flask、Slack 等。
- **支援各種大型語言模型（LLMs）**：包括 OpenAI、Anthropic、Gemini、HuggingFace 等多種 LLM。
- **支援多種 VectorStores**：AzureSearch、Opensearch、PgVector、PineCone 等 VectorStores 均可使用。
- **廣泛支援多種資料庫**：Vanna 支援廣泛的 SQL 資料庫，如 PostgreSQL、MySQL、Oracle、Snowflake、DuckDB 等。

## 突出特點

1. **高度準確性**：透過提供更多的訓練資料，提高模型在大型且複雜數據集上的準確性。
2. **安全與私密**：資料庫內容不會被傳送至 LLM 或 VectorStore，所有 SQL 執行均在使用者的本地環境進行。
3. **自我學習**：可選擇在 Jupyter 環境中自動進行成功執行查詢的訓練，或透過介面進行用戶回饋，以提高未來查詢準確性。
4. **跨資料庫支援**：可連接任何能透過 Python 連接的 SQL 資料庫。
5. **自選前端介面**：使用者可選用 Jupyter Notebook、Slackbot、網頁應用或其他自定義介面。

## 擴展性

Vanna 設計上可連接任何資料庫、大型語言模型和 Vector 資料庫。透過實作 VannaBase 抽象基類，使用者能輕鬆拓展使用自己的 LLM 或 VectorStore，並在任意環境中使用 Vanna。

## 總結

Vanna 的設計目的是簡化 SQL 的生成與執行過程，使使用者能夠透過自然語言與資料庫交互。其提供的多樣化的平台支援，讓使用者能隨心選擇不同場景下的使用方式，迅速將理想的查詢轉化為 SQL 語句，具備高效、安全以及強大的學習能力。
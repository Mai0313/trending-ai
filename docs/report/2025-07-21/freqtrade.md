# freqtrade by freqtrade

## 概要
Freqtrade 是一套以 Python 編寫的免費開源加密貨幣交易機器人，旨在支援主要加密交易所，並透過 Telegram 與內建 Web UI 進行操作管理。其功能涵蓋歷史回測、繪圖、資金管理，並透過機器學習與自適應模型（FreqAI）進行策略參數優化。

## 主要特色
- 支援 Python 3.11+，跨平台（Windows、macOS、Linux）。
- 內建 SQLite 資料庫持久化。
- Dry-run 模式可在不動用真實資金的情況下測試策略。
- 回測（Backtesting）與結果可視化分析。
- 超參數優化（Hyperopt）與機器學習策略優化（FreqAI）。
- 動態／靜態貨幣白名單與黑名單。
- 內建 Web UI 及 Telegram RPC 機制供遠端監控與指令控制。
- 支援法幣報表與績效統計。

## 支援交易所
- 現貨（Spot）：Binance、Bitmart、BingX、Bybit、Gate.io、HTX、Hyperliquid、Kraken、OKX…等（基於 CCXT）。
- 衍生性商品（Futures，實驗性）：Binance、Bybit、Gate.io、OKX、Hyperliquid。
- 社群測試：Bitvavo、KuCoin。

## 技術棧與架構
- 核心語言：Python 3.11+。
- 交易所介面：CCXT 函式庫。
- 資料庫：SQLite。
- UI 控制：FastAPI/WebSockets（Webserver 模組）、python-telegram-bot。
- 機器學習：內建 FreqAI 模組，可結合多種 ML 演算法做策略自動調參。
- 容器化部署：Docker 支援，提供快速啟動範本。

## 使用流程
1. 安裝與環境準備：Python、pip、virtualenv、TA-Lib，或使用 Docker 影像。
2. 建立使用者目錄與初始設定 (`create-userdir`、`new-config`)。
3. 下載歷史 K 線資料 (`download-data`)。
4. 撰寫或產生策略範本（`new-strategy`），可配置指標、ROI 條件、風控參數。
5. 進行回測 (`backtesting`)、繪圖分析 (`plot-profit`)、超參數優化 (`hyperopt`)。
6. 切換至 Dry-run 或正式交易模式（`trade`），並透過 Telegram／Web UI 下達啟停與查詢指令。

## 核心 CLI 功能一覽
- trade、backtesting、hyperopt、strategy-updater、webserver
- 下載／轉換資料：download-data、convert-data、trades-to-ohlcv
- 列表查詢：list-exchanges、list-pairs、list-strategies
- 繪圖視覺化：plot-dataframe、plot-profit
- 偏差檢測：lookahead-analysis、recursive-analysis

## 開發與貢獻
- 分支策略：  
  - `develop`：最新功能開發，較活躍且追求穩定。  
  - `stable`：已測試穩定版本。  
  - `feat/*`：個別新功能分支。  
- 持續整合：GitHub Actions CI、Coveralls 測試覆蓋、CodeClimate 可維護性評分。
- 文件與社群：官方文件（Read the Docs）、Discord 社群討論、GitHub Issue/PR 流程完備。

## 社群與支持
- Discord 伺服器：即時技術交流與問題排解。
- 問題回報：GitHub Issue 追蹤。
- 功能建議：Issue 標籤 enhancement。
- 拉取請求：對準 `develop` 分支，遵循 CONTRIBUTING.md 規範。
- Good first issue：新手友善標籤，歡迎初次貢獻。

## 專案指標
- Stars：40,636
- Forks：8,150
- Open Issues：37
- 最近更新時間：2025-07-21
- 預設分支：develop

Freqtrade 透過豐富的功能和活躍的社群，為想要以程式化方式進行加密貨幣交易的使用者提供了一個全方位且高度可擴充的解決方案。
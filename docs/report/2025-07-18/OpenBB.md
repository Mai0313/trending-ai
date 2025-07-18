# OpenBB by OpenBB-finance

## 簡介

OpenBB 是一個開源的投資研究平台，致力於讓所有人都能夠隨時隨地進行投資研究。該平台提供了廣泛的投資研究工具，覆蓋股票、期權、加密貨幣、外匯、宏觀經濟學、固定收益等領域，並可根據用戶需求提供擴展功能。此平台主要以 Python 和命令行界面（CLI）進行操作。

## 基本資訊

- **GitHub URL:** [https://github.com/OpenBB-finance/OpenBB](https://github.com/OpenBB-finance/OpenBB)
- **主要程式語言:** Python
- **Stars 數量:** 43,118
- **Forks 數量:** 3,864
- **Open Issues 數量:** 54

## 平台功能

OpenBB 平台讓用戶可以訪問不同領域的數據，並通過擴展功能根據用戶需求增強使用體驗。透過安裝 Python 封包，使用者可以快速上手：

### 安裝與開始使用

- 使用 PyPI 安裝: `pip install openbb`
- 獲取股票歷史價格範例：

  ```python
  from openbb import obb
  output = obb.equity.price.historical("AAPL")
  df = output.to_dataframe()
  ```

## OpenBB Workspace

OpenBB Workspace 是一個企業用戶界面，用於視覺化數據集和利用 AI 代理。它將平台與許多數據供應商集成，並通過 Python 或 CLI 提供操作界面。使用者可以在此平台上運行 AI 代理，並進行更深入的數據分析。

### 整合工具

- **數據整合:** 可通過 [docs](https://docs.openbb.co/workspace) 或 [GitHub repo](https://github.com/OpenBB-finance/backends-for-openbb)了解更多細節。
- **AI 代理整合:** 可通過 [GitHub repo](https://github.com/OpenBB-finance/agents-for-openbb)了解更多細節。

## 社群與支持

OpenBB 非常積極地進行社群互動。用戶可以通過以下方式參與：

- **Discord:** [https://discord.com/invite/xPHTuHCmuV](https://discord.com/invite/xPHTuHCmuV)
- **Twitter:** [https://x.com/openbb_finance](https://x.com/openbb_finance)

## 貢獻方式

此專案歡迎各種方式的貢獻，您可以：

- 成為貢獻者，詳細信息請參見 [Contributing Documentation](https://docs.openbb.co/platform/developer_guide/contributing)
- 創建 GitHub 子議題

## 授權與風險

OpenBB 平台使用 AGPLv3 授權。若您決定進行金融交易，請充分瞭解其風險及成本，並仔細考慮您的投資目標、經驗和風險承受能力，必要時請尋求專業意見。
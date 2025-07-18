# OpenBB by OpenBB-finance

## 一、專案概述
OpenBB 是一個開源的投資研究平台，旨在為各種層級的使用者提供統一且自由存取的金融市場數據及分析工具。專案持續活躍於 GitHub，擁有超過 43k 的 stars、3.8k 的 forks，並定期更新以支援最新的市場需求與技術。

## 二、主要功能亮點
- 全面金融資產支援：涵蓋股票、選擇權、衍生性商品、加密貨幣、外匯、固定收益與宏觀經濟指標等多元資產類別。
- 雙介面設計：提供 Python API 與命令列 CLI，滿足程式化與互動式操作需求。
- 擴充性強：利用模組化架構，輕鬆整合第三方數據源與 AI 代理，並可與 OpenBB Workspace（企業級視覺化介面）結合。
- 自架部署：內建 FastAPI 後端伺服器（預設埠號 6900），可在本地或雲端迅速啟動並串接工作區。
- 多種安裝管道：PyPI 套件（pip install openbb）、GitHub 原始碼、Dev Containers、GitHub Codespaces、Google Colab 範例等多元開發環境支援。

## 三、技術架構
- 語言與框架：主要以 Python 撰寫，後端採用 FastAPI + Uvicorn，CLI 基於 Click／Rich。
- 模組化程式庫：分門別類的 `equity`、`crypto`、`fixed_income`、`macro`、`options`、`forex` 等子套件，API 呼叫方式統一且直觀。
- 擴充整合：開放原始碼的後端 Data Backends（backends-for-openbb）與 AI Agents（agents-for-openbb）專案，方便社群持續貢獻與擴增功能。
- 持續整合與測試：GitHub Actions 管線自動化測試、品質檢查與多版本相容性驗證。

## 四、安裝與使用
- Python 環境：支援 Python 3.9.21 至 3.12
- 安裝指令：pip install openbb
- CLI 安裝：pip install openbb-cli
- 啟動後端：openbb-api
- 快速測試：透過瀏覽器開啟 http://127.0.0.1:6900，可檢視內建的 Swagger 文件與 API 列表。
- 範例程式片段：  
  從 Python 程式中匯入並取得蘋果公司歷史股價：  
  `from openbb import obb`  
  `df = obb.equity.price.historical("AAPL").to_dataframe()`

## 五、生態系統與擴充
- OpenBB Workspace：企業級視覺化應用，結合 AI 代理與資料展板，讓非 Python 使用者也能快捷操作。
- Data Integrations：官方文件提供詳細資料來源列表，也可參考 backends-for-openbb 源碼自行增加 API 支援。
- AI Agents：透過 agents-for-openbb 專案，將 LLM 或其他智能代理與資料平台接軌，打造自動化策略分析與報告生成。
- 社群互動：活躍於 Discord、X（Twitter）、官方 Hub 平台，並定期舉辦黑客松與開發挑戰。

## 六、貢獻與社群支持
- 開放授權：AGPLv3，強調回饋與社群共享。
- 貢獻管道：GitHub Issue、Pull Request、官方 Discord 回報與討論；另有完善的開發指南與測試樣板。
- 聯絡方式：support@openbb.co（技術支援）、hello@openbb.co（合作與夥伴）。
- 社群成員：超過數百位貢獻者共同維護，並定期更新星數成長圖以紀錄專案發展里程碑。

---

以上即為 OpenBB by OpenBB-finance 的技術報告，重點突顯其開源金融研究平台架構、功能模組化設計與完善的生態系統支持，適合量化分析師、程式交易員與金融科技開發者深入使用與貢獻。
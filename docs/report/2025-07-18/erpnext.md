# erpnext by frappe

## 簡介  
ERPNext 是一套 100% 開源的企業資源規劃系統（ERP），由 Frappe 團隊維護，旨在整合企業所需的會計、庫存、製造、人力資源、CRM、專案管理等各項功能，並提供現代化的使用者介面及完整的擴展性。

## 主要功能亮點  
- 完整財務會計：從日常分錄、應收應付到損益表、資產負債表等多種報表  
- 訂單與庫存管理：支援多倉儲、多單位換算、採購、銷售、出貨、補貨自動化  
- 製造模組：物料需求計畫（MRP）、工單管理、成本估算、外包加工追蹤  
- 資產管理：資產折舊、維保週期、人員分配與報修流程  
- 專案管理：任務分派、工時登錄、專案進度與盈虧追蹤  
- 客戶關係管理（CRM）：客戶檔案、銷售線索、商機與活動管理  
- POS 與零售：線上、線下收銀、條碼掃描、會員積點  

## 核心技術棧  
- Frappe Framework：以 Python 與 JavaScript 為基礎的全端 Web 應用框架，提供 metadata 驅動的資料庫層、權限管理與 REST API  
- Frappe UI：基於 Vue.js 的現代化元件庫，用於快速構建單頁應用（SPA）  
- 資料庫：推薦使用 MariaDB  
- 部署：支援 Docker Compose、bench CLI，以及傳統手動安裝方式  

## 部署與開發流程  
- Docker 方案：透過 frappe_docker 倉庫與 docker-compose 快速啟動開發或測試環境  
- bench CLI：一鍵建立全套開發環境，管理多個站點與應用安裝  
- 本地開發：bench start + bench new-site + bench get-app/ install-app  
- 支援 ARM 架構與多種 CI/CD 自動化測試  

## 社群與學習資源  
- 文件與 API 參考：docs.frappe.io / docs.erpnext.com  
- 線上課程：Frappe School 提供免費與進階教學  
- 討論區：discuss.erpnext.com  
- 即時社群：Telegram 群組、GitHub Issues  
- 參與貢獻：Issue 指南、Pull Request 流程、Crowdin 翻譯平台  

## 結論  
ERPNext 以其全面的模組覆蓋、開源透明的開發模式及強大的社群生態，為中小企業至大型組織提供具備高度彈性及擴展性的 ERP 解決方案。無論以自託管或雲端服務方式部署，都能快速上手並持續依需求定製化。
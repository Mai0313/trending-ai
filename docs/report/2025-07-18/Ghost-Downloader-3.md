# Ghost-Downloader-3 by XiaoYouChR

## 專案概述
Ghost-Downloader-3 是一款以 Python 打造的跨平台多線程下載器，採用 Fluent Design 介面並內建 AI 加速與 QUIC/HTTP3 支援，具備類似 IDM 的智慧分片機制，無需後續檔案合併即可高速下載。

## 亮點
- AI 智慧加速：自動調整分片數量與併發策略，提高下載穩定度與速度  
- QUIC/HTTP3 支援：底層使用 curl-cffi，可模擬瀏覽器協議指紋，突破傳統 TCP 瓶頸  
- 可擴充插件架構：未來計畫開放插件機制，讓開發者能以 Python 擴展各種功能  
- 跨平台 GUI：基於 PyQt-Fluent-Widgets (或 PySide6) 實現現代化 Fluent Design 介面，同時支援 Windows、macOS、Linux  
- 智能分片無縫下載：彈性切割下載任務，減少磁碟 I/O，無須額外合併步驟  

## 技術棧
- Python 3.x  
- PyQt6 / PySide6 (GUI)  
- curl-cffi（QUIC/HTTP3 客戶端）  
- asyncio 與多線程並行  
- Loguru（日誌管理）  
- Nuitka（可選的 Python 編譯器）  

## 主要功能
- 任務管理：新增/編輯/刪除下載任務  
- 全局與單任務速率限制  
- 計劃任務排程  
- 瀏覽器擴充套件支援（持續優化中）  
- AUR 套件：community-maintained ghost-downloader-bin / ghost-downloader-git  

## 支援平台
- Windows 7 SP1 以上（x86_64 / arm64）  
- macOS 11.0 以上（x86_64 / arm64）  
- Linux glibc 2.35+（x86_64 / arm64）  

## 開發現狀與路線圖
已完成
- 全局設定、下載詳情面板  
- 排程任務  
- 全局速率限制  
- 記憶體優化（Qt 升級、HttpClient 重用）

進行中
- 部分多線程替換為協程

未來計畫
- 將 MVC 重構為 MVVM 並採用事件驅動架構  
- 強化任務編輯、支援多 Client 綁定同一任務  
- Magnet/BT 下載（考慮整合 libtorrent）  
- 完善插件系統與瀏覽器擴充功能  

## 社群與貢獻
- GitHub Stars：3501  
- Forks：174  
- Open Issues：29  
- Bug 報告與功能請求範本  
- 聯絡方式：XiaoYouChR@qq.com、QQ 群  

## 總結
Ghost-Downloader-3 結合了 AI 加速、QUIC 協議與現代化 GUI，提供使用者高效、穩定且易於擴充的下載體驗。專案正積極迭代中，歡迎開發者與使用者共同參與並提出建議。
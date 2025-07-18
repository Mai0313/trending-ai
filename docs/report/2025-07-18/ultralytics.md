# ultralytics by ultralytics

## 概述
- 一個由 Ultralytics 團隊開發、以 YOLO 系列模型為核心的全功能電腦視覺框架
- 支援目標檢測、實例分割、追蹤、影像分類、姿態估計、導向邊界框等多種任務
- 包含 CLI 工具與 Python API，方便使用者快速上手與整合至各種應用場景
- 提供豐富的預訓練模型（YOLO11 家族）及自動下載機制，並具備高效能與可擴充性

## 專案亮點
- 模型速度快、精度高：在 COCO、ImageNet、DOTA 等主流資料集上均有領先表現  
- 全方位任務支援：單一套件即可完成偵測、分割、分類、追蹤、姿態估計及導向邊界框  
- 易用的 CLI：
  - `yolo predict model=yolo11n.pt source=路徑` 即可執行推論  
  - 支援各種附加參數如影像尺寸、批次大小、輸出格式等  
- 靈活的 Python API：
  - 透過 `from ultralytics import YOLO` 載入模型並呼叫 `.train()/.val()/.export()` 等方法  
  - 同樣接受 CLI 等價的設定參數，簡化程式碼撰寫

## 核心功能
- 自動下載與管理 YOLO 預訓練權重  
- 支援 PyTorch、ONNX、TensorRT 等多種部署格式  
- 佈署前後的效能評估：mAP、推理速度（CPU Onnx、GPU TensorRT）  
- 豐富的模型家族：
  - YOLO11n/s/m/l/x（檢測 & 追蹤）  
  - YOLO11*-seg（實例分割）  
  - YOLO11*-cls（影像分類）  
  - YOLO11*-pose（姿態估計）  
  - YOLO11*-obb（導向邊界框）  

## 效能表現
- 在 COCO val2017 上，YOLO11s 達到約 47% mAP，ONNX CPU 約 90ms，TensorRT GPU 約 2.5ms  
- 在 ImageNet 上，YOLO11s-cls top1 約 75.4%、ONNX CPU 約 7.9ms、TensorRT GPU 約 1.3ms  
- 在 DOTA v1 測試集中，YOLO11s-obb mAP 約 79.5%、ONNX CPU 約 219ms、TensorRT GPU 約 5.1ms  

## 整合與擴充
- 與主流實驗追蹤服務整合：Weights & Biases、Comet ML  
- 支援資料標註與管理：Roboflow  
- 加速推理：Intel OpenVINO、Neural Magic DeepSparse  
- 提供 Ultralytics HUB 平台，一站式資料可視化、模型訓練與部署體驗  

## 專案架構
- 根目錄包含核心程式庫、CLI 腳本、文件資源與範例  
- pyproject.toml 定義相依套件，Python>=3.8、PyTorch>=1.8  
- examples 資料夾提供入門教學與 Jupyter Notebook 範例  
- docs 與 README.md 詳載使用說明與模型性能指標  

## 安裝與使用
- 透過 pip 安裝：pip install ultralytics  
- 支援 Conda、Docker 以及原始碼編譯  
- CLI 與 Python API 均可接續相同參數設定，無須額外調整  

## 授權與社群
- 雙授權選擇：
  - AGPL-3.0：鼓勵開源協作  
  - 商業企業授權：滿足商用需求  
- 社群活躍度高：
  - GitHub Stars: 43K+，Forks: 8.4K+  
  - Discord、Reddit、Forum 等多元討論平臺  
  - 定期更新、CI 自動化測試保障品質

## 小結
Ultralytics/ultralytics 是一個完整且靈活的深度學習電腦視覺框架，結合了高效能的 YOLO11 系列模型、簡便的 CLI 與 API，以及多樣化的任務與部署選項，適合研究、開發與商業應用，並透過社群與平台整合持續演進。
# Titel : issj_hrm_services (人事部用アプリ)
Application for HR management services ISSJ

streamlitによる直感的なUI作成
![](images/menu.png)

## 概要
経歴書のアップロード：
　これまでローカルで保管していた候補者の経歴書を、本アプリケーションを通じてアップロードします。

情報の自動抽出と保存：
　アップロードされた経歴書から必要な情報（スキル、職歴、資格など）を自動で抽出し、GitHubデータベースに保存します。

分析用データの生成とダウンロード：
　抽出した情報を分析用の指定フォーマットに変換し、ダウンロード可能とします。これにより、より精度の高いデータ分析が可能になります。

最適な候補者の提案：
　蓄積・分析した情報をもとに、お客様のニーズにしっかりと寄り添った最適な人材をご提案します

## 主な機能

### 1. マルチLLMプロバイダー対応

### 2. Webインターフェース (`app.py`)
- Streamlitベースの使いやすいUI


### 1. 必要なパッケージのインストール
```bash
pip install -r requirements.txt
pip install google-generativeai
pip install openai
```

## 使用方法


### A. Webインターフェースでの実行（推奨）

1. Streamlitアプリケーションを起動：
```bash
streamlit run app.py
```

2. ブラウザで以下のURLにアクセス：
```
http://localhost:8502
```

3. Webインターフェースの使用手順：

### B. コマンドライン実行

## データ形式

## 制限事項

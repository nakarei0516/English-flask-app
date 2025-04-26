# English-flask-app
# 英単語帳管理アプリ（Flask × SQLite）

FlaskとSQLiteを使用して開発した、英単語を登録・管理できるシンプルなWebアプリケーションです。  
ユーザーごとに個別の単語帳を作成・管理できるシステムを実装しました。

---

## 主な機能
- 新規ユーザー登録・ログイン・ログアウト機能
- 単語と意味を登録・表示・削除
- 同じ単語の重複登録を防止
- レスポンシブ対応（Bootstrap5使用）
- セキュリティ対策（パスワードハッシュ化保存）

---

## 使用技術
- Python 3
- Flask
- SQLite
- Flask-Login
- Bootstrap5
- Jinja2 (テンプレートエンジン)

---

## デモ画面
[アプリ画面]
(![スクリーンショット１](https://github.com/user-attachments/assets/566a420a-f248-49fc-ab57-26bcf8ffae55))
![スクリーンショット２](https://github.com/user-attachments/assets/d2df5c8e-9f03-4649-910e-743661d0c128)
![スクリーンショット３](https://github.com/user-attachments/assets/09057f01-4cac-403b-a294-060f6713d3fd)



---

## ディレクトリ構成
vocab-flask-app/ ├── app.py ├── models.py ├── requirements.txt ├── templates/ │ ├── base.html │ ├── login.html │ ├── signup.html │ ├── vocab.html │ └── index.html └── static/（オプション）

## セットアップ手順

1. リポジトリをクローン
2. 仮想環境を作成・有効化
3. `pip install -r requirements.txt`で依存関係をインストール
4. `python app.py`で起動

---

## 今後の改善予定
- 単語編集機能
- 単語クイズ機能
- タグ分類機能

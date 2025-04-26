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
![スクリーンショット1]![image](https://github.com/user-attachments/assets/eb226244-9f9a-4851-a005-edc0903133f6)
![スクリーンショット２]![image](https://github.com/user-attachments/assets/4f4ec858-07a9-4e58-857a-7c6ebaf456b7)
![スクリーンショット３]![image](https://github.com/user-attachments/assets/8ea68edc-800e-4555-b8a3-835bae6dce77)
![スクリーンショット４]![image](https://github.com/user-attachments/assets/b73b2ee5-22d0-4cd6-9e77-373e81f4bc68)
![スクリーンショット５]![image](https://github.com/user-attachments/assets/58d7e188-1415-4a29-8b6e-59f16438a30a)





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

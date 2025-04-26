from flask import Flask, render_template, request, redirect, url_for
from flask_login import LoginManager, login_user, login_required, logout_user, UserMixin, current_user
from werkzeug.security import generate_password_hash, check_password_hash
import models

app = Flask(__name__)
app.secret_key = 'your-secret-key'

login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = "login"

# ユーザークラス
class User(UserMixin):
    def __init__(self, id_, username):
        self.id = id_
        self.username = username

    @staticmethod
    def get(user_id):
        db = models.connect_db()
        user = db.execute("SELECT * FROM user WHERE id = ?", (user_id,)).fetchone()
        if not user:
            return None
        return User(user["id"], user["username"])

    @staticmethod
    def find_by_username(username):
        db = models.connect_db()
        user = db.execute("SELECT * FROM user WHERE username = ?", (username,)).fetchone()
        if not user:
            return None
        return User(user["id"], user["username"])

@login_manager.user_loader
def load_user(user_id):
    return User.get(user_id)

# ログイン
@app.route("/login", methods=["GET", "POST"])
def login():
    error = ""
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]
        db = models.connect_db()
        user = db.execute("SELECT * FROM user WHERE username = ?", (username,)).fetchone()
        if user and check_password_hash(user["password"], password):
            user_obj = User(user["id"], user["username"])
            login_user(user_obj)
            return redirect("/")
        error = "ログイン情報が間違っています"
    return render_template("login.html", error=error)

# サインアップ
@app.route("/signup", methods=["GET", "POST"])
def signup():
    error = ""
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]            
        db = models.connect_db()
        existing = db.execute("SELECT * FROM user WHERE username = ?", (username,)).fetchone()
        if existing:
            error = "そのユーザー名はすでに使われています"
        else:
            hash = generate_password_hash(password)
            db.execute("INSERT INTO user (username, password) VALUES (?, ?)", (username, hash))
            db.commit()
            return redirect("/login")
    return render_template("signup.html", error=error)

# ログアウト
@app.route("/logout")
@login_required
def logout():
    logout_user()
    return redirect("/login")

# 単語一覧表示
@app.route("/vocab")
@login_required
def vocab():
    db = models.connect_db()
    vocab_list = db.execute("SELECT * FROM word WHERE user_id = ?", (current_user.id,)).fetchall()
    return render_template("vocab.html", vocab_list=vocab_list)

# 単語追加
@app.route("/add_word", methods=["POST"])
@login_required
def add_word():
    word = request.form["word"]
    meaning = request.form["meaning"]

    if not word or not meaning:
        return redirect(url_for("vocab"))  # skip if empty
    
    db = models.connect_db()
    
     # Check if word already exists for the user
    existing = db.execute(
        "SELECT * FROM word WHERE word = ? AND user_id = ?",
        (word, current_user.id)
    ).fetchone()

    if existing:
        # You could add a flash message here too
        return redirect(url_for("vocab"))  # Don't add duplicate
    
    db.execute(
        "INSERT INTO word (word, meaning, user_id) VALUES (?, ?, ?)",
        (word, meaning, current_user.id)
    )
    db.commit()
    return redirect(url_for("vocab"))

# 単語削除
@app.route("/delete_vocab/<int:id>")
@login_required
def delete_vocab(id):
    db = models.connect_db()
    db.execute("DELETE FROM word WHERE id = ? AND user_id = ?", (id, current_user.id))
    db.commit()
    return redirect(url_for("vocab"))

@app.route("/")
def index():
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)

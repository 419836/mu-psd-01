import json
import datetime
from flask import Flask
from flask_cors import CORS
import pickledb

app = Flask(__name__)
CORS(app)

db = pickledb.load('example.db', False)
# ここまで定型文、触らなくて良い

# データベースの初期設定
# キー：countに0を設定
db.set("count",0)

# URL「/」に対する処理関数
@app.route("/")
def index():
    # 戻り値がそのままWebサイトに表示される。
    return "This is Backend API Server."

# データ登録サンプル関数
# URLルーティングの<id>,<val>がそれぞれ関数の引数に入ってくる。
@app.route("/adddata/<id>/<val>")
def add_data(id,val):
    # 引数のデータをDBに格納
    db.set(id,val)
    db.dump() # DB保存処理を忘れずに

    # 元の画面に返す処理結果を整形する。
    ret={
        "id":id,
        "value":val
    }
    print(json.dumps(ret)) # 試しに表示してみる。
    return json.dumps(ret)

# データ照会サンプル関数
# URLルーティングの<id>が関数の引数のidに入ってくる。
@app.route("/getdata/<id>")
def get_data(id):
    # 画面に返す処理結果を整形する。
    ret={
        "id":id,
        "value":db.get(id)
    }
    print(json.dumps(ret)) # 試しに表示してみる。
    return json.dumps(ret)


# ここから定型文、触らなくて良い
if __name__ == "__main__":
    app.run(debug=True)

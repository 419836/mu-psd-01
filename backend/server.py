from flask import Flask,jsonify
from flask_cors import CORS
import pickledb

app = Flask(__name__)
CORS(app)

db = pickledb.load('example.db', False)
# ここまで定型文、触らなくて良い
###################################################################


# データベースの初期設定 サンプルデータを登録しておく
db.set("1","ああああ")
db.set("123","いいいい")
db.set("1234","うううう")

# URL「/」に対応して処理する関数
@app.route("/help")
def index():
    # 戻り値がそのままWebサイトに表示される。
    return jsonify({"result":"This is Backend API Server."})


# データ登録サンプル関数
# URLルーティングの<id>,<val>がそれぞれ関数の引数に入ってくる。
@app.route("/adddata/<id>/<val>")
def add_data(id,val):
    db.set(id,val)      # 引数のデータをDBに格納
    db.dump()           # DB保存処理を忘れずに
    return jsonify({"result":id + ":added."})


# データ検索関数
# URLルーティングの<search>が関数の引数のidに入ってくる。
@app.route("/find/<search>")
def find_data(search):
    ret=[]                     # 戻り値：検索結果リストを空で作る
    for key in db.getall():    # 全部のキーを調べる
        if search in key:      # 検索文字列がキーに含まれているか、判定 
            ret.append({       # DBのキーと値を検索結果リストに追加
                "id":key,
                "val":db.get(key)
            })
    return jsonify(ret)        # JSON形式で表示する


###################################################################
# ここから定型文、触らなくて良い
if __name__ == "__main__":
    app.run(debug=True)

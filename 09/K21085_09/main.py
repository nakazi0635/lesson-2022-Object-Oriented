from flask import Flask, request, render_template, jsonify
import json  # Python標準のJSONライブラリを読み込んで、データの保存等に使用する

app = Flask(__name__)
app.config["JSON_AS_ASCII"] = False  # 日本語などのASCII以外の文字列を返したい場合は、こちらを設定しておく


# http://127.0.0.1:5000/address
@app.route('/address', methods=["GET"])
def address_get():

    # 検索パラメータの取得
    p_first_name = request.args.get('fn', None)
    p_last_name = request.args.get('ln', None)
    # name = request.form.get("name")
    p_email = request.args.get('em', None)

    print(p_first_name, p_last_name, p_email)

    with open('address.json') as f:
        json_data = json.load(f)

    # パラメータにより返すデータをフィルタリングする
    if p_first_name is not None:
        json_data = list(filter(lambda item: p_first_name.lower()
                         in item["first_name"].lower(), json_data))
    if p_last_name is not None:
        json_data = list(filter(lambda item: p_last_name.lower()
                         in item["last_name"].lower(), json_data))
    if p_email is not None:
        json_data = list(filter(lambda item: p_email.lower()
                         in item["email"].lower(), json_data))

    return jsonify(json_data)

# データ検索
# http://127.0.0.1:5000/address


@app.route('/address', methods=["POST"])
def address_post():
    print("送信されました")
    p_first_name = request.form.get('fn', None)
    p_last_name = request.form.get('ln', None)
    p_email = request.form.get('em', None)

    json_open = open('address.json', 'r')
    j = json.load(json_open)
    dic = {"email": p_email, "first_name": p_first_name, "last_name": p_last_name}
    j.append(dic)
    print(j)
    with open('address.json', 'w') as file:
        json.dump(j, file, indent=4, ensure_ascii=False)
        print("書き込みが完了")
    return jsonify(j)


# http://127.0.0.1:5000/
@app.route('/')
def index():
    return render_template("addressbook.html")


if __name__ == "__main__":
    # debugモードが不要の場合は、debug=Trueを消してください
    app.run(debug=True)

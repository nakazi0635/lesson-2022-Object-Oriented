from flask import Flask, request, render_template
import datetime
import random   # ランダムデータ作成のためのライブラリ


app = Flask(__name__)
# 1. プロジェクトのトップ（じゃんけんアプリや、課題のアプリへのリンクを配置するだけ）


@app.route('/')
def index():
    return render_template('index.html')


# 2. じゃんけんアプリの入力フォーム
@app.route('/janken')
def janken():
    # じゃんけんの入力画面のテンプレートを呼び出し
    return render_template('janken_form.html')


# 3. じゃんけんデータ送信先とじゃんけん結果表示画面
@app.route('/janken/play', methods=["POST"])
def janken_play():
    # <input type="text" id="your_name" name="name">
    name = request.form.get("name")
    if not name:
        name = "名無しさん"

    # <input type="radio" id="hand_rock" value="rock" name="hand">
    # <input type="radio" id="hand_scissor" value="scissor" name="hand">
    # <input type="radio" id="hand_paper" value="paper" name="hand">
    hand = request.form.get("hand", None)
    settai = request.form.get("is_settai")
    # print(settai)
    # print(hand)
    if hand is None and settai == "on":
        hand = "rock"

    # リストの中からランダムに選ぶ
    cpu = random.choice(["rock", "scissor", "paper"])

    if settai == "on" and hand == "rock":
        cpu = "scissor"
    elif settai == "on" and hand == "scissor":
        cpu = "paper"
    elif settai == "on" and hand == "paper":
        cpu = "rock"

    # じゃんけん処理
    if settai == "on":
        result_message = "{}の勝ち".format(name)
    elif hand == cpu:
        result_message = "あいこ"
    else:
        if hand == "rock":
            if cpu == "scissor":
                result_message = "{}の勝ち".format(name)
            else:
                result_message = "{}の負け".format(name)
        elif hand == "scissor":
            if cpu == "paper":
                result_message = "{}の勝ち".format(name)
            else:
                result_message = "{}の負け".format(name)
        elif hand == "paper":
            if cpu == "rock":
                result_message = "{}の勝ち".format(name)
            else:
                result_message = "{}の負け".format(name)
        else:
            result_message = "後出しはダメです。"

    # 渡したいデータを先に定義しておいてもいいし、テンプレートを先に作っておいても良い
    return render_template('janken_play.html',
                           result_message=result_message,
                           name=name,
                           settai=settai,
                           hand=hand,
                           cpu=cpu)


@app.route('/uranai')
def uranai():
    return render_template('uranai_form.html')


@app.route('/uranai/play', methods=["POST"])
def uranai_play():
    uranai_list = [5, 1, 3, 2, 4]
    uranai_comment_list = ["運勢がいいですね！いい1日になるでしょう。", "運勢が悪いので気をつけましょう。",
                           "いたって普通です。", "いつもより少しだけ気をつけたほうがいいかもしれません。", "ちょっといいことあるかも？"]
    # uranai_comment = "入力不備で占えませんでした"

    birthday = request.form.get("birthday")
    name_len = len(request.form.get("name"))
    dt_replace = True
    dt_now = datetime.date.today()
    # datetime型はstr型に変換する必要あり？
    dt_now = dt_now.strftime("%Y%m%d")
    dt_now = int(dt_now.replace('-', ''))
    try:
        birthday = int(birthday.replace('-', ''))
        date_difference = abs((dt_now) - (birthday)) * name_len
        uranai_result = uranai_list[date_difference % 5]
        uranai_comment = uranai_comment_list[date_difference % 5]
    except Exception:
        dt_replace = False
        uranai_comment = "入力不備で占えませんでした"
    print(type(name_len))

    if name_len == 0 or birthday is None or not len(str(birthday)) == 8 or not dt_replace:
        uranai_result = 1
        uranai_comment = "入力不備で占えませんでした"

    print(uranai_result)
    print(uranai_comment)
    return render_template('uranai_play.html',
                           uranai_result=uranai_result,
                           uranai_comment=uranai_comment)


if __name__ == '__main__':
    app.run(debug=True)

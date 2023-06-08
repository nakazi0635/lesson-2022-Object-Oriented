// データの初期表示
console.log('JavaScript index.js fire!') 
fetch("/address").then(response => { ///addressが取得されたら.then移行が実行される
    // console.log(response);
    response.json().then((data) => { //responseをjsonに変換できたら.then移行が実行される
        console.log(data);  // 取得されたレスポンスデータをデバッグ表示
        // データを表示させる
        const tableBody = document.querySelector("#address-list > tbody");
        if (data && data.length == 0) {
            let tr = document.createElement('tr')
            tr.innerHTML = "表示するデータがありません。"
            tableBody.appendChild(tr)
            return
        }
        data.forEach(elm => {
            // 1行づつ処理を行う
            let tr = document.createElement('tr');
            // first name
            let td = document.createElement('td');
            td.innerText = elm.first_name;
            tr.appendChild(td);
            // last name
            td = document.createElement('td');
            td.innerText = elm.last_name;
            tr.appendChild(td);
            // email
            td = document.createElement('td');
            td.innerText = elm.email;
            tr.appendChild(td);

            // 1行分をtableタグ内のtbodyへ追加する
            tableBody.appendChild(tr);
        });
    });
});

const sb = document.querySelector('#search-submit')
sb.addEventListener("click", (ev) => {
    ev.preventDefault()//HTMLが本来持っている他の正常なボタン処理をなかったことにする
    console.log("検索ボタン押されたよ")

    // fn: 指定されたキーワードがFirst Nameに含まれるデータを返します。省略時全件。
    // ln: 指定されたキーワードがLast Nameに含まれるデータを返します。省略時全件。
    // em: 指定されたキーワードがEmailに含まれるデータを返します。省略時全件。

    //パラメータの取得 
    const params = new URLSearchParams()
    const fn = document.querySelector("#search-firstname").value
    const ln = document.querySelector("#search-lastname").value
    const em = document.querySelector("#search-email").value

    if (fn && fn !== "") params.set("fn", fn)
    if (ln && ln !== "") params.set("ln", ln)
    if (em && em !== "") params.set("em", em)

    console.log(params)

    fetch("/address?" + params.toString()).then(response => { ///addressが取得されたら.then移行が実行される
        console.log(response);
        response.json().then((data) => { //responseをjsonに変換できたら.then移行が実行される
            console.log(data);  // 取得されたレスポンスデータをデバッグ表示
            // データを表示させる
            const tableBody = document.querySelector("#address-list > tbody");
            //tableBody.innerHTML = ""
            while(tableBody.firstChild){
                tableBody.removeChild(tableBody.firstChild)
            }
            if (data && data.length == 0) {
                let tr = document.createElement('tr')
                tr.innerHTML = "表示するデータがありません。"
                tableBody.appendChild(tr)
                return
            }
            data.forEach(elm => {
                // 1行づつ処理を行う
                let tr = document.createElement('tr');
                // first name
                let td = document.createElement('td');
                td.innerText = elm.first_name;
                tr.appendChild(td);
                // last name
                td = document.createElement('td');
                td.innerText = elm.last_name;
                tr.appendChild(td);
                // email
                td = document.createElement('td');
                td.innerText = elm.email;
                tr.appendChild(td);
    
                // 1行分をtableタグ内のtbodyへ追加する
                tableBody.appendChild(tr);
            });
        });
    });

    // データ検索のWeb APIは/addressをGETメソッドで呼び出す
    // 入力項目それぞれが入力されていれば、データの検索条件となる
    // 入力項目がすべて空の場合、全件取得となる
    // 検索ごとに、<table class="table" id="address-list">〜</table>内の<tbody>〜</tbody>内部はクリアされて結果が表示される
    // 検索結果が0件の場合、データがない旨を<tbody>〜</tbody>内で表示する
})


document.getElementById("add-submit").addEventListener("click", (e) => {
    // ボタンイベントのキャンセル
    e.preventDefault()
    console.log("追加ボタン押されたよ")

    // 入力チェック
    let fn = document.getElementById("add-firstname").value
    let ln = document.getElementById("add-lastname").value
    let em = document.getElementById("add-email").value

    // 未入力がある項目ごとにエラーメッセージを積み上げる
    let error_message = ""
    if (!fn && fn === "") error_message += "first nameが未入力です。<br>"
    if (!ln && ln === "") error_message += "last nameが未入力です。<br>"
    if (!em && em === "") error_message += "emailが未入力です。<br>"

    // エラーメッセージがあるかどうかでエラーの表示有無を決定
    if (error_message !== "") {
        document.getElementById('error-container').innerHTML = error_message
        document.getElementById('error-container').style.display = "block"
        document.getElementById('message-container').innerHTML = ""
        document.getElementById('message-container').style.display = "none"
        return
    } else {
        document.getElementById('error-container').innerHTML = ""
        document.getElementById('error-container').style.display = "none"
    }

    // データ送信
    // FormDataのコンストラクタを使い、フォームデータを一括取得(form内の各inputタグにname属性を正しく設定する必要があります)
    let data = new FormData(document.getElementById('add'))
    fetch('/address', {method: 'POST',body: data,}).then((response) => {


        console.log("1")
        // 入力項目の初期化
        document.getElementById("add").reset()
        
        // エラーの表示領域を初期化
        document.getElementById('error-container').innerHTML = ""
        document.getElementById('error-container').style.display = "none"
        // 登録メッセージ等の表示領域を初期化
        document.getElementById('message-container').innerHTML = ""
        document.getElementById('message-container').style.display = "none"

        // レスポンスデータからJSONを取り出し
        response.json().then((data) => {

            console.log("2")

            console.log(data)

            if (data.error) {
                // エラーの受信
                document.getElementById('error-container').innerHTML = data.error
                document.getElementById('error-container').style.display = "block"
                document.getElementById('message-container').innerHTML = data.result
                document.getElementById('message-container').style.display = "none"
                return
            }

            data.result = "登録が完了しました。"

            if (data.result) {
                // メッセージの受信
                document.getElementById('message-container').innerHTML = data.result
                document.getElementById('message-container').style.display = "block"
                if (data) {
                    const tableBody = document.querySelector("#address-list > tbody")
                    tableBody.innerHTML = ""
                    data.forEach(elm => {
                        let tr = document.createElement('tr')
                        // first name
                        let td = document.createElement('td')
                        td.textContent = elm.first_name
                        tr.appendChild(td)
                        // last name
                        td = document.createElement('td')
                        td.textContent = elm.last_name
                        tr.appendChild(td)
                        // email
                        td = document.createElement('td')
                        td.textContent = elm.email
                        tr.appendChild(td)
                        // 1行分をtableタグ内のtbodyへ追加する
                        tableBody.appendChild(tr)
                    })
                }
            }
        })
    })
})
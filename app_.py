from flask import Flask, render_template, request,redirect, url_for, jsonify

app = Flask(__name__)

comments = ["tyt buv ya!"]

@app.route('/')
def index():
    return render_template("index_.html", comments = comments)

@app.route("/comment/ssr", methods=["POST"])
def com_ssr():
    com = request.form.get("com")
    comments.append(com)
    return redirect(url_for("index"))

@app.route("/comment/csr", methods=["POST"])
def com_csr():
    data = request.get_json()
    com = data.get("com")

    comments.append(com)
    respond = {"new_com":com}

    return jsonify(respond)

app.run(debug=True)

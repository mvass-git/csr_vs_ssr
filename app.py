from flask import Flask, render_template, request, redirect, url_for, jsonify

app = Flask(__name__)

comments = []


@app.route("/")
def index():
    return render_template("index.html", comments=comments)


@app.route("/comments/ssr", methods=["POST"])
def add_comment_ssr():
    text = request.form.get("text", "").strip()

    if text:
        comments.append(text)

    return redirect(url_for("index"))


@app.route("/comments/csr", methods=["POST"])
def add_comment_csr():
    data = request.get_json()
    text = data.get("text", "").strip()

    if text:
        comments.append(text)

    return jsonify({
        "comment": text
    })


if __name__ == "__main__":
    app.run(debug=True)
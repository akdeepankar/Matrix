from flask import Flask, render_template, request

import Matrix
from Matrix import Determinant

app = Flask(__name__)


@app.route('/', methods=["GET", "POST"])
def matrix():
    if request.method == "POST":
        a11 = int(request.form.get("a11"))
        a12 = int(request.form.get("a12"))
        a13 = int(request.form.get("a13"))
        a21 = int(request.form.get("a21"))
        a22 = int(request.form.get("a22"))
        a23 = int(request.form.get("a23"))
        a31 = int(request.form.get("a31"))
        a32 = int(request.form.get("a32"))
        a33 = int(request.form.get("a33"))
        if a11 or a12 or a13 or a21 or a22 or a23 or a31 or a32 or a33 is 0:
            return render_template("matrix.html", novalue="VALUE IS MISSING")
        else:
            value = Determinant.order3(a11, a12, a13, a21, a22, a23, a31, a32, a33)
            return render_template("matrix.html", values=value)
    return render_template("matrix.html")


if __name__ == '__main__':
    app.run()
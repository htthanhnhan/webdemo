from flask import Flask, render_template, request, redirect
import data

app = Flask(__name__)
app.secret_key = "webdemo"


@app.route('/school', methods=['get'])
def school():
    list = data.read()
    return render_template("index.html", list=list)


@app.route('/create', methods=["GET"])
def create():
    return render_template("create.html")


@app.route('/create', methods=["POST"])
def do_create():
    name = request.form['name']
    age = request.form['age']
    data.create(name, age)
    return redirect("/school")


@app.route('/school', methods=["POST"])
def do_delete():
    id = request.form['id']
    data.delete(id)
    return redirect("/school")


@app.route('/update/<int:id>', methods=["GET"])
def update(id):
    s = data.student(id)
    return render_template("update.html", s=s)


@app.route('/update/<int:id>', methods=["POST"])
def do_update(id):
    name = request.form['name']
    age = request.form['age']
    data.update(id, name, age)
    return redirect("/school")


if __name__ == "__main__":
    from waitress import serve
    serve(app, host="0.0.0.0", port=8080)

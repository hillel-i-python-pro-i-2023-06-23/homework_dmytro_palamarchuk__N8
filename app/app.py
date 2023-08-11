"""Entry point"""
from flask import Flask, render_template, request

app = Flask(__name__)


@app.route("/", methods=["GET"])
def hello_world() -> str:
    """Route to display a static greeting message."""
    return render_template("index.html", data="Hello World!!!")


@app.route("/<string:name>/<int:number>")
def hello_world_dynamic(name: str, number: int) -> str:
    """Route to display a dynamic greeting message with route parameters."""
    return render_template(
        "dynamic.html",
        task_title="Приветствие с динамическим маршрутом.",
        name=name,
        number=number,
    )


@app.route("/query")
def hello_world_query() -> str:
    """Route to display a dynamic greeting message with query parameters."""
    name = request.args.get("name", default="Unknown person")
    number = request.args.get("number", default="undefined")
    return render_template(
        "dynamic.html",
        task_title="Приветствие с query в URL.",
        name=name,
        number=number,
    )


if __name__ == "__main__":
    app.run()

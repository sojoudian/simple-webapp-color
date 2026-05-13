import os
import random
import socket

from flask import Flask, abort, render_template

COLOR_CODES = {
    "red": "#e74c3c",
    "green": "#16a085",
    "blue": "#2980b9",
    "blue2": "#30336b",
    "pink": "#be2edd",
    "darkblue": "#130f40",
}

app = Flask(__name__)
color = os.environ.get("APP_COLOR") or random.choice(list(COLOR_CODES))


def hex_for(name):
    if name not in COLOR_CODES:
        abort(404)
    return COLOR_CODES[name]


@app.get("/")
def main():
    return render_template("hello.html", name=socket.gethostname(), color=hex_for(color))


@app.get("/color/<new_color>")
def change_color(new_color):
    return render_template("hello.html", name=socket.gethostname(), color=hex_for(new_color))


@app.get("/read_file")
def read_file():
    with open("/data/testfile.txt") as f:
        contents = f.read()
    return render_template(
        "hello.html", name=socket.gethostname(), contents=contents, color=hex_for(color)
    )


@app.get("/healthz")
def healthz():
    return {"status": "ok"}


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)

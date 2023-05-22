from flask import Flask, render_template
import os
app = Flask(__name__,)

@app.route('/')
def hello_world():
    return render_template("test.html")

if __name__ == "__main__":
    app.run(
        host=os.getenv("IP", "0.0.0.0"),
        port=int(os.getenv("PORT", 8080)),
        debug=True,
    )
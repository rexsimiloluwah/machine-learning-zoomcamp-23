from flask import Flask, jsonify, render_template

app = Flask("simple_k8s_example")

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/healthcheck", methods=["GET"])
def healthcheck():
    response = {"status": True, "message": "Server is up and running!"}
    return jsonify(response)

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=9698)
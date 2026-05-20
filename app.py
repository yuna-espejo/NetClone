'''
This module needs to starts the flask web server

    1. Import the Flask service
    2. Create the aplication with each route
    3. Start the aplication


'''

from flask import Flask, render_template, request, jsonify

app = Flask(__name__, template_folder="app/templates")

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/apply", methods=["POST"])
def apply():
    ssid = request.form.get("ssid")
    wifi_password = request.form.get("wifi_password")
    brand = request.form.get("brand")
    model = request.form.get("model")

    return jsonify({
        "ssid": ssid,
        "brand": brand,
        "model": model,
        "status": "received"
    })
if __name__ == "__main__":
    app.run(debug=True)
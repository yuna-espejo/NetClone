'''
This module needs to starts the flask web server

    1. Import the Flask service
    2. Create the aplication with each route
    3. Start the aplication


'''

from flask import Flask

app = Flask(__name__)

@app.route("/")
def index():
    return "NetClone Funcionando"

if __name__ == "__main__":
    app.run(debug=True)
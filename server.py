from flask import Flask, request
from functions import get_sunrise_sunset_times

app = Flask(__name__)

API_KEY = "a6d738363a19437e9730bea42200f43f"
API_KEY2 = "aUrzQwdOTzoBvKMWRmwf"


@app.route("/server/api/sunrise-sunset-times", methods=["POST"])
def getApi():

    try:
        data = request.json
        country, date = data["country"], data["date"]

        server_response, status = get_sunrise_sunset_times(
            country, date, API_KEY, API_KEY2
        )
    except:
        server_response, status = {"error": "bad request!"}, 400

    return server_response, status


if __name__ == "__main__":
    app.run(port=5000, debug=True)

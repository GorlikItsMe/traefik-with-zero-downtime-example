from time import sleep
from flask import Flask
from flask import jsonify
import random

app = Flask(__name__)

random_number = random.randint(1, 100000)


@app.route("/")
def blog():
    data = {
        "foo": "bar",
        "random_number": random_number,
    }
    return jsonify(data)


@app.route("/health")
def health():
    msg = {
        "message": "Healthy"
    }
    return jsonify(msg)


if __name__ == '__main__':
    print("Fake slow booting up app...")
    for i in range(1, 10 + 1):
        print(i)
        sleep(1)
    print("Now starting app (for real)...")
    print("Random number is: {}".format(random_number))
    app.run(debug=True, host='0.0.0.0')

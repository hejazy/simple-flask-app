from flask import Flask

app = Flask(__name__)

import app as application


if __name__ == '__main__':
    app.run(debug=True)

from flask import Flask
import os
template_dir = os.path.abspath('./app/templates')

app = Flask(__name__, template_folder=template_dir)
SECRET_KEY = os.urandom(32)
app.config['SECRET_KEY'] = SECRET_KEY

import app as application


if __name__ == '__main__':
    app.run(debug=True)

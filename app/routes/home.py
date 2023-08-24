from flask import render_template, request
from __main__ import app

from app.helpers.devices import load_devices_from_excel

@app.route('/', methods=['GET', 'POST'])
def home():
    print('page')
    devices = load_devices_from_excel()
    search_query = request.args.get('search', '')
    if search_query:
        devices_filtered = [device for device in devices if search_query.lower() in device['hostname'].lower()]
        return render_template('home.html', devices=devices_filtered, search_query=search_query)
    return render_template('home.html', devices=devices, search_query='')

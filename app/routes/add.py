from app.classes.device import DeviceForm
from flask import render_template, request, redirect, flash
from __main__ import app

from app.helpers.devices import save_device_to_excel

@app.route('/add_device', methods=['GET', 'POST'])
def add_device():
    form = DeviceForm()
    print(request.form)
    if request.method == 'POST' :
        hostname = request.form.get('hostname')
        ip_address = request.form.get('ip_address')
        port = request.form.get('port')
        switch = request.form.get('switch')
        device = {'hostname': hostname, 'ip_address': ip_address, 'port': port, 'switch': switch}
        save_device_to_excel(device)
        flash('Device added successfully.', 'success')
        return redirect('/')
    return render_template('add_device.html', form=form)



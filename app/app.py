from flask import Flask, render_template, session, request
from flask.ext.socketio import SocketIO, emit
import glob
import os

app = Flask(__name__)
#app.debug = True
app.config['SECRET_KEY'] = ';fwpl;xcmz,.v.zxv.nkeoISNRRT:Nevn;;flqg0;43l50;'
socketio = SocketIO(app)
#Mapping from layername to visibility
layers = {}

@app.route('/')
def index():
    return render_template('index.html', layers=layers)

@app.route('/control')
def control():
    return render_template('control.html', layers=layers)

@socketio.on('set_visibility')
def set_visibility(message):
    message = message['data']
    if message['layer'] in layers.keys():
        layers[message['layer']] = message['state']
        emit('set_visibility',
            {'data': {'layer': message['layer'], 'state': message['state']}},
            broadcast=True)

@socketio.on('disconnect')
def test_disconnect():
    print('Client disconnected')


if __name__ == '__main__':
    for path in glob.glob("./static/layers/*.png"):
        layername = os.path.splitext(os.path.basename(path))[0]
        layers[layername] = False

    socketio.run(app, host='0.0.0.0')

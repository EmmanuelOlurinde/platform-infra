from flask import Flask, jsonify
import datetime
import socket

app = Flask(__name__)

@app.route('/api/v1/details')
def hello_world():
    return jsonify({
        'time': datetime.datetime.utcnow().isoformat(),
        'hostname': socket.gethostname(),
        'message': 'Welcome to the platform infrastructure API'
    })

@app.route('/api/v1/healthz')
def health():
    return jsonify({
        'status': 'up'
    })

if __name__ == '__main__':
    app.run(host="0.0.0.0")
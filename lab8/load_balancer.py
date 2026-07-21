from flask import Flask, request, redirect
import random

app = Flask(__name__)

backend_servers = ['http://localhost:5001', 'http://localhost:5002']

@app.route('/')
def load_balancer():
    chosen_server = random.choice(backend_servers)
    return redirect(chosen_server)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
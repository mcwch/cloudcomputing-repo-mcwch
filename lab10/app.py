from flask import Flask
import logging

app = Flask(__name__)

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

@app.route('/')
def home():
    logging.info("Home page accessed.")
    return "This is the home page."

@app.route('/error')
def trigger_error():
    logging.error("Simulated error occurred.")
    return "Simulated error triggered."

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

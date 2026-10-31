
from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/")
def home():
    return """
    <h1>Welcome to Security CI/CD Demo</h1>
    <p>OWASP ZAP Security Scanning</p>
    """

@app.route("/login")
def login():
    return jsonify({
        "message": "Login page",
        "status": "Application running"
    })

@app.route("/health")
def health():
    return jsonify({"status": "healthy"})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

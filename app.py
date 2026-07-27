import os
from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    message = os.getenv("APP_MESSAGE", "Default message")
    db_pass_status = "Loaded Successfully" if os.getenv("DB_PASSWORD") else "Missing"
    return f"{message} | Database Password Status: {db_pass_status}"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
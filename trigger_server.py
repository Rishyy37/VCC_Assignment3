from flask import Flask, jsonify
import subprocess

app = Flask(__name__)

APP_RUNNING = False


@app.route("/")
def home():
    return "Trigger server is running"


@app.route("/start-instance", methods=["POST"])
def start_instance():
    global APP_RUNNING

    if not APP_RUNNING:
        print("⚡ Scaling triggered! Starting app...")

        # Start app in background
        subprocess.Popen(["python3", "app.py"])

        APP_RUNNING = True
        return jsonify({"status": "App started on cloud VM"})

    return jsonify({"status": "App already running"})


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
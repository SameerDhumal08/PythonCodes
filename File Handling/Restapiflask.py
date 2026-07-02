from flask import Flask, request, jsonify
import subprocess

app = Flask(__name__)

@app.route('/run-playbook', methods=['POST'])
def run_playbook():

    data = request.get_json()

    ip_address = data.get("ip_address")
    playbook_name = data.get("playbook_name")

    if not ip_address or not playbook_name:
        return jsonify({
            "status": "failed",
            "message": "ip_address and playbook_name are required"
        }), 400

    command = [
        "ansible-playbook",
        playbook_name,
        "-i",
        f"{ip_address},",
        "--extra-vars",
        f"target_ip={ip_address}"
    ]

    try:
        process = subprocess.Popen(
            command,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True
        )

        stdout, stderr = process.communicate()

        return jsonify({
            "status": "completed",
            "return_code": process.returncode,
            "stdout": stdout,
            "stderr": stderr
        })

    except Exception as e:
        return jsonify({
            "status": "error",
            "message": str(e)
        }), 500


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

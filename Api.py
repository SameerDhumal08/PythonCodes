from flask import Flask, request, jsonify
import requests
import time

app = Flask(__name__)

JENKINS_URL = "http://localhost:8080"
JOB_NAME = "Automation-Pipeline"

USERNAME = "admin"
API_TOKEN = "your_api_token"

@app.route("/trigger", methods=["POST"])
def trigger_pipeline():

    data = request.get_json()

    ticket_id = data.get("ticket_id")
    server = data.get("server")
    alert = data.get("alert")

    build_url = f"{JENKINS_URL}/job/{JOB_NAME}/buildWithParameters"

    parameters = {
        "TICKET_ID": ticket_id,
        "SERVER": server,
        "ALERT": alert
    }

    response = requests.post(
        build_url,
        params=parameters,
        auth=(USERNAME, API_TOKEN)
    )

    if response.status_code != 201:
        return jsonify({"error": "Unable to trigger Jenkins"}), 500

    queue_url = response.headers["Location"] + "api/json"

    build_number = None

    while True:
        queue_response = requests.get(
            queue_url,
            auth=(USERNAME, API_TOKEN)
        ).json()

        executable = queue_response.get("executable")

        if executable:
            build_number = executable["number"]
            break

        time.sleep(2)

    while True:
        build_api = f"{JENKINS_URL}/job/{JOB_NAME}/{build_number}/api/json"

        build = requests.get(
            build_api,
            auth=(USERNAME, API_TOKEN)
        ).json()

        if not build["building"]:
            break

        time.sleep(5)

    return jsonify({
        "Ticket": ticket_id,
        "Server": server,
        "Alert": alert,
        "Build_Number": build["number"],
        "Result": build["result"],
        "Duration": build["duration"],
        "Build_URL": build["url"]
    })

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

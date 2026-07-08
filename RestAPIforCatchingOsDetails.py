
from flask import Flask, request, jsonify
import requests
import time

app = Flask(__name__)

# Jenkins Configuration
JENKINS_URL = "http://your-jenkins-server:8080"
JOB_NAME = "Demo-Pipeline"
USERNAME = "admin"
API_TOKEN = "your_api_token"

@app.route('/run-job', methods=['POST'])
def run_job():
    try:
        # Read JSON input
        data = request.get_json()

        server_name = data.get("server_name")
        alert_type = data.get("alert_type")
        ticket_id = data.get("ticket_id")

        # Jenkins Build URL
        trigger_url = f"{JENKINS_URL}/job/{JOB_NAME}/buildWithParameters"

        params = {
            "SERVER_NAME": server_name,
            "ALERT_TYPE": alert_type,
            "TICKET_ID": ticket_id
        }

        # Trigger Jenkins Job
        response = requests.post(
            trigger_url,
            params=params,
            auth=(USERNAME, API_TOKEN)
        )

        if response.status_code not in [200, 201]:
            return jsonify({
                "status": "Failed",
                "message": "Unable to trigger Jenkins Job"
            }), 500

        # Wait for Jenkins to create build
        time.sleep(5)

        # Fetch Last Build Number
        build_api = f"{JENKINS_URL}/job/{JOB_NAME}/lastBuild/api/json"

        build_response = requests.get(
            build_api,
            auth=(USERNAME, API_TOKEN)
        )

        build_data = build_response.json()

        result = {
            "Build_Number": build_data.get("number"),
            "Status": build_data.get("result"),
            "Building": build_data.get("building"),
            "Duration(ms)": build_data.get("duration"),
            "Build_URL": build_data.get("url")
        }

        return jsonify(result)

    except Exception as e:
        return jsonify({
            "status": "Error",
            "message": str(e)
        }), 500


if __name__ == '__main__':
    app.run(debug=True)

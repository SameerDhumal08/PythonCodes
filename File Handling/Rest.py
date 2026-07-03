from flask import Flask, request, jsonify

app = Flask(__name__)

# Demo token (normally store this securely)
API_TOKEN = "my-secret-token"

@app.route("/device", methods=["POST"])
def device():

    # Get Authorization header
    auth_header = request.headers.get("Authorization")

    if not auth_header:
        return jsonify({"error": "Authorization header missing"}), 401

    if not auth_header.startswith("Bearer "):
        return jsonify({"error": "Invalid authentication format"}), 401

    token = auth_header.split(" ")[1]

    if token != API_TOKEN:
        return jsonify({"error": "Invalid token"}), 401

    # Get JSON object
    data = request.get_json()

    ip_address = data.get("ip_address")
    playbook = data.get("playbook_name")

    return jsonify({
        "message": "Request received successfully",
        "ip_address": ip_address,
        "playbook_name": playbook
    }), 200


if __name__ == "__main__":
    app.run(debug=True)

from flask import Flask, request, jsonify
import subprocess
import yaml

app = Flask(__name__)

# Load server configuration from server.yaml
with open('server.yaml', 'r') as f:
    config = yaml.safe_load(f)

HOST = config.get('host', '0.0.0.0')
PORT = config.get('port', 4735)

@app.route('/logs/cat', methods=['POST'])
def concatenate_logs():
    data = request.get_json()
    if not data or 'prefix' not in data:
        return jsonify({'error': 'Invalid input. Expected JSON payload with a "prefix" field.'}), 400
    
    prefix = data['prefix']
    try:
        # Run the concatenate script with the given prefix
        result = subprocess.run(['sh', 'concatenate_logs.sh', prefix], check=True, capture_output=True, text=True)
        return jsonify({'message': 'Concatenation complete.', 'output': result.stdout}), 200
    except subprocess.CalledProcessError as e:
        return jsonify({'error': 'Failed to run concatenation script.', 'details': e.stderr}), 500

if __name__ == '__main__':
    app.run(host=HOST, port=PORT)

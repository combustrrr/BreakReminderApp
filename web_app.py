from flask import Flask, render_template, jsonify, request
import json
import os

app = Flask(__name__)

SETTINGS_FILE = "settings.json"
DEFAULT_INTERVAL = 20


def load_settings():
    """Load settings from JSON file."""
    try:
        with open(SETTINGS_FILE, "r") as f:
            return json.load(f)
    except FileNotFoundError:
        return {"interval": str(DEFAULT_INTERVAL)}


def save_settings(settings):
    """Save settings to JSON file."""
    with open(SETTINGS_FILE, "w") as f:
        json.dump(settings, f)


@app.route('/')
def index():
    """Render the main page."""
    settings = load_settings()
    return render_template('index.html', interval=settings.get('interval', DEFAULT_INTERVAL))


@app.route('/api/settings', methods=['GET', 'POST'])
def settings():
    """Handle settings API requests."""
    if request.method == 'POST':
        data = request.json
        save_settings(data)
        return jsonify({"status": "success", "settings": data})
    else:
        return jsonify(load_settings())


if __name__ == '__main__':
    # Create templates directory if it doesn't exist
    os.makedirs('templates', exist_ok=True)
    os.makedirs('static', exist_ok=True)
    
    # Run the Flask app
    # Use 0.0.0.0 to make it accessible from other devices on the network
    app.run(host='0.0.0.0', port=5000, debug=True)

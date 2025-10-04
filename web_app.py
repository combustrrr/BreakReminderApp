from flask import Flask, render_template, jsonify, request
import json
import os
from datetime import datetime, timedelta
from collections import defaultdict

app = Flask(__name__)

SETTINGS_FILE = "settings.json"
SYMPTOMS_FILE = "symptom_logs.json"
USAGE_FILE = "usage_stats.json"
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


def load_symptom_logs():
    """Load symptom logs from JSON file."""
    try:
        with open(SYMPTOMS_FILE, "r") as f:
            return json.load(f)
    except FileNotFoundError:
        return []


def save_symptom_log(log_entry):
    """Save a symptom log entry."""
    logs = load_symptom_logs()
    logs.append(log_entry)
    with open(SYMPTOMS_FILE, "w") as f:
        json.dump(logs, f, indent=2)


def load_usage_stats():
    """Load usage statistics from JSON file."""
    try:
        with open(USAGE_FILE, "r") as f:
            return json.load(f)
    except FileNotFoundError:
        return []


def save_usage_event(event):
    """Save a usage event (break taken/skipped/session)."""
    stats = load_usage_stats()
    stats.append(event)
    with open(USAGE_FILE, "w") as f:
        json.dump(stats, f, indent=2)


def calculate_statistics():
    """Calculate usage statistics."""
    stats = load_usage_stats()
    
    # Group by date
    daily_stats = defaultdict(lambda: {'breaks_taken': 0, 'breaks_skipped': 0, 'screen_time': 0})
    
    for event in stats:
        date = event['timestamp'][:10]  # Get YYYY-MM-DD
        
        if event['type'] == 'break_taken':
            daily_stats[date]['breaks_taken'] += 1
        elif event['type'] == 'break_skipped':
            daily_stats[date]['breaks_skipped'] += 1
        elif event['type'] == 'session':
            daily_stats[date]['screen_time'] += event.get('duration', 0)
    
    # Get last 7 days
    today = datetime.now()
    last_7_days = [(today - timedelta(days=i)).strftime('%Y-%m-%d') for i in range(6, -1, -1)]
    
    weekly_data = {
        'dates': last_7_days,
        'breaks_taken': [daily_stats[date]['breaks_taken'] for date in last_7_days],
        'breaks_skipped': [daily_stats[date]['breaks_skipped'] for date in last_7_days],
        'screen_time': [daily_stats[date]['screen_time'] for date in last_7_days]
    }
    
    # Calculate totals
    total_breaks_taken = sum(daily_stats[date]['breaks_taken'] for date in daily_stats)
    total_breaks_skipped = sum(daily_stats[date]['breaks_skipped'] for date in daily_stats)
    total_screen_time = sum(daily_stats[date]['screen_time'] for date in daily_stats)
    
    return {
        'weekly': weekly_data,
        'totals': {
            'breaks_taken': total_breaks_taken,
            'breaks_skipped': total_breaks_skipped,
            'screen_time': total_screen_time,
            'total_breaks': total_breaks_taken + total_breaks_skipped
        }
    }


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


@app.route('/api/symptoms', methods=['GET', 'POST'])
def symptoms():
    """Handle symptom logging requests."""
    if request.method == 'POST':
        log_entry = request.json
        save_symptom_log(log_entry)
        return jsonify({"status": "success", "message": "Symptom log saved"})
    else:
        return jsonify(load_symptom_logs())


@app.route('/api/usage', methods=['POST'])
def log_usage():
    """Log usage event (break taken/skipped/session)."""
    event = request.json
    event['timestamp'] = datetime.now().isoformat()
    save_usage_event(event)
    return jsonify({"status": "success", "message": "Usage event logged"})


@app.route('/api/statistics', methods=['GET'])
def statistics():
    """Get usage statistics."""
    return jsonify(calculate_statistics())


if __name__ == '__main__':
    # Create templates directory if it doesn't exist
    os.makedirs('templates', exist_ok=True)
    os.makedirs('static', exist_ok=True)
    
    # Run the Flask app
    # Use 0.0.0.0 to make it accessible from other devices on the network
    app.run(host='0.0.0.0', port=5000, debug=True)

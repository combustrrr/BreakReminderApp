# Quick Start Guide - Break Reminder App

## For Desktop/Laptop Users

### Option 1: Auto-Launch (Recommended)
```bash
pip install -r requirements.txt
python launcher.py
```

### Option 2: Web Version
```bash
pip install -r requirements.txt
python web_app.py
```
Then open: http://localhost:5000

### Option 3: Desktop Version (Original)
```bash
python BreakReminderApp.py
```
(Note: Desktop version only works on Windows due to winsound)

## For Mobile/Tablet Users

### Setup (One-time)
1. On your computer, run:
   ```bash
   pip install -r requirements.txt
   python web_app.py
   ```

2. Find your computer's IP address:
   - **Windows**: Open CMD and type `ipconfig`
   - **Mac/Linux**: Open Terminal and type `ifconfig` or `ip addr`
   
   Look for something like `192.168.1.100` or `10.0.0.5`

3. On your mobile device:
   - Open your web browser (Safari, Chrome, etc.)
   - Navigate to: `http://YOUR_COMPUTER_IP:5000`
   - Example: `http://192.168.1.100:5000`

### Add to Home Screen (For App-like Experience)

**iOS (iPhone/iPad):**
1. Open the app in Safari
2. Tap the Share button (square with arrow)
3. Scroll down and tap "Add to Home Screen"
4. Name it "Break Reminder" and tap "Add"
5. Now you can launch it like a native app!

**Android:**
1. Open the app in Chrome
2. Tap the menu (three dots in top right)
3. Tap "Add to Home screen"
4. Name it "Break Reminder" and tap "Add"
5. Now you can launch it like a native app!

## Using the App

1. **Set Interval**: Enter the time between reminders (in minutes)
2. **Start**: Click to start the timer
3. **Pause**: Temporarily pause the timer
4. **Resume**: Resume from where you paused
5. **Stop**: Stop the timer completely

## The 20-20-20 Rule

Every **20 minutes**, look at something **20 feet away** for **20 seconds**.

This helps reduce eye strain from prolonged screen time!

## Troubleshooting

**Can't access from mobile:**
- Make sure both devices are on the same WiFi network
- Check your firewall isn't blocking port 5000
- Try accessing with http:// (not https://)

**No audio on mobile:**
- Make sure your device isn't on silent mode
- Check browser permissions for audio

**Flask not found:**
- Run: `pip install -r requirements.txt`

## Advanced Usage

### Run on Different Port
```bash
# Edit web_app.py, change the last line to:
app.run(host='0.0.0.0', port=8080, debug=True)
```

### Run in Background (Linux/Mac)
```bash
nohup python web_app.py &
```

### Run in Background (Windows)
```bash
start /B python web_app.py
```

## Need Help?

Open an issue on GitHub or check the README.md for more details!

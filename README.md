# Break Reminder App

A periodic break reminder application that helps you follow the 20-20-20 rule for eye health: Every 20 minutes, look at something 20 feet away for 20 seconds.

## 🌟 Features

- Customizable reminder intervals
- Start, Stop, Pause, and Resume functionality
- Visual and audio notifications
- Persistent settings storage
- **Cross-platform support** - works on desktop, mobile, and tablet!

## 📱 Available Versions

### 1. Web Version (Recommended for All Devices)

**Works on: Mobile, Tablet, Laptop, Desktop - Any device with a web browser**

The web version is a responsive, modern web application that can be accessed from any device with a browser.

#### Installation

```bash
# Install dependencies
pip install -r requirements.txt

# Run the web app
python web_app.py
```

The app will be available at:
- Local: http://localhost:5000
- Network: http://YOUR_IP:5000 (accessible from other devices on your network)

#### Features
- ✅ Responsive design for all screen sizes
- ✅ Works on mobile, tablet, and desktop
- ✅ Cross-platform audio notifications
- ✅ Modern, intuitive interface
- ✅ No installation required (just need Python)

### 2. Desktop Version (Windows/Linux/Mac)

**Works on: Desktop computers with Python and Tkinter**

The original desktop version using Tkinter GUI.

#### Installation

```bash
# Run the desktop app
python BreakReminderApp.py
```

**Note:** The desktop version uses `winsound` which only works on Windows. For cross-platform support, use the web version.

## 🚀 Quick Start (Web Version)

1. Install Python 3.7 or higher
2. Clone this repository
3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
4. Run the web app:
   ```bash
   python web_app.py
   ```
5. Open your browser and go to http://localhost:5000
6. Set your desired interval (in minutes)
7. Click "Start" to begin receiving reminders

## 📱 Mobile/Tablet Usage

### Access from Mobile Device:

1. Make sure your mobile device is on the same network as the computer running the app
2. Find your computer's IP address:
   - Windows: `ipconfig`
   - Mac/Linux: `ifconfig` or `ip addr`
3. On your mobile device, open a browser and navigate to:
   ```
   http://YOUR_COMPUTER_IP:5000
   ```
4. For best experience, add the page to your home screen (works like a native app!)

### Add to Home Screen:

**iOS (Safari):**
1. Tap the Share button
2. Scroll down and tap "Add to Home Screen"
3. Name it "Break Reminder"
4. Tap "Add"

**Android (Chrome):**
1. Tap the menu (three dots)
2. Tap "Add to Home screen"
3. Name it "Break Reminder"
4. Tap "Add"

## ⚙️ Configuration

- **Interval**: Set the time between reminders (in minutes)
- **Settings**: Automatically saved and loaded between sessions

## 🎯 The 20-20-20 Rule

This app implements the 20-20-20 rule recommended by eye care professionals:
- Every **20 minutes**, take a break
- Look at something **20 feet away**
- For at least **20 seconds**

This helps reduce eye strain from prolonged screen time.

## 🛠️ Technical Details

### Web Version Stack:
- **Backend**: Python Flask
- **Frontend**: HTML5, CSS3, JavaScript
- **Audio**: Web Audio API (cross-platform)
- **Responsive**: Works on all screen sizes

### Desktop Version Stack:
- **GUI**: Tkinter
- **Audio**: winsound (Windows only)
- **Threading**: Python threading module

## 📝 License

This project is open source and available for personal and educational use.

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## 📞 Support

If you encounter any issues or have suggestions, please open an issue on GitHub.

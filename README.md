# Break Reminder App - Combat Computer Vision Syndrome

A periodic break reminder application that helps you combat Computer Vision Syndrome (CVS) and reduce eye strain by following the 20-20-20 rule: Every 20 minutes, look at something 20 feet away for 20 seconds.

## 👁️ What is Computer Vision Syndrome?

Computer Vision Syndrome (CVS) is a group of eye and vision-related problems that result from prolonged computer, tablet, and phone use. Symptoms include:
- Eye strain and fatigue
- Dry eyes
- Blurred vision
- Headaches
- Neck and shoulder pain

This app helps you combat CVS by reminding you to take regular breaks and rest your eyes.

## 🌟 Features

- **Flexible Timer** - Set your own reminder interval (not forced, you control it!)
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
- ✅ Can be added to home screen (PWA)

### 2. Standalone Applications

Want to distribute the app as a standalone application? Check out our **[DEPLOYMENT.md](DEPLOYMENT.md)** guide for:

- 📱 **Android APK** - Build installable APK for mobile and tablets
- 💻 **Windows EXE** - Create standalone executable for Windows
- 🍎 **macOS APP** - Package as macOS application
- 🐧 **Linux AppImage** - Portable Linux application

All versions are safe to distribute and don't require Play Store or app stores!

### 3. Desktop Version (Windows/Linux/Mac)

**Works on: Desktop computers with Python and Tkinter**

The original desktop version using Tkinter GUI.

#### Installation

```bash
# Run the desktop app
python BreakReminderApp.py
# or use: python launcher.py --desktop
```

**Note:** The desktop version uses `winsound` which only works on Windows. For cross-platform support, use the web version.

## 🚀 Quick Start

### Easy Launch (Recommended)

Use the launcher script that auto-detects the best version for your system:

```bash
# Install dependencies first
pip install -r requirements.txt

# Run the launcher
python launcher.py
```

The launcher will automatically start the web version if Flask is available, or fall back to the desktop version.

### Manual Start (Web Version)

1. Install Python 3.7 or higher
2. Clone this repository
3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
4. Run the web app:
   ```bash
   python web_app.py
   # or use: python launcher.py --web
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

## 🗺️ Roadmap & Future Features

We're constantly evolving! Check out our plans:
- **[ROADMAP.md](ROADMAP.md)** - Long-term vision, research-inspired features, and advanced capabilities
- **[TODO.md](TODO.md)** - Current development tasks and priorities

Upcoming features include:
- 📊 Statistics dashboard with usage analytics
- 🎯 Eye strain risk score prediction
- 🧘 Guided eye exercises during breaks
- 🎨 Radial/circular timer design
- 🌓 Light/dark theme toggle
- 🤖 ML-based adaptive interval optimization
- 📸 Eye tracking and blink detection
- And much more!

Want to contribute? Check the TODO.md for tasks you can help with!

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## 📞 Support

If you encounter any issues or have suggestions, please open an issue on GitHub.

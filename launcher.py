#!/usr/bin/env python3
"""
Break Reminder App - Launcher
Automatically detects and runs the best version for your system.
"""

import sys
import os
import subprocess

def check_flask():
    """Check if Flask is installed."""
    try:
        import flask
        return True
    except ImportError:
        return False

def check_tkinter():
    """Check if tkinter is available."""
    try:
        import tkinter
        return True
    except ImportError:
        return False

def main():
    print("🕐 Break Reminder App Launcher")
    print("=" * 50)
    
    # Check for command line arguments
    if len(sys.argv) > 1:
        if sys.argv[1] == "--web":
            print("Starting web version...")
            if check_flask():
                subprocess.run([sys.executable, "web_app.py"])
            else:
                print("❌ Flask is not installed!")
                print("Install it with: pip install -r requirements.txt")
                sys.exit(1)
        elif sys.argv[1] == "--desktop":
            print("Starting desktop version...")
            if check_tkinter():
                subprocess.run([sys.executable, "BreakReminderApp.py"])
            else:
                print("❌ Tkinter is not available!")
                print("Use the web version instead: python launcher.py --web")
                sys.exit(1)
        elif sys.argv[1] == "--help" or sys.argv[1] == "-h":
            print("\nUsage:")
            print("  python launcher.py           # Auto-detect and run best version")
            print("  python launcher.py --web     # Run web version")
            print("  python launcher.py --desktop # Run desktop version")
            print("  python launcher.py --help    # Show this help")
            sys.exit(0)
        else:
            print(f"❌ Unknown option: {sys.argv[1]}")
            print("Use --help to see available options")
            sys.exit(1)
    else:
        # Auto-detect best version
        print("\n🔍 Auto-detecting best version for your system...")
        
        if check_flask():
            print("✅ Flask detected - Starting web version (recommended)")
            print("\n📱 The web version works on ALL devices!")
            print("   Access from this computer: http://localhost:5000")
            print("   Access from mobile/tablet: http://YOUR_IP:5000")
            print("\n" + "=" * 50 + "\n")
            subprocess.run([sys.executable, "web_app.py"])
        elif check_tkinter():
            print("✅ Tkinter detected - Starting desktop version")
            print("\n💡 Tip: Install Flask for cross-platform web version:")
            print("   pip install -r requirements.txt")
            print("\n" + "=" * 50 + "\n")
            subprocess.run([sys.executable, "BreakReminderApp.py"])
        else:
            print("❌ No compatible version found!")
            print("\nInstall Flask for the web version (recommended):")
            print("  pip install -r requirements.txt")
            print("\nOr ensure tkinter is available for the desktop version.")
            sys.exit(1)

if __name__ == "__main__":
    main()

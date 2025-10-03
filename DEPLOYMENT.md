# Deployment Guide - Standalone Applications

This guide explains how to create standalone versions of the Break Reminder App for different platforms.

## 📱 Android APK (Mobile & Tablet)

### Using Kivy + Buildozer

The web version can be packaged as an Android APK using Kivy and Buildozer.

#### Prerequisites
- Linux system (or WSL on Windows)
- Python 3.7+
- Android SDK

#### Steps to Build APK

1. **Install Buildozer**
   ```bash
   pip install buildozer
   pip install cython
   ```

2. **Create Kivy App** (we'll create a WebView wrapper)
   ```bash
   # The app will use a WebView to display the Flask app
   # Or we can create a native Kivy version
   ```

3. **Initialize Buildozer**
   ```bash
   buildozer init
   ```

4. **Configure buildozer.spec**
   Edit the generated `buildozer.spec` file:
   ```ini
   [app]
   title = Break Reminder
   package.name = breakreminder
   package.domain = org.breakreminder
   source.dir = .
   source.include_exts = py,png,jpg,kv,atlas,json
   version = 1.0
   requirements = python3,flask,kivy
   permissions = INTERNET,VIBRATE
   android.permissions = INTERNET,VIBRATE
   orientation = portrait
   ```

5. **Build the APK**
   ```bash
   buildozer -v android debug
   ```

6. **Find your APK**
   The APK will be in: `bin/breakreminder-1.0-debug.apk`

### Alternative: Using PWA (Progressive Web App)

The web version can be installed as a PWA on Android:

1. Open the web app in Chrome on your Android device
2. Tap the menu (three dots)
3. Select "Add to Home screen"
4. The app will work like a native app!

**Advantages of PWA:**
- No need to build APK
- Automatic updates
- Works on all devices
- Smaller size than native app

## 💻 Windows EXE (Laptop & Desktop)

### Using PyInstaller

Package the web app as a Windows executable using PyInstaller.

#### Prerequisites
- Windows system
- Python 3.7+

#### Steps to Build EXE

1. **Install PyInstaller**
   ```bash
   pip install pyinstaller
   ```

2. **Create a launcher script** (`run_app.py`)
   ```python
   import os
   import sys
   import webbrowser
   import threading
   from time import sleep
   
   # Import the Flask app
   from web_app import app
   
   def open_browser():
       sleep(1.5)  # Wait for server to start
       webbrowser.open('http://127.0.0.1:5000')
   
   if __name__ == '__main__':
       # Start browser in a separate thread
       threading.Thread(target=open_browser).start()
       
       # Run Flask app
       app.run(host='127.0.0.1', port=5000, debug=False)
   ```

3. **Build the EXE**
   ```bash
   pyinstaller --onefile --windowed --icon=icon.ico --name="BreakReminder" run_app.py
   ```

   Options explained:
   - `--onefile`: Creates a single executable
   - `--windowed`: No console window (GUI only)
   - `--icon=icon.ico`: Custom icon (optional)
   - `--name`: Name of the executable

4. **Include templates and static files**
   Create a `BreakReminder.spec` file:
   ```python
   # -*- mode: python ; coding: utf-8 -*-
   
   block_cipher = None
   
   a = Analysis(
       ['run_app.py'],
       pathex=[],
       binaries=[],
       datas=[('templates', 'templates'), ('static', 'static')],
       hiddenimports=['flask'],
       hookspath=[],
       hooksconfig={},
       runtime_hooks=[],
       excludes=[],
       win_no_prefer_redirects=False,
       win_private_assemblies=False,
       cipher=block_cipher,
       noarchive=False,
   )
   pdb = PDB(a.pure, a.zipped_data, cipher=block_cipher)
   
   exe = EXE(
       pdb,
       a.scripts,
       a.binaries,
       a.zipfiles,
       a.datas,
       [],
       name='BreakReminder',
       debug=False,
       bootloader_ignore_signals=False,
       strip=False,
       upx=True,
       upx_exclude=[],
       runtime_tmpdir=None,
       console=False,
       disable_windowed_traceback=False,
       argv_emulation=False,
       target_arch=None,
       codesign_identity=None,
       entitlements_file=None,
       icon='icon.ico'
   )
   ```

5. **Build using spec file**
   ```bash
   pyinstaller BreakReminder.spec
   ```

6. **Find your EXE**
   The executable will be in: `dist/BreakReminder.exe`

### Using Auto-py-to-exe (GUI Tool)

For a more user-friendly approach:

1. **Install auto-py-to-exe**
   ```bash
   pip install auto-py-to-exe
   ```

2. **Run the GUI**
   ```bash
   auto-py-to-exe
   ```

3. **Configure in the GUI:**
   - Select `run_app.py` as the script
   - Choose "One File"
   - Choose "Window Based"
   - Add templates and static folders as additional files
   - Click "Convert .py to .exe"

## 🍎 macOS APP Bundle

### Using PyInstaller on macOS

1. **Install PyInstaller**
   ```bash
   pip install pyinstaller
   ```

2. **Build the APP**
   ```bash
   pyinstaller --onefile --windowed --name="BreakReminder" run_app.py
   ```

3. **Find your APP**
   The app bundle will be in: `dist/BreakReminder.app`

## 🐧 Linux AppImage

### Using PyInstaller + AppImage Tools

1. **Build with PyInstaller**
   ```bash
   pyinstaller --onefile --name="breakreminder" run_app.py
   ```

2. **Create AppImage** (using appimagetool)
   ```bash
   # Download appimagetool
   wget https://github.com/AppImage/AppImageKit/releases/download/continuous/appimagetool-x86_64.AppImage
   chmod +x appimagetool-x86_64.AppImage
   
   # Create AppDir structure
   mkdir -p BreakReminder.AppDir/usr/bin
   cp dist/breakreminder BreakReminder.AppDir/usr/bin/
   
   # Create .desktop file
   cat > BreakReminder.AppDir/breakreminder.desktop << EOF
   [Desktop Entry]
   Name=Break Reminder
   Exec=breakreminder
   Icon=breakreminder
   Type=Application
   Categories=Utility;
   EOF
   
   # Build AppImage
   ./appimagetool-x86_64.AppImage BreakReminder.AppDir
   ```

## 📦 Distribution

### For Safe Distribution

1. **Code Signing (Recommended)**
   - Windows: Use SignTool with a code signing certificate
   - macOS: Use Developer ID certificate
   - Android: Use keystore for release builds

2. **Create Release Package**
   - Include README with instructions
   - Add license file
   - Create changelog
   - Zip the executable with docs

3. **Host on GitHub Releases**
   - Create a release tag
   - Upload compiled binaries
   - Add release notes
   - Users can download safely from GitHub

### Security Notes

- Always scan executables with antivirus before distribution
- Use HTTPS for downloads
- Provide checksums (SHA256) for verification
- Sign your code to avoid "unknown publisher" warnings

## 🔄 Updates

For automatic updates, consider:
- **Web version**: Auto-updates (just refresh the browser)
- **Desktop apps**: Implement update checker that downloads from GitHub releases
- **Android**: Use in-app update mechanism or publish updates as new APK

## ⚠️ Important Notes

1. **APK Building**: Best done on Linux or macOS, Windows can use WSL
2. **EXE Building**: Must be built on Windows for best compatibility
3. **File Size**: Executables will be larger (30-50MB) due to bundled Python runtime
4. **Testing**: Always test on target platform before distributing
5. **Permissions**: Android APK needs internet permission for notifications

## 🚀 Quick Commands Summary

```bash
# Android APK
buildozer -v android debug

# Windows EXE
pyinstaller --onefile --windowed --name="BreakReminder" run_app.py

# macOS APP
pyinstaller --onefile --windowed --name="BreakReminder" run_app.py

# Linux AppImage
pyinstaller --onefile --name="breakreminder" run_app.py
```

## 📱 Recommended Approach

**For Mobile/Tablet:**
- Use PWA (Progressive Web App) - easiest and most maintainable
- Or create native Kivy app for full offline support

**For Desktop:**
- PyInstaller for single executable
- Or keep as web app (most flexible)

The web version approach is recommended as it:
- Works everywhere
- No compilation needed
- Easy to update
- Smaller download size
- Cross-platform by default

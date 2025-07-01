# 🎵 Python Audio Analysis Music Player

A fully-featured, real-time music player built with Python, offering advanced audio visualization, intelligent analysis, and customization tools.

---

## 🚀 Features

- Real-time audio playback
- Built with:
  - `wxPython`, `NumPy`, `SciPy`, `PyBASS`, `Un4seen BASS`, `LoudMax VST`
- Drag-and-drop support for a wide range of audio formats and playlists:
  - `mp2`, `mp3`, `mp4`, `wav`, `m4a`, `ape`, `flac`, `aac`, `ac3`, `aiff`, `wma`, `ogg`, `m3u`
- Displays:
  - Waveform as a seek bar
  - Real-time log-scale mel-frequency spectrum
  - Real-time stereo vectorscope
- Music analysis:
  - Detects tempo, key, and musical highlights
  - Highlights shown on waveform and playable independently
- Multithreaded/multiprocess analysis for speed
- Ultra-fast and accurate BPM detection
- ID3 tag editing supported
- Editable hotkeys
- Automatic gain control using LoudMax VST
- SQLite database caching for fast repeat access

### 🔔 Playlist Indicators

- 🔴 Red icon: Track not analyzed
- 🔵 Blue icon: Currently analyzing
- ✅ No icon: Analysis complete
- ⚠️ Exclamation icon: Track missing or moved (use "Check File Consistency")

---

## 🛠️ How to Install and Run

### ✅ Option 1: Use Prebuilt Installer

Download and install the latest release from the project page.

---

### 🧱 Option 2: Build from Source

**Requirements:**
- Python 3.x
- Dependencies from `requirements.pip`
- [InnoSetup](https://jrsoftware.org/isinfo.php) for packaging (Windows)

**Steps:**
```bash
pip install -r requirements.pip
choco install innosetup  # (for Windows users)
python makebuild.py

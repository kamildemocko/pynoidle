# PyNoIdle

A lightweight Python application that prevents your system from going idle by subtly moving the mouse cursor.

## Description

PyNoIdle runs as a system tray application that automatically **wiggles** your mouse cursor to keep your system active. It features a simple toggle interface and visual **notifications** to let you know when it's active.

## Features

- **System Tray Integration**: Clean interface with start/stop toggle
- **Smart Detection**: Only activates after detecting mouse inactivity
- **Minimal Movement**: Subtle 1-pixel cursor movements

## Requirements

- Python 3.13+
- Dependencies: mouse, pillow, pystray

## Installation

```bash
uv sync
```

## Usage

Run the application:

```bash
uv run pynoidle
```

The application will appear in your system tray with these options:
- **Start/Stop**: Toggle mouse wiggling on/off
- **Quit**: Exit the application

## Configuration

Default settings in `main.py`:
- `START_TIME_AFTER_SEC = 10`: Seconds of inactivity before wiggling starts
- `IN_BETWEEN_DELAY = 3`: Seconds between each wiggle movement

## License

MIT License

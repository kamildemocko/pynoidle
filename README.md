# PyNoIdle

A lightweight Python application that prevents your system from going idle by subtly simulating keyboard activity.

## Description

PyNoIdle runs as a system tray application that automatically simulates keyboard presses to keep your system active. 
It features a simple toggle interface and visual **notifications** to let you know when it's active.

## Features

- **System Tray Integration**: Clean interface with start/stop toggle
- **Minimal Activity**: Subtle key presses that don't interfere with your work

## Requirements

- Dependencies: keyboard, pillow, pystray

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
- **Start/Stop**: Toggle keyboard activity on/off
- **Quit**: Exit the application

## Configuration

Default settings in `main.py`:
- `IN_BETWEEN_DELAY = 20`: Seconds between each key press

## License

MIT License

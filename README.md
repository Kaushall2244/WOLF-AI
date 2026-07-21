# 🐺 WOLF OS

> Your Personal AI-Powered Linux Desktop Assistant

WOLF OS is an open-source desktop AI assistant designed for Linux. It combines voice control, system monitoring, application launching, and local AI models into one intelligent assistant.

Unlike traditional assistants, WOLF is built to become a real desktop copilot capable of controlling applications, understanding natural language, automating tasks, and eventually running completely offline using local Large Language Models (LLMs).

---

# ✨ Current Features

## 🎤 Voice Recognition
- Wake and listen for commands
- Speech-to-text
- Natural voice interaction

## 🔊 Voice Responses
- Text-to-Speech
- Human-like responses
- Custom assistant personality

## 🧠 Intent Detection
- Greeting detection
- System information
- Open applications
- Exit commands
- Unknown command handling

## 💻 Application Launcher
Launch applications using voice.

Currently supported:

- Firefox
- Google Chrome
- Steam
- Discord
- Visual Studio Code
- Kitty Terminal
- Thunar File Manager
- SKLauncher (Minecraft)

Example:

```
Open Steam
Launch Chrome
Open VS Code
Run Minecraft
```

---

## 📊 System Information

Retrieve live system statistics.

Supported:

- CPU Usage
- RAM Usage
- Battery Percentage
- Current Time

Examples:

```
CPU usage
How much memory is used?
Battery
Current time
```

---

## 💬 Personality Engine

WOLF responds naturally instead of using fixed messages.

Example:

```
Hello

↓

Hello Wolf!
```

```
Who are you?

↓

I'm WOLF, your desktop AI.
```

---

## 🧠 Memory System

WOLF remembers:

- Previous command
- Last opened application

This enables future contextual conversations.

Example:

```
Open Steam

↓

Open it again

↓

Close it
```

---

# 📁 Project Structure

```
jarvisOS/

│
├── ai/
├── commands/
├── config/
├── docs/
├── frontend/
├── logs/
├── scripts/
├── sounds/
├── themes/
├── wallpapers/
│
├── backend/
│
│   ├── main.py
│   ├── dashboard.py
│
│   └── core/
│       ├── assistant.py
│       ├── brain.py
│       ├── launcher.py
│       ├── memory.py
│       ├── parser.py
│       ├── personality.py
│       ├── router.py
│       ├── skill_manager.py
│       ├── speech.py
│       ├── system.py
│       ├── utils.py
│       └── __init__.py
│
├── requirements.txt
└── README.md
```

---

# 🛠️ Technologies

- Python 3.14
- Rich
- psutil
- SpeechRecognition
- PyAudio
- pyttsx3
- eSpeak-ng

Future:

- Ollama
- Whisper
- Piper TTS
- Vosk
- Llama
- Qwen
- DeepSeek
- FastAPI
- Electron / Qt

---

# 🚀 Installation

Clone the repository

```bash
git clone https://github.com/yourusername/WOLF-OS.git
```

Go into the project

```bash
cd WOLF-OS
```

Create a virtual environment

```bash
python -m venv .venv
```

Activate it

### Linux (bash)

```bash
source .venv/bin/activate
```

### Fish Shell

```fish
source .venv/bin/activate.fish
```

Install dependencies

```bash
pip install -r requirements.txt
```

Install eSpeak

### Arch Linux

```bash
sudo pacman -S espeak-ng
```

Run

```bash
cd backend

python main.py
```

---

# 🎙️ Example Commands

```
Hello

How are you

Who are you

Open Steam

Open Chrome

Open Firefox

Open VS Code

Open Terminal

Open Minecraft

CPU usage

Battery

RAM

Time

Exit
```

---

# 🚧 Roadmap

## Phase 1 ✅
- Project setup

## Phase 2 ✅
- Dashboard

## Phase 3 ✅
- Voice Recognition

## Phase 4 ✅
- Text To Speech

## Phase 5 ✅
- Brain / Intent Detection

## Phase 6 ✅
- Application Launcher

## Phase 7 ✅
- Skill Manager

## Phase 8 ✅
- Memory System

## Phase 9 ✅
- Personality Engine

---

## Upcoming

### Local AI (Ollama)

- Offline LLM
- Code generation
- Chat
- Reasoning

---

### Automation

- Browser automation
- File management
- Clipboard assistant
- Screenshot assistant

---

### Smart Desktop

- Window management
- Workspace switching
- Notifications
- Media controls

---

### Gaming

- Steam integration
- MangoHud control
- Discord Rich Presence
- FPS monitoring

---

### Development

- Git integration
- VS Code automation
- Project generation
- Terminal assistant

---

### Vision

- OCR
- Image understanding
- Screen reading
- Object detection

---

### Future AI

- Memory database
- Long-term memory
- Personalized responses
- Workflow learning

---

# 🎯 Vision

The goal of WOLF OS is to become a true AI operating system companion—not just a voice assistant.

WOLF is designed to:

- Understand natural language
- Control the Linux desktop
- Automate repetitive tasks
- Help developers
- Assist gamers
- Operate completely offline
- Learn user preferences
- Integrate local AI models

Ultimately, WOLF aims to provide a seamless AI experience where interacting with your computer feels as natural as talking to another person.

---

# 📜 License

MIT License

---

# 👨‍💻 Developer

Developed with ❤️ by **Wolf**

**Project:** WOLF OS

```
"Powering Linux with Intelligence."
```
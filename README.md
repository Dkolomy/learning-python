# Learning Python

A starter project with an isolated Python environment.

## Prerequisites

- Python 3.11+ (you have 3.11.5 installed)

## Setup (one time)

### 1. Activate the virtual environment

**PowerShell** (recommended in Cursor terminal):

```powershell
.\.venv\Scripts\Activate.ps1
```

**Command Prompt:**

```cmd
.venv\Scripts\activate.bat
```

When active, your prompt shows `(.venv)`.

### 2. Install dependencies (when you add packages)

```powershell
pip install -r requirements.txt
```

## Run your code

With the venv activated:

```powershell
python main.py
```

Or without activating (uses the venv Python directly):

```powershell
.\.venv\Scripts\python.exe main.py
```

## Add new packages

```powershell
pip install package-name
pip freeze > requirements.txt
```

## Project layout

```
LearningPython/
├── .venv/           # Virtual environment (do not edit by hand)
├── main.py          # Your first script
├── requirements.txt # Project dependencies
└── README.md
```

## Cursor / VS Code

Select the interpreter: **Python: Select Interpreter** → choose  
`.venv\Scripts\python.exe` in this folder.

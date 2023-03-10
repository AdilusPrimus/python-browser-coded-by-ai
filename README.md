# Discovering Python GUI programming with the help of ChatGPT AI

![You thought that this was strictly science fiction? Think again!](img/Skynet.jpeg)

## Goal

The goal of this experience was to make the **ChatGPT** code for me an application.
I was only contributing the requirements of the web browser and reporting back the behavior of the proposed code, once it was subjected to the Python3 runtime during execution.
So reporting in a natural language the exceptions, and negotiating (*sometimes*) the proposal of solutions.
I chose on purpose a language and frameworks that I never experienced in the past (**Python** and **QT5**), thus leaving the full space for the AI to debug its own proposed code, hoping to contribute in its evolution.
Even if I have a background in software engineering, I'll try to interact with the AI as a newbie, in order to see if a non software engineer could achieve delivering a custom solution that implements his or her business requirements.

> If so, we'll need to update our Linkedin profiles...

I welcome you to join  me in this experience since it is something that I never imagined being able to do one day!

## Building a web browser

So I have decided to build a full fledged web browser, that needs to end up portable on MacOS, Linux and even Windows.
We'll specialize as we go this browser to become yet another interface for OpenAI APis (ChatGPT).
I have started coding on my Mac but I contribute as well source code and configurations from my other setup, that is my Linux workstation (Ubuntu).

> It is amazing how we human beings do adapt to what is in front of us: was it me who became more precise (thus concise), or was it the AI who started to understand the intention here?
> Time will tell...

This project will evolve in time by adding more and more features until this tiny browser resembles the ones we are used to.
We'll be exploring with the AI how to build a web browser that interfaces the ChatGPT (as inspired by other open source projects), following the AI's integration guidelines.

**Please feel free to contribute ideas in the issues section of the repo**.

### Interacting with Chat GPT

In this section, I give you some samples of my conversation with the AI.
This will give you more ideas on how natural a conversation can go, and how this technology behaves in different scenarios.
The odd thing is that it helps me debug its own code!
So if it knows how to do so, it is a lack of precision from our end (when contributing requirements) or a lack of understanding (or the loss of the current context) from the AI, when it interprets our says.

#### The chat with... an AI!?

**Me:**
*Build web browser using **python** and **qtpy5** and show me how to install all dependencies using pip command (python3)*

***ChatGTP:***

``` bash
The QtPy5 library is a Python binding for the Qt5 library, which provides comprehensive GUI and application development support. To install all the dependencies for web browser development using QtPy5 and Python3, you can use the following pip command:

pip install qtpy5==5.15.2 PyQtWebEngine==5.15.2
```

**Me:**

Give me all required dependencies

**ChatGPT:**

``` bash
The following is a list of all the dependencies you will need to build a web browser using QtPy5 and Python3:

- QtPy5 version 5.15.2
- PyQtWebEngine version 5.15.2
- sip version 4.19.15
- Python3
```

**Me:**

Now generate the browser code

**ChatGPT:**

``` bash
The following code can be used to generate a basic web browser using QtPy5 and Python3:
```

``` python
import sys
from PyQt5.QtWidgets import QApplication
from PyQt5.QtWebEngineWidgets import QWebEngineView

# Create an instance of QApplication
app = QApplication(sys.argv)

# Create an instance of QWebEngineView
web_view = QWebEngineView()

# Set the URL for the web page to be displayed
web_view.setUrl("https://www.example.com")

# Show the web page
web_view.show()

# Execute the application
sys.exit(app.exec_())
```

**Me:**

``` bash
I get the following exception:

TypeError: setUrl(self, url: QUrl): argument 1 has unexpected type 'str'
```

***ChatGTP:***

``` bash
This is because the setUrl method requires a QUrl object as the argument, rather than a string.
To fix this, you need to import the QUrl class from the PyQt5.QtCore module and then create a QUrl object from the string before passing it to the setUrl method. For example:
```

``` python
from PyQt5.QtCore import QUrl

# Set the URL for the web page to be displayed
web_view.setUrl(QUrl("https://www.example.com"))
```

**Me:**

I'd like the window to be initially twice the size of the browser window

**ChatGPT:**

```bash
To set the initial window size to twice the size of the browser window, you can use the setGeometry method of the QWebEngineView object. For example:

# Set the window size to twice the size of the browser window
web_view.setGeometry(0, 0, 2*web_view.width(), 2*web_view.height())
```

...

And this exchange went like this until I was able to stabilize the browser application.

> Each time I had a configuration or exception in the code, I submitted it to the AI:
> Almost no code was designed or patched based on my thoughts, the AI thought it all.
I played only the role of the analyst and technical secretary, when contirbuting the proposed changes.

## Pre-requisites

### Mac

> Installing python3, pip3, qt5 framework and the packager for distrution pyinstaller

``` bash
brew install python3 qt5 pyinstaller
echo 'export PATH="/opt/homebrew/opt/qt@5/bin:$PATH"' >> ~/.zshrc
```

### Linux

``` bash
sudo apt install -y python3 qtcreator qtbase5-dev qt5-qmake cmake  pyqt5-dev-tools qttools5-dev-tools
```

### Windows

> *Coming soon*

### Github configuration

The Github Action scripts where defined accordingly by leveraging the AI guiding and the Github ready to use templates:
    - Software Composition Analysis (SCA) by dependabot
      - .github/dependabot.yml
      - .github/workflows/dependency-review.yml
    - Static Application Security Testing (SAST) including build and packaging with CodeQL for Python:
      - .github/workflows/codeql.yml
    - SAST with Bandit for Python:
      - .github/workflows/bandit.yml

### vscode configuration

> We need to configure an Interpreter for the your the project workspace
Please select Python 3.10.x interpreter (CTRL+SHIT+P Python: Select Interpreter)
> The AI already told us how to configure a Debugger: see .vscode/launch.json

Install proposed extensions: .vscode/extensions.json
> vscode will prompt an option automatically when loading workspace

### Workspace setup

Generating our sandbox (workspace isolation)

From the Terminal of vscode pointing to the project root, type the following commands:

```bash
python3 -m venv .venv
chmod u+x .venv/bin/activate
.venv/bin/activate
```

### Managing dependencies

> Downloading required libraries using pip

```bash
python3 -m pip install --upgrade pip
python3 -m pip install sip PyQtWebEngine pyinstaller
python3 -m pip install pyqt5 --config-settings --confirm-license= --verbose
python3 -m pip freeze > requirements.txt
```

> Wait for a while for completion

```bash
...
Successfully installed PyQt5-sip-12.11.0 pyqt5-5.15.7
```

### Packaging the application (generating binary)

```bash
$ pyinstaller --log-level=DEBUG --clean browser.spec

75 INFO: PyInstaller: 5.7.0
75 INFO: Python: 3.10.9
94 INFO: Platform: macOS-13.1-arm64-arm-64bit
95 INFO: wrote /Users/bond007/Workspaces/PythonBrowser/browser.spec
97 INFO: UPX is not available.
97 INFO: Extending PYTHONPATH with paths

...

2202 INFO: Warnings written to /Users/bond007/Workspaces/PythonBrowser/build/browser/
3813 INFO: Appending PKG archive to EXE
3815 INFO: Fixing EXE headers for code signing
3818 INFO: Re-signing the EXE
3838 INFO: Building EXE from EXE-00.toc completed successfully.
```

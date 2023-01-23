# Exploring Python with the help of ChatGPT

## Building a web browser

The goal of this experience was to make the **ChatGPT** code for me an application.
I was only contributing the requirements of the web browser and reporting back the behavior of the proposed code, once it was subjected to the Python3 runtime during execution.
So reporting in a natural language the exceptions, and negotiating (*sometimes*) the proposal of solutions.
I chose on purpose a language and frameworks that I never experienced in the past, thus leaving the full space for the AI to debug its own proposed code, hoping to contribute in its evolution.

> It is amazing how we human beings do adapt to what is in front of us: was it me who became more precise (thus concise) or was it the AI who started to understand the intention here.

This project will evolve in time by adding more and more features until this tiny browser resembles the ones we are used to.

### Interacting with Chat GPT

In this section, I give you some samples of my conversation with the AI.

> I wil only transcript the parts that I found either interesting, weird or that amazed me with some personal thoughts of course.

#### The beginning

**Me:** 
*Build web browser using python and qtpy5 and show me how t install all dependencies using pip command (python3)*

***ChatGTP:***

``` bash
The QtPy5 library is a Python binding for the Qt5 library, which provides comprehensive GUI and application development support. To install all the dependencies for web browser development using QtPy5 and Python3, you can use the following pip command:

pip install qtpy5==5.15.2 PyQtWebEngine==5.15.2
```

**Me:** 

*Give me all required dependencies*

**ChatGPT:**

``` bash
The following is a list of all the dependencies you will need to build a web browser using QtPy5 and Python3:

- QtPy5 version 5.15.2
- PyQtWebEngine version 5.15.2
- sip version 4.19.15
- Python3
```

**Me:**

*Now generate the browser code*

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
This is because the setUrl method requires a QUrl object as the argument, rather than a string. To fix this, you need to import the QUrl class from the PyQt5.QtCore module and then create a QUrl object from the string before passing it to the setUrl method. For example:
```

``` python
from PyQt5.QtCore import QUrl

# Set the URL for the web page to be displayed
web_view.setUrl(QUrl("https://www.example.com"))
```

**Me:**

*I'd like the window to be initially twice the size of the browser window*

**ChatGPT:**

```bash
To set the initial window size to twice the size of the browser window, you can use the setGeometry method of the QWebEngineView object. For example:

# Set the window size to twice the size of the browser window
web_view.setGeometry(0, 0, 2*web_view.width(), 2*web_view.height())
```

...

And this exchange went like this until I was able to stabilize the browser application.

> Each time I had a configuration or exception in the code, I submitted it to the AI: nothing was fixed or contributed by myself, I was only the main in the middle here

## Pre-requisites

### Mac:

> Installing python3, pip3, qt5 framework and the packager for distrution pyinstaller

``` bash
brew install python3 pip3 qt5 pyinstaller
echo 'export PATH="/opt/homebrew/opt/qt@5/bin:$PATH"' >> ~/.zshrc
```

### vscode configuration

Install proposed extensions: .vscode/extensions.json
> vscode will prompt an option automatically when loading workspace

### Workspace

> Generating our sandbox (workspace isolation)

``` bash
python3 -m venv .venv
.venv/bin/activate
```

### Managing dependencies

> Downloading required libraries using pip

``` bash
python3 -m pip install --upgrade pip
python3 -m pip install sip PyQtWebEngine PyQt5 --config-settings --confirm-license= --verbose
```

> Wait for a while for completition

``` bash
...
Successfully installed PyQt5-sip-12.11.0 pyqt5-5.15.7
```

### Packaging the application (generating binary)

``` bash
$ pyinstaller --onefile --paths "/opt/homebrew/opt/qt@5" browser.py

75 INFO: PyInstaller: 5.7.0
75 INFO: Python: 3.10.9
94 INFO: Platform: macOS-13.1-arm64-arm-64bit
95 INFO: wrote /Users/bond007/Workspaces/PythonBrowser/browser.spec
97 INFO: UPX is not available.
97 INFO: Extending PYTHONPATH with paths
['/Users/bond007/Workspaces/PythonBrowser',
 '/opt/homebrew/opt/qt@5']
206 INFO: checking Analysis
208 INFO: Building because pathex changed
208 INFO: Initializing module dependency graph...
210 INFO: Caching module graph hooks...
216 INFO: Analyzing base_library.zip ...
606 INFO: Loading module hook 'hook-encodings.py' from '/opt/homebrew/lib/python3.10/site-packages/PyInstaller/hooks'...
818 INFO: Loading module hook 'hook-heapq.py' from '/opt/homebrew/lib/python3.10/site-packages/PyInstaller/hooks'...
982 INFO: Loading module hook 'hook-pickle.py' from '/opt/homebrew/lib/python3.10/site-packages/PyInstaller/hooks'...
1975 INFO: Caching module dependency graph...
2024 INFO: running Analysis Analysis-00.toc
2027 INFO: Analyzing /Users/bond007/Workspaces/PythonBrowser/browser.py
2029 INFO: Processing module hooks...
2036 INFO: Looking for ctypes DLLs
2037 INFO: Analyzing run-time hooks ...
2038 INFO: Including run-time hook '/opt/homebrew/lib/python3.10/site-packages/PyInstaller/hooks/rthooks/pyi_rth_inspect.py'
2041 INFO: Looking for dynamic libraries
2200 INFO: Looking for eggs
2200 INFO: Using Python library /opt/homebrew/Cellar/python@3.10/3.10.9/Frameworks/Python.framework/Versions/3.10/Python
2202 INFO: Warnings written to /Users/bond007/Workspaces/PythonBrowser/build/browser/warn-browser.txt
2209 INFO: Graph cross-reference written to /Users/bond007/Workspaces/PythonBrowser/build/browser/xref-browser.html
2212 INFO: checking PYZ
2213 INFO: Building because toc changed
2213 INFO: Building PYZ (ZlibArchive) /Users/bond007/Workspaces/PythonBrowser/build/browser/PYZ-00.pyz
2333 INFO: Building PYZ (ZlibArchive) /Users/bond007/Workspaces/PythonBrowser/build/browser/PYZ-00.pyz completed successfully.
2336 INFO: EXE target arch: arm64
2336 INFO: Code signing identity: None
2336 INFO: checking PKG
2337 INFO: Building because toc changed
2337 INFO: Building PKG (CArchive) browser.pkg
3775 INFO: Building PKG (CArchive) browser.pkg completed successfully.
3778 INFO: Bootloader /opt/homebrew/lib/python3.10/site-packages/PyInstaller/bootloader/Darwin-64bit/run
3778 INFO: checking EXE
3779 INFO: Building because toc changed
3779 INFO: Building EXE from EXE-00.toc
3779 INFO: Copying bootloader EXE to /Users/bond007/Workspaces/PythonBrowser/dist/browser
3780 INFO: Converting EXE to target arch (arm64)
3798 INFO: Removing signature(s) from EXE
3813 INFO: Appending PKG archive to EXE
3815 INFO: Fixing EXE headers for code signing
3818 INFO: Re-signing the EXE
3838 INFO: Building EXE from EXE-00.toc completed successfully.
```

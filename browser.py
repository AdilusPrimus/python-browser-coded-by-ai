import sys
import PyQt5

from PyQt5.QtCore import QUrl, Qt
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QHBoxLayout, QPushButton, QLineEdit
from PyQt5.QtWebEngineWidgets import QWebEngineView

class Browser(QWebEngineView):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Safarire')
        self.setGeometry(0, 0, 1024, 600)
        self.setWindowFlags(Qt.Window | Qt.WindowStaysOnTopHint | Qt.WindowCloseButtonHint | Qt.WindowFullscreenButtonHint)

def main():
    app = QApplication(sys.argv)
    browser = Browser()
    try:
        browser.load(QUrl('https://heeeeeeeey.com'))
    except Exception as e:
        print("Error occured while loading the web page: ", e)
        return

    # Create buttons
    backButton = QPushButton('Back')
    forwardButton = QPushButton('Forward')
    refreshButton = QPushButton('Refresh')
    goButton = QPushButton('Go')
    
    # Connect buttons to functions
    backButton.clicked.connect(browser.back)
    forwardButton.clicked.connect(browser.forward)
    refreshButton.clicked.connect(browser.reload)

    # Create a container widget to hold the layout and the buttons
    container = QWidget()

    # Add a line edit for the URL
    url_line_edit = QLineEdit()
    url_line_edit.setText('https://puginarug.com')

    # Add buttons to layout
    layout = QVBoxLayout()
    layout_inner = QHBoxLayout()
    layout_inner.addWidget(backButton)
    layout_inner.addWidget(forwardButton)
    layout_inner.addWidget(refreshButton)
    layout_inner.addWidget(url_line_edit)
    layout_inner.addWidget(goButton)    
    layout.addLayout(layout_inner)
    layout.addWidget(browser)

    # Set the layout for the container widget
    container.setLayout(layout)

    # Show the container widget
    container.show()
    goButton.clicked.connect(lambda: browser.load(QUrl(url_line_edit.text())))
    app.exec_()
    browser.deleteLater()

if __name__ == '__main__':
    main()

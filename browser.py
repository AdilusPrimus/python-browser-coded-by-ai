import sys, os

from PyQt5.QtGui import QIcon
from PyQt5.QtCore import QUrl, Qt
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QHBoxLayout, QPushButton, QLineEdit
from PyQt5.QtWebEngineWidgets import QWebEngineView

basedir = os.path.dirname(__file__)
class Browser(QWebEngineView):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Safarire')
        self.setGeometry(0, 0, 1024, 600)
        self.setWindowFlags(Qt.Window | Qt.WindowStaysOnTopHint | Qt.WindowCloseButtonHint | Qt.WindowFullscreenButtonHint)
        self.setWindowIcon(QIcon(os.path.join(basedir, './img/appstorm.svg')))

def main():
    app = QApplication(sys.argv)
    browser = Browser()
    try:
        browser.load(QUrl('https://heeeeeeeey.com'))
    except Exception as e:
        print("Error occurred while loading the web page: ", e)
        return

    # Create buttons
    back_button = QPushButton('Back')
    forward_button = QPushButton('Forward')
    refresh_button = QPushButton('Refresh')
    go_button = QPushButton('Go')
    
    # Connect buttons to functions
    back_button.clicked.connect(browser.back)
    forward_button.clicked.connect(browser.forward)
    refresh_button.clicked.connect(browser.reload)

    # Create a container widget to hold the layout and the buttons
    container = QWidget()

    # Add a line edit for the URL
    url_line_edit = QLineEdit()
    url_line_edit.setText('https://puginarug.com')

    # Add buttons to layout
    layout = QVBoxLayout()
    layout_inner = QHBoxLayout()
    layout_inner.addWidget(back_button)
    layout_inner.addWidget(forward_button)
    layout_inner.addWidget(refresh_button)
    layout_inner.addWidget(url_line_edit)
    layout_inner.addWidget(go_button)    
    layout.addLayout(layout_inner)
    layout.addWidget(browser)

    # Set the layout for the container widget
    container.setLayout(layout)

    # Show the container widget
    container.show()
    go_button.clicked.connect(lambda: browser.load(QUrl(url_line_edit.text())))
    app.exec_()
    browser.deleteLater()

if __name__ == '__main__':
    main()

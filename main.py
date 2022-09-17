from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtWebEngineWidgets import *


class StarBrowser ():
    def __init__(self):
        self.window = QWidget()
        self.window.setStyleSheet("background-color: #373737;")
        self.window.setWindowTitle("StarBrowser")

        self.layout = QVBoxLayout()
        self.horizontal = QHBoxLayout

        self.input_url = QTextEdit()
        self.input_url.setMaximumHeight(30)
        self.input_url.setStyleSheet("background-color: #373737; color: #FFF; font-weight: 700;")

        self.search_btn = QPushButton("Поиск")
        self.search_btn.setMaximumHeight(30)
        self.search_btn.setStyleSheet(
            "background-color: #141414; color: #fff; font-weight: 900; width: 70px; border: 2px solid #000;")

        self.back_btn = QPushButton("<")
        self.back_btn.setMaximumHeight(30)
        self.back_btn.setStyleSheet(
            "background-color: #212121; color: #fff; font-weight: 900; width: 30px; border: 2px solid #212121;")

        self.forward_btn = QPushButton(">")
        self.forward_btn.setMaximumHeight(30)
        self.forward_btn.setStyleSheet(
            "background-color: #212121; color: #fff; font-weight: 900; width: 30px; border: 2px solid #212121;")

        self.reload_btn = QPushButton("@")
        self.reload_btn.setMaximumHeight(30)
        self.reload_btn.setStyleSheet(
            "background-color: #212121; color: #fff; font-weight: 900; width: 30px; border: 2px solid #212121;")

        self.menu = QPushButton("≡")
        self.menu.setMaximumHeight(30)
        self.menu.setStyleSheet("background-color: #212121; color: #fff; font-weight: 900; width: 30px; border: 2px "
                                "solid #212121;")

        self.horizontal.addWidget(self.back_btn)
        self.horizontal.addWidget(self.forward_btn)
        self.horizontal.addWidget(self.reload_btn)
        self.horizontal.addWidget(self.input_url)
        self.horizontal.addWidget(self.search_btn)
        self.horizontal.addWidget(self.menu)

        self.browser = QWebEngineView()

        self.search_btn.clicked.connect(lambda: self.navigate(self.input_url.toPlainText()))
        self.back_btn.clicked.connect(self.browser.back)
        self.forward_btn.clicked.connect(self.browser.forward)
        self.reload_btn.clicked.connect(self.browser.reload)

        self.layout.addLayout(self.horizontal)
        self.layout.addWidget(self.browser)

        self.browser.setUrl(QUrl("http://google.com"))

        self.window.setLayout(self.layout)
        self.window.show()

    def navigate(self, url):
        if not url.startswith("http"):
            url = "http://" + input_url
            self.input_url.setText(url)
        self.browser.setUrl(QUrl(url))

    app = QApplication([])
    window = StarBrowser()
    app.exec_()

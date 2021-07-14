import sys
from PyQt5.QtCore import *
from PyQt5 import QtGui 
from PyQt5.QtWidgets import *
from PyQt5.QtWebEngineWidgets import *


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.browser = QWebEngineView()
        self.browser.setUrl(QUrl('https://duckduckgo.com/'))
        self.setCentralWidget(self.browser)
        self.showMaximized()

        # navbar
        navbar = QToolBar()
        self.addToolBar(navbar)

        back_btn = QAction('Back', self)
        back_btn.triggered.connect(self.browser.back)
        self.setWindowIcon(QtGui.QIcon('logo.jpg'))
        navbar.addAction(back_btn)

        forward_btn = QAction('Forward', self)
        forward_btn.triggered.connect(self.browser.forward)
        navbar.addAction(forward_btn)

        reload_btn = QAction('Reload', self)
        reload_btn.triggered.connect(self.browser.reload)
        navbar.addAction(reload_btn)

        youtube_btn = QAction('Youtube', self)
        youtube_btn.triggered.connect(self.navigate_yt)
        navbar.addAction(youtube_btn)

        mineapp_btn = QAction('Mine App', self)
        mineapp_btn.triggered.connect(self.navigate_app)
        navbar.addAction(mineapp_btn)
        
        home_btn = QAction('Home', self)
        home_btn.triggered.connect(self.navigate_home)
        navbar.addAction(home_btn)

        maps_btn = QAction('Maps', self)
        maps_btn.triggered.connect(self.navigate_maps)
        navbar.addAction(maps_btn)

        self.url_bar = QLineEdit()
        self.url_bar.returnPressed.connect(self.navigate_to_url)
        navbar.addWidget(self.url_bar)

        self.browser.urlChanged.connect(self.update_url)

    def navigate_maps(self):
        self.browser.setUrl(QUrl('https://www.google.com/maps'))    

    def navigate_app(self):
        self.browser.setUrl(QUrl('https://play.google.com/store/apps/details?id=com.raihandeveloperapp.picstarfinal'))    

    def navigate_yt(self):
        self.browser.setUrl(QUrl('https://www.youtube.com/'))    

    def navigate_home(self):
        self.browser.setUrl(QUrl('http://google.com'))

    def navigate_to_url(self):
        url = self.url_bar.text()
        self.browser.setUrl(QUrl(url))

    def update_url(self, q):
        self.url_bar.setText(q.toString())


app = QApplication(sys.argv)
QApplication.setApplicationName('Next Level Browser')
window = MainWindow()
app.exec_()
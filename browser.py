import sys
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtWebEngineWidgets import *
from PyQt5.QtGui import QIcon
import logging

logging.basicConfig(level=logging.DEBUG)

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()

        # Set window properties
        self.setWindowTitle('PyBrowser')
        self.setWindowIcon(QIcon('icon.webp'))

        # Create tab widget
        self.tabs = QTabWidget()
        self.tabs.setTabsClosable(True)
        self.tabs.tabCloseRequested.connect(self.close_tab)
        self.setCentralWidget(self.tabs)

        # Create toolbar
        toolbar = QToolBar()
        self.addToolBar(toolbar)

        # Add back button
        back_btn = QAction('⮜', self)
        back_btn.triggered.connect(lambda: self.current_browser().back())
        toolbar.addAction(back_btn)

        # Add forward button
        forward_btn = QAction('⮞', self)
        forward_btn.triggered.connect(lambda: self.current_browser().forward())
        toolbar.addAction(forward_btn)

        # Add reload button
        reload_btn = QAction('⟳', self)
        reload_btn.triggered.connect(lambda: self.current_browser().reload())
        toolbar.addAction(reload_btn)

        # Add home button
        home_btn = QAction('⌂', self)
        home_btn.triggered.connect(self.navigate_home)
        toolbar.addAction(home_btn)

        # Add new tab button
        add_tab_btn = QAction('+', self)
        add_tab_btn.triggered.connect(self.add_tab)
        toolbar.addAction(add_tab_btn)

        # Add URL bar
        self.url_bar = QLineEdit()
        self.url_bar.returnPressed.connect(self.navigate_to_url)
        toolbar.addWidget(self.url_bar)

        # Add first tab
        self.add_tab()
        
    def add_tab(self):
        browser = QWebEngineView()
        browser.setUrl(QUrl('https://google.com'))
        self.tabs.addTab(browser, 'New Tab')
        self.tabs.setCurrentWidget(browser)
        self.tabs.setTabText(self.tabs.currentIndex(), 'Loading...')
        browser.titleChanged.connect(self.update_tab_title)
        browser.urlChanged.connect(self.update_url)
        browser.loadFinished.connect(self.on_load_finished)  # Connect loadFinished

    def close_tab(self, index):
        browser_widget = self.tabs.widget(index)

        if browser_widget.url().host() == "www.youtube.com":
            browser_widget.page().runJavaScript("document.getElementsByTagName('video')[0].pause();")

        if self.tabs.count() < 2:
            self.close()
        else:
            self.tabs.removeTab(index)
            browser_widget.deleteLater()

    def navigate_home(self):
        if self.current_browser():
            self.current_browser().setUrl(QUrl('https://www.google.com'))

    def navigate_to_url(self):
        url = self.url_bar.text()
        if 'http' not in url:
            url = 'https://' + url
        if self.current_browser():
            self.current_browser().setUrl(QUrl(url))

    def update_url(self, q):
        if self.current_browser():
            self.url_bar.setText(q.toString())
            self.url_bar.setCursorPosition(0)
            logging.debug(f"URL changed to: {q.toString()}")  # Debug URL change

    def update_tab_title(self, title):
        if self.current_browser():
            index = self.tabs.indexOf(self.current_browser())
            self.tabs.setTabText(index, title)
            logging.debug(f"Tab title updated to: {title}")  # Debug tab title change

    def on_load_finished(self, ok):
        if ok:
            logging.debug("Page loaded successfully")
            if self.current_browser():
                index = self.tabs.indexOf(self.current_browser())
                self.tabs.setTabText(index, self.current_browser().title())
        else:
            logging.debug("Page failed to load")

    def current_browser(self):
        return self.tabs.currentWidget() if self.tabs.currentWidget() else None
    
app = QApplication(sys.argv)
app.setApplicationName('PyBrow')
app.setApplicationDisplayName('PyBrow')
app.setOrganizationName('WCA')
window = MainWindow()
window.showMaximized()
app.exec_()
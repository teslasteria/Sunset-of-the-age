import sys
from pathlib import Path
from PyQt5.QtGui import QMovie, QFont, QFontDatabase
from PyQt5.QtWidgets import (
            QApplication, 
            QMainWindow, 
            QWidget, 
            QVBoxLayout, 
            QHBoxLayout, 
            QPushButton, 
            QLabel)
from PyQt5.QtCore import Qt, QPoint

font_path = 'fonts/PixelOperator.ttf'

IMAGE_PATH = "assets/sunset_v2.gif"

class MainWindow(QMainWindow):
    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

        # remove default frame
        self.setWindowFlags(Qt.FramelessWindowHint)
        self.setFixedSize(520, 560)

        if Path(font_path).is_file():
            font_id = QFontDatabase.addApplicationFont("fonts/PixelOperator.ttf")
            font_family = QFontDatabase.applicationFontFamilies(font_id)[0]

        # Central Widget & Layout
        central = QWidget()
        self.setCentralWidget(central)
        main_layout = QVBoxLayout(central)
        main_layout.setContentsMargins(0, 0, 0, 0)
        main_layout.setSpacing(0)
        
        self.label = QLabel()
        self.label.setObjectName('GIF')
        self.label.setAlignment(Qt.AlignHCenter)
        # self.label.setContentsMargins(10, 0, 10, 10)

        # Connect gif
        if Path(IMAGE_PATH).is_file():
            # Implementing main image
            self.movie = QMovie(IMAGE_PATH)
            self.label.setMovie(self.movie)
            self.movie.start()

        else:
            print('something went wrong')

        # Custom Title Bar
        self.title_bar = QWidget()
        self.title_bar.setObjectName('title_bar')
        self.title_bar.setFixedHeight(36)

        title_layout = QHBoxLayout(self.title_bar)
        title_layout.setContentsMargins(12, 0, 8, 0)
        title_layout.setSpacing(6)

        self.title_label = QLabel("Sunset of the age")
        self.title_label.setFont(QFont(font_family))
        # self.title_label.setAttribute(Qt.WA_TransparentForMouseEvents)

        # Min button
        self.min_btn = QPushButton("─")
        self.min_btn.setFixedSize(32, 28)
        self.min_btn.clicked.connect(self.showMinimized)

        # Max button
        self.max_btn = QPushButton("🗖")
        self.max_btn.setFixedSize(32, 28)
        self.max_btn.clicked.connect(self.showNormal)

        # Close button
        self.close_btn = QPushButton("✕")
        self.close_btn.setObjectName('close_button')
        self.close_btn.setFixedSize(32, 28)
        self.close_btn.clicked.connect(self.close)

        # Adding widgets to the central layout
        title_layout.addWidget(self.title_label, 1)
        title_layout.addWidget(self.min_btn)
        title_layout.addWidget(self.max_btn)
        title_layout.addWidget(self.close_btn)

        main_layout.addWidget(self.title_bar)
        main_layout.addWidget(self.label)

    # === Drag Setup ===
        self.dragging = False
        self.drag_offset = QPoint()

    # === Window Movement Logic ===
    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            # Only drag if click is on the title bar (not on buttons)
            if self.title_bar.geometry().contains(event.pos()):
                self.dragging = True
                self.drag_offset = event.globalPos() - self.frameGeometry().topLeft()
                event.accept()
        super().mousePressEvent(event)

    def mouseMoveEvent(self, event):
        if self.dragging and event.buttons() == Qt.LeftButton:
            self.move(event.globalPos() - self.drag_offset)
            event.accept()
        super().mouseMoveEvent(event)

    def mouseReleaseEvent(self, event):
        self.dragging = False
        super().mouseReleaseEvent(event)

    def mouseDoubleClickEvent(self, event):
        # Double-click title bar to toggle maximize
        if self.title_bar.geometry().contains(event.pos()):
            if self.isMaximized():
                self.showNormal()
            else:
                self.showMaximized()
            event.accept()
        super().mouseDoubleClickEvent(event)

def application():

    # main app point
    app = QApplication(sys.argv)

    # connect qss styles
    app.setStyleSheet(Path('scheme.qss').read_text())
    
    # GUI of the application
    window = MainWindow()
    window.show()

    # start up app
    sys.exit(app.exec_())


if __name__ == '__main__':
    application()
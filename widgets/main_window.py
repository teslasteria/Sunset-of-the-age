from PyQt5.QtGui import QMovie, QIcon
from PyQt5.QtWidgets import (
            QMainWindow, 
            QWidget, 
            QVBoxLayout, 
            QHBoxLayout, 
            QPushButton, 
            QLabel)
from PyQt5.QtCore import QUrl, Qt, QPoint
from PyQt5.QtMultimedia import QMediaContent, QMediaPlayer, QAudioOutput

from utils.path_manager import GIF_PATH, ICON_PATH, MUSIC_PATH, TITLE


class MainWindow(QMainWindow):
    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

        # remove default frame
        self.setWindowFlags(Qt.FramelessWindowHint)
        self.setFixedSize(520, 560)

        # Central Widget & Layout
        central = QWidget()
        self.setCentralWidget(central)
        main_layout = QVBoxLayout(central)
        main_layout.setContentsMargins(0, 0, 0, 0)
        main_layout.setSpacing(0)

        # setting up GIF to application
        self.label = QLabel()
        self.label.setObjectName('GIF')
        self.label.setAlignment(Qt.AlignHCenter)
        self.movie = QMovie(str(GIF_PATH))
        self.label.setMovie(self.movie)
        self.movie.start()

        # add music track
        self.player = QMediaPlayer()
        self.audio_output = QAudioOutput()
        self.player.setVolume(70)

        # Custom Title Bar
        self.title_bar = QWidget()
        self.title_bar.setObjectName('title_bar')
        self.title_bar.setFixedHeight(36)

        title_layout = QHBoxLayout(self.title_bar)
        title_layout.setContentsMargins(12, 0, 8, 0)
        title_layout.setSpacing(6)

        # Title of the app
        self.title_label = QLabel(TITLE)

        # Min button
        self.min_btn = QPushButton("─")
        self.min_btn.setFixedSize(32, 28)
        self.min_btn.clicked.connect(self.showMinimized)

        # Max button
        self.max_btn = QPushButton()
        self.max_btn.setIcon(QIcon(str(ICON_PATH)))
        self.max_btn.setText('')
        self.max_btn.setFlat(True)
        self.max_btn.setFixedSize(32, 28)
        self.max_btn.clicked.connect(self.play_music)

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

    def play_music(self):
        music_file = QUrl.fromLocalFile(str(MUSIC_PATH))
        self.player.setMedia(QMediaContent(music_file))
        self.player.play()

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
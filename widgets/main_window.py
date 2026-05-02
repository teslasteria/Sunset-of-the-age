import pygame

from PyQt5.QtGui import QMovie, QIcon
from PyQt5.QtWidgets import (
            QMainWindow, 
            QWidget, 
            QVBoxLayout, 
            QHBoxLayout, 
            QPushButton, 
            QLabel)
from PyQt5.QtCore import Qt, QPoint

from utils.path_manager import GIF_PATH, ICON_PLAY_PATH, MUSIC_PATH, TITLE, ICON_PAUSE_PATH


class MainWindow(QMainWindow):
    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

        pygame.mixer.init()
        self.is_playing = False

        self.icon_play = QIcon(str(ICON_PLAY_PATH))
        self.icon_pause = QIcon(str(ICON_PAUSE_PATH))

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
        self.play_button = QPushButton()
        self.play_button.setFlat(True)
        self.play_button.setIcon(self.icon_play)
        self.play_button.setFixedSize(32, 28)
        self.play_button.clicked.connect(self.play_music)

        # Close button
        self.close_btn = QPushButton("✕")
        self.close_btn.setObjectName('close_button')
        self.close_btn.setFixedSize(32, 28)
        self.close_btn.clicked.connect(self.close)

        # Adding widgets to the central layout
        title_layout.addWidget(self.title_label, 1)
        title_layout.addWidget(self.min_btn)
        title_layout.addWidget(self.play_button)
        title_layout.addWidget(self.close_btn)  

        main_layout.addWidget(self.title_bar)
        main_layout.addWidget(self.label)

        # === Drag Setup ===
        self.dragging = False
        self.drag_offset = QPoint()

    def play_music(self):
        if self.is_playing:
            pygame.mixer.music.pause()
            self.play_button.setIcon(self.icon_play)
            self.is_playing = False
        else:
            # If starting from beginning or resuming
            if pygame.mixer.music.get_busy():
                pygame.mixer.music.unpause()
            else:
                try:
                    pygame.mixer.music.load(str(MUSIC_PATH))
                    pygame.mixer.music.play()
                except pygame.error as e:
                    print(f'Loading error: {e}')
            
            self.play_button.setIcon(self.icon_pause)
            self.is_playing = True

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
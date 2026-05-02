import sys
import os
import pygame
from PyQt5.QtWidgets import QApplication, QHBoxLayout, QPushButton, QWidget

# Initialize pygame mixer only once
pygame.mixer.init()

class AudioPlayer(QWidget):
    def __init__(self):
        super().__init__()
        self.is_playing = False
        self.music_path = self.get_resource_path("assets/RunToYou.mp3")
        self.init_ui()

    def get_resource_path(self, relative_path):
        """Get absolute path to resource, works for dev and for PyInstaller"""
        if getattr(sys, 'frozen', False):
            # We are running in a bundle
            base_path = sys._MEIPASS
        else:
            # We are running in a normal Python environment
            base_path = os.path.abspath(".")
        return os.path.join(base_path, relative_path)

    def init_ui(self):
        self.setWindowTitle("Meditation Player")
        self.setGeometry(100, 100, 300, 100)

        layout = QHBoxLayout()
        self.play_button = QPushButton("Play Audio")
        self.play_button.clicked.connect(self.toggle_play)
        layout.addWidget(self.play_button)
        self.setLayout(layout)

    def toggle_play(self):
        if not os.path.exists(self.music_path):
            print(f"Error: File not found at {self.music_path}")
            return

        if self.is_playing:
            pygame.mixer.music.pause()
            self.play_button.setText("Play Audio")
            self.is_playing = False
        else:
            # If starting from beginning or resuming
            if pygame.mixer.music.get_busy():
                pygame.mixer.music.unpause()
            else:
                pygame.mixer.music.load(self.music_path)
                pygame.mixer.music.play()
            
            self.play_button.setText("Pause")
            self.is_playing = True

def application():
    app = QApplication(sys.argv)
    window = AudioPlayer()
    window.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    application()
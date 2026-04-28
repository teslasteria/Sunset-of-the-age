import sys
from pathlib import Path
from PyQt5.QtGui import QFont, QFontDatabase
from PyQt5.QtWidgets import QApplication

from utils.path_manager import SCHEME_PATH, FONT_PATH, check_is_valid_pathes
from widgets.main_window import MainWindow


def application():
    check_is_valid_pathes()

    # main app point
    app = QApplication(sys.argv)

    # connect qss styles
    app.setStyleSheet(Path(SCHEME_PATH).read_text())
        
    # setting up fonts:
    font_id = QFontDatabase.addApplicationFont(str(FONT_PATH))
    font_families = QFontDatabase.applicationFontFamilies(font_id)
    font_family = font_families[0]

    app.setFont(QFont(font_family))
    
    # GUI of the application
    window = MainWindow()
    window.show()

    # start up app
    sys.exit(app.exec_())


if __name__ == '__main__':
    application()
from pathlib import Path

TITLE = "Sunset of the age"

# base dir of the project
BASEDIR_PATH = Path(__file__).resolve().parent.parent

# play icon for title bar
ICON_PLAY_PATH = BASEDIR_PATH / 'assets' / 'play_icon.png'

# pause icon for title bar
ICON_PAUSE_PATH = BASEDIR_PATH / 'assets' / 'pause.png'

# main gif onject
GIF_PATH = BASEDIR_PATH / 'assets' / 'main.gif'

# scheme path
SCHEME_PATH = BASEDIR_PATH / 'assets' / 'styles' / 'style.qss'

# font path
FONT_PATH = BASEDIR_PATH / 'assets' / 'fonts' / 'PixelOperator.ttf'

# Music file path
MUSIC_PATH = BASEDIR_PATH / 'assets' / 'RunToYou.mp3'


def check_icons_path():
    '''checking valid path to icon'''
    if ICON_PLAY_PATH.is_file() and ICON_PAUSE_PATH.is_file():
        return ICON_PLAY_PATH, ICON_PAUSE_PATH
    else:
        print(f'Icon not found at: {ICON_PLAY_PATH}')
        print(f'Current working directory: {Path.cwd()}')

        return None


def check_gif_path():
    '''checking valid path to gif'''
    if GIF_PATH.is_file():
        return GIF_PATH
    else:
        print(f'GIF not found at: {GIF_PATH}')
        print(f'Current working directory: {Path.cwd()}')

        return None


def check_font_path():
    '''checking valid path to font'''
    if FONT_PATH.is_file():
        return FONT_PATH
    else:
        print(f'GIF not found at: {FONT_PATH}')
        print(f'Current working directory: {Path.cwd()}')

        return None


def check_music_path():
    '''checking valid path to font'''
    if MUSIC_PATH.is_file():
        print('music path is okay')
        return MUSIC_PATH
    else:
        print(f'GIF not found at: {MUSIC_PATH}')
        print(f'Current working directory: {Path.cwd()}')

        return None


def check_scheme_path():
    '''checking valid path to scheme'''
    if SCHEME_PATH.is_file():
        return SCHEME_PATH
    else:
        print(f'GIF not found at: {SCHEME_PATH}')
        print(f'Current working directory: {Path.cwd()}')

        return None


def check_is_valid_pathes():
    '''run all tests'''
    check_icon_path()
    check_gif_path()
    check_font_path()
    check_scheme_path()
    check_music_path()
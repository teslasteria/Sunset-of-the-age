from PyQt6.QtCore import Qt, QPoint


class WindowDragMixin:
    """Mixin class for window dragging functionality"""
    
    def __init__(self):
        self.dragging = False
        self.drag_offset = QPoint()
        self.title_bar = None
    
    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton and self.title_bar:
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
        if self.title_bar and self.title_bar.geometry().contains(event.pos()):
            if self.isMaximized():
                self.showNormal()
            else:
                self.showMaximized()
            event.accept()
        super().mouseDoubleClickEvent(event)
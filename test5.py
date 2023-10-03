
from PyQt5.QtWidgets import QApplication, QWidget, QComboBox, QVBoxLayout, QTabWidget

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()

        self.combo_box = QComboBox()
        self.combo_box.addItem("Tab 1")
        self.combo_box.addItem("Tab 2")
        self.combo_box.addItem("Tab 3")

        self.tab_widget = QTabWidget()
        self.tab_widget.addTab(QWidget(), "Tab 1")
        self.tab_widget.addTab(QWidget(), "Tab 2")
        self.tab_widget.addTab(QWidget(), "Tab 3")

        layout = QVBoxLayout()
        layout.addWidget(self.combo_box)
        layout.addWidget(self.tab_widget)
        self.setLayout(layout)

        self.combo_box.activated.connect(self.open_tab)

    def open_tab(self, index):
        self.tab_widget.setCurrentIndex(index)

if __name__ == "__main__":
    app = QApplication([])
    window = MainWindow()
    window.show()
    app.exec_()

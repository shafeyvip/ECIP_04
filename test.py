
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QComboBox, QTabWidget, QWidget


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()

        self.setWindowTitle("ComboBox and TabWidget Example")

        # Create a layout for the main window
        layout = QVBoxLayout()

        # Create a combobox widget
        self.combo_box = QComboBox()
        self.combo_box.addItem("Tab 1")
        self.combo_box.addItem("Tab 2")
        self.combo_box.addItem("Tab 3")
        self.combo_box.currentIndexChanged.connect(self.open_tab_widget)

        layout.addWidget(self.combo_box)

        # Create a tab widget
        self.tab_widget = QTabWidget()

        layout.addWidget(self.tab_widget)

        # Set the layout to the main window
        main_widget = QWidget()
        main_widget.setLayout(layout)
        self.setCentralWidget(main_widget)


    def open_tab_widget(self, index):
        self.tab_widget.setCurrentIndex(index)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())

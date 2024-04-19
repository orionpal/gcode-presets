import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLineEdit, QPushButton, QVBoxLayout, QLabel
from Box.input import *


class InputForm(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        # Create a QVBoxLayout instance
        layout = QVBoxLayout()

        # Create labels
        self.edge_label = QLabel("Box Edge Length (in inches): ")
        self.thickness_label = QLabel("Material/Stock thickness (in inches): ")
        
        # Create QLineEdit widgets
        self.edge = QLineEdit(self)
        self.thickness = QLineEdit(self)
        
        # Create a QPushButton and connect the clicked signal to the submit function
        self.button = QPushButton('Submit', self)
        self.button.clicked.connect(self.submit)

        # Add widgets to the layout
        layout.addWidget(self.edge_label)
        layout.addWidget(self.edge)
        layout.addWidget(self.thickness_label)
        layout.addWidget(self.thickness)
        layout.addWidget(self.button)

        # Set the layout on the application's window
        self.setLayout(layout)
        self.setWindowTitle('Box gcode Creator')

    def submit(self):
        # This method is called when the button is clicked
        edge = float(self.edge.text())
        thickness = float(self.thickness.text())
        create_box_gcode("test.txt", edge, thickness)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    form = InputForm()
    form.show()
    sys.exit(app.exec_())

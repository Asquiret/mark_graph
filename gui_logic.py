from PyQt5 import QtWidgets
import matplotlib
from matplotlib.figure import Figure
from matplotlib.backends.backend_qt5agg import (
    FigureCanvasQTAgg as FigureCanvas)

from gui import Ui_Dialog


class GuiProgram(Ui_Dialog):

    def __init__(self, dialog: QtWidgets.QDialog) -> None:
        Ui_Dialog.__init__(self)
        self.setupUi(dialog)

        self.ax_1 = None
        self.fig_1 = None
        self.canvas_1 = None
        self.intialize_graph()

        self.pushButton.clicked.connect(self.show_graph)

    def intialize_graph(self) -> None:
        self.fig_1 = Figure()
        self.ax_1 = self.fig_1.add_subplot(111)
        self.canvas_1 = FigureCanvas(self.fig_1)
        self.plotLayout.addWidget(self.canvas_1)

    def plotting(self, data_y):
        self.ax_1.clear()
        self.ax_1.plot(data_y)
        self.fig_1.tight_layout()
        self.canvas_1.draw()

    def show_graph(self):
        text = self.lineEdit.text()
        list_n = text.split(" ")
        list_number = list(map(float, list_n))
        self.plotting(list_number)

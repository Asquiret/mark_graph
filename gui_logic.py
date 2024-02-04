from PyQt5 import QtWidgets
import matplotlib
from matplotlib.figure import Figure
from matplotlib.backends.backend_qt5agg import (
FigureCanvasQTAgg as FigureCanvas)

from gui import Ui_Dialog





class GuiProgram(Ui_Dialog):

    def __init__(self, dialog: QtWidgets.QDialog) -> None:
        Ui_Dialog.__init__(self)
        self.fir_var = 0
        self.sec_var = 0
        self.thir_var = 0
        self.four_var = 0
        self.try_num = 1
        self.setupUi(dialog)

        self.ax_1 = None
        self.fig_1 = None
        self.canvas_1 = None

        self.btn_2.clicked.connect(self.action_from_2)
        self.btn_3.clicked.connect(self.action_from_3)
        self.btn_4.clicked.connect(self.action_from_4)
        self.btn_5.clicked.connect(self.action_from_5)
        self.btn_entry.clicked.connect(self.action_from_entr)



    def action_from_2(self):
        if self.try_num == 1:
            self.fir_var = 2
            self.try_num = self.try_num + 1
        else:
            if self.try_num == 2:
                self.sec_var = 2
                self.try_num = self.try_num + 1
            else:
                if self.try_num == 3:
                    self.thir_var = 2
                    self.try_num = self.try_num + 1
                else:
                    if self.try_num == 4:
                        self.four_var = 2
                        self.try_num = self.try_num + 1

    def action_from_3(self):
        if self.try_num == 1:
            self.fir_var = 3
            self.try_num = self.try_num + 1
        else:
            if self.try_num == 2:
                self.sec_var = 3
                self.try_num = self.try_num + 1
            else:
                if self.try_num == 3:
                    self.thir_var = 3
                    self.try_num = self.try_num + 1
                else:
                    if self.try_num == 4:
                        self.four_var = 3
                        self.try_num = self.try_num + 1

    def action_from_4(self):
        if self.try_num == 1:
            self.fir_var = 4
            self.try_num = self.try_num + 1
        else:
            if self.try_num == 2:
                self.sec_var = 4
                self.try_num = self.try_num + 1
            else:
                if self.try_num == 3:
                    self.thir_var = 4
                    self.try_num = self.try_num + 1
                else:
                    if self.try_num == 4:
                        self.four_var = 4
                        self.try_num = self.try_num + 1

    def action_from_5(self):
        if self.try_num == 1:
            self.fir_var = 5
            self.try_num = self.try_num + 1
        else:
            if self.try_num == 2:
                self.sec_var = 5
                self.try_num = self.try_num + 1
            else:
                if self.try_num == 3:
                    self.thir_var = 5
                    self.try_num = self.try_num + 1
                else:
                    if self.try_num == 4:
                        self.four_var = 5
                        self.try_num = self.try_num + 1




    def action_from_entr(self):
         self.intialize_graph()
         k = self.fir_var
         l = self.sec_var
         m = self.thir_var
         n = self.four_var
         b = [k, l, m, n]
         a = [1, 2, 3,4]
         self.plotting(a, b)
         # print(self.try_num)



    def intialize_graph(self) ->None:
        self.fig_1 = Figure()
        self.ax_1 = self.fig_1.add_subplot(111)
        self.canvas_1 = FigureCanvas(self.fig_1)
        self.plotLayout.addWidget(self.canvas_1)

    def plotting(self, data_x, data_y):

        self.ax_1.clear()
        self.ax_1.plot(data_x, data_y, color='r')
        self.fig_1.tight_layout()
        self.canvas_1.draw()















# import time

# import numpy as np
# from PyQt5 import QtCore
# from pyqtgraph import PlotWidget


# class CustomPlotWidget(PlotWidget):
#     position = QtCore.pyqtSignal(float)

#     def __init__(self, *args, **kwargs):
#         super().__init__(*args, **kwargs)

#     def mouseMoveEvent(self, event):
#         position_y = self.getPlotItem().getViewBox().mapSceneToView(event.pos()).y()
#         self.position.emit(position_y)

import time

import numpy as np
from PyQt5 import QtCore
from pyqtgraph import PlotWidget


class CustomPlotWidget(PlotWidget):
    dataPoint = QtCore.pyqtSignal(float)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.lastPos = None
        self.lastTime = None

    def mouseMoveEvent(self, event):
        self.dataPoint.emit(event.pos().y())

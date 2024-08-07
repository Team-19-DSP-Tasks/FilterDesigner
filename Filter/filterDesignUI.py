import csv
import webbrowser

import icons as icons
import pyqtgraph as pg
from filterDesignBackend import Backend
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QAction, QMenu
from pyqtgraph import PlotWidget
from widgets.all_pass_library_button import AllPassProcessButton
from widgets.mouse_plot_widget import MousePlotWidget
from widgets.plane_dock_widget import PlaneDockWidget
from widgets.validator import CustomValidator


class Ui_FilterDesigner(object):
    def setupUi(self, FilterDesigner):
        FilterDesigner.setObjectName("FilterDesigner")
        FilterDesigner.resize(1280, 720)
        icon = QtGui.QIcon()
        icon.addPixmap(
            QtGui.QPixmap(":/appIcon/processing.png"),
            QtGui.QIcon.Normal,
            QtGui.QIcon.Off,
        )
        FilterDesigner.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(FilterDesigner)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout_9 = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout_9.setObjectName("verticalLayout_9")
        self.applicationGraphs = QtWidgets.QGroupBox(self.centralwidget)
        self.applicationGraphs.setMaximumSize(QtCore.QSize(16777215, 16777215))
        font = QtGui.QFont()
        font.setFamily("Open Sans")
        font.setPointSize(12)
        self.applicationGraphs.setFont(font)
        self.applicationGraphs.setAlignment(QtCore.Qt.AlignCenter)
        self.applicationGraphs.setObjectName("applicationGraphs")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout(self.applicationGraphs)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.originalSignalPlot = PlotWidget(self.applicationGraphs)
        self.originalSignalPlot.setMinimumSize(QtCore.QSize(0, 0))
        self.originalSignalPlot.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.originalSignalPlot.setObjectName("originalApplicationSignal")
        self.originalSignalPlot.setTitle("Original Signal")
        self.originalSignalPlot.setLabel("bottom", "time")
        self.originalSignalPlot.setLabel("left", "ampltiude")
        self.filteredSignalPlot = PlotWidget(self.applicationGraphs)
        self.filteredSignalPlot.setMinimumSize(QtCore.QSize(0, 0))
        self.filteredSignalPlot.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.filteredSignalPlot.setObjectName("filteredSignal")
        self.filteredSignalPlot.setTitle("Filtered Signal")
        self.filteredSignalPlot.setLabel("bottom", "time")
        self.filteredSignalPlot.setLabel("left", "ampltiude")
        self.correctedPhaseSignalPlot = PlotWidget(self.applicationGraphs)
        self.correctedPhaseSignalPlot.setMinimumSize(QtCore.QSize(0, 0))
        self.correctedPhaseSignalPlot.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.correctedPhaseSignalPlot.setObjectName("filteredSignal")
        self.correctedPhaseSignalPlot.setTitle("Signal with Corrected Phase")
        self.correctedPhaseSignalPlot.setLabel("bottom", "time")
        self.correctedPhaseSignalPlot.setLabel("left", "ampltiude")
        self.verticalLayout_7.addWidget(self.originalSignalPlot)
        self.verticalLayout_7.addWidget(self.filteredSignalPlot)
        self.verticalLayout_7.addWidget(self.correctedPhaseSignalPlot)
        self.verticalLayout_9.addWidget(self.applicationGraphs)

        self.filteredSignalPlot.setXLink(self.originalSignalPlot)
        self.filteredSignalPlot.setYLink(self.originalSignalPlot)
        self.correctedPhaseSignalPlot.setXLink(self.originalSignalPlot)
        self.correctedPhaseSignalPlot.setYLink(self.originalSignalPlot)

        self.mousePadGroupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.mousePadGroupBox.setMinimumSize(QtCore.QSize(0, 200))
        self.mousePadGroupBox.setMaximumSize(QtCore.QSize(116777215, 200))
        font = QtGui.QFont()
        font.setFamily("Open Sans")
        font.setPointSize(12)
        self.mousePadGroupBox.setFont(font)
        self.mousePadGroupBox.setAlignment(QtCore.Qt.AlignCenter)
        self.mousePadGroupBox.setObjectName("mousePadGroupBox")

        self.mousePadHorizontalLayout = QtWidgets.QHBoxLayout()
        self.mousePadHorizontalLayout.addWidget(self.mousePadGroupBox)

        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.mousePadGroupBox)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.label = QtWidgets.QLabel(self.mousePadGroupBox)
        font = QtGui.QFont()
        font.setPointSize(9)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.verticalLayout_5.addWidget(self.label)
        self.mousePad = MousePlotWidget(self.mousePadGroupBox)
        self.mousePad.setMinimumSize(QtCore.QSize(0, 0))
        self.mousePad.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.mousePad.setObjectName("mousePad")
        self.verticalLayout_5.addWidget(self.mousePad)
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        spacerItem = QtWidgets.QSpacerItem(
            40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum
        )
        self.horizontalLayout_6.addItem(spacerItem)
        self.generateSignal = QtWidgets.QPushButton(self.mousePadGroupBox)
        self.generateSignal.setObjectName("generateSignal")
        self.generateSignal.setCheckable(True)
        self.horizontalLayout_6.addWidget(self.generateSignal)
        spacerItem1 = QtWidgets.QSpacerItem(
            40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum
        )
        self.horizontalLayout_6.addItem(spacerItem1)
        self.verticalLayout_5.addLayout(self.horizontalLayout_6)
        self.verticalLayout_9.addLayout(self.mousePadHorizontalLayout)
        FilterDesigner.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(FilterDesigner)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1280, 21))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        self.menuHelp = QtWidgets.QMenu(self.menubar)
        self.menuHelp.setObjectName("menuHelp")
        self.menuTools = QtWidgets.QMenu(self.menubar)
        self.menuTools.setObjectName("menuTools")
        self.menuView = QtWidgets.QMenu(self.menubar)
        self.menuView.setObjectName("menuView")
        FilterDesigner.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(FilterDesigner)
        self.statusbar.setObjectName("statusbar")
        FilterDesigner.setStatusBar(self.statusbar)
        self.allPassLibrary = QtWidgets.QDockWidget(FilterDesigner)
        self.allPassLibrary.setMinimumSize(QtCore.QSize(437, 413))
        self.allPassLibrary.setObjectName("allPassLibrary")
        self.dockWidgetContents_3 = QtWidgets.QWidget()
        self.dockWidgetContents_3.setObjectName("dockWidgetContents_3")
        self.verticalLayout_8 = QtWidgets.QVBoxLayout(self.dockWidgetContents_3)
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.allPassLibraryScrollArea = QtWidgets.QScrollArea(self.dockWidgetContents_3)
        self.allPassLibraryScrollArea.setWidgetResizable(True)
        self.allPassLibraryScrollArea.setObjectName("allPassLibraryScrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 417, 95))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.gridLayout = QtWidgets.QGridLayout(self.scrollAreaWidgetContents)
        self.gridLayout.setObjectName("gridLayout")
        self.allPassLibraryScrollArea.setWidget(self.scrollAreaWidgetContents)
        self.verticalLayout_8.addWidget(self.allPassLibraryScrollArea)

        self.CascadedLabel = QtWidgets.QLabel(self.dockWidgetContents_3)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.CascadedLabel.setFont(font)
        self.CascadedLabel.setAlignment(QtCore.Qt.AlignLeft)
        self.CascadedLabel.setObjectName("label")
        self.verticalLayout_8.addWidget(self.CascadedLabel)

        self.allPassCascaded = QtWidgets.QScrollArea(self.dockWidgetContents_3)
        self.allPassCascaded.setWidgetResizable(True)
        self.allPassCascaded.setObjectName("allPassCascaded")
        self.scrollAreaWidgetContents_2 = QtWidgets.QWidget()
        self.scrollAreaWidgetContents_2.setGeometry(QtCore.QRect(0, 0, 417, 95))
        self.scrollAreaWidgetContents_2.setObjectName("scrollAreaWidgetContents_2")
        self.gridLayoutForCascaded = QtWidgets.QGridLayout(
            self.scrollAreaWidgetContents_2
        )
        self.gridLayoutForCascaded.setObjectName("gridLayoutForCascaded")
        self.allPassCascaded.setWidget(self.scrollAreaWidgetContents_2)
        self.verticalLayout_8.addWidget(self.allPassCascaded)

        self.removeAllPasses = QtWidgets.QPushButton(self.dockWidgetContents_3)
        self.removeAllPasses.setObjectName("removeAllPasses")
        self.verticalLayout_8.addWidget(self.removeAllPasses)

        self.allPassDesignGroupBox = QtWidgets.QGroupBox(self.dockWidgetContents_3)
        font = QtGui.QFont()
        font.setFamily("Open Sans")
        font.setPointSize(12)
        self.allPassDesignGroupBox.setFont(font)
        self.allPassDesignGroupBox.setAlignment(QtCore.Qt.AlignCenter)
        self.allPassDesignGroupBox.setObjectName("allPassDesignGroupBox")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.allPassDesignGroupBox)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.inputALabel = QtWidgets.QLabel(self.allPassDesignGroupBox)
        self.inputALabel.setMinimumSize(QtCore.QSize(80, 0))
        self.inputALabel.setMaximumSize(QtCore.QSize(80, 60))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.inputALabel.setFont(font)
        self.inputALabel.setObjectName("inputALabel")
        self.horizontalLayout.addWidget(self.inputALabel)
        self.gainInput = QtWidgets.QLineEdit(self.allPassDesignGroupBox)
        self.gainInput.setPlaceholderText("Enter a value")
        self.validator = CustomValidator()
        self.gainInput.setValidator(self.validator)
        self.gainInput.setObjectName("textField")
        self.horizontalLayout.addWidget(self.gainInput)
        self.verticalLayout_4.addLayout(self.horizontalLayout)
        self.addAllPassFilter = QtWidgets.QPushButton(self.allPassDesignGroupBox)
        self.addAllPassFilter.setObjectName("pushButton")
        self.addAllPassFilter.setShortcut(QtGui.QKeySequence(QtCore.Qt.Key_Enter))

        self.value_error = QtWidgets.QLabel()
        self.verticalLayout_4.addWidget(self.value_error)
        self.value_error.setStyleSheet("letter-spacing: 3px;")
        self.value_error.setVisible(False)

        self.verticalLayout_4.addWidget(self.addAllPassFilter)
        self.verticalLayout_8.addWidget(self.allPassDesignGroupBox)
        # self.dockWidgetContents_3

        self.allPassPhaseResponse = PlotWidget(self.dockWidgetContents_3)
        self.allPassPhaseResponse.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.allPassPhaseResponse.setObjectName("allPassPhaseResponse")
        self.allPassPhaseResponse.setTitle("All Pass Filter Phase Response")
        self.allPassPhaseResponse.setLabel("bottom", "Frequency [rad/sample]")
        self.allPassPhaseResponse.setLabel("left", "Phase [radians]")
        self.verticalLayout_8.addWidget(self.allPassPhaseResponse)
        self.correctPhase = QtWidgets.QPushButton(self.dockWidgetContents_3)
        self.correctPhase.setObjectName("correctPhase")
        self.correctPhase.setCheckable(True)
        self.verticalLayout_8.addWidget(self.correctPhase)

        ### label for error upon correcting phase
        self.filterNotChosen = QtWidgets.QLabel()
        self.verticalLayout_8.addWidget(self.filterNotChosen)
        self.filterNotChosen.setStyleSheet("letter-spacing: 3px;")
        self.filterNotChosen.setVisible(False)

        self.allPassLibrary.setWidget(self.dockWidgetContents_3)
        FilterDesigner.addDockWidget(QtCore.Qt.DockWidgetArea(2), self.allPassLibrary)
        self.zPlane_dock_widget = PlaneDockWidget(FilterDesigner)
        self.zPlane_dock_widget.setObjectName("dockWidget_3")
        self.dockWidgetContents_4 = QtWidgets.QWidget()
        self.dockWidgetContents_4.setObjectName("dockWidgetContents_4")
        self.dockWidgetContents_4.setMinimumSize(QtCore.QSize(400, 0))
        self.dockWidgetContents_4.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.dockWidgetContents_4)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.filterDesignGroupBox = QtWidgets.QGroupBox(self.dockWidgetContents_4)
        font = QtGui.QFont()
        font.setFamily("Open Sans")
        font.setPointSize(12)
        self.filterDesignGroupBox.setFont(font)
        self.filterDesignGroupBox.setAlignment(QtCore.Qt.AlignCenter)
        self.filterDesignGroupBox.setObjectName("filterDesignGroupBox")

        self.z_plane_VerticalLayout = QtWidgets.QVBoxLayout(self.filterDesignGroupBox)
        self.z_plane_VerticalLayout.setObjectName("z_plane_VerticalLayout")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.unitCirclePlot = PlotWidget(self.filterDesignGroupBox)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred
        )
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.unitCirclePlot.sizePolicy().hasHeightForWidth()
        )
        self.unitCirclePlot.setSizePolicy(sizePolicy)
        self.unitCirclePlot.setMinimumSize(QtCore.QSize(150, 150))
        self.unitCirclePlot.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.unitCirclePlot.setObjectName("unitCirclePlot")
        self.unitCirclePlot.setMenuEnabled(False)

        # Create a CircleROI
        circle_roi = pg.CircleROI(
            [-1, -1],
            size=(2, 2),
            pen=pg.mkPen(color="orange", width=2),
            movable=False,
            resizable=False,
            rotatable=False,
        )
        # Create lines for the X and Y axes
        x_axis = pg.InfiniteLine(
            angle=0, movable=False, pen=pg.mkPen(color="w", width=1)
        )
        y_axis = pg.InfiniteLine(
            angle=90, movable=False, pen=pg.mkPen(color="w", width=1)
        )

        # Add the CircleROI and axes to the PlotWidget
        self.unitCirclePlot.addItem(circle_roi)
        self.unitCirclePlot.addItem(x_axis)
        self.unitCirclePlot.addItem(y_axis)
        self.unitCirclePlot.hideAxis("bottom")
        self.unitCirclePlot.hideAxis("left")
        self.mousePad.hideAxis("bottom")
        self.mousePad.hideAxis("left")
        # self.mousePad.setRange(xRange=(-50, 250), yRange=(-200, 200))
        # self.mousePad.setLimits(xMin=-50, xMax=250, yMin=-200, yMax=400)

        circle_roi.removeHandle(0)
        # Set the view range
        # self.unitCirclePlot.setMouseEnabled(x=False, y=False)

        self.horizontalLayout_2.addWidget(self.unitCirclePlot)

        self.zPlaneDesignControls = QtWidgets.QGroupBox(self.filterDesignGroupBox)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum
        )
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.zPlaneDesignControls.sizePolicy().hasHeightForWidth()
        )
        self.zPlaneDesignControls.setSizePolicy(sizePolicy)
        self.zPlaneDesignControls.setMinimumSize(QtCore.QSize(131, 191))
        self.zPlaneDesignControls.setMaximumSize(QtCore.QSize(100, 16777215))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.zPlaneDesignControls.setFont(font)
        self.zPlaneDesignControls.setAlignment(QtCore.Qt.AlignCenter)
        self.zPlaneDesignControls.setObjectName("zPlaneDesignControls")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.zPlaneDesignControls)
        self.verticalLayout.setObjectName("verticalLayout")
        self.addZero = QtWidgets.QPushButton(self.zPlaneDesignControls)
        self.addZero.setObjectName("addZero")
        self.addZero.setCheckable(True)
        self.verticalLayout.addWidget(self.addZero)
        self.addPole = QtWidgets.QPushButton(self.zPlaneDesignControls)
        self.addPole.setObjectName("addPole")
        self.addPole.setCheckable(True)
        self.verticalLayout.addWidget(self.addPole)
        self.removeAllPoles = QtWidgets.QPushButton(self.zPlaneDesignControls)
        self.removeAllPoles.setObjectName("removeAllPoles")
        self.verticalLayout.addWidget(self.removeAllPoles)
        self.removeAllZeros = QtWidgets.QPushButton(self.zPlaneDesignControls)
        self.removeAllZeros.setObjectName("removeAllZeros")
        self.verticalLayout.addWidget(self.removeAllZeros)
        self.resetDesign = QtWidgets.QPushButton(self.zPlaneDesignControls)
        self.resetDesign.setObjectName("resetDesign")
        self.verticalLayout.addWidget(self.resetDesign)
        self.addConjugatesCheckBox = QtWidgets.QCheckBox(self.zPlaneDesignControls)
        self.addConjugatesCheckBox.setObjectName("addConjugatesCheckBox")
        self.verticalLayout.addWidget(self.addConjugatesCheckBox)
        self.applyFilterButton = QtWidgets.QPushButton(self.zPlaneDesignControls)
        self.applyFilterButton.setObjectName("applyFilterButton")
        self.verticalLayout.addWidget(self.applyFilterButton)
        self.applyFilterButton.raise_()
        self.addPole.raise_()
        self.addZero.raise_()
        self.removeAllPoles.raise_()
        self.removeAllZeros.raise_()
        self.resetDesign.raise_()
        self.addConjugatesCheckBox.raise_()
        self.horizontalLayout_2.addWidget(self.zPlaneDesignControls)

        ###### Export filter ######
        self.exportFilter = QtWidgets.QPushButton()
        self.exportFilter.setObjectName("export_filter")
        self.z_plane_VerticalLayout.addLayout(self.horizontalLayout_2)
        self.z_plane_VerticalLayout.addWidget(self.exportFilter)
        self.emptyDesign = QtWidgets.QLabel()
        self.emptyDesign.setStyleSheet("letter-spacing: 3px;")
        self.z_plane_VerticalLayout.addWidget(self.emptyDesign)
        self.emptyDesign.setVisible(False)
        ###########################

        ###### Import filter ######
        self.importFilter = QtWidgets.QPushButton()
        self.importFilter.setObjectName("import_filter")
        self.z_plane_VerticalLayout.addLayout(self.horizontalLayout_2)
        self.z_plane_VerticalLayout.addWidget(self.importFilter)
        ###########################

        self.verticalLayout_2.addWidget(self.filterDesignGroupBox)
        self.frequencyResponseGroupBox = QtWidgets.QGroupBox(self.dockWidgetContents_4)
        font = QtGui.QFont()
        font.setFamily("Open Sans")
        font.setPointSize(12)
        self.frequencyResponseGroupBox.setFont(font)
        self.frequencyResponseGroupBox.setAlignment(QtCore.Qt.AlignCenter)
        self.frequencyResponseGroupBox.setObjectName("frequencyResponseGroupBox")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.frequencyResponseGroupBox)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.magFrequencyResponse = PlotWidget(self.frequencyResponseGroupBox)
        self.magFrequencyResponse.setMinimumSize(QtCore.QSize(0, 0))
        self.magFrequencyResponse.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.magFrequencyResponse.setObjectName("magFrequencyResponse")
        self.magFrequencyResponse.setTitle("Filter Magnitude Response")
        self.magFrequencyResponse.setLabel("bottom", "Frequency (rad/sample)")
        self.magFrequencyResponse.setLabel("left", "Magnitude (dB)")
        self.verticalLayout_3.addWidget(self.magFrequencyResponse)
        self.phaseFrequencyResponse = PlotWidget(self.frequencyResponseGroupBox)
        self.phaseFrequencyResponse.setMinimumSize(QtCore.QSize(0, 0))
        self.phaseFrequencyResponse.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.phaseFrequencyResponse.setObjectName("phaseFrequencyResponse")
        self.phaseFrequencyResponse.setTitle("Filter Phase Response")
        self.phaseFrequencyResponse.setLabel("bottom", "Frequency (rad/sample)")
        self.phaseFrequencyResponse.setLabel("left", "Phase (radians)")
        self.magFrequencyResponse.setLogMode(x=True, y=True)
        self.phaseFrequencyResponse.setLogMode(x=True, y=False)
        self.magFrequencyResponse.showGrid(True, True)
        self.phaseFrequencyResponse.showGrid(True, True)
        self.allPassPhaseResponse.showGrid(True, True)
        self.verticalLayout_3.addWidget(self.phaseFrequencyResponse)
        self.verticalLayout_2.addWidget(self.frequencyResponseGroupBox)
        self.zPlane_dock_widget.setWidget(self.dockWidgetContents_4)
        FilterDesigner.addDockWidget(
            QtCore.Qt.DockWidgetArea(1), self.zPlane_dock_widget
        )
        self.actionImport_Signal = QtWidgets.QAction(FilterDesigner)
        self.actionImport_Signal.setObjectName("actionImport_Signal")
        self.actionImport_Signal.setShortcut("Ctrl+I")
        self.actionExit = QtWidgets.QAction(FilterDesigner)
        self.actionExit.setObjectName("actionExit")
        self.actionExit.setShortcut("Ctrl+Q")
        self.actionExit.triggered.connect(self.exitApplication)
        self.menuFile.addAction(self.actionImport_Signal)
        self.menuFile.addAction(self.actionExit)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuView.menuAction())
        self.menubar.addAction(self.menuTools.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())

        # View menubar: show or hide dockwidgets
        self.toggle_dock1_action = QtWidgets.QAction(
            "Z-Plane Filter Design", FilterDesigner
        )
        self.toggle_dock1_action.setCheckable(True)
        self.toggle_dock1_action.setChecked(True)
        self.toggle_dock1_action.triggered.connect(
            lambda: self.toggle_dock_visibility(self.zPlane_dock_widget)
        )
        self.menuView.addAction(self.toggle_dock1_action)

        self.toggle_dock2_action = QAction("All-Pass Library", FilterDesigner)
        self.toggle_dock2_action.setCheckable(True)
        self.toggle_dock2_action.setChecked(True)
        self.toggle_dock2_action.triggered.connect(
            lambda: self.toggle_dock_visibility(self.allPassLibrary)
        )
        self.menuView.addAction(self.toggle_dock2_action)
        self.toggle_dock3_action = QAction("Mouse Pad", FilterDesigner)
        self.toggle_dock3_action.setCheckable(True)
        self.toggle_dock3_action.setChecked(True)
        self.toggle_dock3_action.triggered.connect(
            lambda: self.toggle_dock_visibility(self.mousePadGroupBox)
        )
        self.menuView.addAction(self.toggle_dock3_action)

        self.zPlane_dock_widget.visibilityChanged.connect(self.toggleZPlaneButton)
        self.allPassLibrary.visibilityChanged.connect(self.toggleAllpassButton)

        ##### Tools Menu #####
        self.actionExamples = QAction("Examples", FilterDesigner)
        self.menuExamples = QMenu("Examples", FilterDesigner)
        self.menuTools.addMenu(self.menuExamples)

        self.actionBandPass = QAction("Band-Pass", FilterDesigner)
        self.actionHighPass = QAction("High-Pass", FilterDesigner)
        self.actionLowPass = QAction("Low-Pass", FilterDesigner)

        self.menuExamples.addAction(self.actionBandPass)
        self.menuExamples.addAction(self.actionHighPass)
        self.menuExamples.addAction(self.actionLowPass)

        #### End Tools <3 ####

        self.actionOpen_Docs = QAction("App Documentation", FilterDesigner)
        self.actionOpen_Docs.triggered.connect(self.open_documentation)
        self.menuHelp.addAction(self.actionOpen_Docs)

        self.allPass00 = AllPassProcessButton(
            0.7,
            1,
            self.scrollAreaWidgetContents,
        )
        self.allPass01 = AllPassProcessButton(
            1 + 2j,
            2,
            self.scrollAreaWidgetContents,
        )
        self.allPass02 = AllPassProcessButton(
            0.3 + 0.2j,
            3,
            self.scrollAreaWidgetContents,
        )
        self.allPass03 = AllPassProcessButton(
            1.5j,
            4,
            self.scrollAreaWidgetContents,
        )
        self.allPass04 = AllPassProcessButton(
            5 + 1j,
            5,
            self.scrollAreaWidgetContents,
        )
        self.allPass05 = AllPassProcessButton(
            -0.9,
            6,
            self.scrollAreaWidgetContents,
        )
        self.allPass06 = AllPassProcessButton(
            1.2,
            7,
            self.scrollAreaWidgetContents,
        )
        self.allPass07 = AllPassProcessButton(
            3,
            8,
            self.scrollAreaWidgetContents,
        )
        self.allPass08 = AllPassProcessButton(
            0.2,
            9,
            self.scrollAreaWidgetContents,
        )

        ### Plotting Controls
        #####################
        self.exportSignal = QtWidgets.QPushButton()
        self.exportSignal.setObjectName("export_filtered_signal")
        self.pause_play_button = QtWidgets.QPushButton()
        self.pause_play_button.setCheckable(True)
        self.pause_play_button.setObjectName("pause_play_button")
        self.pause_play_button.setIcon(QtGui.QIcon("Resources/Icons/pause_button.png"))
        self.resetSignal = QtWidgets.QPushButton()
        self.resetSignal.setObjectName("resetSignal")
        self.resetSignal.setIcon(QtGui.QIcon("Resources/Icons/reset.png"))
        spacerItem4 = QtWidgets.QSpacerItem(
            40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum
        )
        spacerItem5 = QtWidgets.QSpacerItem(
            40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum
        )
        self.filtration_label = QtWidgets.QLabel("Filtered Points: 1")
        self.filtration_slider = QtWidgets.QSlider(QtCore.Qt.Horizontal)
        self.filtration_slider.setFixedWidth(300)
        self.filtration_slider.setMinimum(1)
        self.filtration_slider.setMaximum(100)
        self.filtration_slider.setValue(1)
        self.filtration_slider.setTickInterval(1)
        self.filtration_slider.setTickPosition(QtWidgets.QSlider.TicksBelow)
        self.label_min = QtWidgets.QLabel(
            str(self.filtration_slider.minimum()), FilterDesigner
        )
        self.label_max = QtWidgets.QLabel(
            str(self.filtration_slider.maximum()), FilterDesigner
        )
        self.label_min.setAlignment(QtCore.Qt.AlignLeft)
        self.label_max.setAlignment(QtCore.Qt.AlignRight)
        self.speedLabelsHorizontalLayout = QtWidgets.QHBoxLayout()
        self.speedLabelsHorizontalLayout.addWidget(self.label_min)
        self.speedLabelsHorizontalLayout.addWidget(self.label_max)
        self.speedControllerVerticalLayout = QtWidgets.QVBoxLayout()
        self.speedControllerVerticalLayout.addWidget(self.filtration_label)
        self.speedControllerVerticalLayout.addWidget(self.filtration_slider)
        self.speedControllerVerticalLayout.addLayout(self.speedLabelsHorizontalLayout)
        self.speedHLayout = QtWidgets.QHBoxLayout()

        self.speedHLayout.addItem(spacerItem4)
        self.speedHLayout.addWidget(self.pause_play_button)
        self.speedHLayout.addWidget(self.resetSignal)
        self.speedHLayout.addLayout(self.speedControllerVerticalLayout)
        self.speedHLayout.addItem(spacerItem5)
        self.speedHLayout.addWidget(self.exportSignal)
        self.verticalLayout_7.addLayout(self.speedHLayout)

        self.context_menu = QMenu()
        self.remove_action = QAction("Remove")
        self.context_menu.addAction(self.remove_action)

        ### Examples Menu
        self.bandpass_zeros = []
        self.bandpass_zeros.append(QtCore.QPointF(0.95, 0))
        self.bandpass_zeros.append(QtCore.QPointF(-0.95, 0))

        self.bandpass_poles = []
        self.bandpass_poles.append(QtCore.QPointF(0, 0))

        self.highpass_zeros = []
        self.highpass_zeros.append(QtCore.QPointF(0.95, 0))

        self.highpass_poles = []
        self.highpass_poles.append(QtCore.QPointF(0.75, 0))

        self.lowpass_zeros = []
        self.lowpass_zeros.append(QtCore.QPointF(0, 0))

        self.lowpass_poles = []
        self.lowpass_poles.append(QtCore.QPointF(0.95, 0))

        self.retranslateUi(FilterDesigner)
        QtCore.QMetaObject.connectSlotsByName(FilterDesigner)

    def toggleZPlaneButton(self, visible):
        # Update the toggle button's state based on the visibility of the dock widget
        self.toggle_dock1_action.setChecked(visible)

    def toggleAllpassButton(self, visible):
        # Update the toggle button's state based on the visibility of the dock widget
        self.toggle_dock2_action.setChecked(visible)

    def toggle_dock_visibility(self, dock):
        if dock.isVisible():
            dock.close()
        else:
            dock.show()

    def exitApplication(self):
        sys.exit()

    def open_documentation(self):
        webbrowser.open("https://github.com/Team-19-DSP-Tasks/Task06-FilterDesign")

    def retranslateUi(self, FilterDesigner):
        _translate = QtCore.QCoreApplication.translate
        FilterDesigner.setWindowTitle(_translate("FilterDesigner", "Filter Designer"))
        self.applicationGraphs.setTitle(
            _translate("FilterDesigner", "Application Signals")
        )
        self.mousePadGroupBox.setTitle(_translate("FilterDesigner", "Mouse Pad"))
        self.label.setText(
            _translate("FilterDesigner", "Generate signal by moving your mouse")
        )
        self.CascadedLabel.setText(
            _translate("FilterDesigner", "Cascaded All-Pass Filters:")
        )
        self.removeAllPasses.setText(
            _translate("FilterDesigner", "Remove all cascaded filters")
        )
        self.generateSignal.setText(_translate("FilterDesigner", "Generate Signal"))
        self.menuFile.setTitle(_translate("FilterDesigner", "File"))
        self.menuHelp.setTitle(_translate("FilterDesigner", "Help"))
        self.menuTools.setTitle(_translate("FilterDesigner", "Tools"))
        self.menuView.setTitle(_translate("FilterDesigner", "View"))
        self.allPassLibrary.setWindowTitle(
            _translate("FilterDesigner", "All-Pass Library")
        )
        self.allPassDesignGroupBox.setTitle(
            _translate("FilterDesigner", "Custom All-Pass Filter")
        )
        self.inputALabel.setText(_translate("FilterDesigner", "Input 'a'"))
        self.addAllPassFilter.setText(
            _translate("FilterDesigner", "Add custom all-pass filter")
        )
        self.correctPhase.setText(_translate("FilterDesigner", "Correct Phase"))
        self.zPlane_dock_widget.setWindowTitle(
            _translate("FilterDesigner", "Z-Plane Filter Design")
        )
        self.filterDesignGroupBox.setTitle(
            _translate("FilterDesigner", "Filter Design")
        )
        self.zPlaneDesignControls.setTitle(
            _translate("FilterDesigner", "Design Controls")
        )
        self.addPole.setText(_translate("FilterDesigner", "Add Pole"))
        self.addZero.setText(_translate("FilterDesigner", "Add Zero"))
        self.removeAllPoles.setText(_translate("FilterDesigner", "Remove all Poles"))
        self.removeAllZeros.setText(_translate("FilterDesigner", "Remove all Zeros"))
        self.resetDesign.setText(_translate("FilterDesigner", "Reset Design"))
        self.addConjugatesCheckBox.setText(
            _translate("FilterDesigner", "Add Conjugates")
        )
        self.applyFilterButton.setText(_translate("FilterDesigner", "Apply Filter"))
        self.exportSignal.setText(_translate("FilterDesigner", "Export Filtered Data"))
        self.exportFilter.setText(_translate("FilterDesigner", "Export Filter"))
        self.importFilter.setText(_translate("FilterDesigner", "Import Filter"))
        self.frequencyResponseGroupBox.setTitle(
            _translate("FilterDesigner", "Frequency Response")
        )
        self.actionImport_Signal.setText(_translate("FilterDesigner", "Import Signal"))
        self.actionExit.setText(_translate("FilterDesigner", "Exit"))


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    with open("Filter\stylesheet.qss", "r") as f:
        stylesheet = f.read()
        app.setStyleSheet(stylesheet)
    FilterDesigner = QtWidgets.QMainWindow()
    ui = Ui_FilterDesigner()
    ui.setupUi(FilterDesigner)
    backend = Backend(ui)
    FilterDesigner.show()
    sys.exit(app.exec_())

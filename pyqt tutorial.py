<<<<<<< HEAD
from PyQt5 import QtWidgets,QtCore,QtGui
from skip_frac import Ui_MainWindow
from run_desc import Ui_MainWindow2
from PyQt5 import QtCore, QtGui, QtWidgets
import pandas as pd
import sys
import pandas as pd
#
# class DataFrameModel(QtCore.QAbstractTableModel):
#     DtypeRole = QtCore.Qt.UserRole + 1000
#     ValueRole = QtCore.Qt.UserRole + 1001
#
#     def __init__(self, df=pd.DataFrame(), parent=None):
#         super(DataFrameModel, self).__init__(parent)
#         self._dataframe = df
#
#     def setDataFrame(self, dataframe):
#         self.beginResetModel()
#         self._dataframe = dataframe.copy()
#         self.endResetModel()
#
#     def dataFrame(self):
#         return self._dataframe
#
#     dataFrame = QtCore.pyqtProperty(pd.DataFrame, fget=dataFrame, fset=setDataFrame)
#
#     @QtCore.pyqtSlot(int, QtCore.Qt.Orientation, result=str)
#     def headerData(self, section: int, orientation: QtCore.Qt.Orientation, role: int = QtCore.Qt.DisplayRole):
#         if role == QtCore.Qt.DisplayRole:
#             if orientation == QtCore.Qt.Horizontal:
#                 return self._dataframe.columns[section]
#             else:
#                 return str(self._dataframe.index[section])
#         return QtCore.QVariant()
#
#     def rowCount(self, parent=QtCore.QModelIndex()):
#         if parent.isValid():
#             return 0
#         return len(self._dataframe.index)
#
#     def columnCount(self, parent=QtCore.QModelIndex()):
#         if parent.isValid():
#             return 0
#         return self._dataframe.columns.size
#
#     def data(self, index, role=QtCore.Qt.DisplayRole):
#         if not index.isValid() or not (0 <= index.row() < self.rowCount() \
#             and 0 <= index.column() < self.columnCount()):
#             return QtCore.QVariant()
#         row = self._dataframe.index[index.row()]
#         col = self._dataframe.columns[index.column()]
#         dt = self._dataframe[col].dtype
#
#         val = self._dataframe.iloc[row][col]
#         if role == QtCore.Qt.DisplayRole:
#             return str(val)
#         elif role == DataFrameModel.ValueRole:
#             return val
#         if role == DataFrameModel.DtypeRole:
#             return dt
#         return QtCore.QVariant()
#
#     def roleNames(self):
#         roles = {
#             QtCore.Qt.DisplayRole: b'display',
#             DataFrameModel.DtypeRole: b'dtype',
#             DataFrameModel.ValueRole: b'value'
#         }
#         return roles


class PandasModel(QtCore.QAbstractTableModel):
    """
    Class to populate a table view with a pandas dataframe
    """
    def __init__(self, data, parent=None):
        QtCore.QAbstractTableModel.__init__(self, parent)
        self._data = data

    def rowCount(self, parent=None):
        return len(self._data.values)

    def columnCount(self, parent=None):
        return self._data.columns.size

    def data(self, index, role=QtCore.Qt.DisplayRole):
        if index.isValid():
            if role == QtCore.Qt.DisplayRole:
                return str(self._data.values[index.row()][index.column()])
        return None

    def headerData(self, col, orientation, role):
        if orientation == QtCore.Qt.Horizontal and role == QtCore.Qt.DisplayRole:
            return self._data.columns[col]
        return None

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(662, 512)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setObjectName("lineEdit")
        self.verticalLayout.addWidget(self.lineEdit)
        self.tableView = QtWidgets.QTableView(self.centralwidget)
        self.tableView.setObjectName("tableView")
        self.verticalLayout.addWidget(self.tableView)
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setObjectName("pushButton")
        self.verticalLayout.addWidget(self.pushButton)
        self.horizontalLayout.addLayout(self.verticalLayout)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 662, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton.setText(_translate("MainWindow", "PushButton"))


        self.pushButton.clicked.connect(self.btn_clk)

        MainWindow.show()

    def btn_clk(self):
        path = self.lineEdit.text()
        df = pd.read_csv(path)
        model = PandasModel(df)
        self.tableView.setModel(model)

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
=======
from PyQt5 import QtWidgets,QtCore,QtGui
from skip_frac import Ui_MainWindow
from run_desc import Ui_MainWindow2
from PyQt5 import QtCore, QtGui, QtWidgets
import pandas as pd
import sys
import pandas as pd
#
# class DataFrameModel(QtCore.QAbstractTableModel):
#     DtypeRole = QtCore.Qt.UserRole + 1000
#     ValueRole = QtCore.Qt.UserRole + 1001
#
#     def __init__(self, df=pd.DataFrame(), parent=None):
#         super(DataFrameModel, self).__init__(parent)
#         self._dataframe = df
#
#     def setDataFrame(self, dataframe):
#         self.beginResetModel()
#         self._dataframe = dataframe.copy()
#         self.endResetModel()
#
#     def dataFrame(self):
#         return self._dataframe
#
#     dataFrame = QtCore.pyqtProperty(pd.DataFrame, fget=dataFrame, fset=setDataFrame)
#
#     @QtCore.pyqtSlot(int, QtCore.Qt.Orientation, result=str)
#     def headerData(self, section: int, orientation: QtCore.Qt.Orientation, role: int = QtCore.Qt.DisplayRole):
#         if role == QtCore.Qt.DisplayRole:
#             if orientation == QtCore.Qt.Horizontal:
#                 return self._dataframe.columns[section]
#             else:
#                 return str(self._dataframe.index[section])
#         return QtCore.QVariant()
#
#     def rowCount(self, parent=QtCore.QModelIndex()):
#         if parent.isValid():
#             return 0
#         return len(self._dataframe.index)
#
#     def columnCount(self, parent=QtCore.QModelIndex()):
#         if parent.isValid():
#             return 0
#         return self._dataframe.columns.size
#
#     def data(self, index, role=QtCore.Qt.DisplayRole):
#         if not index.isValid() or not (0 <= index.row() < self.rowCount() \
#             and 0 <= index.column() < self.columnCount()):
#             return QtCore.QVariant()
#         row = self._dataframe.index[index.row()]
#         col = self._dataframe.columns[index.column()]
#         dt = self._dataframe[col].dtype
#
#         val = self._dataframe.iloc[row][col]
#         if role == QtCore.Qt.DisplayRole:
#             return str(val)
#         elif role == DataFrameModel.ValueRole:
#             return val
#         if role == DataFrameModel.DtypeRole:
#             return dt
#         return QtCore.QVariant()
#
#     def roleNames(self):
#         roles = {
#             QtCore.Qt.DisplayRole: b'display',
#             DataFrameModel.DtypeRole: b'dtype',
#             DataFrameModel.ValueRole: b'value'
#         }
#         return roles


class PandasModel(QtCore.QAbstractTableModel):
    """
    Class to populate a table view with a pandas dataframe
    """
    def __init__(self, data, parent=None):
        QtCore.QAbstractTableModel.__init__(self, parent)
        self._data = data

    def rowCount(self, parent=None):
        return len(self._data.values)

    def columnCount(self, parent=None):
        return self._data.columns.size

    def data(self, index, role=QtCore.Qt.DisplayRole):
        if index.isValid():
            if role == QtCore.Qt.DisplayRole:
                return str(self._data.values[index.row()][index.column()])
        return None

    def headerData(self, col, orientation, role):
        if orientation == QtCore.Qt.Horizontal and role == QtCore.Qt.DisplayRole:
            return self._data.columns[col]
        return None

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(662, 512)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setObjectName("lineEdit")
        self.verticalLayout.addWidget(self.lineEdit)
        self.tableView = QtWidgets.QTableView(self.centralwidget)
        self.tableView.setObjectName("tableView")
        self.verticalLayout.addWidget(self.tableView)
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setObjectName("pushButton")
        self.verticalLayout.addWidget(self.pushButton)
        self.horizontalLayout.addLayout(self.verticalLayout)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 662, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton.setText(_translate("MainWindow", "PushButton"))


        self.pushButton.clicked.connect(self.btn_clk)

        MainWindow.show()

    def btn_clk(self):
        path = self.lineEdit.text()
        df = pd.read_csv(path)
        model = PandasModel(df)
        self.tableView.setModel(model)

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
>>>>>>> 14dd7a7d363abd73c3382bddcb4bbae63a207333
    sys.exit(app.exec_())
from PyQt5 import QtWidgets,QtCore,QtGui
from PyQt5.QtWidgets import QTableView
from PyQt5.QtCore import QAbstractTableModel, Qt
from skip_frac import Ui_MainWindow
from run_desc import Ui_MainWindow2
from polymer_bounds import Ui_MainWindow3

import sys
import pandas as pd
import numpy as np


def filtered_data(name,time_underscore):
    # file_name = 'Burst on PThio DNA.txt'
    f = open(name, 'r')
    headers = ['Dye', 'Peak Number', 'Height', 'Time', 'Well', 'Area', 'Data Point']
    # data = pd.read_csv('Burst on PThio DNA.txt')
    f.readline()
    col_data = []
    count = 0
    # reads each line in the text file
    for test in f:
        # Splits column data based on header
        # Dye/Sample Peak,Sample File Name,Size, Height, Area,Data Point

        test_set = test.split()
        # Output: ['"B,1"', 'PT_100nM_0_TLD_4.2.19_1_2019-04-02_A05.fsa', '894', '11056', '2524']

        # print(test_set)
        # strips the underscore in long description
        desc_fix = test_set[1].split('_')
        # Output: ['PT', '100nM', '0', 'TLD', '4.2.19', '1', '2019-04-02', 'A05.fsa']

        # print(desc_fix)
        # removes long description name
        test_set.pop(1)
        # Output: ['"B,1"','894', '11056', '2524']
        # print(test_set)
        # print(test_set)

        # inserts time into test_set
        test_set.insert(2, desc_fix[time_underscore])

        # Output:['"B,1"', 'PT_100nM_0_TLD_4.2.19_1_2019-04-02_A05.fsa', '0', '894', '11056', '2524']

        # inserts Well number at the end of test_set
        test_set.insert(3, desc_fix[len(desc_fix) - 1])

        # Output: #['"B,1"', 'PT_100nM_0_TLD_4.2.19_1_2019-04-02_A05.fsa', '0', 'A05.fsa', '894', '11056', '2524']

        # print(test_set)

        # splits dye and peak number and puts them into separate columns
        dye_peak = test_set[0].strip('\"').replace(',', '')
        test_set.pop(0)
        i = 0
        while i < len(dye_peak):
            test_set.insert(i, dye_peak[i])
            i += 1
        # print(test_set)
        # adding all data to each column
        col_data.append(test_set)
        count += 1
    # pprint.pprint(col_data)
    df = pd.DataFrame(col_data, columns=headers)
    # print(col_data)

    # filters height above user input. Note that if filter height
    # is above internal standard height, then error will raise
    # have to add try/except block here for future use
    return df
    # df_int_all = df.loc[df['Dye'] == 'Y']
    # return df_int_all
    # print()
    # print("These are all the internal std. peaks\n")
    # print('---------------------------------------\n')
    # print(df_int_all)
    # print()
    #min_height = input("Please enter the minimum height (make sure bigger than int std desired): ")
    # while string_alpha_check(min_height):
    #     min_height = input("Not valid integer, please try again: ")

    # min_height = int(min_height)
    # df_hmin = df.loc[df['Height'].astype(int) > min_height]
    # return df_hmin


def int_std_all(df):
    df_int_all = df.loc[df['Dye'] == 'Y']
    return df_int_all

def all_peaks_filtered(df,min_height):
    df_hmin = df.loc[df['Height'].astype(int) > min_height]
    return df_hmin
def int_std_filtered(df):
    df_int_std_filtered = df.loc[df['Dye'] == 'Y']
    return df_int_std_filtered

class pandasModel(QAbstractTableModel):

    def __init__(self, data):
        QAbstractTableModel.__init__(self)
        self._data = data

    def rowCount(self, parent=None):
        return self._data.shape[0]

    def columnCount(self, parent=None):
        return self._data.shape[1]

    def data(self, index, role=Qt.DisplayRole):
        if index.isValid():
            if role == Qt.DisplayRole:
                return str(self._data.iloc[index.row(), index.column()])
        return None

    def headerData(self, col, orientation, role):
        if orientation == Qt.Horizontal and role == Qt.DisplayRole:
            return self._data.columns[col]
        return None




class MyWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(MyWindow,self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.setWindowTitle('Skip Frac vs. Size')
        self.show()
        self.ui.pushButton.clicked.connect(self.on_push_yes)
        # self.ui.hide()
        self.ui.pushButton_2.clicked.connect(self.on_push_no)


    def on_push_yes(self):
        print('Hello')
    def on_push_no(self):
        self.close()
        self.RunDesc = RunDesc()
        #self.ui.close()
        # window_RunD = RunDesc()
        # window_RunD.show()



class RunDesc(QtWidgets.QMainWindow):
    def __init__(self):
        super(RunDesc,self).__init__()
        self.ui2 = Ui_MainWindow2()
        self.ui2.setupUi2(self)
        self.setWindowTitle('Run Description')
        self.show()
        #Gets the file run description from text file
        self.ui2.pushButton.clicked.connect(self.getTxt)
        #Gets the time underscore
        self.ui2.pushButton_2.clicked.connect(self.getTimeUnderscore) #Gets the time underscore
        self.ui2.pushButton_3.clicked.connect(self.pressBack) #Goes to the previous frame
        self.ui2.pushButton_8.clicked.connect(self.showAllPeaks) #Shows all the peaks before filtering
        self.ui2.pushButton_4.clicked.connect(self.showAllIntStdPeaks) #Shows all internal standard peaks
        self.ui2.pushButton_5.clicked.connect(self.getMinHeight) #Gets the minimum height filter
        self.ui2.pushButton_6.clicked.connect(self.showAllFilteredPeaks) #Shows all the filtered peaks
        self.ui2.pushButton_7.clicked.connect(self.showFilteredStd) #Shows all the filtered internal std. peaks
        self.ui2.pushButton_9.clicked.connect(self.showPolymerBounds)


#fileName, _ = QtWidgets.QFileDialog.getOpenFileName(self, 'Single File', QtCore.QDir.rootPath() , '*.xlsm')

    def getTxt(self):
        global fileName
        #options = QtGui.QFileDialog.Options()
        fileName, _ = QtWidgets.QFileDialog.getOpenFileName(self, 'Single File', QtCore.QDir.rootPath(), '*.txt')
        #self.ui2.lineEdit_2.setText(fileName)
        file = open(fileName,'r')
        file.readline()
        second_line = file.readline()
        split_second_line = second_line.split()
        txt_file_name = split_second_line[1]
        file.close()
        self.ui2.lineEdit_2.setText(fileName)
        self.ui2.RunDescLabel.setText(txt_file_name)
        # self.df = filtered_data(fileName,2)
        # model = pandasModel(self.df)
        # self.view = QTableView()
        # self.view.setModel(model)
        # self.view.setWindowTitle('Internal Standard Peaks')
        # self.view.resize(800, 600)
        # self.view.show()

    #Have to error check in case not an integer
    def getTimeUnderscore(self):
        global time_underscore
        time_underscore = int(self.ui2.lineEdit.text())


    def pressBack(self):
        self.close()
        self.backFrac = MyWindow()

    def getMinHeight(self):
        global min_height
        min_height = int(self.ui2.lineEdit_3.text())


    def showAllPeaks(self):
        self.df_all_peaks = filtered_data(fileName,time_underscore)
        #self.df_int_std_all = int_std_all(self.df_all_peaks)
        model = pandasModel(self.df_all_peaks)
        self.view = QTableView()
        self.view.setModel(model)
        self.view.setWindowTitle('All Peaks')
        self.view.resize(800, 600)
        #self.close()
        self.view.show()

    def showAllIntStdPeaks(self):
        self.df_all_int_std_peaks = int_std_all(self.df_all_peaks)
        model_all_int = pandasModel(self.df_all_int_std_peaks)
        self.view_int_std_all = QTableView()
        self.view_int_std_all.setModel(model_all_int)
        self.view_int_std_all.setWindowTitle('All Internal Std. Peaks')
        self.view_int_std_all.resize(800, 600)
        # self.close()
        self.view_int_std_all.show()

    def showAllFilteredPeaks(self):
        global df_global_peaks #For use in another class
        self.df_all_filtered_peaks = all_peaks_filtered(self.df_all_peaks,min_height)
        df_global_peaks = all_peaks_filtered(self.df_all_filtered_peaks,min_height)
        model_all_filtered = pandasModel(self.df_all_filtered_peaks)
        self.view_all_filtered = QTableView()
        self.view_all_filtered.setModel(model_all_filtered)
        self.view_all_filtered.setWindowTitle('All Filtered Peaks')
        self.view_all_filtered.resize(800,600)
        #self.close()
        self.view_all_filtered.show()

    def showFilteredStd(self):
        self.df_int_std_filter = int_std_filtered(self.df_all_filtered_peaks)
        model_int_std_filter = pandasModel(self.df_int_std_filter)
        self.view_int_std_filter = QTableView()
        self.view_int_std_filter.setModel(model_int_std_filter)
        self.view_int_std_filter.setWindowTitle('Filtered internal std. peaks')
        self.view_int_std_filter.resize(800,600)
        #self.close()
        self.view_int_std_filter.show()

    def showPolymerBounds(self):
        self.polymer = polymerBounds()
        #pass

def sample_distance(filtered_data):
    # gets peaks without internal standard
    df_no_int = filtered_data.loc[filtered_data['Dye'] == 'B']
    #print(df_no_int)

    # gets peaks with internal standard
    df_int_std = filtered_data.loc[filtered_data['Dye'] == 'Y']

    #Exports the internal standard data
    #export_int_std = df_int_std.to_csv('Export_data_int_std.csv',sep = ',')
    # print('These are the internal std. peaks after filtering')
    # print('------------------------------------------------')
    # print(df_int_std)
    # print()
    # makes list of int standard data points
    int_stdlist = df_int_std['Data Point'].tolist()

    # makes list of int standard time points
    int_stdtimelist = df_int_std['Time'].tolist()

    # makes list of sample data points
    sample_list = df_no_int['Data Point'].tolist()

    # makes list of sample time points
    sample_timelist = df_no_int['Time'].tolist()
    # print(sample_timelist)

    #zips the internal standard time points and data points into a dictionary
    # Ex: {1:2,3:4}
    int_std_dict = dict(zip(int_stdtimelist, int_stdlist))

    #zips the sample time points and data points into a nested list
    # Ex: [[1,2],[3,4]]
    sample_2d = [list(a) for a in zip(sample_timelist, sample_list)]

    #pprint.pprint(sample_2d)

    # if sample_2d[i][0] in int_std_dict:

    #Creates a column in the pandas dataframe for difference
    #(internal standard - sample) by using datapoint
    #For each time
    diff_list = []
    for i in range(len(sample_2d)):
        #Subtracts the internal std value by the sample datapoint
        #Method is inefficient, could probably use nested list
        # for the internal standards as well
        #diff = int(int_std_dict[sample_2d[i][0]]) - int(sample_2d[i][1])
        diff = round(float(int(int_std_dict[sample_2d[i][0]])/int(sample_2d[i][1])) * 100,2)
        diff_list.append(diff)

    #This is to prevent pandas SettingwithCopyWarning
    df_diff = df_no_int.copy()
    df_diff['Diff'] = diff_list

    # exports data with compared to internal standard
    #export_excel_difference = df_diff.to_csv('Export_data_intstd_Diff.csv',sep=',')

    #Returns a dataframe containing values with differences and
    #No intenal standard column
    return (df_diff)

polymer_list = []
class polymerBounds(QtWidgets.QMainWindow):

    def __init__(self):
        super(polymerBounds,self).__init__()

        self.ui3 = Ui_MainWindow3()
        self.ui3.setupUi3(self)
        self.setWindowTitle('Polymer Bounds')
        self.show()


        self.ui3.pushButton.clicked.connect(self.showDifferencesTable)
        self.ui3.pushButton_5.clicked.connect(self.showDifferences)
        self.ui3.pushButton_2.clicked.connect(self.getPolymerName)
        # self.ui3.pushButton_3.clicked.connect(self.getLowerBound)
        # self.ui3.pushButton_4.clicked.connect(self.getUpperBound)
        #
        for name in polymer_list:
            self.ui3.label.setText(name)
        # self.ui3.label_5.setText(self.lower_bound)
        # self.ui3.label_5.setText(self.upper_bound)

        # self.df_all_peaks = filtered_data(fileName, time_underscore)
        # # self.df_int_std_all = int_std_all(self.df_all_peaks)
        # model = pandasModel(self.df_all_peaks)
        # self.view = QTableView()
        # self.view.setModel(model)
        # self.view.setWindowTitle('All Peaks')
        # self.view.resize(800, 600)
        # # self.close()
        # self.view.show()

    def showDifferencesTable(self):
        self.df_differences = sample_distance(df_global_peaks)
        self.df_diff_ranges = self.df_differences['Diff'].tolist()
        self.df_diff_ranges.sort()
        self.df_diff_ranges_tab = pd.DataFrame(self.df_diff_ranges,columns=['Diff'])


        #for table
        model = pandasModel(self.df_differences)
        self.view_diff = QTableView()
        self.view_diff.setModel(model)
        self.view_diff.setWindowTitle('Differences Table')
        self.view_diff.resize(800,600)
        #self.close
        self.view_diff.show()


    def showDifferences(self):
        self.df_differences2 = sample_distance(df_global_peaks)
        self.df_diff_ranges2= self.df_differences2['Diff'].tolist()
        self.df_diff_ranges2.sort()
        self.df_diff_ranges_tab = pd.DataFrame(self.df_diff_ranges, columns=['Diff'])

        # For ranges only
        model2 = pandasModel(self.df_diff_ranges_tab)
        self.view_diff2 = QTableView()
        self.view_diff2.setModel(model2)
        self.view_diff2.setWindowTitle('Differences')
        self.view_diff2.resize(500, 600)
        # self.close
        self.view_diff2.show()
    def getPolymerName(self):
        self.polymer_name = self.ui3.lineEdit_2.text()
        polymer_list.append(self.polymer_name)
    #     self.ui3.label_5.setText(self.polymer_name)
    #
    # def getLowerBound(self):
    #     self.lower_bound = float(self.ui3.lineEdit_3.text())
    #     self.ui3.label_5.setText(self.lower_bound)
    #
    # def getUpperBound(self):
    #     self.upper_bound = float(self.ui3.lineEdit_4.text())
    #     self.ui3.label_5.setText(self.upper_bound)





# class RunDesc(QtWidgets.QMainWindow):
#     def __init__(self):
#         super(RunDesc,self).__init__()
#         self.ui2 = Ui_MainWindow2()
#         self.ui2.setupUi2(self)
#         self.setWindowTitle('Run Description')

    #     self.ui2.pushButton.clicked.connect(self.gettxt)
    #
    # def gettxt(self):
    #     txtName = QtGui.QFileDialog.getOpenFileName(self, 'Single File', 'C:\\', '*.py')
sys._excepthook = sys.excepthook
def exception_hook(exctype, value, traceback):
    print(exctype, value, traceback)
    sys._excepthook(exctype, value, traceback)
    sys.exit(1)
sys.excepthook = exception_hook
app = QtWidgets.QApplication(sys.argv)
application = MyWindow()
application.show()
sys.exit(app.exec_())
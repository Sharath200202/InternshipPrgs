#PYQUIT CODE:
# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'fra.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(968, 795)
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(330, 30, 311, 51))
        self.label.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgb(0, 0, 0);\n"
"font: 75 14pt \"Palatino Linotype\";")
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(60, 130, 55, 71))
        self.label_2.setStyleSheet("font: 12pt \"MV Boli\";")
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(Form)
        self.label_3.setGeometry(QtCore.QRect(50, 200, 151, 51))
        self.label_3.setStyleSheet("font: 12pt \"MV Boli\";")
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(Form)
        self.label_4.setGeometry(QtCore.QRect(50, 260, 131, 71))
        self.label_4.setStyleSheet("font: 12pt \"MV Boli\";")
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(Form)
        self.label_5.setGeometry(QtCore.QRect(50, 330, 171, 71))
        self.label_5.setStyleSheet("font: 12pt \"MV Boli\";")
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(Form)
        self.label_6.setGeometry(QtCore.QRect(50, 400, 81, 71))
        self.label_6.setStyleSheet("font: 12pt \"MV Boli\";")
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(Form)
        self.label_7.setGeometry(QtCore.QRect(50, 460, 151, 71))
        self.label_7.setStyleSheet("font: 12pt \"MV Boli\";")
        self.label_7.setObjectName("label_7")
        self.label_8 = QtWidgets.QLabel(Form)
        self.label_8.setGeometry(QtCore.QRect(140, 650, 131, 71))
        self.label_8.setStyleSheet("font: 12pt \"MV Boli\";")
        self.label_8.setObjectName("label_8")
        self.label_9 = QtWidgets.QLabel(Form)
        self.label_9.setGeometry(QtCore.QRect(50, 530, 81, 71))
        self.label_9.setStyleSheet("font: 12pt \"MV Boli\";")
        self.label_9.setObjectName("label_9")
        self.ag = QtWidgets.QLineEdit(Form)
        self.ag.setGeometry(QtCore.QRect(120, 150, 251, 31))
        self.ag.setObjectName("ag")
        self.wkg = QtWidgets.QLineEdit(Form)
        self.wkg.setGeometry(QtCore.QRect(170, 210, 251, 31))
        self.wkg.setObjectName("wkg")
        self.hcm = QtWidgets.QLineEdit(Form)
        self.hcm.setGeometry(QtCore.QRect(170, 280, 251, 31))
        self.hcm.setObjectName("hcm")
        self.wtm = QtWidgets.QLineEdit(Form)
        self.wtm.setGeometry(QtCore.QRect(200, 350, 251, 31))
        self.wtm.setObjectName("wtm")
        self.bmd = QtWidgets.QLineEdit(Form)
        self.bmd.setGeometry(QtCore.QRect(120, 420, 251, 31))
        self.bmd.setObjectName("bmd")
        self.med = QtWidgets.QLineEdit(Form)
        self.med.setGeometry(QtCore.QRect(200, 480, 251, 31))
        self.med.setObjectName("med")
        self.sexn = QtWidgets.QLineEdit(Form)
        self.sexn.setGeometry(QtCore.QRect(130, 550, 251, 31))
        self.sexn.setObjectName("sexn")
        self.fran = QtWidgets.QLineEdit(Form)
        self.fran.setGeometry(QtCore.QRect(270, 680, 251, 31))
        self.fran.setObjectName("fran")
        self.button = QtWidgets.QPushButton(Form)
        self.button.setGeometry(QtCore.QRect(430, 600, 141, 51))
        self.button.clicked.connect(self.frac)
        self.button.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgb(0, 0, 0);\n"
"font: 12pt \"MV Boli\";")
        self.button.setObjectName("button")
        self.textEdit = QtWidgets.QTextEdit(Form)
        self.textEdit.setGeometry(QtCore.QRect(70, 700, 191, 61))
        self.textEdit.setStyleSheet("font: 8pt \"MV Boli\";")
        self.textEdit.setObjectName("textEdit")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)
    def frac(self):
        import pandas as ps
        path="C:\\Users\\Shaea\\OneDrive\\Desktop\\projects\\Logistic\\Predcit fracture or not\\bmd.csv"
        data = ps.read_csv(path)
        print(data)
        print(data.info())

        import sklearn      #importing
        from sklearn.preprocessing import LabelEncoder  # which is used to the encode the values 
        la_medication=LabelEncoder()                        # which used to transfrom the values of specific column of company 
        la_sex=LabelEncoder()
        la_fracture=LabelEncoder()

        data['medication_n']=la_medication.fit_transform(data['medication'])
        data['sex_n']=la_sex.fit_transform(data['sex'])
        data['fracture_n']=la_fracture.fit_transform(data['fracture'])

        inputs = data.drop(['id','fracture','fracture_n','sex','medication'],axis=1)
        output = data.drop(['id','age','sex_n','medication_n','weight_kg','height_cm','bmd','waiting_time','sex','medication','fracture'],axis=1)

        print(inputs)
        print(output)

        import sklearn
        from sklearn.model_selection import train_test_split
        x_train,x_test,y_train,y_test=train_test_split(inputs,output,train_size=0.2)

        from sklearn.preprocessing import StandardScaler  # increase the accuracy
        x_train.columns=['age','weight_kg','height_cm','waiting_time','bmd','medication_n','sex_n']
        x_test.columns=['age','weight_kg','height_cm','waiting_time','bmd','medication_n','sex_n']
        sc=StandardScaler()
        x_train=sc.fit_transform(x_train)
        x_test=sc.transform(x_test)
        
        inputage = self.ag.text()
        inputweight_kg = self.wkg.text()
        inputheight_cm = self.hcm.text()
        inputwaiting_time = self.wtm.text()
        inputbmd = self.bmd.text()
        inputmedication_n = self.med.text()
        inputsex_n = self.sexn.text()
        

        from sklearn.svm import SVC    # importing the model
        model=SVC()
        model.fit(x_train,y_train)
        y_pred=model.predict(x_test)
        print(y_test)
        print(y_pred)

        acc=model.score(x_train,y_train)*100
        print("acc :",acc)

        from sklearn.metrics import confusion_matrix
        cm=confusion_matrix(y_test,y_pred)
        print("cm=",cm)

        import numpy as np
        newinputs = np.array([[float(inputage),float(inputweight_kg),float(inputheight_cm),int(inputwaiting_time),float(inputbmd),int(inputmedication_n),int(inputsex_n)]])  #to cal predict ([[age,salary,gender_n]])
        newinputs = sc.transform(newinputs)
        res = model.predict(newinputs)
        print(res)

        self.fran.setText(str(res))
        

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label.setText(_translate("Form", "   FRACTURE PREDICTION"))
        self.label_2.setText(_translate("Form", "age :"))
        self.label_3.setText(_translate("Form", "weight_kg :"))
        self.label_4.setText(_translate("Form", "height_cm :"))
        self.label_5.setText(_translate("Form", "waiting_time :"))
        self.label_6.setText(_translate("Form", "bmd :"))
        self.label_7.setText(_translate("Form", "medication_n :"))
        self.label_8.setText(_translate("Form", "fracture_n :"))
        self.label_9.setText(_translate("Form", "sex_n :"))
        self.button.setText(_translate("Form", "PREDICT"))
        self.textEdit.setHtml(_translate("Form", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MV Boli\'; font-size:8pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"justify\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'MS Shell Dlg 2\'; font-size:7.8pt; font-weight:600; font-style:italic;\">FOR FRACTURED = 1  </span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'MS Shell Dlg 2\'; font-size:7.8pt; font-weight:600; font-style:italic;\">FOR NOT FRACTURED = 0</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'MS Shell Dlg 2\'; font-size:7.8pt; font-weight:600; font-style:italic;\"><br /></p></body></html>"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
    
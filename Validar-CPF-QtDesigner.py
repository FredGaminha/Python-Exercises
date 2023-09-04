from PyQt5 import QtCore, QtGui, QtWidgets
import time
import os

#primeiroDigito = False
#segundoDigito = False

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(470, 213)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.lbl_tituloCPF = QtWidgets.QLabel(self.centralwidget)
        self.lbl_tituloCPF.setGeometry(QtCore.QRect(150, 10, 161, 21))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.lbl_tituloCPF.setFont(font)
        self.lbl_tituloCPF.setObjectName("lbl_tituloCPF")
        self.lbl_digiteCPF = QtWidgets.QLabel(self.centralwidget)
        self.lbl_digiteCPF.setGeometry(QtCore.QRect(30, 40, 47, 21))
        self.lbl_digiteCPF.setObjectName("lbl_digiteCPF")
        self.txt_digiteCPF = QtWidgets.QLineEdit(self.centralwidget)
        self.txt_digiteCPF.setGeometry(QtCore.QRect(80, 40, 281, 20))
        self.txt_digiteCPF.setObjectName("txt_digiteCPF")
        self.btn_validarCPF = QtWidgets.QPushButton(self.centralwidget)
        self.btn_validarCPF.setGeometry(QtCore.QRect(370, 40, 75, 23))
        self.btn_validarCPF.setObjectName("btn_validarCPF")
        self.lbl_validacaoCPF = QtWidgets.QLabel(self.centralwidget)
        self.lbl_validacaoCPF.setEnabled(True)
        self.lbl_validacaoCPF.setGeometry(QtCore.QRect(150, 70, 160, 16))
        self.lbl_validacaoCPF.setText("")
        self.lbl_validacaoCPF.setObjectName("lbl_validacaoCPF")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 470, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.btn_validarCPF.clicked.connect(self.validarCPF)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "CPF"))
        self.lbl_tituloCPF.setText(_translate("MainWindow", "Validador de CPF"))
        self.lbl_digiteCPF.setText(_translate("MainWindow", "CPF:"))
        self.btn_validarCPF.setText(_translate("MainWindow", "Validar"))

    def validarCPF(self):
        userCPF = self.txt_digiteCPF.text()
        #valida_primeiroDigito(userCPF)
        #valida_segundoDigito(userCPF)

        if(userCPF.isdigit and len(userCPF) == 11):
            if(valida_primeiroDigito(userCPF) and valida_segundoDigito(userCPF)) == True:
                self.lbl_validacaoCPF.setText(f'O CPF {userCPF} é VÁLIDO')
            else:
                self.lbl_validacaoCPF.setText(f'O CPF {userCPF} é INVÁLIDO')
        else:
                self.lbl_validacaoCPF.setText(f'O CPF digitado está errado')

def valida_primeiroDigito(userCPF):
    primeiroDigito_Multiplicador = 10
    digitoSoma = 0
    corpoCPF = userCPF[:9]
    primeiroDigito = False

    for i in corpoCPF:
        resultado = int(i) * primeiroDigito_Multiplicador
        #print(f'{int(i)} x {primeiroDigito_Multiplicador} = {resultado}')
        primeiroDigito_Multiplicador -= 1
        digitoSoma += resultado

    #print(f'A soma dos nove dígitos do CPF é {digitoSoma}')

    primeiroDigito_SomaMult = digitoSoma * 10
    #print(primeiroDigito_SomaMult)

    primeiroDigito_Resto = primeiroDigito_SomaMult % 11
    #print(primeiroDigito_Resto)

    if(primeiroDigito_Resto <= 9):
        if(primeiroDigito_Resto == int(userCPF[9:10])):
            #print("Primeiro dígito OK")
            primeiroDigito = True
    elif(primeiroDigito_Resto > 9):
        primeiroDigito_Resto = 0
        if(primeiroDigito_Resto == int(userCPF[9:10])):
            #print("Primeiro dígito OK")
            primeiroDigito = True

    return primeiroDigito

def valida_segundoDigito(userCPF):
    segundoDigito_Multiplicador = 11
    digitoSoma = 0
    corpoCPF = userCPF[:10]
    segundoDigito = False

    for i in corpoCPF:
        resultado = int(i) * segundoDigito_Multiplicador
        #print(f'{int(i)} x {segundoDigito_Multiplicador} = {resultado}')
        segundoDigito_Multiplicador -= 1
        digitoSoma += resultado
    
    #print(f'A soma dos nove dígitos do CPF é {digitoSoma}')

    segundoDigito_SomaMult = digitoSoma * 10
    #print(segundoDigito_SomaMult)

    segundoDigito_Resto = segundoDigito_SomaMult % 11
    #print(segundoDigito_Resto)

    #print(segundoDigito_Resto == int(userCPF[10:11]))

    if(segundoDigito_Resto <= 9):
        if(segundoDigito_Resto == int(userCPF[10:11])):
            #print("Segundo dígito OK")
            segundoDigito = True
    elif(segundoDigito_Resto > 9):
        segundoDigito_Resto = 0
        if(segundoDigito_Resto == int(userCPF[10:11])):
            #print("Segundo dígito OK")
            segundoDigito = True

    return segundoDigito

"""
primeiroDigito = False
segundoDigito = False

while True:
    userCPF = input("Digite um CPF: ")

    if userCPF.isdigit and len(userCPF) == 11:
        #print("Fazendo validação")
        #time.sleep(2)
        valida_primeiroDigito(userCPF, primeiroDigito)
        valida_segundoDigito(userCPF, segundoDigito)
        if (valida_primeiroDigito and valida_segundoDigito) == True:
            print("CPF Válido")
            time.sleep(3)
            break
        else:
            print("CPF Inválido")
            time.sleep(3)
"""

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

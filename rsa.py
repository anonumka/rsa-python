import random
import sys
from unicodedata import digit
from PyQt5 import QtCore, QtGui, QtWidgets

e = 65537
first_primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 
                53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101, 103, 107, 
                109, 113, 127, 131, 137, 139, 149, 151, 157, 163, 167, 
                173, 179, 181, 191, 193, 197, 199, 211, 223, 227, 229, 
                233, 239, 241, 251, 257, 263, 269, 271, 277, 281, 283, 
                293, 307, 311, 313, 317, 331, 337, 347, 349, 353, 359,
                367, 373, 379, 383, 389, 397, 401, 409]

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(599, 500)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(0, 0, 611, 471))
        self.tabWidget.setObjectName("tabWidget")
        self.user_A = QtWidgets.QWidget()
        self.user_A.setObjectName("user_A")
        self.gridLayoutWidget_2 = QtWidgets.QWidget(self.user_A)
        self.gridLayoutWidget_2.setGeometry(QtCore.QRect(10, 10, 581, 421))
        self.gridLayoutWidget_2.setObjectName("gridLayoutWidget_2")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.gridLayoutWidget_2)
        self.gridLayout_3.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.label_17 = QtWidgets.QLabel(self.gridLayoutWidget_2)
        self.label_17.setObjectName("label_17")
        self.gridLayout_3.addWidget(self.label_17, 7, 2, 1, 1)
        self.label_18 = QtWidgets.QLabel(self.gridLayoutWidget_2)
        self.label_18.setObjectName("label_18")
        self.gridLayout_3.addWidget(self.label_18, 3, 2, 1, 1)
        self.enterText_A = QtWidgets.QTextEdit(self.gridLayoutWidget_2)
        self.enterText_A.setObjectName("enterText_A")
        self.gridLayout_3.addWidget(self.enterText_A, 0, 2, 1, 2)
        self.label_19 = QtWidgets.QLabel(self.gridLayoutWidget_2)
        self.label_19.setObjectName("label_19")
        self.gridLayout_3.addWidget(self.label_19, 5, 2, 1, 1)
        self.label_20 = QtWidgets.QLabel(self.gridLayoutWidget_2)
        self.label_20.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.label_20.setObjectName("label_20")
        self.gridLayout_3.addWidget(self.label_20, 0, 0, 1, 1)
        self.label_21 = QtWidgets.QLabel(self.gridLayoutWidget_2)
        self.label_21.setObjectName("label_21")
        self.gridLayout_3.addWidget(self.label_21, 2, 2, 1, 1)
        self.label_22 = QtWidgets.QLabel(self.gridLayoutWidget_2)
        self.label_22.setObjectName("label_22")
        self.gridLayout_3.addWidget(self.label_22, 4, 2, 1, 1)
        self.pub_key_n_A = QtWidgets.QLineEdit(self.gridLayoutWidget_2)
        self.pub_key_n_A.setObjectName("pub_key_n_A")
        self.gridLayout_3.addWidget(self.pub_key_n_A, 4, 3, 1, 1)
        self.label_23 = QtWidgets.QLabel(self.gridLayoutWidget_2)
        self.label_23.setObjectName("label_23")
        self.gridLayout_3.addWidget(self.label_23, 6, 2, 1, 1)
        self.pub_key_e_A = QtWidgets.QLineEdit(self.gridLayoutWidget_2)
        self.pub_key_e_A.setObjectName("pub_key_e_A")
        self.gridLayout_3.addWidget(self.pub_key_e_A, 3, 3, 1, 1)
        self.priv_key_s_A = QtWidgets.QLineEdit(self.gridLayoutWidget_2)
        self.priv_key_s_A.setObjectName("priv_key_s_A")
        self.gridLayout_3.addWidget(self.priv_key_s_A, 6, 3, 1, 1)
        self.priv_key_n_A = QtWidgets.QLineEdit(self.gridLayoutWidget_2)
        self.priv_key_n_A.setObjectName("priv_key_n_A")
        self.gridLayout_3.addWidget(self.priv_key_n_A, 7, 3, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_3.addItem(spacerItem, 0, 1, 1, 1)
        self.label_24 = QtWidgets.QLabel(self.gridLayoutWidget_2)
        self.label_24.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.label_24.setObjectName("label_24")
        self.gridLayout_3.addWidget(self.label_24, 1, 0, 1, 1)
        self.receivedText_A = QtWidgets.QTextEdit(self.gridLayoutWidget_2)
        self.receivedText_A.setReadOnly(True)
        self.receivedText_A.setObjectName("receivedText_A")
        self.gridLayout_3.addWidget(self.receivedText_A, 1, 2, 1, 2)
        self.encode_A = QtWidgets.QPushButton(self.gridLayoutWidget_2)
        self.encode_A.setObjectName("encode_A")
        self.gridLayout_3.addWidget(self.encode_A, 8, 3, 1, 1)
        self.send_A = QtWidgets.QPushButton(self.gridLayoutWidget_2)
        self.send_A.setObjectName("send_A")
        self.gridLayout_3.addWidget(self.send_A, 8, 0, 1, 3)
        self.tabWidget.addTab(self.user_A, "")
        self.user_B = QtWidgets.QWidget()
        self.user_B.setObjectName("user_B")
        self.gridLayoutWidget_3 = QtWidgets.QWidget(self.user_B)
        self.gridLayoutWidget_3.setGeometry(QtCore.QRect(10, 10, 581, 421))
        self.gridLayoutWidget_3.setObjectName("gridLayoutWidget_3")
        self.gridLayout_6 = QtWidgets.QGridLayout(self.gridLayoutWidget_3)
        self.gridLayout_6.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_6.setObjectName("gridLayout_6")
        self.label_41 = QtWidgets.QLabel(self.gridLayoutWidget_3)
        self.label_41.setObjectName("label_41")
        self.gridLayout_6.addWidget(self.label_41, 7, 2, 1, 1)
        self.label_42 = QtWidgets.QLabel(self.gridLayoutWidget_3)
        self.label_42.setObjectName("label_42")
        self.gridLayout_6.addWidget(self.label_42, 3, 2, 1, 1)
        self.enterText_B = QtWidgets.QTextEdit(self.gridLayoutWidget_3)
        self.enterText_B.setObjectName("enterText_B")
        self.gridLayout_6.addWidget(self.enterText_B, 0, 2, 1, 2)
        self.label_43 = QtWidgets.QLabel(self.gridLayoutWidget_3)
        self.label_43.setObjectName("label_43")
        self.gridLayout_6.addWidget(self.label_43, 5, 2, 1, 1)
        self.label_44 = QtWidgets.QLabel(self.gridLayoutWidget_3)
        self.label_44.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.label_44.setObjectName("label_44")
        self.gridLayout_6.addWidget(self.label_44, 0, 0, 1, 1)
        self.label_45 = QtWidgets.QLabel(self.gridLayoutWidget_3)
        self.label_45.setObjectName("label_45")
        self.gridLayout_6.addWidget(self.label_45, 2, 2, 1, 1)
        self.label_46 = QtWidgets.QLabel(self.gridLayoutWidget_3)
        self.label_46.setObjectName("label_46")
        self.gridLayout_6.addWidget(self.label_46, 4, 2, 1, 1)
        self.pub_key_n_B = QtWidgets.QLineEdit(self.gridLayoutWidget_3)
        self.pub_key_n_B.setObjectName("pub_key_n_B")
        self.gridLayout_6.addWidget(self.pub_key_n_B, 4, 3, 1, 1)
        self.label_47 = QtWidgets.QLabel(self.gridLayoutWidget_3)
        self.label_47.setObjectName("label_47")
        self.gridLayout_6.addWidget(self.label_47, 6, 2, 1, 1)
        self.pub_key_e_B = QtWidgets.QLineEdit(self.gridLayoutWidget_3)
        self.pub_key_e_B.setObjectName("pub_key_e_B")
        self.gridLayout_6.addWidget(self.pub_key_e_B, 3, 3, 1, 1)
        self.priv_key_s_B = QtWidgets.QLineEdit(self.gridLayoutWidget_3)
        self.priv_key_s_B.setObjectName("priv_key_s_B")
        self.gridLayout_6.addWidget(self.priv_key_s_B, 6, 3, 1, 1)
        self.priv_key_n_B = QtWidgets.QLineEdit(self.gridLayoutWidget_3)
        self.priv_key_n_B.setObjectName("priv_key_n_B")
        self.gridLayout_6.addWidget(self.priv_key_n_B, 7, 3, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_6.addItem(spacerItem1, 0, 1, 1, 1)
        self.label_48 = QtWidgets.QLabel(self.gridLayoutWidget_3)
        self.label_48.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.label_48.setObjectName("label_48")
        self.gridLayout_6.addWidget(self.label_48, 1, 0, 1, 1)
        self.receivedText_B = QtWidgets.QTextEdit(self.gridLayoutWidget_3)
        self.receivedText_B.setReadOnly(True)
        self.receivedText_B.setObjectName("receivedText_B")
        self.gridLayout_6.addWidget(self.receivedText_B, 1, 2, 1, 2)
        self.encode_B = QtWidgets.QPushButton(self.gridLayoutWidget_3)
        self.encode_B.setObjectName("encode_B")
        self.gridLayout_6.addWidget(self.encode_B, 8, 3, 1, 1)
        self.send_B = QtWidgets.QPushButton(self.gridLayoutWidget_3)
        self.send_B.setObjectName("send_B")
        self.gridLayout_6.addWidget(self.send_B, 8, 0, 1, 3)
        self.tabWidget.addTab(self.user_B, "")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 599, 22))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        MainWindow.setMenuBar(self.menubar)
        self.actionGenerate_public_and_private_keys = QtWidgets.QAction(MainWindow)
        self.actionGenerate_public_and_private_keys.setObjectName("actionGenerate_public_and_private_keys")
        self.actionAbout = QtWidgets.QAction(MainWindow)
        self.actionAbout.setObjectName("actionAbout")
        self.actionExit = QtWidgets.QAction(MainWindow)
        self.actionExit.setObjectName("actionExit")
        self.menuFile.addAction(self.actionGenerate_public_and_private_keys)
        self.menuFile.addAction(self.actionAbout)
        self.menuFile.addAction(self.actionExit)
        self.menubar.addAction(self.menuFile.menuAction())

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.actionClicked()

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "RSA Scrambler"))
        self.label_17.setText(_translate("MainWindow", "n ="))
        self.label_18.setText(_translate("MainWindow", "e ="))
        self.label_19.setText(_translate("MainWindow", "Приватные ключи:"))
        self.label_20.setText(_translate("MainWindow", "Отправить текст:"))
        self.label_21.setText(_translate("MainWindow", "Публичные ключи:"))
        self.label_22.setText(_translate("MainWindow", "n = "))
        self.label_23.setText(_translate("MainWindow", "s ="))
        self.label_24.setText(_translate("MainWindow", "Полученный текст:"))
        self.encode_A.setText(_translate("MainWindow", "Расшифровать"))
        self.send_A.setText(_translate("MainWindow", "Отправить"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.user_A), _translate("MainWindow", "Абонент А"))
        self.label_41.setText(_translate("MainWindow", "n ="))
        self.label_42.setText(_translate("MainWindow", "e ="))
        self.label_43.setText(_translate("MainWindow", "Приватные ключи:"))
        self.label_44.setText(_translate("MainWindow", "Отправить текст:"))
        self.label_45.setText(_translate("MainWindow", "Публичные ключи:"))
        self.label_46.setText(_translate("MainWindow", "n = "))
        self.label_47.setText(_translate("MainWindow", "s ="))
        self.label_48.setText(_translate("MainWindow", "Полученный текст:"))
        self.encode_B.setText(_translate("MainWindow", "Расшифровать"))
        self.send_B.setText(_translate("MainWindow", "Отправить"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.user_B), _translate("MainWindow", "Абонент Б"))
        self.menuFile.setTitle(_translate("MainWindow", "Файл"))
        self.actionGenerate_public_and_private_keys.setText(_translate("MainWindow", "Генерация ключей"))
        self.actionAbout.setText(_translate("MainWindow", "Об программе"))
        self.actionExit.setText(_translate("MainWindow", "Закрыть программу"))

    def actionClicked(self):
        self.actionGenerate_public_and_private_keys.triggered.connect(lambda: self.gen_keys())
        self.actionAbout.triggered.connect(lambda: self.aboutClicked())
        self.actionExit.triggered.connect(lambda: MainWindow.close())

        self.send_A.clicked.connect(lambda: self.send(False))
        self.send_B.clicked.connect(lambda: self.send(True))

        self.encode_A.clicked.connect(lambda: self.decode(False))
        self.encode_B.clicked.connect(lambda: self.decode(True))

    def aboutClicked(self):
        dlg = QtWidgets.QDialog()
        dlg.setWindowTitle("RSA Scrambler")
        dlg.resize(240, 120)
        lyt = QtWidgets.QGridLayout()
        dlg.setLayout(lyt)

        lbl_text = "Author: <a href=\"mailto:cergeu912@gmail.com\">Antsiferov Denis</a><br>"
        lbl_text += "Github: <a href=\"https://github.com/anonumka/rsa-python\">*click*</a><br>"
        lbl_text += "Version RSA Scrambler: v1.0<br> Version QT: " + QtCore.qVersion()
        lbl = QtWidgets.QLabel(lbl_text)
        lbl.setAlignment(QtCore.Qt.AlignTop)
        lbl.setFont(QtGui.QFont('Calibri', 12))

        exit_window = QtWidgets.QPushButton()
        exit_window.setObjectName("exit_window")
        exit_window.clicked.connect(lambda: dlg.close())
        exit_window.setText("Закрыть окно")

        lyt.addWidget(lbl)
        lyt.addWidget(exit_window)

        dlg.exec()

    def gen_keys(self):
        dlg = QtWidgets.QDialog()
        dlg.setWindowTitle("RSA Scrambler")
        dlg.resize(150, 100)
        lyt = QtWidgets.QGridLayout()
        dlg.setLayout(lyt)
        lbl = QtWidgets.QLabel("Введите количество десятичных знаков: ")
        byte = QtWidgets.QLineEdit()

        btnBox = QtWidgets.QDialogButtonBox(QtWidgets.QDialogButtonBox.Ok | QtWidgets.QDialogButtonBox.Cancel)
        btnBox.accepted.connect(dlg.accept)
        btnBox.rejected.connect(dlg.reject)
        
        lyt.addWidget(lbl)
        lyt.addWidget(byte)
        lyt.addWidget(btnBox)

        byte.setValidator(QtGui.QIntValidator())
        byte.setFocus()
        
        if (dlg.exec() != QtWidgets.QDialog.Accepted):
            return
        if (not byte.text().isdigit() or int(byte.text()) <= 0):
            box = QtWidgets.QMessageBox()
            box.setIcon(QtWidgets.QMessageBox.Critical)
            box.setWindowTitle("Ошибка")
            box.setText("Введите положительное число")
            box.exec()
            return

        (e, n, s) = genKeypair(int(int(byte.text())/2))

        ui.pub_key_n_B.setText(str(n))
        ui.pub_key_e_B.setText(str(e))
        ui.priv_key_s_A.setText(str(s))
        ui.priv_key_n_A.setText(str(n))

        (e, n, s) = genKeypair(int(int(byte.text())/2))

        ui.pub_key_n_A.setText(str(n))
        ui.pub_key_e_A.setText(str(e))
        ui.priv_key_s_B.setText(str(s))
        ui.priv_key_n_B.setText(str(n))



    def send(self, user):
        if (not user):
            #print("user A")
            if ((len(ui.pub_key_n_A.text())) == 0) or (len(ui.pub_key_e_A.text()) == 0):
                box = QtWidgets.QMessageBox()
                box.setIcon(QtWidgets.QMessageBox.Critical)
                box.setWindowTitle("Ошибка")
                box.setText("Поле публичных ключей пустые")
                box.exec()
                return
            
            enterText = str(ui.enterText_A.toPlainText())
            n = int(ui.pub_key_n_A.text())
            
        else:
            #print ("user B")
            if (len(ui.pub_key_n_B.text()) == 0) or (len(ui.pub_key_e_B.text()) == 0):
                box = QtWidgets.QMessageBox()
                box.setIcon(QtWidgets.QMessageBox.Critical)
                box.setWindowTitle("Ошибка")
                box.setText("Поле публичных ключей пустые")
                box.exec()
                return

            
            enterText = str(ui.enterText_B.toPlainText())
            n = int(ui.pub_key_n_B.text())
            
        encrypted_text = [pow(ord(char), e, n) for char in enterText]

        if (not user):
            ui.receivedText_B.setText(str(encrypted_text))
        else:
            ui.receivedText_A.setText(str(encrypted_text))

        

    def decode(self, user):
        if (not user):
            #print("user A")
            if ((len(ui.priv_key_n_A.text()) == 0) or (len(ui.priv_key_s_A.text()) == 0)):
                box = QtWidgets.QMessageBox()
                box.setIcon(QtWidgets.QMessageBox.Critical)
                box.setWindowTitle("Ошибка")
                box.setText("Поле приватных ключей пустые")
                box.exec()
                return

            ciphertext = str(ui.receivedText_A.toPlainText())
            s = int(ui.priv_key_s_A.text())
            n = int(ui.priv_key_n_A.text())
            
        else:
            #print ("user B")
            if ((len(ui.priv_key_n_B.text()) == 0) or (len(ui.priv_key_s_B.text()) == 0)):
                box = QtWidgets.QMessageBox()
                box.setIcon(QtWidgets.QMessageBox.Critical)
                box.setWindowTitle("Ошибка")
                box.setText("Поле приватных ключей пустые")
                box.exec()
                return

            ciphertext = str(ui.receivedText_B.toPlainText())
            s = int(ui.priv_key_s_B.text())
            n = int(ui.priv_key_n_B.text())
            
        ciphertext = ciphertext.replace('[', '')
        ciphertext = ciphertext.replace(']', '')
        ciphertext = ciphertext.replace(',', '')
        ciphertext = ciphertext.split()
        
        for i in range(len(ciphertext)):
            ciphertext[i] = int(ciphertext[i])

        plaintext = [chr(pow(char, s, n)) for char in ciphertext]

        plaintext = "".join(plaintext)

        if (not user):
            ui.enterText_A.setText(str(plaintext))
        else:
            ui.enterText_B.setText(str(plaintext))   

def gcdExtended(a, b):  
    if b == 0:
        return a, 1, 0
    else:
        d, x, y = gcdExtended(b, a % b)
        return d, y, x - y * (a // b)

def multInvMod(num, mod):
    gcd,x,y = gcdExtended(num, mod)
    if x > 0:
        return x
    else:
        return mod+x

def nBitRandom(n):
    return int(random.randrange(10**n+1, 10**(n+1)))

def isPrime(n):
    while True: 
        prime_candidate = nBitRandom(n)  
        for divisor in first_primes:  
            if prime_candidate % divisor == 0 and divisor**2 <= prime_candidate: 
                break
            return prime_candidate 

def isPrimeMillerRabin(mrc):
    max_divisions_by_two = 0
    ec = mrc-1
    while ec % 2 == 0: 
        ec >>= 1
        max_divisions_by_two += 1

    def trialComposite(round_tester): 
        if pow(round_tester, ec, mrc) == 1: 
            return False
        for i in range(max_divisions_by_two): 
            if pow(round_tester, 2**i * ec, mrc) == mrc-1: 
                return False
        return True

    trials_amount = 20 
    for i in range(trials_amount): 
        round_tester = random.randrange(2, mrc) 
        if trialComposite(round_tester): 
            return False
    return True

def genPrime(bits):
    while True:
        p = isPrime(bits)
        if not isPrimeMillerRabin(p): 
            continue
        return p

def genKeypair(bits):
    n = 0
    p = 0
    q = 0
    while ((len(str(n)) != bits*2) and (p == q)):
        p = genPrime(bits)
        q = genPrime(bits)
        n = p*q
    phi = (p-1) * (q-1)

    s = multInvMod(e, phi)
    return (e, n, s)

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

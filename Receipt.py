'''
___________________________________________________________

Aufgabe:            Bibliothek der Funktionen

Author:             Egzon Bytyqi

zuletzt geändert:   11.11.22

___________________________________________________________

'''



from PyQt5 import QtWidgets, uic, QtCore
from PyQt5.QtWidgets import QMessageBox, QTableWidgetItem
from datetime import datetime
import csv
import re
import ReceiptBibliothek as RBT



# ___________________________________________________________
# ___________________________________________________________
class Receipt(QtWidgets.QDialog):
    def __init__(self):
        super(Receipt, self).__init__()

        uic.loadUi('RechnungDesign.ui', self)



    # ___________________________________________________________
    # ___________________________________________________________
        # Button
        self.copyAdressBtn.clicked.connect(self.adresscopy) #funktioniert
        self.newAdressBtn.clicked.connect(self.deleteAdress) #funktioniert
        self.printBtn.clicked.connect(self.print) 
        self.settingBtn.clicked.connect(self.setting)
        self.resetBtn.clicked.connect(self.save) #funktioniert
        self.addProductBtn.clicked.connect(self.addProduct)
        self.removeProductBtn.clicked.connect(self.deleteProduct)
        self.clearListBtn.clicked.connect(self.clearList)
        self.extraAddBtn.clicked.connect(self.extraIngredients)
        self.deliveryAddBtn.clicked.connect(self.removePlus)



    # ___________________________________________________________
    # ___________________________________________________________
        #TODO Finde Heraus was das ist.
        self.productAddLEdit.returnPressed.connect(self.addProduct)



    # ___________________________________________________________
    # ___________________________________________________________
        timerTime = QtCore.QTimer(self)
        timerTime.start(1000)
        self.time.setText(datetime.now().strftime('%H:%M:%S'))
        timerTime.timeout.connect(self.updateDate)
        self.date.setText(datetime.now().strftime('%d.%m.%Y'))


        sumAll = []
        print(sumAll)

    # ___________________________________________________________
    # ___________________________________________________________
        with open('archive.csv') as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=';')
            currentNumber = sum(1 for row in csv_reader) + 1
            self.orderNumberLabel.setText("Bestell Nr.: " + str(currentNumber))
      


    # ___________________________________________________________
    # ___________________________________________________________
    def updateDate(self):
        '''Die Zeit wird immer aktualisiert'''

        date = QtCore.QDateTime.currentDateTime()
        self.time.setText(date.toString("hh:mm:ss"))



    # ___________________________________________________________
    # ___________________________________________________________
    def event(self, event):
        '''Den Tasten werden Befehle gegeben.'''

        if event.type() == QtCore.QEvent.KeyPress:
            if event.key() in (QtCore.Qt.Key_Return, QtCore.Qt.Key_Enter):
                self.focusNextPrevChild(True)
        return super().event(event)



    # ___________________________________________________________
    # ___________________________________________________________
    def connectProduct(self):

        self.productAddLEdit.alignment()



    # ___________________________________________________________
    # ___________________________________________________________
    def adresscopy(self):
        '''Fügt die kopierte Adresse in die Adresszeile ein.'''

        self.adressTxt.clear()
        self.adressTxt.paste()



    # ___________________________________________________________
    # ___________________________________________________________
    def deleteAdress(self):
        '''Die jetzige Adresse wird gelöscht.'''

        self.adressTxt.clear()



    # ___________________________________________________________
    # ___________________________________________________________
    def print(self):
        pass
        
        

    # ___________________________________________________________
    # ___________________________________________________________
    def setting(self):
        pass



    # ___________________________________________________________
    # ___________________________________________________________
    def save(self):
        '''Speichert denn letzten Eintrag und bereitet alles für den nächsten Eintrag.'''
        
        adress = self.adressTxt.toPlainText()
        adress = adress.replace('\n',", ")
        adress = adress.replace('\t',", ")
        adress = re.sub(' +', ' ', adress)
        

        with open('archive.csv') as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=';')
            currentNumber = sum(1 for row in csv_reader) + 1
            ncurrentNumber = currentNumber + 1
            self.orderNumberLabel.setText("Bestell Nr.: " + str(ncurrentNumber))
            print(ncurrentNumber)

        now = datetime.now()
        dt_string = now.strftime("%d/%m/%Y %H:%M:%S")

        with open('archive.csv', 'a', newline='', encoding='utf8') as archive_file:
            archive_writer = csv.writer(archive_file, delimiter=';', quotechar='"', quoting=csv.QUOTE_MINIMAL)
            archive_writer.writerow([currentNumber, adress, dt_string])
            
        self.adressTxt.clear()

        self.tableWidget.clearContents()
        self.tableWidget.setRowCount(0)
               



    # ___________________________________________________________
    # ___________________________________________________________
    def addProduct(self):
        '''Produkt und Betrag wird in die Listwidget eingetragen.'''
        
        quantity = self.quantityProductLEdit.text() 
        product = self.productAddLEdit.text()

        with open('meny.csv') as file:
            for line in file:
                list = line.strip().split(';')
                
                if product == '' or quantity == '':
                    self.warning('Achtung!', 'Bitte ein Produkt eingeben.')
                    break


                elif quantity.isspace() or product.isspace():
                    self.warning('Achtung!','Bitte nicht nur Leerzeichen verwenden.')

                
                elif product == list[0]:
                    floatlist = float(list[2])
                    floatquantity = float(quantity)
                    costProduct = floatquantity * floatlist
                    
                    header = self.tableWidget.horizontalHeader()
                    header.setSectionResizeMode(QtWidgets.QHeaderView.Stretch)
                    header.setSectionResizeMode(1, QtWidgets.QHeaderView.ResizeToContents)
                    header.setSectionResizeMode(2, QtWidgets.QHeaderView.ResizeToContents)
                     
                    rowPosition = self.tableWidget.rowCount()
                    self.tableWidget.insertRow(rowPosition)
                    
                    numcols = self.tableWidget.columnCount()
                    numrows = self.tableWidget.rowCount()
                    self.tableWidget.setRowCount(numrows)
                    self.tableWidget.setColumnCount(numcols)
                    self.tableWidget.setItem(numrows -1,0, QTableWidgetItem(quantity + ' ' + list[1]))
                    self.tableWidget.setItem(numrows -1,1, QTableWidgetItem(list[2]))
                    self.tableWidget.setItem(numrows -1,2, QTableWidgetItem(str(costProduct)))
                    print(costProduct)

                    global sumAll
                    sumAll.append(costProduct)
                self.quantityProductLEdit.clear()
                self.productAddLEdit.clear()
        
        
        if product == '32':
            self.menyNormal() 

        if product == '232':
            self.menyLarge()



    # ___________________________________________________________
    # ___________________________________________________________
    def menyNormal(): 
        pass
        
        
        
    # ___________________________________________________________
    # ___________________________________________________________
    def menyLarge():
        pass



    # ___________________________________________________________
    # ___________________________________________________________
    def deleteProduct(self):
        '''Der ausgewählte Produkt wird aus der ListWidget gelöscht.'''

        productList = self.tableWidget.currentRow() 
        self.tableWidget.removeRow(productList)



        

    # ___________________________________________________________
    # ___________________________________________________________
    def clearList(self):
        '''Die tableListWidget wird geleert.'''

        self.tableWidget.clearContents()
        self.tableWidget.setRowCount(0)
        


    # ___________________________________________________________
    # ___________________________________________________________
    def extraIngredients(self):
        pass



    # ___________________________________________________________
    # ___________________________________________________________
    def removePlus(self):
        pass

    

    # ___________________________________________________________
    # ___________________________________________________________
    def warning(self, title, text):
        
        box = QMessageBox()
        box.setIcon(QMessageBox.Warning)
        box.setWindowTitle(title)
        box.setText(text)
        box.setStandardButtons(QMessageBox.Yes)
        buttonMade = box.button(QMessageBox.Yes)
        buttonMade.setText('OK')
        box.exec_()



    # ___________________________________________________________
    # ___________________________________________________________
    def clickedConnect(self, i):

        i.clear()
        i.alignment()



    # ___________________________________________________________
    # ___________________________________________________________
if __name__ == '__main__':
    app = QtWidgets.QApplication([])
    win = Receipt()
    win.show()
    app.exec()
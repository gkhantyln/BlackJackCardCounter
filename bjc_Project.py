from PyQt5 import QtWidgets
from PyQt5.QtCore import *
from bjc_Theme import Ui_MainWindow
from bjc_BasicPage import Ui_BasicPage

import keyboard

from time import sleep

hilo_Stm = {'2': 1,'3': 1,'4': 1,'5': 1,'6': 1, '7': 0,'8': 0,'9': 0,'10 - J Q K A': -1,'A': -1}
hiloOpt2_Stm = {'2': 1,'3': 1,'4': 2, '5': 2,'6': 1,'7': 1,'8': 0,'9': 0,'10': -2,'11': 0}
ustonApc_Stm = {'2': 1,'3': 1,'4': 1,'5': 1,'6': 1, '7': 0,'8': 0,'9': 0,'10': -1,'11': -1}
zen_Stm = {'2': 1, '3': 1,'4': 2,'5': 2,'6': 2,'7': 1,'8': 0,'9': 0,'10': -2,'11': -1}

#omega2_Stm = {'2': 1,'3': 1, '4': 2,'5': 2, '6': 2,'7': 1,'8': 0,'9': -1,'10': -2,'11': 0}

high = 0.0
oneDeck = 52.0
decksDeger = '8'

class Template_main(QtWidgets.QMainWindow,Ui_MainWindow):

        global hilo_Stm
        global hiloOpt2_Stm
        global ustonApc_Stm
        global zen_Stm
        global high
        global oneDeck
        global decksDeger

        def __init__(self):
                super().__init__()
                self.setWindowFlags(Qt.WindowStaysOnTopHint)
                self.setFixedSize(271, 379)
                self.setupUi(self)
                self.show()

                self.btn_Stop.setEnabled(False) #Stop Butonu Deaktif
                self.btn_Stop.setStyleSheet("color: grey;")
                self.btn_highCards.setEnabled(False)
                for i in range(1, 10):
                        card_btn = getattr(self, f"btn_Card_{i}")
                        card_btn.setEnabled(False)

                self.btn_Basic.setEnabled(False)
                self.btn_Reset.setEnabled(False)
                
                self.btn_Start.clicked.connect(self.StartConnectButton)
                self.btn_Stop.clicked.connect(self.StopConnectButton)
                self.btn_Basic.clicked.connect(self.BasicConnectButton)

                #self.cb_Strategy.currentIndexChanged.connect(self.StrategyType)

                self.btn_highCards.clicked.connect(self.cardButtonClicked)
                for i in range(1, 10):
                        card_btn = getattr(self, f"btn_Card_{i}")
                        card_btn.clicked.connect(self.cardButtonClicked)

                
                self.btn_Basic.clicked.connect(self.BasicClick)
                self.btn_Reset.clicked.connect(self.ResetClick)
                self.btn_Reset.setStyleSheet("color: grey;")

                self.txt_Decks.setText(decksDeger)

        def BasicConnectButton(self):
                #self.setWindowFlags(Qt.WindowStaysOnTopHint)
                self.window = QtWidgets.QMainWindow()
                self.ui = Ui_BasicPage()
                self.ui.setupUi(self.window)
                self.window.show()


        def StartConnectButton(self):
                
                 try:
                         self.btn_highCards.setEnabled(True)
                         for i in range(1, 10):
                                 card_btn = getattr(self, f"btn_Card_{i}")
                                 card_btn.setEnabled(True)

                         
                         self.btn_Basic.setEnabled(True)
                         self.btn_Reset.setEnabled(True)
                         self.btn_Reset.setStyleSheet("color: rgb(103, 0, 1);")
                         self.btn_Start.setEnabled(False)
                         self.btn_Start.setStyleSheet("color: grey;")
                         self.btn_Stop.setEnabled(True)
                         self.btn_Stop.setStyleSheet("color: rgb(103, 0, 1);")

                         self.txt_Decks.setEnabled(False)
                         self.cb_Strategy.setEnabled(False)
                         
                         decksDeger = int(self.txt_Decks.toPlainText())
                         totalCard = round(int(decksDeger) * oneDeck)
                         #self.txt_totalCard.clear()
                         totalCards = self.txt_totalCard.setText(format(float(totalCard),'.15g'))

                         cbValue = self.cb_Strategy.currentIndex()

                         if cbValue == 0:
                                 self.btn_Card_1.setEnabled(False)
                                 self.btn_Card_1.setStyleSheet("color: grey;")
                                 self.txt_lowCard.setText('0')
                                 self.txt_highCard.setText('0')
                                 self.txt_middleCard.setText('0')
                         else:
                                self.btn_Card_1.setStyleSheet("color: rgb(255, 0, 0);")
                 except:
                         pass

        def StopConnectButton(self):

                 try:

                         self.btn_Start.setEnabled(True)
                         self.btn_Start.setStyleSheet("color: rgb(0, 184, 0);")
                         self.btn_Stop.setEnabled(False)
                         self.btn_Stop.setStyleSheet("color: grey;")
                         
                         self.txt_Decks.setEnabled(True)
                         self.cb_Strategy.setEnabled(True)
                         
                         self.btn_highCards.setEnabled(False)

                         for i in range(1, 10):
                                 card_btn = getattr(self, f"btn_Card_{i}")
                                 card_btn.setEnabled(False)
                         
                         self.btn_Basic.setEnabled(False)
                         self.btn_Reset.setEnabled(False)
                         self.btn_Reset.setStyleSheet("color: grey;")

                         self.txt_totalCard.clear()
                         self.txt_lowCard.clear()
                         self.txt_highCard.clear()
                         self.txt_middleCard.clear()
                        
                         self.txt_TrueCount.clear()
                         self.txt_RunCount.clear()

                 except:
                         pass
        
        def cardButtonClicked(self):

                running_count = 0
                high_card = 0
                low_card = 0
                middle_card = 0
                
                button = self.sender()

                cbValue = self.cb_Strategy.currentIndex() #currentText değeri almak combo

                dt = [] #butontoplam

                if button.text() == 'A':
                        
                        if cbValue == 0: #combo değeri hi-lo

                                btnValue = hilo_Stm['A']

                                totalDeger = int(self.txt_totalCard.toPlainText()) #Toplam Kart Değeri

                                totalDeger -= 1

                                if totalDeger == 0:
                                        self.ResetClick()
                                else:
                                        
                                        decksDeger = int(self.txt_Decks.toPlainText()) #8
                                        totalCards = self.txt_totalCard.setText(format(float(totalDeger),'.15g'))

                                        runningCard = self.txt_RunCount.toPlainText()
                                        
                                        if runningCard == "":
                                                runningCard = btnValue #0
                                        else:
                                                runningCard = int(self.txt_RunCount.toPlainText()) + btnValue
                                                 
                                        runningCard = self.txt_RunCount.setText(format(float(runningCard),'.15g'))
                                        runningCard = int(self.txt_RunCount.toPlainText())

                                        true_count = round(runningCard/(totalDeger/oneDeck)) #True Count 
                                        trueCardNo = self.txt_TrueCount.setText(format(float(true_count),'.15g'))

                        elif cbValue == 1:
                                print('DEMO')
                        elif cbValue == 2:
                                print('DEMO')
                        elif cbValue == 3:
                                print('DEMO')
                        else:
                                print('DEMO')

                elif button.text() == '10 - J Q K A':
                        
                        if cbValue == 0: #combo değeri hi-lo
                                high_card = int(self.txt_highCard.toPlainText())
                                high_card +=1
                                self.txt_highCard.setText(str(high_card))
                                
                                btnValue = hilo_Stm['10 - J Q K A']

                                totalDeger = int(self.txt_totalCard.toPlainText()) #Toplam Kart Değeri

                                totalDeger -= 1

                                if totalDeger == 0:
                                        self.ResetClick()
                                else:
                                        
                                        decksDeger = int(self.txt_Decks.toPlainText()) #8
                                        totalCards = self.txt_totalCard.setText(format(float(totalDeger),'.15g'))

                                        runningCard = self.txt_RunCount.toPlainText()
                                        
                                        if runningCard == "":
                                                runningCard = btnValue #0
                                        else:
                                                runningCard = int(self.txt_RunCount.toPlainText()) + btnValue
                                                 
                                        runningCard = self.txt_RunCount.setText(format(float(runningCard),'.15g'))
                                        runningCard = int(self.txt_RunCount.toPlainText())
                                        true_count = round(runningCard/(totalDeger/oneDeck)) #True Count 
                                        trueCardNo = self.txt_TrueCount.setText(format(float(true_count),'.15g'))

                        elif cbValue == 1:
                                print('DEMO')
                        elif cbValue == 2:
                                print('DEMO')
                        elif cbValue == 3:
                                print('DEMO')
                        else:
                                print('DEMO')

                elif button.text() == '2':
                        

                        if cbValue == 0:

                                low_card = int(self.txt_lowCard.toPlainText())
                                low_card +=1
                                self.txt_lowCard.setText(str(low_card))

                                btnValue = hilo_Stm['2']

                                totalDeger = int(self.txt_totalCard.toPlainText()) #Toplam Kart Değeri

                                totalDeger -= 1

                                if totalDeger == 0:
                                        self.ResetClick()
                                else:
                                        
                                        decksDeger = int(self.txt_Decks.toPlainText()) #8
                                        totalCards = self.txt_totalCard.setText(format(float(totalDeger),'.15g'))

                                        runningCard = self.txt_RunCount.toPlainText()
                                        
                                        if runningCard == "":
                                                runningCard = btnValue #0
                                        else:
                                                runningCard = int(self.txt_RunCount.toPlainText()) + btnValue
                                                 
                                        runningCard = self.txt_RunCount.setText(format(float(runningCard),'.15g'))
                                        runningCard = int(self.txt_RunCount.toPlainText())

                                        true_count = round(runningCard/(totalDeger/oneDeck)) #True Count 
                                        trueCardNo = self.txt_TrueCount.setText(format(float(true_count),'.15g'))

                        elif cbValue == 1:
                                print('DEMO')
                        elif cbValue == 2:
                                print('DEMO')
                        elif cbValue == 3:
                                print('DEMO')
                        else:
                                print('DEMO')
                                
                elif button.text() == '3':
                       
                        
                        if cbValue == 0:

                                low_card = int(self.txt_lowCard.toPlainText())
                                low_card +=1
                                self.txt_lowCard.setText(str(low_card))

                                btnValue = hilo_Stm['3']

                                totalDeger = int(self.txt_totalCard.toPlainText()) #Toplam Kart Değeri

                                totalDeger -= 1

                                if totalDeger == 0:
                                        self.ResetClick()
                                else:
                                        
                                        decksDeger = int(self.txt_Decks.toPlainText()) #8
                                        totalCards = self.txt_totalCard.setText(format(float(totalDeger),'.15g'))

                                        runningCard = self.txt_RunCount.toPlainText()
                                        
                                        if runningCard == "":
                                                runningCard = btnValue #0
                                        else:
                                                runningCard = int(self.txt_RunCount.toPlainText()) + btnValue
                                                 
                                        runningCard = self.txt_RunCount.setText(format(float(runningCard),'.15g'))
                                        runningCard = int(self.txt_RunCount.toPlainText())

                                        true_count = round(runningCard/(totalDeger/oneDeck)) #True Count 
                                        trueCardNo = self.txt_TrueCount.setText(format(float(true_count),'.15g'))

                        elif cbValue == 1:
                                print('DEMO')
                        elif cbValue == 2:
                                print('DEMO')
                        elif cbValue == 3:
                                print('DEMO')
                        else:
                                print('DEMO')
                                
                elif button.text() == '4':
                        
                        
                        if cbValue == 0:

                                low_card = int(self.txt_lowCard.toPlainText())
                                low_card +=1
                                self.txt_lowCard.setText(str(low_card))

                                btnValue = hilo_Stm['4']

                                totalDeger = int(self.txt_totalCard.toPlainText()) #Toplam Kart Değeri

                                totalDeger -= 1

                                if totalDeger == 0:
                                        self.ResetClick()
                                else:
                                        
                                        decksDeger = int(self.txt_Decks.toPlainText()) #8
                                        totalCards = self.txt_totalCard.setText(format(float(totalDeger),'.15g'))

                                        runningCard = self.txt_RunCount.toPlainText()
                                        
                                        if runningCard == "":
                                                runningCard = btnValue #0
                                        else:
                                                runningCard = int(self.txt_RunCount.toPlainText()) + btnValue
                                                 
                                        runningCard = self.txt_RunCount.setText(format(float(runningCard),'.15g'))
                                        runningCard = int(self.txt_RunCount.toPlainText())

                                        true_count = round(runningCard/(totalDeger/oneDeck)) #True Count 
                                        trueCardNo = self.txt_TrueCount.setText(format(float(true_count),'.15g'))

                        elif cbValue == 1:
                                print('DEMO')
                        elif cbValue == 2:
                                print('DEMO')
                        elif cbValue == 3:
                                print('DEMO')
                        else:
                                print('DEMO')
                                
                elif button.text() == '5':
                        
                        if cbValue == 0:

                                low_card = int(self.txt_lowCard.toPlainText())
                                low_card +=1
                                self.txt_lowCard.setText(str(low_card))


                                btnValue = hilo_Stm['5']

                                totalDeger = int(self.txt_totalCard.toPlainText()) #Toplam Kart Değeri

                                totalDeger -= 1

                                if totalDeger == 0:
                                        self.ResetClick()
                                else:
                                        
                                        decksDeger = int(self.txt_Decks.toPlainText()) #8
                                        totalCards = self.txt_totalCard.setText(format(float(totalDeger),'.15g'))

                                        runningCard = self.txt_RunCount.toPlainText()
                                        
                                        if runningCard == "":
                                                runningCard = btnValue #0
                                        else:
                                                runningCard = int(self.txt_RunCount.toPlainText()) + btnValue
                                                 
                                        runningCard = self.txt_RunCount.setText(format(float(runningCard),'.15g'))
                                        runningCard = int(self.txt_RunCount.toPlainText())

                                        true_count = round(runningCard/(totalDeger/oneDeck)) #True Count 
                                        trueCardNo = self.txt_TrueCount.setText(format(float(true_count),'.15g'))

                        elif cbValue == 1:
                                print('DEMO')
                        elif cbValue == 2:
                                print('DEMO')
                        elif cbValue == 3:
                                print('DEMO')
                        else:
                                print('DEMO')
                elif button.text() == '6':
                        
                        if cbValue == 0:

                                low_card = int(self.txt_lowCard.toPlainText())
                                low_card +=1
                                self.txt_lowCard.setText(str(low_card))


                                btnValue = hilo_Stm['6']

                                totalDeger = int(self.txt_totalCard.toPlainText()) #Toplam Kart Değeri

                                totalDeger -= 1

                                if totalDeger == 0:
                                        self.ResetClick()
                                else:
                                        
                                        decksDeger = int(self.txt_Decks.toPlainText()) #8
                                        totalCards = self.txt_totalCard.setText(format(float(totalDeger),'.15g'))

                                        runningCard = self.txt_RunCount.toPlainText()
                                        
                                        if runningCard == "":
                                                runningCard = btnValue #0
                                        else:
                                                runningCard = int(self.txt_RunCount.toPlainText()) + btnValue
                                                 
                                        runningCard = self.txt_RunCount.setText(format(float(runningCard),'.15g'))
                                        runningCard = int(self.txt_RunCount.toPlainText())

                                        true_count = round(runningCard/(totalDeger/oneDeck)) #True Count 
                                        trueCardNo = self.txt_TrueCount.setText(format(float(true_count),'.15g'))

                        elif cbValue == 1:
                                print('DEMO')
                        elif cbValue == 2:
                                print('DEMO')
                        elif cbValue == 3:
                                print('DEMO')
                        else:
                                print('DEMO')
                                
                elif button.text() == '7':
                        
                        if cbValue == 0:
                        
                                middle_card = int(self.txt_middleCard.toPlainText())
                                middle_card +=1
                                self.txt_middleCard.setText(str(middle_card))

                                btnValue = hilo_Stm['7']

                                totalDeger = int(self.txt_totalCard.toPlainText()) #Toplam Kart Değeri

                                totalDeger -= 1

                                if totalDeger == 0:
                                        self.ResetClick()
                                else:
                                        
                                        decksDeger = int(self.txt_Decks.toPlainText()) #8
                                        totalCards = self.txt_totalCard.setText(format(float(totalDeger),'.15g'))

                                        runningCard = self.txt_RunCount.toPlainText()
                                        
                                        if runningCard == "":
                                                runningCard = btnValue #0
                                        else:
                                                runningCard = int(self.txt_RunCount.toPlainText()) + btnValue
                                                 
                                        runningCard = self.txt_RunCount.setText(format(float(runningCard),'.15g'))
                                        runningCard = int(self.txt_RunCount.toPlainText())

                                        true_count = round(runningCard/(totalDeger/oneDeck)) #True Count 
                                        trueCardNo = self.txt_TrueCount.setText(format(float(true_count),'.15g'))

                        elif cbValue == 1:
                                print('DEMO')
                        elif cbValue == 2:
                                print('DEMO')
                        elif cbValue == 3:
                                print('DEMO')
                        else:
                                print('DEMO')
                                
                elif button.text() == '8':
                        
                        if cbValue == 0:
                        
                                middle_card = int(self.txt_middleCard.toPlainText())
                                middle_card +=1
                                self.txt_middleCard.setText(str(middle_card))

                                btnValue = hilo_Stm['8']

                                totalDeger = int(self.txt_totalCard.toPlainText()) #Toplam Kart Değeri

                                totalDeger -= 1

                                if totalDeger == 0:
                                        self.ResetClick()
                                else:
                                        
                                        decksDeger = int(self.txt_Decks.toPlainText()) #8
                                        totalCards = self.txt_totalCard.setText(format(float(totalDeger),'.15g'))

                                        runningCard = self.txt_RunCount.toPlainText()
                                        
                                        if runningCard == "":
                                                runningCard = btnValue #0
                                        else:
                                                runningCard = int(self.txt_RunCount.toPlainText()) + btnValue
                                                 
                                        runningCard = self.txt_RunCount.setText(format(float(runningCard),'.15g'))
                                        runningCard = int(self.txt_RunCount.toPlainText())

                                        true_count = round(runningCard/(totalDeger/oneDeck)) #True Count 
                                        trueCardNo = self.txt_TrueCount.setText(format(float(true_count),'.15g'))

                        elif cbValue == 1:
                                print('DEMO')
                        elif cbValue == 2:
                                print('DEMO')
                        elif cbValue == 3:
                                print('DEMO')
                        else:
                                print('DEMO')
                                
                elif button.text() == '9':
                        
                        if cbValue == 0:
                        
                                middle_card = int(self.txt_middleCard.toPlainText())
                                middle_card +=1
                                self.txt_middleCard.setText(str(middle_card))

                                btnValue = hilo_Stm['9']

                                totalDeger = int(self.txt_totalCard.toPlainText()) #Toplam Kart Değeri

                                totalDeger -= 1

                                if totalDeger == 0:
                                        self.ResetClick()
                                else:
                                        
                                        decksDeger = int(self.txt_Decks.toPlainText()) #8
                                        totalCards = self.txt_totalCard.setText(format(float(totalDeger),'.15g'))

                                        runningCard = self.txt_RunCount.toPlainText()
                                        
                                        if runningCard == "":
                                                runningCard = btnValue #0
                                        else:
                                                runningCard = int(self.txt_RunCount.toPlainText()) + btnValue
                                                 
                                        runningCard = self.txt_RunCount.setText(format(float(runningCard),'.15g'))
                                        runningCard = int(self.txt_RunCount.toPlainText())

                                        true_count = round(runningCard/(totalDeger/oneDeck)) #True Count 
                                        trueCardNo = self.txt_TrueCount.setText(format(float(true_count),'.15g'))

                        elif cbValue == 1:
                                print('DEMO')
                        elif cbValue == 2:
                                print('DEMO')
                        elif cbValue == 3:
                                print('DEMO')
                        else:
                                print('DEMO')
                        
                else:
                        pass

## setText

        def BasicClick(self):
                pass
        def ResetClick(self):
                
                self.txt_lowCard.clear()
                self.txt_highCard.clear()
                self.txt_middleCard.clear()
                
                self.txt_TrueCount.clear()
                self.txt_RunCount.clear()

                decksDeger = int(self.txt_Decks.toPlainText()) #Deste Değeri
                totalCard = round(decksDeger * oneDeck)
                self.txt_totalCard.clear()
                self.txt_totalCard.setText(format(float(totalCard),'.15g'))
                
                self.txt_lowCard.setText('0')
                self.txt_highCard.setText('0')
                self.txt_middleCard.setText('0')

         

          
        
        

                

        

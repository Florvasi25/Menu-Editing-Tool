from PySide6.QtWidgets import QFileDialog, QMessageBox, QMainWindow
from jsonSection import jsonSection
from VouchersAndAlcohol import VouchersAndAlcohol
from parsejson import parsejson
#from CocaColaUpdates import CocaColaUpdates
from ui_form import Ui_MainWindow
import json

datos = dict()
datos = None

class MainWindow(QMainWindow):

    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.setWindowTitle('Menu Editing Tool 2.3.2')
        self.tagToRemove = []
        self.itemTagsRemove = []
        #self.setWindowIcon(QIcon('images\iconoFlipdish.png'))
        #button ejemplo
        self.archivo = ""



        #self.ui.stackedWidget.hide()
        self.ui.PARSEBUTTON.clicked.connect(self.clickedParse_JSON)
        self.ui.PARSEBUTTON.clicked.connect(self.clickedPARSEBUTTON)
        self.ui.TAXBUTTON.clicked.connect(self.clickedTAXBUTTON)
        self.ui.PRICEBUTTON.clicked.connect(self.clickedPRICEBUTTON)
        self.ui.DRINKSBUTTON.clicked.connect(self.clickedDRINKSBUTTON)
        self.ui.ADDTAGSBUTTON.clicked.connect(self.clickedADDTAGSBUTTON)
        self.ui.REMOVETAGSBUTTON.clicked.connect(self.clickedREMOVETAGSBUTTON)
        self.ui.ADDSNOOZETAGSBUTTON.clicked.connect(self.clickedADDSNOOZETAGSBUTTON)
        self.ui.TAXABLEYES.clicked.connect(self.clickedTAXABLEYES)
        self.ui.actionLoad_Json.triggered.connect(self.clickedLoad)
        self.ui.actionSave_Json.triggered.connect(self.clickedSave)
        self.ui.actionExit.triggered.connect(self.close)

        self.ui.actionRemove_Tax_from_All_Sections.triggered.connect(self.clickedRemoveTax)
        self.ui.actionApply_Tax_to_All_Sections.triggered.connect(self.clickedAllSections)
        #self.ui.actionCoca_ColaChecker.triggered.connect(self.clickedCocaColaChecker)
        self.ui.actionParse_JSON.triggered.connect(self.clickedParse_JSON)

        global sectionName
        sectionName = list()

        self.ui.taxImpSec.clicked.connect(self.clickedSectionImp)
        self.ui.priceImpSec.clicked.connect(self.clickedSectionImp2)
        self.ui.implementVASM.clicked.connect(self.clickedSectionImp3)

        self.ui.addSection.clicked.connect(self.slot_addedSections)
        self.ui.addSection_2.clicked.connect(self.slot_addedSections2)
        self.ui.addSection_3.clicked.connect(self.slot_addedSections3)
        self.ui.addSection_4.clicked.connect(self.slot_addedSections4)
        self.ui.addSection_5.clicked.connect(self.slot_addedSections5)


        #self.ui.addItem_3.clicked.connect(self.slot_addedItems_3)
        #self.ui.implementVAIM.clicked.connect(self.clickedItemImp3)


        global item
        item = list()
        global aux
        aux = list()
        self.ui.addItem.clicked.connect(self.slot_addedItem)
        self.ui.taxImpIt.clicked.connect(self.clickedItemImp)

        self.ui.addItem_2.clicked.connect(self.slot_addedItem2)
        self.ui.priceImpIt.clicked.connect(self.clickedItemImp2)

        self.ui.addItem_3.clicked.connect(self.slot_addedItem3)
        self.ui.implementVAIM.clicked.connect(self.clickedItemImp3)
        
        self.ui.addItem_4.clicked.connect(self.slot_addedItem4)
        self.ui.tagsImpIt.clicked.connect(self.clickedItemImp4)

        self.ui.addItem_5.clicked.connect(self.slot_addedItem5)

        global osFjson
        osFjson = list()

        global os
        os = list()
        global aux2
        aux2 = list()
        global osOption
        osOption = list()
        global auxiliar
        auxiliar = list()
        global auxOS
        auxOS = list()
        global data
        data = list()
        global auxOSMaster
        auxOSMaster = list()
        global osOptions
        osOptions = list()
        global osOptions2
        osOptions2 = list()
        global texto1
        texto1 = str()
        self.ui.osList.activated.connect(self.setOptionList)
        self.ui.addOS.clicked.connect(self.slot_addedOsOption)
        self.ui.taxImpOS.clicked.connect(self.clickedOSImp)

        self.ui.osList_2.activated.connect(self.setOptionList2)
        self.ui.addOS_2.clicked.connect(self.slot_addedOsOption2)
        self.ui.priceImpOS.clicked.connect(self.clickedOSImp2)

        global smartSearch
        smartSearch = list()
        global text
        text = list()
        global auxSS
        auxSS = list()
        global price
        price = float()
        global newTags
        newTags = list()

        self.ui.addSmartSearch_3.clicked.connect(self.slot_addedSS3)
        self.ui.implementVASS.clicked.connect(self.clickedSSImp3)

        self.ui.leSmartSearch.editingFinished.connect(self.slot_setSSList)
        self.ui.addSmartSearch.clicked.connect(self.slot_addedSS)
        self.ui.taxImpSmartSearch.clicked.connect(self.clickedSSImp)

        self.ui.leSmartSearch_2.editingFinished.connect(self.slot_setSSList2)
        self.ui.addSmartSearch_2.clicked.connect(self.slot_addedSS2)
        self.ui.priceImpSmartSearch.clicked.connect(self.clickedSSImp2)
        self.ui.rounding.hide()
        self.ui.labelInfo2.setText("Increase or decrease the price in the chosen percentaje, to drecrease use '-'")
        self.ui.leSmartSearch_3.editingFinished.connect(self.slot_setSSList3)

        self.ui.roundTo5.clicked.connect(self.slot_roundingButtons)
        self.ui.roundTo10.clicked.connect(self.slot_roundingButtons)
        self.ui.roundTo99.clicked.connect(self.slot_roundingButtons)
        self.ui.roundToInt.clicked.connect(self.slot_roundingButtons)

        self.ui.priceListSelected.activated.connect(self.indexHasChanged)
        self.ui.leIncrease.editingFinished.connect(self.slot_Increase)

        self.ui.lineEditTag.editingFinished.connect(self.add_tags)
        self.ui.lineEditTag_2.editingFinished.connect(self.remove_tags)
        self.ui.tagsImpSec.clicked.connect(self.clickedSectionImp4)
        self.ui.tagsImpSec_2.clicked.connect(self.clickedSectionImp5)
        self.ui.tagsImpIt_2.clicked.connect(self.clickedItemImp5)

        self.ui.GETITEMSNAMEBUTTON.clicked.connect(self.getItemsName)

##########################################################################################
##########################################################################################
#sets the screen for working with TAXES
    def clickedTAXBUTTON(self):
        self.ui.stackedWidget.setCurrentWidget(self.ui.taxPage)
        self.clear_all()
        self.ui.stackedWidget.show()

#sets the screen for working with PRICES
    def clickedPRICEBUTTON(self):
        self.ui.stackedWidget.setCurrentWidget(self.ui.pricePage)
        self.clear_all()
        self.ui.stackedWidget.show()

#sets the screen for working with DRINKS
    def clickedDRINKSBUTTON(self):
        self.ui.stackedWidget.setCurrentWidget(self.ui.drinksPage) # setCurrentWidget hace visible una página nueva
        self.clear_all()
        self.ui.stackedWidget.show()

    def clickedPARSEBUTTON(self):
        self.ui.stackedWidget.setCurrentWidget(self.ui.homePage)
        self.clear_all()
        self.ui.stackedWidget.show()

    def clickedADDTAGSBUTTON(self):
        self.ui.stackedWidget.setCurrentWidget(self.ui.tagsPage)
        self.clear_all()
        self.ui.stackedWidget.show()
    
    def clickedREMOVETAGSBUTTON(self):
        self.ui.stackedWidget.setCurrentWidget(self.ui.removeTagsPage)
        self.clear_all()
        self.ui.stackedWidget.show()

    def clickedTAXABLEYES(self):
        parser = parsejson(self.archivo)
        parser.setTaxableTrue(datos)
        QMessageBox.information(self,'Success!','You have set the taxes to True',QMessageBox.Ok)

#loads the json and sets up all the dropping lists
    def clickedLoad(self):
        self.archivo, _ = QFileDialog.getOpenFileName(self, ("Open JSON"), "", ("txt or JSON file (*.json *.txt)"))
        self.ui.stackedWidget.setCurrentWidget(self.ui.homePage)
        self.clear_all()
        self.ui.stackedWidget.show()

        print(self.archivo) #archivo es una tupla

        """if archivo[0].lower().endswith('.txt'):
            p = Path(archivo[0])
            new_p = Path(p.parent.as_posix() + '/' + p.stem + '.json')"""
        
        global file
        global newTags
        global tagToRemove
        self.clear_all()
        if self.archivo == '':
            self.ui.taxList.clear()
            self.ui.sectionList.clear()
            self.ui.itemsList.clear()
            self.ui.itemsList_2.clear()
            self.ui.osList.clear()
            self.ui.osList_2.clear()
            self.ui.optionsList.clear()
            self.ui.optionsList_2.clear()
            self.ui.addedOS.clear()
            self.ui.addedOS_2.clear()
            self.ui.addedItems_2.clear()
            self.ui.addedItems.clear()
            self.ui.labelInfoTag.clear()
            self.ui.labelInfoTag_2.clear()
            newTags = []
            tagToRemove = []
            pass
        else:
            global datos
            file = self.archivo
            datos = jsonSection.openJson(jsonSection,file)
            isAdminJson = self.is_admin_json()

            if isAdminJson:
                self.set_enable_main_view_btns(True)
                self.ui.ADDTAGSBUTTON.setEnabled(False)
                self.ui.TAXABLEYES.setEnabled(False)
                self.ui.REMOVETAGSBUTTON.setEnabled(False)
                self.ui.GETITEMSNAMEBUTTON.setEnabled(False)
                self.ui.ADDSNOOZETAGSBUTTON.setEnabled(False)
                QMessageBox.information(self, 'Success!','You loaded a Legacy JSON',QMessageBox.Ok)
                self.find_empty_values()
                self.setTaxList()
                self.setSectionList()
                self.setItemsList()
                self.setOSList()
                self.ui.addedOS.clear()
                self.ui.addedOS_2.clear()
                self.ui.addedItems_2.clear()
                self.ui.addedItems.clear()
            else:
                self.setSectionList()
                self.setItemsList()
                self.set_enable_main_view_btns(False)
                self.ui.ADDTAGSBUTTON.setEnabled(True)
                self.ui.TAXABLEYES.setEnabled(True)
                self.ui.REMOVETAGSBUTTON.setEnabled(True)
                self.ui.GETITEMSNAMEBUTTON.setEnabled(True)
                self.ui.ADDSNOOZETAGSBUTTON.setEnabled(True)
                QMessageBox.information(self, 'Success!','You loaded a POS JSON',QMessageBox.Ok)
                self.ui.labelInfoTag.clear()
                self.ui.labelInfoTag_2.clear()
                newTags = []
                tagToRemove = []

           

    def is_admin_json(self):
        global datos
        return "WhiteLabelConfigId" in datos
    
    def set_enable_main_view_btns(self, enabled):
        self.ui.DRINKSBUTTON.setEnabled(enabled)
        self.ui.PRICEBUTTON.setEnabled(enabled)
        self.ui.TAXBUTTON.setEnabled(enabled)
        self.ui.PARSEBUTTON.setEnabled(enabled)


    def disableButtons(self):
        self.ui.DRINKSBUTTON.setEnabled(False)
        self.ui.PRICEBUTTON.setEnabled(False)
        self.ui.TAXBUTTON.setEnabled(False)
        self.ui.PARSEBUTTON.setEnabled(False)
        self.ui.ADDTAGSBUTTON.setEnabled(False)
        self.ui.TAXABLEYES.setEnabled(False)
        self.ui.REMOVETAGSBUTTON.setEnabled(False)
        self.ui.GETITEMSNAMEBUTTON.setEnabled(False)
        self.ui.ADDSNOOZETAGSBUTTON.setEnabled(False)

#closes the program
    def closeEvent(self, event):
        reply = QMessageBox.question(self, 'Window Close', 'Are you sure you want to close the window?',
            QMessageBox.Yes | QMessageBox.No, QMessageBox.No)

        if reply == QMessageBox.Yes:
            event.accept()
        elif reply == QMessageBox.No:
            event.ignore()

#Searchs for empty items.
    def find_empty_values(self):

        secciones = jsonSection.slot_mostrarSecciones(jsonSection,datos, True)
        itemTitles = jsonSection.get_item_names(jsonSection,datos)
        osTitles  = jsonSection.slot_get_OS_titles(jsonSection,datos)
        emptyOsItems = jsonSection.find_empty_valuess(jsonSection,datos)


        #print(emptyOsItems)
        if "" in secciones:
            QMessageBox.critical(self, 'Error',
            'You have an unnamed section in your menu, correct it and upload the file again.',QMessageBox.Ok)
            self.disableButtons()

        if bool(itemTitles): #if bool is true then itemTitles is not empty
            QMessageBox.critical(self, 'Error',f'You have an unnamed item in "{itemTitles[0]}" section, correct it and upload the file again.',QMessageBox.Ok)
            self.disableButtons()

        if bool(osTitles):#if bool is true then osTitles is not empty
            QMessageBox.critical(self, 'Error',
            f'You have an unnamed Option Set title in "{osTitles[0]}" Section -> "{osTitles[1]}" item, correct it and upload the file again.',QMessageBox.Ok)
            self.disableButtons()

        if bool(emptyOsItems):#if bool is true then emptyOsItems is not empty
            QMessageBox.critical(self, 'Error',
            f'You have an unnamed Option Set item in "{emptyOsItems[0]}" Section -> "{emptyOsItems[1]}" Item -> "{emptyOsItems[2]}" Option Set. Correct it and upload the file again.',QMessageBox.Ok)
            self.disableButtons()

#############################################################################################
#############################################################################################
#SETLISTS

#sets the list of taxes that are on the menu
    def setTaxList(self):
        self.ui.taxList.clear()
        taxes = jsonSection.slot_mostrarTax(jsonSection,datos)
        for i in range(0,len(taxes)):
            self.ui.taxList.addItem(taxes[i])

#sets the list of sections that are on the menu
    def setSectionList(self):

        isAdmin = self.is_admin_json() #True or False
        #print(isAdmin)
        self.ui.sectionList.clear()
        self.ui.sectionList_2.clear()
        self.ui.sectionList_3.clear()
        self.ui.sectionList_4.clear()
        self.ui.sectionList_5.clear()
        sectionsList = jsonSection.slot_mostrarSecciones(jsonSection,datos,isAdmin)

        sectionsList.insert(0,"Change All")
        for section in sectionsList:
            self.ui.sectionList.addItem(section)
            self.ui.sectionList_2.addItem(section)
            self.ui.sectionList_3.addItem(section)
            self.ui.sectionList_4.addItem(section)
            self.ui.sectionList_5.addItem(section)

#sets the list of items that are on the menu
    def setItemsList(self):
        isAdmin = self.is_admin_json()
        self.ui.itemsList.clear()
        self.ui.itemsList_2.clear()
        self.ui.itemsList_3.clear()
        self.ui.itemsList_4.clear()
        self.ui.itemsList_5.clear()
        itemsList = jsonSection.slot_mostrarItems(jsonSection,datos,isAdmin)

        itemsList.insert(0,"Change All")
        for item in itemsList:
            self.ui.itemsList.addItem(item)
            self.ui.itemsList_2.addItem(item)
            self.ui.itemsList_3.addItem(item)
            self.ui.itemsList_4.addItem(item)
            self.ui.itemsList_5.addItem(item)

#sets the lists of OS available on the menu
    def setOSList(self):
        global osFjson
        self.ui.osList.clear()
        self.ui.osList_2.clear()
        osFjson  = jsonSection.slot_mostrarOS(jsonSection,datos)
        os = ""
        osOp = list()
        #print(osFjson)

        for i in range(0,len(osFjson)):
            for j in range(0,len(datos["MenuSections"])):
                for k in range(0,len(datos["MenuSections"][j]["MenuItems"])):
                    for l in range(0,len(datos["MenuSections"][j]["MenuItems"][k]["MenuItemOptionSets"])):
                        if osFjson [i] == datos["MenuSections"][j]["MenuItems"][k]["MenuItemOptionSets"][l]['Name']:
                            os = datos["MenuSections"][j]["MenuItems"][k]["MenuItemOptionSets"][l]['Name']
                            for m in range(0,len(datos["MenuSections"][j]["MenuItems"][k]["MenuItemOptionSets"][l]["MenuItemOptionSetItems"])):
                                osOp.append(datos["MenuSections"][j]["MenuItems"][k]["MenuItemOptionSets"][l]["MenuItemOptionSetItems"][m]['Name'])

            if os == None and osOp == []:
                pass
            elif os != None and osOp == []:
                pass
            else:
                self.ui.osList.addItem(os)
                self.ui.osList_2.addItem(os)
                self.setOptionList()
                self.setOptionList2()
            osOp.clear()

#sets the list of options that are on each OS on the menu
    def setOptionList(self):
        global osOptions
        global data
        osOptions.clear()
        self.ui.optionsList.clear()
        for i in range(0,len(osFjson)):
            for j in range(0,len(datos["MenuSections"])):
                for k in range(0,len(datos["MenuSections"][j]["MenuItems"])):
                    for l in range(0,len(datos["MenuSections"][j]["MenuItems"][k]["MenuItemOptionSets"])):
                        if self.ui.osList.currentText() == "" and datos["MenuSections"][j]["MenuItems"][k]["MenuItemOptionSets"][l]['Name'] == None:
                            data = datos["MenuSections"][j]["MenuItems"][k]["MenuItemOptionSets"][l]['Name']
                            for m in range(0,len(datos["MenuSections"][j]["MenuItems"][k]["MenuItemOptionSets"][l]["MenuItemOptionSetItems"])):
                                if datos["MenuSections"][j]["MenuItems"][k]["MenuItemOptionSets"][l]["IsMasterOptionSet"] == False:
                                    smt = datos["MenuSections"][j]["MenuItems"][k]["MenuItemOptionSets"][l]["MenuItemOptionSetItems"][m]['Name']
                                    if smt not in osOptions:
                                        osOptions.append(smt)
                        elif self.ui.osList.currentText() == datos["MenuSections"][j]["MenuItems"][k]["MenuItemOptionSets"][l]['Name']:
                            data = datos["MenuSections"][j]["MenuItems"][k]["MenuItemOptionSets"][l]['Name']
                            for m in range(0,len(datos["MenuSections"][j]["MenuItems"][k]["MenuItemOptionSets"][l]["MenuItemOptionSetItems"])):
                                if datos["MenuSections"][j]["MenuItems"][k]["MenuItemOptionSets"][l]["IsMasterOptionSet"] == False:
                                    smt = datos["MenuSections"][j]["MenuItems"][k]["MenuItemOptionSets"][l]["MenuItemOptionSetItems"][m]['Name']
                                    if smt not in osOptions:
                                        osOptions.append(smt)
        osOptions.insert(0,"Change All")
        for i in range(0,len(osOptions)):
            if self.ui.osList.currentText()== "":
                selfCurrentT = None
            if self.ui.osList.currentText() == data or selfCurrentT == data:
                self.ui.optionsList.addItem(osOptions[i])

#sets the list of options that are on each OS on the menu
    def setOptionList2(self):
        global osOptions2
        global data
        osOptions2.clear()
        self.ui.optionsList_2.clear()
        """section = None
        item = None
        optionSet = None
        unnamedItems = []"""

        for i in range(0,len(osFjson)):
            for j in range(0,len(datos["MenuSections"])):
                for k in range(0,len(datos["MenuSections"][j]["MenuItems"])):
                    for l in range(0,len(datos["MenuSections"][j]["MenuItems"][k]["MenuItemOptionSets"])):
                        if self.ui.osList_2.currentText() == "" and datos["MenuSections"][j]["MenuItems"][k]["MenuItemOptionSets"][l]['Name'] == None:
                            data = datos["MenuSections"][j]["MenuItems"][k]["MenuItemOptionSets"][l]['Name']
                            for m in range(0,len(datos["MenuSections"][j]["MenuItems"][k]["MenuItemOptionSets"][l]["MenuItemOptionSetItems"])):
                                if datos["MenuSections"][j]["MenuItems"][k]["MenuItemOptionSets"][l]["IsMasterOptionSet"] == False:
                                    smt = datos["MenuSections"][j]["MenuItems"][k]["MenuItemOptionSets"][l]["MenuItemOptionSetItems"][m]['Name']
                                    if smt not in osOptions2:
                                        osOptions2.append(smt)
                        elif self.ui.osList_2.currentText() == datos["MenuSections"][j]["MenuItems"][k]["MenuItemOptionSets"][l]['Name']:
                            data = datos["MenuSections"][j]["MenuItems"][k]["MenuItemOptionSets"][l]['Name']
                            for m in range(0,len(datos["MenuSections"][j]["MenuItems"][k]["MenuItemOptionSets"][l]["MenuItemOptionSetItems"])):
                                if datos["MenuSections"][j]["MenuItems"][k]["MenuItemOptionSets"][l]["IsMasterOptionSet"] == False:
                                    smt = datos["MenuSections"][j]["MenuItems"][k]["MenuItemOptionSets"][l]["MenuItemOptionSetItems"][m]['Name']
                                    if smt not in osOptions2:
                                        osOptions2.append(smt)
        osOptions2.insert(0,"Change All")
        for i in range(0,len(osOptions2)):
            if self.ui.osList_2.currentText()== "":
                selfCurrentT2 = None
            if self.ui.osList_2.currentText() == data or selfCurrentT2 == data:
                self.ui.optionsList_2.addItem(osOptions2[i])

        """for sections in datos["MenuSections"]:
            for items in sections["MenuItems"]:
                for optionSets in items["MenuItemOptionSets"]:
                    for itemsInOptionSets in optionSets["MenuItemOptionSetItems"]:
                        if itemsInOptionSets["Name"] == "" or itemsInOptionSets["Name"] == None:
                            section = sections["Name"]
                            item = items["Name"]
                            optionSet = optionSets["Name"]
                            unnamedItems.append((section, item, optionSet))
                            break
        if unnamedItems:

            message = '\n'.join([f'You have an unnamed item inside an Option Set in "{section}" Section -> "{item}" item -> "{optionSet}" Option Set. Correct it and upload the file again.' for section, item, optionSet in unnamedItems])
            QMessageBox.warning(self, 'Warning', message, QMessageBox.Ok)"""

#sets the list of options and items that matches the search
    def slot_setSSList(self):
        self.ui.smartSearchList.clear()
        smartSearch.clear()
        textito = "" #string
        textito = self.ui.leSmartSearch.text()
        for j in range(0,len(datos["MenuSections"])):
            for k in range(0,len(datos["MenuSections"][j]["MenuItems"])):
                itemsSS = datos["MenuSections"][j]["MenuItems"][k]["Name"] #string
                if textito.lower() in ascii(datos["MenuSections"][j]["MenuItems"][k]["Name"]).lower():
                    if itemsSS not in smartSearch:
                        smartSearch.append(itemsSS)
                        if textito not in text:
                            text.append(textito)
                if len(datos["MenuSections"][j]["MenuItems"][k]["MenuItemOptionSets"]) == 0:
                    pass
                else:
                    for l in range(0,len(datos["MenuSections"][j]["MenuItems"][k]["MenuItemOptionSets"])):
                        for m in range(0,len(datos["MenuSections"][j]["MenuItems"][k]["MenuItemOptionSets"][l]["MenuItemOptionSetItems"])):
                            opSS = datos["MenuSections"][j]["MenuItems"][k]["MenuItemOptionSets"][l]["MenuItemOptionSetItems"][m]['Name']
                            if textito.lower() in ascii(datos["MenuSections"][j]["MenuItems"][k]["MenuItemOptionSets"][l]["MenuItemOptionSetItems"][m]['Name']).lower() and opSS not in smartSearch:
                                smartSearch.append(opSS)
                                if textito not in text:
                                    text.append(textito)
        if len(smartSearch) != 0:
            smartSearch.insert(0,"Change All")
        for i in range(0,len(smartSearch)):
            self.ui.smartSearchList.addItem(smartSearch[i])
        self.ui.leSmartSearch.clear()

#sets the list of options and items that matches the search
    def slot_setSSList2(self):
        self.ui.smartSearchList_2.clear()
        smartSearch.clear()
        textito = ""
        textito = self.ui.leSmartSearch_2.text()
        for j in range(0,len(datos["MenuSections"])):
            for k in range(0,len(datos["MenuSections"][j]["MenuItems"])):
                itemsSS = datos["MenuSections"][j]["MenuItems"][k]["Name"]
                if textito.lower() in ascii(datos["MenuSections"][j]["MenuItems"][k]["Name"]).lower():
                    if itemsSS not in smartSearch:
                        smartSearch.append(itemsSS)
                        if textito not in text:
                            text.append(textito)
                if len(datos["MenuSections"][j]["MenuItems"][k]["MenuItemOptionSets"]) == 0:
                    pass
                else:
                    for l in range(0,len(datos["MenuSections"][j]["MenuItems"][k]["MenuItemOptionSets"])):
                        for m in range(0,len(datos["MenuSections"][j]["MenuItems"][k]["MenuItemOptionSets"][l]["MenuItemOptionSetItems"])):
                            opSS = datos["MenuSections"][j]["MenuItems"][k]["MenuItemOptionSets"][l]["MenuItemOptionSetItems"][m]['Name']
                            if textito.lower() in ascii(datos["MenuSections"][j]["MenuItems"][k]["MenuItemOptionSets"][l]["MenuItemOptionSetItems"][m]['Name']).lower() and opSS not in smartSearch:
                                smartSearch.append(opSS)
                                if textito not in text:
                                    text.append(textito)
        if len(smartSearch) != 0:
            smartSearch.insert(0,"Change All")
        for i in range(0,len(smartSearch)):
            self.ui.smartSearchList_2.addItem(smartSearch[i])
        self.ui.leSmartSearch_2.clear()


#
    def slot_setSSList3(self):
        self.ui.smartSearchList_3.clear()
        smartSearch.clear()
        textito = ""
        textito = self.ui.leSmartSearch_3.text()
        for j in range(0,len(datos["MenuSections"])):
            for k in range(0,len(datos["MenuSections"][j]["MenuItems"])):
                itemsSS = datos["MenuSections"][j]["MenuItems"][k]["Name"]
                if textito.lower() in ascii(datos["MenuSections"][j]["MenuItems"][k]["Name"]).lower():
                    if itemsSS not in smartSearch:
                        smartSearch.append(itemsSS)
                        if textito not in text:
                            text.append(textito)
        if len(smartSearch) != 0:
            smartSearch.insert(0,"Change All")
        for i in range(0,len(smartSearch)):
            self.ui.smartSearchList_3.addItem(smartSearch[i])
        self.ui.leSmartSearch_3.clear()
################################################################################
################################################################################

#Sets the QTextEdit of selected items/sections/etc

#shows the sections selected on the text edit [TAXES]
    def slot_addedSections(self):
        texto = ''
        if self.ui.sectionList.currentText() in sectionName:
            pass
        else:
            sectionName.append(self.ui.sectionList.currentText())
        for i in range(0,len(sectionName)):
            texto += sectionName[i]
            if texto != "":
                texto += "\n"
                self.ui.addedSections.setText(texto)

#shows the sections selected on the text edit [PRICES]
    def slot_addedSections2(self):
        texto = ''
        if self.ui.sectionList_2.currentText() in sectionName:
            pass
        else:
            sectionName.append(self.ui.sectionList_2.currentText())
        for i in range(0,len(sectionName)):
            texto += sectionName[i]
            if texto != "":
                texto += "\n"
                self.ui.addedSections_2.setText(texto)

#shows the sections selected on the text edit [DRINKS]
    def slot_addedSections3(self):
        texto = ''
        if self.ui.sectionList_3.currentText() in sectionName:
            pass
        else:
            sectionName.append(self.ui.sectionList_3.currentText())
        for i in range(0,len(sectionName)):
            texto += sectionName[i]
            if texto != "":
                texto += "\n"
                self.ui.addedSections_3.setText(texto)

#shows the sections selected on the text edit [Tags]
    def slot_addedSections4(self):
        texto = ''
        if self.ui.sectionList_4.currentText() in sectionName:
            pass
        else:
            sectionName.append(self.ui.sectionList_4.currentText())
        for section in sectionName:
            texto += section
            if texto != "":
                texto += "\n"
                self.ui.addedSections_4.setText(texto)

#shows the sections selected on the remove text edit [Tags]
    def slot_addedSections5(self):
        texto = ''
        if self.ui.sectionList_5.currentText() in sectionName:
            pass
        else:
            sectionName.append(self.ui.sectionList_5.currentText())
        for section in sectionName:
            texto += section
            if texto != "":
                texto += "\n"
                self.ui.addedSections_5.setText(texto)

#shows the items selected on the text edit [TAX]
    def slot_addedItem(self):
        texto = ''
        if self.ui.itemsList.currentText() in aux:
            pass
        else:
            aux.append(self.ui.itemsList.currentText())
            for i in range(0,len(aux)):
                texto += aux[i]
                item.append(aux[i].split(sep=': '))
                if texto != "":
                    texto += "\n"
                    self.ui.addedItems.setText(texto)

#shows the items selected on the text edit [PRICES]
    def slot_addedItem2(self):
        texto = ''
        if self.ui.itemsList_2.currentText() in aux:
            pass
        else:
            aux.append(self.ui.itemsList_2.currentText())
            for i in range(0,len(aux)):
                texto += aux[i]
                item.append(aux[i].split(sep=': '))
                if texto != "":
                    texto += "\n"
                    self.ui.addedItems_2.setText(texto)

#shows the items selected on the text edit [TAX]
    def slot_addedItem3(self):
        texto = ''
        if self.ui.itemsList_3.currentText() in aux:
            pass
        else:
            aux.append(self.ui.itemsList_3.currentText())
            for i in range(0,len(aux)):
                texto += aux[i]
                item.append(aux[i].split(sep=': '))
                if texto != "":
                    texto += "\n"
                    self.ui.addedItems_3.setText(texto)

#shows the items selected on the text edit [Tags]
    def slot_addedItem4(self):
        texto = ''
        if self.ui.itemsList_4.currentText() in aux:
            pass
        else:
            aux.append(self.ui.itemsList_4.currentText())
        for auxItem in aux:
            texto += auxItem
            if texto != "":
                texto += "\n"
                self.ui.addedItems_4.setText(texto)

    def slot_addedItem5(self):
        texto = ''
        self.itemTagsRemove.append(self.ui.itemsList_5.currentText())
        #print("Items: ",self.itemTagsRemove)
        if self.ui.itemsList_5.currentText() in aux:
            pass
        else:
            aux.append(self.ui.itemsList_5.currentText())
        for auxItem in aux:
            texto += auxItem
            if texto != "":
                texto += "\n"
                self.ui.addedItems_5.setText(texto)

#shows the OS options selected on the text edit [TAX]
    def slot_addedOsOption(self):
        texto = ''
        if self.ui.optionsList.currentText() in auxOS:
            if self.ui.osList.currentText() in auxOSMaster:
                pass
            else:
                auxOS.append(self.ui.optionsList.currentText())
                auxOSMaster.append(self.ui.osList.currentText())
                for i in range(0,len(auxOS)):
                    texto += auxOSMaster[i] + ": " + auxOS[i]
                    if texto != "":
                        texto += "\n"
                        self.ui.addedOS.setText(texto)
        else:
            auxOS.append(self.ui.optionsList.currentText())
            auxOSMaster.append(self.ui.osList.currentText())
            for i in range(0,len(auxOS)):
                texto += auxOSMaster[i] + ": " + auxOS[i]
                if texto != "":
                    texto += "\n"
                    self.ui.addedOS.setText(texto)


#shows the OS options selected on the text edit [PRICES]
    def slot_addedOsOption2(self):
        texto = ''
        if self.ui.optionsList_2.currentText() in auxOS:
            if self.ui.osList_2.currentText() in auxOSMaster:
                pass
            else:
                auxOS.append(self.ui.optionsList_2.currentText())
                auxOSMaster.append(self.ui.osList_2.currentText())
                for i in range(0,len(auxOS)):
                    texto += auxOSMaster[i] + ": " + auxOS[i]
                    if texto != "":
                        texto += "\n"
                        self.ui.addedOS_2.setText(texto)
        else:
            auxOS.append(self.ui.optionsList_2.currentText())
            auxOSMaster.append(self.ui.osList_2.currentText())
            for i in range(0,len(auxOS)):
                texto += auxOSMaster[i] + ": " + auxOS[i]
                if texto != "":
                    texto += "\n"
                    self.ui.addedOS_2.setText(texto)

#shows the SS options selected on the text edit [TAXES]
    def slot_addedSS(self):
        texto = ''
        if self.ui.smartSearchList.currentText() in auxSS:
                pass
        elif self.ui.smartSearchList.currentText() == "Change All":
            for i in range(1,len(smartSearch)):
                auxSS.append(smartSearch[i])
            for i in range(0,len(auxSS)):
                texto += auxSS[i]
                if texto != "":
                    texto += "\n"
                    self.ui.addedSS.setText(texto)
        else:
            auxSS.append(self.ui.smartSearchList.currentText())
            for i in range(0,len(auxSS)):
                texto += auxSS[i]
                if texto != "":
                    texto += "\n"
                    self.ui.addedSS.setText(texto)

#shows the SS (price) options selected on the text edit [PRICES]
    def slot_addedSS2(self):
        texto = ''
        if self.ui.smartSearchList_2.currentText() in auxSS:
                pass
        elif self.ui.smartSearchList_2.currentText() == "Change All":
            for i in range(1,len(smartSearch)):
                auxSS.append(smartSearch[i])
            for i in range(0,len(auxSS)):
                texto += auxSS[i]
                if texto != "":
                    texto += "\n"
                    self.ui.addedSS_2.setText(texto)
        else:
            auxSS.append(self.ui.smartSearchList_2.currentText())
            for i in range(0,len(auxSS)):
                texto += auxSS[i]
                if texto != "":
                    texto += "\n"
                    self.ui.addedSS_2.setText(texto)

#shows the SS (price) options selected on the text edit [DRINKS]
    def slot_addedSS3(self):
        texto = ''
        if self.ui.smartSearchList_3.currentText() in auxSS:
                pass
        elif self.ui.smartSearchList_3.currentText() == "Change All":
            for i in range(1,len(smartSearch)):
                auxSS.append(smartSearch[i])
            for i in range(0,len(auxSS)):
                texto += auxSS[i]
                if texto != "":
                    texto += "\n"
                    self.ui.addedSS_3.setText(texto)
        else:
            auxSS.append(self.ui.smartSearchList_3.currentText())
            for i in range(0,len(auxSS)):
                texto += auxSS[i]
                if texto != "":
                    texto += "\n"
                    self.ui.addedSS_3.setText(texto)

#button that applies tax to the selected sections [TAXES]
    def clickedSectionImp(self):
        global datos
        if datos == None:
            QMessageBox.warning(self, 'Warning',
            'You must load a JSON File first!',QMessageBox.Ok)
        else:
            tax = self.ui.taxList.currentIndex()
            jsonSection.slot_changeTaxSelectedSections(jsonSection,datos,sectionName,tax)
            QMessageBox.information(self, 'Success!',
            'The selected sections have been updated',QMessageBox.Ok)
        sectionName.clear()
        self.ui.addedSections.clear()

#button that applies tax to the selected items [TAXES]
    def clickedItemImp(self):
        global datos
        if datos == None:
            QMessageBox.warning(self, 'Warning',
            'You must load a JSON File first!',QMessageBox.Ok)
        else:
            tax = self.ui.taxList.currentIndex()
            jsonSection.slot_changeTaxSelectedItems(jsonSection,datos,item,tax)
            QMessageBox.information(self, 'Success!',
            'The selected items have been updated',QMessageBox.Ok)
        aux.clear()
        item.clear()
        self.ui.addedItems.clear()

#button that applies tax to the selected option OS [TAXES]
    def clickedOSImp(self):
        global datos
        if datos == None:
            QMessageBox.warning(self, 'Warning',
            'You must load a JSON File first!',QMessageBox.Ok)
        else:
            tax = self.ui.taxList.currentIndex()
            jsonSection.slot_changeTaxSelectedOS(jsonSection,datos,auxOS,auxOSMaster,tax)
            QMessageBox.information(self, 'Success!',
            'The selected sections have been updated',QMessageBox.Ok)
        osOptions.clear()
        auxOSMaster.clear()
        auxOS.clear()
        self.ui.addedOS.clear()

#button that applies tax to the selected SS items [TAXES]
    def clickedSSImp(self):
        global datos
        if datos == None:
            QMessageBox.warning(self, 'Warning',
            'You must load a JSON File first!',QMessageBox.Ok)
        else:
            tax = self.ui.taxList.currentIndex()
            jsonSection.slot_changeTaxSelectedSS(jsonSection,datos,auxSS,text,tax)
            QMessageBox.information(self, 'Success!',
            'The selected items have been updated',QMessageBox.Ok)
        auxSS.clear()
        text.clear()
        self.ui.smartSearchList.clear()
        self.ui.addedSS.clear()

#applies taxes to all the menu [TAXES]
    def clickedAllSections(self):
        global datos
        if datos == None:
            QMessageBox.warning(self, 'Warning',
            'You must load a JSON File first!',QMessageBox.Ok)
        else:
            tax = self.ui.taxList.currentIndex()
            jsonSection.slot_changeTaxAllSections(jsonSection,datos,tax)
            QMessageBox.information(self, 'Success!',
            'All the items have been updated',QMessageBox.Ok)
        self.clear_all()

#removes taxes from all the menu [TAXES]
    def clickedRemoveTax(self):
        global datos
        if datos == None:
            QMessageBox.warning(self, 'Warning',
            'You must load a JSON File first!',QMessageBox.Ok)
        else:
            tax = None
            jsonSection.slot_RemoveTaxAllItems(jsonSection,datos,tax)
            QMessageBox.information(self, 'Success!',
            'All taxes have been removed from your Menu',QMessageBox.Ok)
        self.clear_all()

#saves the json file
    def clickedSave(self):
        global datos
        if datos == None:
            QMessageBox.warning(self, 'Warning',
            'You must load a JSON File first!',QMessageBox.Ok)
        else:
            dialog = QFileDialog()
            dialog.setAcceptMode(QFileDialog.AcceptSave)
            dialog.setDefaultSuffix("json")
            dialog.setNameFilter("JSON files (*.json)")

            if dialog.exec_() == QFileDialog.Accepted:
                selectedFile = dialog.selectedFiles()[0]  # Get the first selected file
                with open(selectedFile, 'w') as archivo_nuevo:
                    json.dump(datos, archivo_nuevo)
            #jsonSection.save_json(jsonSection,datos,file)
            QMessageBox.information(self, 'Success!',
            'Json Succesfully Saved!',QMessageBox.Ok)
        self.ui.stackedWidget.setCurrentWidget(self.ui.homePage)
        self.clear_all()
        self.ui.stackedWidget.show()
        self.disableButtons()

    def clear_all(self):
        self.ui.addedItems.clear()
        self.ui.addedSections.clear()
        self.ui.addedOS.clear()
        self.ui.addedItems_2.clear()
        self.ui.addedSections_2.clear()
        self.ui.addedItems_3.clear()
        self.ui.addedSections_3.clear()
        self.ui.addedOS_2.clear()
        self.ui.smartSearchList.clear()
        self.ui.addedSS.clear()
        self.ui.smartSearchList_2.clear()
        self.ui.addedSS_2.clear()
        self.ui.smartSearchList_3.clear()
        self.ui.addedSS_3.clear()
        auxSS.clear()
        auxOS.clear()
        osOptions.clear()
        auxOSMaster.clear()
        item.clear()
        sectionName.clear()
        aux.clear()
        text.clear()

###############################################################################
###############################################################################


#TAGS MODIFICATIONS
    def add_tags(self):
        newTags.append(self.ui.lineEditTag.text())
        self.ui.lineEditTag.clear()
        for i in range(len(newTags)):
            newTags[i] = newTags[i].replace(" ", "")

        labelTags = list(set(newTags))
        if len(labelTags) > 1:
            labelTags[-2] += ' and ' + labelTags[-1]
            labelTags.pop()
        labelTagsSentence = ', '.join(labelTags) + '.'
        self.ui.labelInfoTag.setText("You are about to add the following Tag/s: " + labelTagsSentence)


        print("TAGS: ", newTags)
        #print(len(tags))
    
    def remove_tags(self):

        self.tagToRemove.append(self.ui.lineEditTag_2.text().replace(" ", ""))
        self.ui.lineEditTag_2.clear()
        self.tagToRemove = list(set(self.tagToRemove))
        displayTags = self.tagToRemove

        if len(displayTags) > 1:
            displayTags = list(set(displayTags))
            print("self.tagToRemove: ", self.tagToRemove)
            displayTags[-2] += ' and ' + displayTags[-1]
            displayTags.pop()

        labelTagsSentence = ', '.join(displayTags) + '.'
        self.ui.labelInfoTag_2.setText("You are about to remove the following Tag/s: " + labelTagsSentence)

    def clickedSectionImp4(self):
        global datos
        global newTags
        print(self.tagToRemove)
        if len(newTags) == 0:
            QMessageBox.warning(self, 'Warning',
            'You must add tags first!',QMessageBox.Ok)
        else:
            parser = parsejson(self.archivo)
            parser.category_add_tag(datos, newTags, sectionName)
            QMessageBox.information(self, 'Success!',
            'The selected sections have been updated',QMessageBox.Ok)

            sectionName.clear()
            self.ui.addedSections_4.clear()
            self.ui.labelInfoTag.clear()
            newTags = []
            
    def clickedItemImp4(self):
        global datos
        global newTags
        if len(newTags) == 0:
            QMessageBox.warning(self, 'Warning',
            'You must add tags first!',QMessageBox.Ok)
        else:
            parser = parsejson(self.archivo)
            parser.item_add_tag(datos, newTags, aux)
            QMessageBox.information(self, 'Success!',
            'The selected items have been updated',QMessageBox.Ok)

            aux.clear()
            self.ui.addedItems_4.clear()
            self.ui.labelInfoTag.clear()
            newTags = []

    def clickedSectionImp5(self): #Remove tags in sections
        global datos
        if len(self.tagToRemove) == 0:
            QMessageBox.warning(self, 'Warning',
            'You must add tags first!',QMessageBox.Ok)
        else:
            parser = parsejson(self.archivo)
            parser.section_remove_tag(datos, self.tagToRemove, sectionName)
            QMessageBox.information(self, 'Success!',
            'The selected tags have been removed',QMessageBox.Ok)

            sectionName.clear()
            self.ui.addedSections_5.clear()
            self.ui.labelInfoTag_2.clear()
            self.tagToRemove = []


    def clickedItemImp5(self): #Remove tags in items
        global datos
        if len(self.tagToRemove) == 0:
            QMessageBox.warning(self, 'Warning',
            'You must add tags first!',QMessageBox.Ok)
        else:
            parser = parsejson(self.archivo)
            parser.item_remove_tag(datos, self.tagToRemove, self.itemTagsRemove)
            QMessageBox.information(self, 'Success!',
            'The selected tags have been removed',QMessageBox.Ok)
            #self.ui.itemsList_5.clear()
            self.ui.addedItems_5.clear()
            self.ui.labelInfoTag_2.clear()
            self.tagToRemove = []

    def getItemsName(self): #get the name of every item and exports it as a txt file
        global datos
        filePath = ""
        parser = parsejson(self.archivo)
        itemsList = parser.get_items_name(datos)

        file_dialog = QFileDialog()
        file_dialog.setAcceptMode(QFileDialog.AcceptSave)
        file_dialog.setDefaultSuffix(".txt")
        file_dialog.setNameFilters(["Text Files (*.txt)"])
        file_dialog.setWindowTitle("Save Dictionary")

        default_file_name = "itemNames.txt"
        file_dialog.selectFile(default_file_name)

        if file_dialog.exec():
            filePath = file_dialog.selectedFiles()[0]

        if filePath:
            with open(filePath, "w", encoding='utf-8') as file:
                file.write('\n'.join(itemsList))
    
    def clickedADDSNOOZETAGSBUTTON(self): #adds Snooze Tags to all items
        global datos
        parser = parsejson(self.archivo)
        parser.add_snooze_tags(datos)
        QMessageBox.information(self, 'Success!',
        'Snooze tags were added!',QMessageBox.Ok)


#PRICE MODIFICATIONS
    def indexHasChanged(self):
        self.ui.labelInfo2.show()
        if self.ui.priceListSelected.currentIndex() == 0:
            self.ui.rounding.hide()
            self.ui.leIncrease.show()
            self.ui.price.clear()
            self.ui.leIncrease.clear()
            self.ui.leIncrease.setValidator(None)
            self.ui.labelInfo2.setText("Increase or decrease the price in the chosen percentaje. To drecrease use '-'")
        elif self.ui.priceListSelected.currentIndex() == 1:
            self.ui.rounding.hide()
            self.ui.leIncrease.show()
            self.ui.price.clear()
            self.ui.leIncrease.clear()
            self.ui.leIncrease.setValidator(None)
            self.ui.labelInfo2.setText("Increase or decrease the price with the chosen values. To decrease use '-'")
        elif self.ui.priceListSelected.currentIndex() == 2:
            self.ui.rounding.hide()
            self.ui.leIncrease.show()
            self.ui.price.clear()
            self.ui.leIncrease.clear()
            self.ui.leIncrease.setValidator(None)
            self.ui.labelInfo2.setText("Replaces the full price of the item")
        elif self.ui.priceListSelected.currentIndex() == 3:
            self.ui.price.clear()
            self.ui.leIncrease.hide()
            self.ui.rounding.show()
            self.ui.labelInfo2.setText("Rounds the prices up to the next decimal selected.")

#line edit that receives the price or porcentaje to update
    def slot_Increase(self):
        global price
        if self.ui.priceListSelected.currentIndex() == 0:
            aux = self.ui.leIncrease.text()
            if "," in aux:
                aux = aux.replace(",", ".")
            if float(aux) < -100 or float(aux) > 100:
                self.ui.price.setText("The percentaje must be between -100% and 100%")
            elif float(aux) >= -100 or float(aux) <= 100:
                if "E" in aux:
                    aux = aux.split("E")
                    price = float(aux[0].replace(",", "."))
                else:
                    price = float(aux.replace(",", "."))
                self.ui.price.setText("Prices will be updated by " + str(price)+ "%")
        elif self.ui.priceListSelected.currentIndex() == 1:
            aux = self.ui.leIncrease.text()
            if "E" in aux:
                aux = aux.split("E")
                price = float(aux[0].replace(",", "."))
            else:
                price = float(aux.replace(",", "."))
            if price >= 0:
                self.ui.price.setText("Prices will be updated +" + str(price))
            else:
                self.ui.price.setText("Prices will be updated " + str(price))
        elif self.ui.priceListSelected.currentIndex() == 2:
            aux = self.ui.leIncrease.text()
            if "E" in aux:
                aux = aux.split("E")
                price = float(aux[0].replace(",", "."))
            else:
                price = float(aux.replace(",", "."))
            if price >= 0:
                self.ui.price.setText("Prices will be replaced with " + str(price))
            else:
                self.ui.price.setText("The price must be a positive number")

#rounding functions
    def slot_roundingButtons(self):
        global price
        if self.ui.roundTo5.isChecked() == True:
            price = 5
        elif self.ui.roundTo10.isChecked() == True:
            price = 10
        elif self.ui.roundTo99.isChecked() == True:
            price = 99
        elif self.ui.roundToInt.isChecked() == True:
            price = 1

#button that applies new price to the selected sections [PRICES]
    def clickedSectionImp2(self):
        global datos
        global price
        if datos == None:
            QMessageBox.warning(self, 'Warning',
            'You must load a JSON File first!',QMessageBox.Ok)
        else:
            if self.ui.priceListSelected.currentText() == "Replace Price":
                jsonSection.slot_changePriceSelectedSections(jsonSection,datos,sectionName,price,self.ui.modMO.isChecked(),self.ui.modOS.isChecked())
                QMessageBox.information(self, 'Success!',
                'The selected sections have been updated',QMessageBox.Ok)
            elif self.ui.priceListSelected.currentText() == "Increase or Decrease %":
                jsonSection.slot_changePricePercentajeSelectedSections(jsonSection,datos,sectionName,price,self.ui.modMO.isChecked(),self.ui.modOS.isChecked())
                QMessageBox.information(self, 'Success!',
                'The selected sections have been updated',QMessageBox.Ok)
            elif self.ui.priceListSelected.currentText() == "Increase or Decrease Fixed Amount":
                jsonSection.slot_changePriceFixedAmountSelectedSections(jsonSection,datos,sectionName,price,self.ui.modMO.isChecked(),self.ui.modOS.isChecked())
                QMessageBox.information(self, 'Success!',
                'The selected sections have been updated',QMessageBox.Ok)
            elif self.ui.priceListSelected.currentText() == "Round Prices":
                jsonSection.slot_roundPricesSelectedSections(jsonSection,datos,sectionName,price,self.ui.modMO.isChecked(),self.ui.modOS.isChecked())
                QMessageBox.information(self, 'Success!',
                'The selected sections have been updated',QMessageBox.Ok)

        sectionName.clear()
        price = 0
        self.ui.leIncrease.clear()
        self.ui.addedSections_2.clear()

#button that applies new price to the selected items [PRICES]
    def clickedItemImp2(self):
        global datos
        global price
        if datos == None:
            QMessageBox.warning(self, 'Warning',
            'You must load a JSON File first!',QMessageBox.Ok)
        else:
            if self.ui.priceListSelected.currentText() == "Replace Price":
                jsonSection.slot_changePriceSelectedItems(jsonSection,datos,item,price,self.ui.modMO1.isChecked(),self.ui.modSO1.isChecked())
                QMessageBox.information(self, 'Success!',
                'The selected sections have been updated',QMessageBox.Ok)
            elif self.ui.priceListSelected.currentText() == "Increase or Decrease %":
                jsonSection.slot_changePricePercentajeSelectedItems(jsonSection,datos,item,price,self.ui.modMO1.isChecked(),self.ui.modSO1.isChecked())
                QMessageBox.information(self, 'Success!',
                'The selected items have been updated',QMessageBox.Ok)
            elif self.ui.priceListSelected.currentText() == "Increase or Decrease Fixed Amount":
                jsonSection.slot_changePriceFixedAmountSelectedItems(jsonSection,datos,item,price,self.ui.modMO1.isChecked(),self.ui.modSO1.isChecked())
                QMessageBox.information(self, 'Success!',
                'The selected items have been updated',QMessageBox.Ok)
            elif self.ui.priceListSelected.currentText() == "Round Prices":
                jsonSection.slot_roundPricesSelectedItems(jsonSection,datos,item,price,self.ui.modMO1.isChecked(),self.ui.modSO1.isChecked())
                QMessageBox.information(self, 'Success!',
                'The selected items have been updated',QMessageBox.Ok)
        aux.clear()
        item.clear()
        price = 0
        self.ui.leIncrease.clear()
        self.ui.addedItems_2.clear()

#button that applies new price to the selected option OS [PRICES]
    def clickedOSImp2(self):
        global datos
        global price
        if datos == None:
            QMessageBox.warning(self, 'Warning',
            'You must load a JSON File first!',QMessageBox.Ok)
        else:
            if self.ui.priceListSelected.currentText() == "Replace Price":
                jsonSection.slot_changePriceSelectedOS(jsonSection,datos,auxOS,auxOSMaster,price)
                QMessageBox.information(self, 'Success!',
                'The selected sections have been updated',QMessageBox.Ok)
            elif self.ui.priceListSelected.currentText() == "Increase or Decrease %":
                jsonSection.slot_changePricePercentajeSelectedOS(jsonSection,datos,auxOS,auxOSMaster,price)
                QMessageBox.information(self, 'Success!',
                'The selected sections have been updated',QMessageBox.Ok)
            elif self.ui.priceListSelected.currentText() == "Increase or Decrease Fixed Amount":
                jsonSection.slot_changePriceFixedAmountSelectedOS(jsonSection,datos,auxOS,auxOSMaster,price)
                QMessageBox.information(self, 'Success!',
                'The selected sections have been updated',QMessageBox.Ok)
            elif self.ui.priceListSelected.currentText() == "Round Prices":
                jsonSection.slot_roundPricesSelectedOS(jsonSection,datos,auxOS,auxOSMaster,price)
                QMessageBox.information(self, 'Success!',
                'The selected sections have been updated',QMessageBox.Ok)
        osOptions.clear()
        auxOSMaster.clear()
        auxOS.clear()
        price = 0
        self.ui.leIncrease.clear()
        self.ui.addedOS_2.clear()

#button that applies new price to the selected SS items [PRICES]
    def clickedSSImp2(self):
        global datos
        global price
        if datos == None:
            QMessageBox.warning(self, 'Warning',
            'You must load a JSON File first!',QMessageBox.Ok)
        else:
            if self.ui.priceListSelected.currentText() == "Replace Price":
                jsonSection.slot_changePriceSelectedSelectedSS(jsonSection,datos,auxSS,text,price,self.ui.modMO2.isChecked(),self.ui.modSO2.isChecked())
                QMessageBox.information(self, 'Success!',
                'The selected sections have been updated',QMessageBox.Ok)
            elif self.ui.priceListSelected.currentText() == "Increase or Decrease %":
                jsonSection.slot_changePricePercentajeSelectedSS(jsonSection,datos,auxSS,text,price,self.ui.modMO2.isChecked(),self.ui.modSO2.isChecked())
                QMessageBox.information(self, 'Success!',
                'The selected sections have been updated',QMessageBox.Ok)
            elif self.ui.priceListSelected.currentText() == "Increase or Decrease Fixed Amount":
                jsonSection.slot_changePriceFixedAmountSelectedSS(jsonSection,datos,auxSS,text,price,self.ui.modMO2.isChecked(),self.ui.modSO2.isChecked())
                QMessageBox.information(self, 'Success!',
                'The selected sections have been updated',QMessageBox.Ok)
            elif self.ui.priceListSelected.currentText() == "Round Prices":
                jsonSection.slot_roundPricesSelectedSS(jsonSection,datos,auxSS,text,price,self.ui.modMO2.isChecked(),self.ui.modSO2.isChecked())
                QMessageBox.information(self, 'Success!',
                'The selected sections have been updated',QMessageBox.Ok)
        auxSS.clear()
        text.clear()
        price = 0
        self.ui.smartSearchList_2.clear()
        self.ui.leIncrease.clear()
        self.ui.addedSS_2.clear()


#DRINKS MODIFICATION

#button that applies Drinks to the selected sections [DRINKS]
    def clickedSectionImp3(self):
        global datos
        if datos == None: #datos es el JSON cargado
            QMessageBox.warning(self, 'Warning',
            'You must load a JSON File first!',QMessageBox.Ok)
        else:
            if self.ui.imVoucherSM.isChecked() == False and self.ui.imAlcoholSM.isChecked() == False:
                QMessageBox.warning(self, 'Warning',
                'You need to check an option or both',QMessageBox.Ok)
            else:
                VouchersAndAlcohol.slot_changeVoucherAlcoholSelectedSections(VouchersAndAlcohol,datos,sectionName,self.ui.imVoucherSM.isChecked(),self.ui.imAlcoholSM.isChecked() )
                QMessageBox.information(self, 'Success!',
                'The selected sections have been updated',QMessageBox.Ok)

        sectionName.clear()
        self.ui.addedSections_3.clear()

#button that applies Drinks to the selected item [DRINKS]
    def clickedItemImp3(self):
        global datos
        if datos == None: #datos es el JSON cargado
            QMessageBox.warning(self, 'Warning',
            'You must load a JSON File first!',QMessageBox.Ok)
        else:
            if self.ui.imVoucherIM.isChecked() == False and self.ui.imAlcoholIM.isChecked() == False:
                QMessageBox.warning(self, 'Warning',
                'You need to check an option or both',QMessageBox.Ok)
            else:
                VouchersAndAlcohol.slot_changeVoucherAlcoholSelectedItems(VouchersAndAlcohol, datos,item, self.ui.imVoucherIM.isChecked(), self.ui.imAlcoholIM.isChecked())
                QMessageBox.information(self, 'Success!',
                'The selected Items have been updated',QMessageBox.Ok)
        item.clear()
        aux.clear()
        self.ui.addedItems_3.clear()

#button that applies Drinks to the selected item [DRINKS]
    def clickedSSImp3(self):
        global datos
        if datos == None: #datos es el JSON cargado
            QMessageBox.warning(self, 'Warning',
            'You must load a JSON File first!',QMessageBox.Ok)
        else:
            if self.ui.imVoucherSS.isChecked() == False and self.ui.imAlcoholSS.isChecked() == False:
                QMessageBox.warning(self, 'Warning',
                'You need to check an option or both',QMessageBox.Ok)
            else:
                VouchersAndAlcohol.slot_changeVoucherAlcoholSelectedSS(VouchersAndAlcohol, datos,auxSS, text, self.ui.imVoucherSS.isChecked(), self.ui.imAlcoholSS.isChecked())
                QMessageBox.information(self, 'Success!',
                'The selected Items have been updated',QMessageBox.Ok)
        auxSS.clear()
        text.clear()
        self.ui.smartSearchList_3.clear()
        self.ui.addedSS_3.clear()

#transform menu json into POS json.
    def clickedParse_JSON(self):
        global datos
        if datos == None:
            QMessageBox.critical(self, 'Error', 'You must load a Json File first!',QMessageBox.Ok)
        else:
            linkCodes = jsonSection.find_link_codes(jsonSection,datos)

            if not linkCodes: #checks whether a list is empty
                
                nuevojson, _ = QFileDialog.getSaveFileName(self, ("Save JSON"), "", ("JSON file (*.json)"))

                if nuevojson:
                    parser = parsejson(nuevojson)
                    posJSON = parser.slot_generate_new_JSON(datos)
                    #parser.check_and_disable_overrides(posJSON)
                    QMessageBox.information(self, 'Success!','The POS JSON file has been created.',QMessageBox.Ok)

            else:

                QMessageBox.critical(self, 'Error',
                f'Link codes are not allow in POS Menus. You have one in "{linkCodes[0][0]}" Section -> "{linkCodes[0][1]}" Item -> "{linkCodes[0][2]}" Option Set. Delete it and upload the file again.',QMessageBox.Ok)






import json
import uuid

from datetime import datetime, timedelta, date

class parsejson:
    def __init__(self, filePath):

        self.filePath = filePath

    def saveJSON(self, myDict):
        with open(self.filePath, 'w') as outfile:
            json.dump(myDict, outfile, indent=4)

    def generate_UUID(self):
        '''Returns a Universally Unique Identifier'''
        return str(uuid.uuid4())

    def store_name(self, datos):

        '''Returns the name of the store'''
        return datos['Name']

    # def get_tax(self, TaxRateId, datos):

    #     '''Returns the tax value of an item for a given TaxRateId'''
    #     if TaxRateId == None:

    #         return 0

    #     elif TaxRateId in self.tax_rates_dict(datos):

    #         return self.tax_rates_dict(datos)[TaxRateId]

    # def tax_rates_dict(self, datos):

    #     '''Returns a dictionary with the tax rates of the menu'''

    #     if len(datos["TaxRates"]) != 0:

    #         tax_dict = {tax_rate["TaxRateId"]: tax_rate["Rate"] for tax_rate in datos["TaxRates"]}
    #         #print(tax_dict)

    #         return tax_dict

    #     else:

    #         return {} #empty dictionary

    def get_mo_prices(self,optionSet):

        '''Returns a list with the prices of the Master Options of an item'''
        priceList = []

        for price in optionSet['MenuItemOptionSetItems']:

            priceList.append(price['Price'])

        minimumPrice = min(priceList)
        priceList = [x - minimumPrice for x in priceList]
        PriceList =  [float(str(x)[:4]) for x in priceList] #shorten the number of decimal places to two
        #print (roundedPriceList)

        return PriceList

    def get_image(self, url):

        '''Returns the URL of the image of an item'''
        #if imageId == None:
        if url == None:

            return None

        else:

            image = url

            resizedImage = "{}?w={}&h={}".format(image, 225, 255) #resize image to 225x255

            return resizedImage

    def get_name_option_set(self, name):

        if name == None or name == "":
            return "Option"
        else:
            return name

    def get_time_settings_section(self, section):

        timeOptions = section['MenuSectionAvailability']['AvailableTimes']
        nameSection = section['Name']

        return timeOptions, nameSection

    def get_time_settings_item(self, item):

        timeOptions = item['DailySpecialHours']
        nameItem = item['Name']

        return timeOptions, nameItem

    def get_days_mapping(self, dayOfWeek):

        weekDayMapper = {
            0: "sundayEnabled",
            1: "mondayEnabled",
            2: "tuesdayEnabled",
            3: "wednesdayEnabled",
            4: "thursdayEnabled",
            5: "fridayEnabled",
            6: "saturdayEnabled"
        }

        weekDayKey = weekDayMapper[dayOfWeek]

        return weekDayKey

    def get_hours_availability(self, startTimeString, periodString):

        dateNumber = date.today()
        dateString = dateNumber.strftime("%Y-%m-%d")

        timeNumber = datetime.strptime(startTimeString, "%H:%M:%S")
        periodNumber = datetime.strptime(periodString, "%H:%M:%S")

        sumTime = timeNumber + timedelta(hours=periodNumber.hour, minutes=periodNumber.minute, seconds=periodNumber.second)

        sumTimeString = sumTime.strftime(f"{dateString} %H:%M:%S")
        timeNumberWithDate = timeNumber.strftime(f"{dateString} %H:%M:%S")

        return sumTimeString, timeNumberWithDate

    def get_params_to_string(self, weekDayKey, dayAvailability, timeNumberWithDate, sumTimeString, names):

        paramsJson = {
            weekDayKey: dayAvailability,
            "fromTime": timeNumberWithDate,
            "toTime": sumTimeString,
            "name": names,
            "enabled": True
        }

        # paramsJsonToString = json.dumps(paramsJson)
        # return paramsJsonToString

        return paramsJson

    def get_overrides(self, eachTime, name):

        overrides = []
        seenTimeSettings = {}

        if eachTime != None:
            for times in eachTime:

                if times['Period'] == "00:00:00":
                    continue

                weekDayKey = self.get_days_mapping(times['DayOfWeek'])
                sumTimeString, timeNumberWithDate = self.get_hours_availability(
                    times['StartTime'],
                    times['Period']
                )

                key = (timeNumberWithDate, sumTimeString)

                if key in seenTimeSettings:

                    seenTimeSettings[key].append(weekDayKey)

                else:

                    seenTimeSettings[key] = [weekDayKey]

            for timeSetting, weekDays in seenTimeSettings.items():

                newOverride = {
                    "id": self.generate_UUID(),
                    "paramsJson": {
                        "fromTime": timeSetting[0],
                        "toTime": timeSetting[1],
                        "name": f"{name} - hidden",
                        "enabled": True
                    },
                    "type": "generic"
                }

                for day in weekDays:
                    newOverride["paramsJson"][day] = True
                newOverride["paramsJson"] = json.dumps(newOverride["paramsJson"])

                overrides.append(newOverride)

        return overrides

    def get_frecuency(self, id, myDict):
        '''Get frecuency of Option sets throughout the menu.'''
        frecuency = 0
        for categories in myDict["categories"]:
            for item in categories["items"]:
                for modifierMember in item["modifierMembers"]:
                    if modifierMember["modifierId"] == id:
                        frecuency += 1
        return frecuency

    def change_modifiers_name(self, name, id, myDict):
        for modifiers in myDict["modifiers"]:
            if modifiers["id"] == id:
               modifiers["caption"] = "{} - {}".format(modifiers["caption"], name)

    def category_add_tag(self, datos, newTags, selectedSections):

        newTags = list(set(filter(None, newTags))) #eliminate duplicates and empty values
        changeAllExists = "Change All" in selectedSections
        for eachSection in selectedSections:
            for category in datos["categories"]:
                if category["caption"] == eachSection or changeAllExists:
                    for item in category["items"]:
                        self.add_tags_to_item(item, newTags)
    
    def item_add_tag(self, datos, newTags, selectedItems):

        newTags = list(set(filter(None, newTags))) #eliminate duplicates and empty values
        changeAllExists = "Change All" in selectedItems
        for eachItem in selectedItems:
            for category in datos["categories"]:
                for item in category["items"]:
                    if item["caption"] == eachItem or changeAllExists:
                        self.add_tags_to_item(item, newTags)
    

    def add_tags_to_item(self, item, newTags):

        paramsJsonString = item["paramsJson"]
        print(item["caption"], ": ", paramsJsonString)
        paramsJsonDict = json.loads(paramsJsonString) # paso el string dentro de paramsJson a dictionary
        if "stationTags" in paramsJsonDict["kdsConfiguration"]: #Chequea si ya había tags en el menú

            currentTags = paramsJsonDict["kdsConfiguration"]["stationTags"]

            listCurrentTags = currentTags.split(",") #convierto los tags en una lista
            print("Tags presentes en menú: ", listCurrentTags)
            uniqueTags = set(listCurrentTags + newTags)
            newStationTags = ','.join(uniqueTags) # Convierto la lista a string
        else:
            newStationTags = ",".join(newTags) #convierte la lista de tags a string

        paramsJsonDict["kdsConfiguration"]["stationTags"] = newStationTags
        item["paramsJson"] = json.dumps(paramsJsonDict)
        print("Nuevos tags presentes en el menú: ", newStationTags)


    def section_remove_tag(self, datos, tagToRemove, sectionName):

       for i in range(0,len(sectionName)):
            for section in datos["categories"]:
                if section["caption"] == sectionName[i] or sectionName[i] == "Change All":
                    for items in section["items"]:

                        paramsJsonString = items["paramsJson"]
                        print("Item con paramsJson: ",items["caption"], ": ", paramsJsonString)
                        paramsJsonDict = json.loads(paramsJsonString) #paso a diccionario el string paramsJson
                        print("Diccionario: ", paramsJsonDict)

                        if "stationTags" in paramsJsonDict["kdsConfiguration"]: #Chequea si ya había tags en el menú

                            currentTags = paramsJsonDict["kdsConfiguration"]["stationTags"]

                            listCurrentTags = currentTags.split(",") #convierto los tags en una lista
                            print("Tags presentes en el item ", items["caption"], ": ", listCurrentTags)

                            for tag in tagToRemove:
                                if tag in listCurrentTags:
                                    listCurrentTags.remove(tag)

                            print("Tags finales: ", listCurrentTags)
                            newTags = ",".join(listCurrentTags)
                            paramsJsonDict["kdsConfiguration"]["stationTags"] = newTags
                            items["paramsJson"] = json.dumps(paramsJsonDict)
                            print("ParamsJson final: ", items["paramsJson"] )
                        else:
                            pass

    def item_remove_tag(self, datos, tagToRemove, itemsName):
        itemsList = [item.split(': ')[-1] for item in itemsName]  #remove the section name from the item List e.g: ('BURGERS: Cheeseburger') -> ('Cheeseburger')

        for i in range(0,len(itemsList)):
             for section in datos["categories"]:
                     for items in section["items"]:
                         if items["caption"] == itemsList[i] or itemsList[i] == "Change All":

                             paramsJsonString = items["paramsJson"]
                             print("Item con paramsJson: ",items["caption"], ": ", paramsJsonString)
                             paramsJsonDict = json.loads(paramsJsonString) #paso a diccionario el string paramsJson
                             print("Diccionario: ", paramsJsonDict)

                             if "stationTags" in paramsJsonDict["kdsConfiguration"]: #Chequea si ya había tags en el menú

                                 currentTags = paramsJsonDict["kdsConfiguration"]["stationTags"]

                                 listCurrentTags = currentTags.split(",") #convierto los tags en una lista
                                 print("Tags presentes en el item ", items["caption"], ": ", listCurrentTags)

                                 for tag in tagToRemove:
                                     if tag in listCurrentTags:
                                         listCurrentTags.remove(tag)

                                 print("Tags finales: ", listCurrentTags)
                                 newTags = ",".join(listCurrentTags)
                                 paramsJsonDict["kdsConfiguration"]["stationTags"] = newTags
                                 items["paramsJson"] = json.dumps(paramsJsonDict)
                                 print("ParamsJson final: ", items["paramsJson"] )

                             else:
                                 pass
                             
    def retrieve_paramsJson_dict(self, item): 
        paramsJsonString = item['paramsJson']
        paramsJsonDict = json.loads(paramsJsonString)
        #print(paramsJsonDict)
        return paramsJsonDict

    def delete_duplicates_in_list(self, listCurrentSnoozeTags):

        return list(set(listCurrentSnoozeTags))

    def filter_snooze_tags(self, paramsJsonDict): 
        if 'snoozeConfiguration' not in paramsJsonDict:
            paramsJsonDict['snoozeConfiguration'] = {}
        if 'snoozeTags' in paramsJsonDict['snoozeConfiguration']:
            currentSnoozeTags = paramsJsonDict['snoozeConfiguration']['snoozeTags']
            listCurrentSnoozeTags = currentSnoozeTags.split(",")

        else:
            listCurrentSnoozeTags = []
        return listCurrentSnoozeTags
    
    def insert_snooze_tags(self, listCurrentSnoozeTags, paramsJsonDict, item):

        itemWithoutSpaces = item['caption'].replace(" ", "")
        print("Hola")
        if itemWithoutSpaces not in listCurrentSnoozeTags:

            itemFiltered = self.filter_utf8(itemWithoutSpaces)
            print("Sin utf8: ", itemFiltered)
            listCurrentSnoozeTags.append(itemFiltered)
            listCurrentSnoozeTagsWithoutDuplicates = self.delete_duplicates_in_list(listCurrentSnoozeTags)
            print("Lista ", listCurrentSnoozeTagsWithoutDuplicates)
            newTags = ",".join(listCurrentSnoozeTagsWithoutDuplicates)
            print("new snooze tags: ", newTags)
            paramsJsonDict["snoozeConfiguration"]["snoozeTags"] = newTags
            item["paramsJson"] = json.dumps(paramsJsonDict)

    def add_snooze_tags(self, datos):
        for section in datos['categories']:
            for item in section['items']:
                paramsJson = self.retrieve_paramsJson_dict(item)
                listCurrentSnoozeTagsWithoutSpaces = self.filter_snooze_tags(paramsJson)
                self.insert_snooze_tags(listCurrentSnoozeTagsWithoutSpaces, paramsJson, item)

    def slot_generate_new_JSON(self, datos):
        myDict = {
                "franchisorId": self.generate_UUID(),
                "id": self.generate_UUID(),
                "type": "Store",
                "name": self.store_name(datos),
                "notes": None,
                "categories": [],
                "modifiers": []
            }

        for section in datos['MenuSections']:

            newCategory = {
                "id": self.generate_UUID(),
                "caption": section['Name'],
                "enabled": section['IsAvailable'],
                "notes": section["Description"],
                "overrides": [],
                "items": []
            }

            timeAvailabilitySection, nameSection = self.get_time_settings_section(section)
            newCategory['overrides'] = self.get_overrides(timeAvailabilitySection, nameSection)

            for item in section['MenuItems']:

                itemForSnoozeTag = item['Name'].replace(" ", "")

                newItem = {
                    "caption": item['Name'],
                    "enabled": item['IsAvailable'],
                    "id": self.generate_UUID(),
                    "notes": item["Description"],
                    "imageUrl": self.get_image(item["ImageUrl"]),
                    "paramsJson": {
                        "kdsConfiguration": {
                            "kdsCaption": self.filter_utf8(item['Name'])
                        },
                        "snoozeConfiguration": {
                            "snoozeTags": self.filter_utf8(itemForSnoozeTag)
                        }
                    },
                    "overrides": [],
                    "pricingProfiles": [ {
                        "collectionPrice": item['Price'],
                        "collectionTax": 0,
                        "collectionTaxable": True,
                        "deliveryPrice": item['Price'],
                        "deliveryTax": 0,
                        "deliveryTaxable": True,
                        "dineInPrice": item['Price'],
                        "dineInTax": 0,
                        "dineInTaxable": True,
                        "priceBandId": 'cc4efdb0-78a1-11ed-a7b2-713c0ffdd9d3',
                        "takeawayPrice": item['Price'],
                        "takeawayTax": 0,
                        "takeawayTaxable": True
                    } ],
                    "modifierMembers": [],
                }

                newItem["paramsJson"] = json.dumps(newItem["paramsJson"])

                for masterOption in item["MenuItemOptionSets"]:

                    if masterOption["IsMasterOptionSet"] == True:
                        # if item have a master option, its price will be the minimum price of the master option.
                        newItem["pricingProfiles"][0]["collectionPrice"] = masterOption["MinPrice"]
                        newItem["pricingProfiles"][0]["deliveryPrice"] = masterOption["MinPrice"]
                        newItem["pricingProfiles"][0]["dineInPrice"] = masterOption["MinPrice"]
                        newItem["pricingProfiles"][0]["takeawayPrice"] = masterOption["MinPrice"]

                newCategory["items"].append(newItem)

                for modifier in item['MenuItemOptionSets']:

                    new_menuOptionSet = {
                        "caption": self.get_name_option_set(modifier['Name']),
                        "enabled": True,
                        "modifierId": modifier['MenuItemOptionSetId'],
                        "overrides": []
                    }

                    newItem["modifierMembers"].append(new_menuOptionSet)

                for optionSet in item['MenuItemOptionSets']:

                    isMasterOption = optionSet['IsMasterOptionSet'] == True and len(optionSet['MenuItemOptionSetItems']) != 0
                    newOptionSet = { # modifiers
                            "canSameItemBeSelectedMultipleTimes": False,
                            "caption": self.get_name_option_set(optionSet['Name']),
                            "id": optionSet['MenuItemOptionSetId'],
                            "enabled": True,
                            "max": optionSet['MaxSelectCount'],
                            "min": optionSet['MinSelectCount'],
                            "position": optionSet['DisplayOrder'],
                            "overrides": [],
                            "items": []
                        }

                    for index, osItem in enumerate(optionSet['MenuItemOptionSetItems']):

                        # taxValue = self.get_tax(osItem["TaxRateId"], datos) #osItem["TaxRateId"] is the tax id for the osItem
                        # booleano = False if osItem["TaxRateId"] is None else True
                        newItemInOptionSet = { # items inside modifiers
                            "caption": osItem['Name'],
                            "enabled": osItem['IsAvailable'],
                            "id": osItem['MenuItemOptionSetItemId'],
                            "paramsJson": {
                                "kdsConfiguration": {
                                    "kdsCaption": osItem['Name']
                                }
                            },
                            "overrides": [],
                            "pricingProfiles": [ {
                                "collectionPrice": osItem['Price'],
                                "collectionTax": 0,
                                "collectionTaxable": True,
                                "deliveryPrice": osItem['Price'],
                                "deliveryTax": 0,
                                "deliveryTaxable": True,
                                "dineInPrice": osItem['Price'],
                                "dineInTax": 0,
                                "dineInTaxable": True,
                                "priceBandId": 'cc4efdb0-78a1-11ed-a7b2-713c0ffdd9d3',
                                "takeawayPrice": osItem['Price'],
                                "takeawayTax": 0,
                                "takeawayTaxable": True
                            } ],
                            "modifierMembers": []
                        }

                        newItemInOptionSet["paramsJson"] = json.dumps(newItemInOptionSet["paramsJson"])

                        if isMasterOption:
                            priceList = self.get_mo_prices(optionSet)
                            newItemInOptionSet['pricingProfiles'][0]['collectionPrice'] = priceList[index]
                            newItemInOptionSet['pricingProfiles'][0]['deliveryPrice'] = priceList[index]
                            newItemInOptionSet['pricingProfiles'][0]['dineInPrice'] = priceList[index]
                            newItemInOptionSet['pricingProfiles'][0]['takeawayPrice'] = priceList[index]
                        newOptionSet["items"].append(newItemInOptionSet)

                    if isMasterOption:
                        newOptionSet['max'] = 1
                        newOptionSet['min'] = 1
                        newOptionSet['position'] = -1
                    myDict["modifiers"].append(newOptionSet)

                timeAvailabilityItem, nameItem = self.get_time_settings_item(item)
                newItem['overrides'] = self.get_overrides(timeAvailabilityItem, nameItem)

            myDict["categories"].append(newCategory)

        # remove duplicates
        encountered_modifiers = {}

        for j, first_modifier in enumerate(myDict["modifiers"]):
            for second_modifier in myDict["modifiers"][j+1:]:


                if (first_modifier["caption"].lower() == second_modifier["caption"].lower() and
                    len(first_modifier["items"]) == len(second_modifier["items"]) and
                    first_modifier["max"] == second_modifier["max"] and
                    first_modifier["min"] == second_modifier["min"]):

                    first_modifier["items"] = sorted(first_modifier["items"], key=lambda x: x["caption"])
                    second_modifier["items"] = sorted(second_modifier["items"], key=lambda x: x["caption"])

                    flag = 0
                    for i in range(len(first_modifier["items"])):
                        if (first_modifier["items"][i]["caption"] == second_modifier["items"][i]["caption"] and
                            first_modifier["items"][i]["enabled"] == second_modifier["items"][i]["enabled"] and
                            first_modifier["items"][i]["pricingProfiles"][0]["collectionPrice"] == second_modifier["items"][i]["pricingProfiles"][0]["collectionPrice"] and
                            first_modifier["items"][i]["pricingProfiles"][0]["collectionTax"] == second_modifier["items"][i]["pricingProfiles"][0]["collectionTax"]):

                            flag += 1
                            if flag >= len(first_modifier["items"]):
                                # Remove duplicate modifier
                                id_to_remove = second_modifier["id"]
                                encountered_modifiers[id_to_remove] = first_modifier["id"]

        # Replace duplicate modifier id with the original modifier id
        for key in encountered_modifiers:

            if key in encountered_modifiers.values():
                valor = encountered_modifiers[key]
                clave = list(encountered_modifiers.keys())[list(encountered_modifiers.values()).index(key)]
                encountered_modifiers[clave] = valor

        # Remove encountered duplicate modifiers using list comprehension
        myDict["modifiers"] = [modifier for modifier in myDict["modifiers"] if modifier["id"] not in encountered_modifiers]

        if(len(encountered_modifiers) > 0):
            #example output: {51038380: 51038379,
                                #51038381: 51038379,
                                #51038386: 51038379,
                                #51038387: 51038379,
                                #51038388: 51038385}
            for categories in myDict["categories"]:
                for item in categories["items"]:
                    for modifierMember in item["modifierMembers"]:
                        if modifierMember["modifierId"] in encountered_modifiers:
                            modifierMember["modifierId"] = encountered_modifiers[modifierMember["modifierId"]]

        idDictionary = {}
        for modifiers in myDict["modifiers"]:
            idDictionary[modifiers["id"]] = self.get_frecuency(modifiers["id"], myDict)


        #if the OS is unique (frecuency = 1), it will add the name of the item in the OS title.
        for id in idDictionary:
            if idDictionary[id] == 1:
                for categories in myDict["categories"]:
                    for item in categories["items"]:
                        name = item["caption"]
                        for modifierMember in item["modifierMembers"]:
                            if modifierMember["modifierId"] == id:
                                self.change_modifiers_name(name, id, myDict)
                                modifierMember["caption"] = "{} - {}".format(modifierMember["caption"], name)


        #Eliminates hidden sections without items and descriptions.
        for category in myDict["categories"][:]: #The [:] notation creates a shallow copy of the original list,
                                                 #which allows you to iterate over the original list while modifying it.
            if category["enabled"] == False and category["notes"] == None and category["items"] == []:
                myDict["categories"].remove(category)

        self.check_and_disable_overrides(myDict)

        # open the file for writing, and save the dictionary as JSON
        self.saveJSON(myDict)

        return myDict

    def get_items_name(self, datos):
        itemsList = list()
        for section in datos["categories"]:
            for items in section["items"]:
                itemFiltered = self.filter_utf8(items["caption"])
                itemsList.append(itemFiltered)
        itemsListWithoutDuplicates = list(dict.fromkeys(itemsList))
        itemsListWithoutSpaces =  [s.replace(" ", "") for s in itemsListWithoutDuplicates]

        return itemsListWithoutSpaces

    def filter_utf8(self, text):
        filtered_text = ""
        text = text.replace("）", ")")
        text = text.replace("（", "(")
        text = text.replace (",", "")
        for char in text:
            if char.isascii():
                try:
                    char.encode('utf-8')
                    filtered_text += char
                except UnicodeEncodeError:
                    pass
        filtered_text = filtered_text.replace("()", "")
        return filtered_text

    def check_and_disable_overrides(self, myDict):
        #if items or sections have overrides set as enable, then that section or item must be set unavailable.
        #since the override itself will determine the availability of the item/section
        for categories in myDict["categories"]:
            if len(categories["overrides"]) > 0:
                for override in categories["overrides"]:
                    # Check if "paramsJson" is not empty
                    if override["paramsJson"]:
                        paramsJson = json.loads(override["paramsJson"])
                        if paramsJson["enabled"]:
                            categories["enabled"] = False



        for categories in myDict["categories"]:
            for items in categories["items"]:
                if len(items["overrides"]) > 0:
                    for override in items["overrides"]:
                        # Check if "paramsJson" is not empty
                        if override["paramsJson"]:
                            paramsJson = json.loads(override["paramsJson"])
                            if paramsJson["enabled"]:
                                items["enabled"] = False

    def setTaxableTrue(self, datos):
        for categories in datos["categories"]:
            for items in categories["items"]:
                for pricingProfiles in items["pricingProfiles"]:

                    pricingProfiles["collectionTaxable"] = True
                    pricingProfiles["deliveryTaxable"] = True
                    pricingProfiles["dineInTaxable"] = True
                    pricingProfiles["takeawayTaxable"] = True

        for modifiers in datos["modifiers"]:
            for items in modifiers["items"]:
                for pricingProfiles in items["pricingProfiles"]:

                    pricingProfiles["collectionTaxable"] = True
                    pricingProfiles["deliveryTaxable"] = True
                    pricingProfiles["dineInTaxable"] = True
                    pricingProfiles["takeawayTaxable"] = True

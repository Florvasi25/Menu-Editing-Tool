import unittest
import parsejson

class TestParsejson(unittest.TestCase):
    #we inherit from unittest.TestCase
    @classmethod
    def setUpClass(cls):
        cls.parser = parsejson.parsejson()

    def test_generate_UUID(self):
        # test that the UUID generated is a string
        uuid_string = self.parser.generate_UUID()
        self.assertIsInstance(uuid_string, str)
        
    def test_store_name(self):
         # create a dictionary with some test data
        datos = {"Name": "Test Store"}
    
        # test that the store name generated matches the expected result
        name = self.parser.store_name(datos)
        self.assertEqual(name, "Test Store")

    def test_get_tax(self):
         # Test that the function returns 0 when TaxRateId is None
        tax_rate = self.parser.get_tax(None, {})
        self.assertEqual(tax_rate, 0)

        # Test that the function returns a valid tax rate for a given TaxRateId
        #tax_rates = {'1': 0.05, '2': 0.10, '3': 0.15}
        tax_rate = self.parser.get_tax('2', {'TaxRates': [{'TaxRateId': '1', 'Rate': 0.05}, {'TaxRateId': '2', 'Rate': 0.10}, {'TaxRateId': '3', 'Rate': 0.15}]})
        self.assertEqual(tax_rate, 0.10)

    def test_tax_rates_dict(self):
        # test that the function returns a dictionary
        datos = {"TaxRates":[{"TaxRateId": 1, "Name":"tax1","Rate":2.000}]}
        tax_dict = self.parser.tax_rates_dict(datos)
        self.assertIsInstance(tax_dict, dict)

        # test that the dictionary is not empty when there are tax rates in the menu
        self.assertTrue(bool(tax_dict))

    def test_get_mo_prices(self):
        # test that the function returns a list
        optionSet = {'MenuItemOptionSetItems': [{'Price': 5.00}, {'Price': 7.50}, {'Price': 9.00}]}
        price_list = self.parser.get_mo_prices(optionSet)
        self.assertIsInstance(price_list, list)

        # test that the function returns the expected list of prices
        expected_list = [0.0, 2.5, 4.0]
        self.assertEqual(price_list, expected_list)

    def test_get_image(self):
        # test that the function returns None when imageId is None
        image_url = self.parser.get_image(None)
        self.assertIsNone(image_url)

        # test that the function returns a valid resized image URL when imageId is not None
        item = 'https://example.com/image.jpg'
        image_url = self.parser.get_image(item)
        self.assertEqual(image_url, 'https://example.com/image.jpg?w=225&h=255')

    def test_get_name_option_set(self):
        # test that the function returns "Option" when name is None or empty string
        name_option_set = self.parser.get_name_option_set(None)
        self.assertEqual(name_option_set, 'Option')

        name_option_set = self.parser.get_name_option_set('')
        self.assertEqual(name_option_set, 'Option')

        # test that the function returns the input name when it is not None or empty string
        name_option_set = self.parser.get_name_option_set('Extra Cheese')
        self.assertEqual(name_option_set, 'Extra Cheese')

    def setUp(self):
        # example section for testing
        self.section = {
            "Name": "Breakfast",
            "MenuSectionAvailability": {
                "AvailableTimes": [
                    {
                        "DayOfWeek": 1,
                        "StartTime": "06:00:00",
                        "Period": "03:00:00"
                    },
                    {
                        "DayOfWeek": 2,
                        "StartTime": "07:00:00",
                        "Period": "02:30:00"
                    }
                ]
            }
        }
        # example item for testing
        self.item = {
            "Name": "Special omelette",
            "DailySpecialHours": {
                "StartTime": "08:00:00",
                "Period": "01:30:00"
            }
        }

    def test_get_time_settings_section(self):

        timeOptions, nameSection = self.parser.get_time_settings_section(self.section)
        self.assertEqual(nameSection, "Breakfast")
        self.assertEqual(len(timeOptions), 2)
        self.assertEqual(timeOptions[0]["DayOfWeek"], 1)
        self.assertEqual(timeOptions[0]["StartTime"], "06:00:00")
        self.assertEqual(timeOptions[0]["Period"], "03:00:00")

    def test_get_time_settings_item(self):

        timeOptions, nameItem = self.parser.get_time_settings_item(self.item)
        self.assertEqual(nameItem, "Special omelette")
        self.assertEqual(timeOptions["StartTime"], "08:00:00")
        self.assertEqual(timeOptions["Period"], "01:30:00")

    def test_get_days_mapping(self):

        self.assertEqual(self.parser.get_days_mapping(0), "sundayEnabled")
        self.assertEqual(self.parser.get_days_mapping(1), "mondayEnabled")
        self.assertEqual(self.parser.get_days_mapping(2), "tuesdayEnabled")
        self.assertEqual(self.parser.get_days_mapping(3), "wednesdayEnabled")
        self.assertEqual(self.parser.get_days_mapping(4), "thursdayEnabled")
        self.assertEqual(self.parser.get_days_mapping(5), "fridayEnabled")
        self.assertEqual(self.parser.get_days_mapping(6), "saturdayEnabled")

    def test_get_hours_availability(self):

        startTimeString = "09:30:00"
        periodString = "02:15:00"
        sumTimeString, timeNumberWithDate = self.parser.get_hours_availability(startTimeString, periodString)
        self.assertEqual(timeNumberWithDate, "2023-03-14 09:30:00")
        self.assertEqual(sumTimeString, "2023-03-14 11:45:00")

        
if __name__ == '__main__':
    unittest.main()

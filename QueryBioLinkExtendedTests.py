import unittest
from QueryBioLinkExtended import QueryBioLinkExtended as QBLEx
import json


def get_from_test_file(key):
    f = open('test_data.json', 'r')
    test_data = f.read()
    try:
        test_data_dict = json.loads(test_data)
        print(test_data_dict)
        f.close()
        return test_data_dict[key]
    except ValueError:
        f.close()
        return None

class QueryBioLinkExtendedTestCase(unittest.TestCase):


    def test_get_anatomy_entity(self):
        extended_info_json = QBLEx.get_anatomy_entity('UBERON:0004476')
        self.assertIsNotNone(extended_info_json)
        self.assertEqual(extended_info_json, get_from_test_file('anatomy'))

    def test_get_phenotype_entity(self):
        extended_info_json = QBLEx.get_phenotype_entity('HP:0011515')
        self.assertIsNotNone(extended_info_json)
        self.assertEqual(extended_info_json, get_from_test_file('phenotype'))

    def test_get_disease_entity(self):
        extended_info_json = QBLEx.get_disease_entity('DOID:3965')
        self.assertIsNotNone(extended_info_json)
        self.assertEqual(extended_info_json, get_from_test_file('disease'))

    def test_get_bio_process_entity(self):
        extended_info_json = QBLEx.get_bio_process_entity('GO:0097289')
        self.assertIsNotNone(extended_info_json)
        self.assertEqual(extended_info_json, get_from_test_file('bio_process'))


if __name__ == '__main__':
    unittest.main()
"""
    Run this module outside `tests` folder.
        $ cd [git repo]/code/reasoningtool/
        $ python3 -m unittest tests/UpdateNodesInfoTests.py
"""

import unittest
import json
import random

import os,sys
parentdir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0,parentdir)

from Neo4jConnection import Neo4jConnection
from QueryMyChem import QueryMyChem


def random_int_list(start, stop, length):
    start, stop = (int(start), int(stop)) if start <= stop else (int(stop), int(start))
    length = int(abs(length)) if length else 0
    random_list = []
    for i in range(length):
        random_list.append(random.randint(start, stop))
    return random_list


class UpdateNodesInfoTestCase(unittest.TestCase):

    def test_update_chemical_substance_entity(self):
        f = open('config.json', 'r')
        config_data = f.read()
        f.close()
        config = json.loads(config_data)

        conn = Neo4jConnection(config['url'], config['username'], config['password'])
        nodes = conn.get_chemical_substance_nodes()

        # generate random number array
        random_indexes = random_int_list(0, len(nodes)-1, 100)

        for i in random_indexes:
            #   retrieve data from Neo4j
            node_id = nodes[i]
            extended_info_json_from_api = QueryMyChem.get_chemical_substance_entity(node_id)
            self.assertIsNotNone(extended_info_json_from_api)

            # retrieve phenotype entities from BioLink API
            node = conn.get_chemical_substance_node(node_id)
            self.assertIsNotNone(node['n']['name'])
            self.assertIsNotNone(node['n']['extended_info_json'])
            self.assertEqual(node_id, node['n']['name'])
            self.maxDiff = None
            # self.assertEqual(extended_info_json_from_api, node['n']['extended_info_json'])
            if node['n']['extended_info_json'] != "UNKNOWN":
                self.assertEqual(json.loads(extended_info_json_from_api), json.loads(node['n']['extended_info_json']))

        conn.close()


if __name__ == '__main__':
    unittest.main()


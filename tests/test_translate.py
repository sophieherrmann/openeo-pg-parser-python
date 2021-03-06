import os
import unittest
from openeo_pg_parser.translate import translate_process_graph


class TranslateTester(unittest.TestCase):
    """  Testing the module `translate` for different process graph translations. """

    def setUp(self):
        """ Setting up variables for one test. """
        self.pg_dirpath = os.path.join(os.path.dirname(__file__), 'process_graphs')
        self.uc1_polarization_pg_filepath = os.path.join(self.pg_dirpath, "s1_uc1_polarization.json")
        self.non_existing_filepath = os.path.join(self.pg_dirpath, "does_not_exist.json")

    def test_translate_process_graph(self):
        """ Translates a process graph from openEO syntax to a Python traversable object. """

        graph = translate_process_graph(self.uc1_polarization_pg_filepath)
        print(graph)
        assert True

    def test_process_graph_not_found(self):
        """ Checks if an error is thrown when a process graph file cannot be found. """

        try:
            translate_process_graph(self.non_existing_filepath)
        except FileNotFoundError:
            assert True

    def test_from_global_parameter(self):
        """ Tests parsing of a globally defined parameter. """
        global_parameter_filepath = os.path.join(self.pg_dirpath, "s2_max_ndvi_global_parameter.json")
        parameters = {'test_from_parameter': 3}
        graph = translate_process_graph(global_parameter_filepath, parameters=parameters)

        assert graph['ndvi_6'].arguments['y'] == 3

    def test_from_local_parameter(self):
        """ Tests parsing of a locally defined parameter. """
        local_parameter_filepath = os.path.join(self.pg_dirpath, "s2_max_ndvi_local_parameter.json")
        graph = translate_process_graph(local_parameter_filepath)

        assert graph['ndvi_6'].arguments['y'] == 3


if __name__ == '__main__':
    unittest.main()
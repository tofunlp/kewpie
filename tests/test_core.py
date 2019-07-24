from unittest import TestCase

from kewpie.core import Core


class CoreCase(TestCase):

    def setUp(self):
        self.core = Core()
        pass

    def tearDown(self):
        pass

    def test_core(self):
        self.assertEqual(self.core.say(), "Hola mundo!")

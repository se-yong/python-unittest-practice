import unittest

class MyCalcTest(unittest.TestCase):
    def setUp(self):
        print("1. Executing the setUp method")
        self.fixture = { 'a' : 1 }
    
    def tearDown(self):
        print("3. Executing the tearDown method")
        self.fixture = None

    def test_fixture(self):
        print("2. Executing the test_fixture method")
        self.assertEqual(self.fixture['a'], 1)

unittest.main()
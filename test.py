import unittest
import mycalc

class MyCalcTest(unittest.TestCase):
    def test_add(self):
        c = mycalc.add(20,10)
        self.assertEqual(c, 30)

    def test_substract(self):
        c = mycalc.substract(20, 10)
        self.assertEqual(c, 10)
    
    def test_add_error(self):
        c = mycalc.add(20,10)
        self.assertEqual(c, 35)
    
    def test_substarct_error(self):
        c = mycalc.substract(20, 10)
        self.assertEqual(c, 15)
    
if __name__ == '__main__':
    unittest.main()

# 터미널 테스트 실행 명령어 python -m unittest --v 
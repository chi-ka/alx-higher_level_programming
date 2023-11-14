#!/usr/bin/python3

class TestSquare(unittest.TestCase):
    def test_init(self):
        square = Square(5, 2, 3, 4)
        self.assertEqual(square.size, 5)
        self.assertEqual(square.x, 2)
        self.assertEqual(square.y, 3)
        self.assertEqual(square.id, 4)

    def test_size_setter(self):
        square = Square(5)
        square.size = 10
        self.assertEqual(square.size, 10)

if __name__ == '__main__':
    unittest.main()

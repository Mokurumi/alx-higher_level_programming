#!/usr/bin/python3
'''
module for testing the rectangle class
'''


import unittest
import os
from models.rectangle import Rectangle
from models.base import Base
from models.square import Square


class TestSquare(unittest.TestCase):
    def setUp(self):
       Base._Base__nb_objects = 0

    def tearDown(self):
        try:
            os.remove("Square.json")
        except FileNotFoundError:
            pass

    def test_valid_attributes(self):
        obj = Square(5, 1, 2, 42)
        self.assertEqual(obj.id, 42)
        self.assertEqual(obj.size, 5)
        self.assertEqual(obj.x, 1)
        self.assertEqual(obj.y, 2)

    def test_default_attributes(self):
        obj = Square(5)
        self.assertEqual(obj.id, 1)
        self.assertEqual(obj.size, 5)
        self.assertEqual(obj.x, 0)
        self.assertEqual(obj.y, 0)

    def test_size_type_error(self):
        with self.assertRaises(TypeError):
            obj = Square("invalid")

    def test_size_value_error(self):
        with self.assertRaises(ValueError):
            obj = Square(0)

    def test_area(self):
        obj = Square(5)
        self.assertEqual(obj.area(), 25)

    """
    def test_display(self):
        obj = Square(2, 1, 1)
        expected_output = " #\n #\n"
        with unittest.mock.patch('sys.stdout', new_callable=io.StringIO) as mock_stdout:
            obj.display()
            self.assertEqual(mock_stdout.getvalue(), expected_output)
    """

    def test_str(self):
        obj = Square(3, 1, 2, 42)
        self.assertEqual(str(obj), "[Square] (42) 1/2 - 3")

    def test_update_args(self):
        obj = Square(1, 2, 3, 42)
        obj.update(5, 6, 7, 8)
        self.assertEqual(obj.id, 5)
        self.assertEqual(obj.size, 6)
        self.assertEqual(obj.x, 7)
        self.assertEqual(obj.y, 8)

    def test_update_kwargs(self):
        obj = Square(1, 2, 3, 42)
        obj.update(id=5, size=6, x=7, y=8)
        self.assertEqual(obj.id, 5)
        self.assertEqual(obj.size, 6)
        self.assertEqual(obj.x, 7)
        self.assertEqual(obj.y, 8)

    def test_to_dictionary(self):
        obj = Square(3, 1, 2, 42)
        expected_dict = {
            "id": 42,
            "size": 3,
            "x": 1,
            "y": 2
        }
        self.assertEqual(obj.to_dictionary(), expected_dict)

    def test_save_to_file(self):
        obj1 = Square(1, 1, 1, 1)
        obj2 = Square(2, 2, 2, 2)
        Square.save_to_file([obj1, obj2])
        with open("Square.json", "r") as file:
            content = file.read()
        expected_json = '[{"id": 1, "size": 1, "x": 1, "y": 1}, ' \
                        '{"id": 2, "size": 2, "x": 2, "y": 2}]'
        self.assertEqual(content, expected_json)

    def test_load_from_file(self):
        obj1 = Square(1, 1, 1, 1)
        obj2 = Square(2, 2, 2, 2)
        Square.save_to_file([obj1, obj2])
        instances = Square.load_from_file()
        self.assertEqual(len(instances), 2)
        self.assertEqual(instances[0].id, 1)
        self.assertEqual(instances[1].id, 2)

    def test_invalid_size_type(self):
        with self.assertRaises(TypeError):
            obj = Square(1, "2")

    def test_invalid_x_type(self):
        with self.assertRaises(TypeError):
            obj = Square(1, 2, "3")

    def test_negative_size_value(self):
        with self.assertRaises(ValueError):
            obj = Square(-1)

    def test_negative_x_value(self):
        with self.assertRaises(ValueError):
            obj = Square(1, -2)

    def test_negative_y_value(self):
        with self.assertRaises(ValueError):
            obj = Square(1, 2, -3)

    def test_save_to_file_with_none(self):
        Square.save_to_file(None)
        with open("Square.json", "r") as file:
            content = file.read()
        self.assertEqual(content, "[]")

    def test_save_to_file_with_empty_list(self):
        Square.save_to_file([])
        with open("Square.json", "r") as file:
            content = file.read()
        self.assertEqual(content, "[]")

if __name__ == '__main__':
    unittest.main()

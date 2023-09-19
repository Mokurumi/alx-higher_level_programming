#!/usr/bin/python3
'''
module for testing the rectangle class
'''


import unittest
import unittest.mock
import os
import io
from models.rectangle import Rectangle
from models.base import Base


class TestRectangle(unittest.TestCase):
    """
    models/rectangle tests
    """

    def setUp(self):
        Base._Base__nb_objects = 0

    def tearDown(self):
        try:
            os.remove("Rectangle.json")
        except FileNotFoundError:
            pass

    def test_valid_attributes(self):
        obj = Rectangle(10, 20, 1, 2, 42)
        self.assertEqual(obj.id, 42)
        self.assertEqual(obj.width, 10)
        self.assertEqual(obj.height, 20)
        self.assertEqual(obj.x, 1)
        self.assertEqual(obj.y, 2)

    def test_default_attributes(self):
        obj = Rectangle(10, 20)
        self.assertEqual(obj.id, 1)
        self.assertEqual(obj.width, 10)
        self.assertEqual(obj.height, 20)
        self.assertEqual(obj.x, 0)
        self.assertEqual(obj.y, 0)

    def test_width_type_error(self):
        with self.assertRaises(TypeError):
            obj = Rectangle("invalid", 20)

    def test_width_value_error(self):
        with self.assertRaises(ValueError):
            obj = Rectangle(-10, 20)

    def test_height_type_error(self):
        with self.assertRaises(TypeError):
            obj = Rectangle(10, "invalid")

    def test_height_value_error(self):
        with self.assertRaises(ValueError):
            obj = Rectangle(10, -20)

    def test_x_type_error(self):
        with self.assertRaises(TypeError):
            obj = Rectangle(10, 20, "invalid")

    def test_x_value_error(self):
        with self.assertRaises(ValueError):
            obj = Rectangle(10, 20, -1)

    def test_y_type_error(self):
        with self.assertRaises(TypeError):
            obj = Rectangle(10, 20, 1, "invalid")

    def test_y_value_error(self):
        with self.assertRaises(ValueError):
            obj = Rectangle(10, 20, 1, -2)

    def test_area(self):
        obj = Rectangle(5, 10)
        self.assertEqual(obj.area(), 50)

    def test_display(self):
        obj = Rectangle(2, 3, 1, 1)
        expected_output = "\n" \
                          " ##\n" \
                          " ##\n" \
                          " ##\n"
        with unittest.mock.patch(
                'sys.stdout', new_callable=io.StringIO
                ) as mock_stdout:
            obj.display()
            self.assertEqual(mock_stdout.getvalue(), expected_output)

    def test_display_without_x_and_y(self):
        obj = Rectangle(2, 3)
        expected_output = "##\n" \
                          "##\n" \
                          "##\n"
        with unittest.mock.patch(
                'sys.stdout', new_callable=io.StringIO
                ) as mock_stdout:
            obj.display()
            self.assertEqual(mock_stdout.getvalue(), expected_output)

    def test_display_without_y(self):
        obj = Rectangle(2, 3, 1)
        expected_output = " ##\n" \
                          " ##\n" \
                          " ##\n"
        with unittest.mock.patch(
                'sys.stdout', new_callable=io.StringIO
                ) as mock_stdout:
            obj.display()
            self.assertEqual(mock_stdout.getvalue(), expected_output)

    def test_display_width_zero(self):
        with self.assertRaises(ValueError):
            obj = Rectangle(0, 2)

    def test_display_height_zero(self):
        with self.assertRaises(ValueError):
            obj = Rectangle(1, 0)

    def test_str(self):
        obj = Rectangle(3, 4, 1, 2, 42)
        self.assertEqual(str(obj), "[Rectangle] (42) 1/2 - 3/4")

    def test_update_args(self):
        obj = Rectangle(1, 2, 3, 4, 42)
        obj.update(5, 6, 7, 8, 9)
        self.assertEqual(obj.id, 5)
        self.assertEqual(obj.width, 6)
        self.assertEqual(obj.height, 7)
        self.assertEqual(obj.x, 8)
        self.assertEqual(obj.y, 9)

    def test_update_kwargs(self):
        obj = Rectangle(1, 2, 3, 4, 42)
        obj.update(id=5, width=6, height=7, x=8, y=9)
        self.assertEqual(obj.id, 5)
        self.assertEqual(obj.width, 6)
        self.assertEqual(obj.height, 7)
        self.assertEqual(obj.x, 8)
        self.assertEqual(obj.y, 9)

    def test_to_dictionary(self):
        obj = Rectangle(3, 4, 1, 2, 42)
        expected_dict = {
            "id": 42,
            "width": 3,
            "height": 4,
            "x": 1,
            "y": 2
        }
        self.assertEqual(obj.to_dictionary(), expected_dict)

    def test_save_to_file(self):
        obj1 = Rectangle(1, 2, 3, 4, 1)
        obj2 = Rectangle(5, 6, 7, 8, 2)
        Rectangle.save_to_file([obj1, obj2])
        with open("Rectangle.json", "r") as file:
            content = file.read()
        expected_json = '[{"id": 1, "width": 1, "height": 2, "x": 3, "y": 4}, ' \
                        '{"id": 2, "width": 5, "height": 6, "x": 7, "y": 8}]'
        self.assertEqual(content, expected_json)

    def test_save_to_file_with_none(self):
        # Call save_to_file(None)
        Rectangle.save_to_file(None)

        # Check if the "Rectangle.json" file is empty
        with open("Rectangle.json", "r") as file:
            file_contents = file.read()
        self.assertEqual(file_contents, "[]")

    def test_load_from_file(self):
        obj1 = Rectangle(1, 2, 3, 4, 1)
        obj2 = Rectangle(5, 6, 7, 8, 2)
        Rectangle.save_to_file([obj1, obj2])
        instances = Rectangle.load_from_file()
        self.assertEqual(len(instances), 2)
        self.assertEqual(instances[0].id, 1)
        self.assertEqual(instances[1].id, 2)

if __name__ == '__main__':
    unittest.main()

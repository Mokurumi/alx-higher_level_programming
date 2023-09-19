#!/usr/bin/python3
'''
module for testing the base class
'''


import unittest
import os
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square


class TestBase(unittest.TestCase):
    """
    tests for model/base
    """

    def setUp(self):
        Base._Base__nb_objects = 0

    def tearDown(self):
        try:
            os.remove("Base.json")
        except FileNotFoundError:
            pass

    def test_id_given(self):
        obj = Base(42)
        self.assertEqual(obj.id, 42)

    def test_id_not_given(self):
        obj1 = Base()
        obj2 = Base()
        self.assertEqual(obj1.id, 1)
        self.assertEqual(obj2.id, 2)

    def test_private_attr_access(self):
        obj = Base()
        with self.assertRaises(AttributeError):
            obj.__nb_objects

    """
    def test_invalid_args(self):
        with self.assertRaises(TypeError):
            obj = Base("invalid_argument")
    """

    def test_class(self):
        obj = Base()
        self.assertEqual(obj.__class__.__name__, "Base")

    def test_to_json_string(self):
        obj = Base(1)
        json_string = obj.to_json_string([{"id": 1}])
        self.assertEqual(json_string, '[{"id": 1}]')

    def test_none_to_json_string(self):
        obj = Base()
        json_string = obj.to_json_string(None)
        self.assertEqual(json_string, "[]")

    def test_empty_to_json_string(self):
        obj = Base()
        json_string = obj.to_json_string([])
        self.assertEqual(json_string, "[]")

    def test_from_json_string(self):
        obj = Base()
        instance_list = obj.from_json_string('[{"id": 1}]')
        self.assertEqual(instance_list, [{"id": 1}])

    def test_from_none_json_string(self):
        obj = Base()
        instance_list = obj.from_json_string(None)
        self.assertEqual(instance_list, [])

    def test_from_empty_json_string(self):
        obj = Base()
        instance_list = obj.from_json_string("[]")
        self.assertEqual(instance_list, [])

    def test_create(self):
        obj = Rectangle(1, 1)  # Use Rectangle as an example
        dummy_dict = {"id": 42, "width": 2, "height": 3}
        instance = obj.create(**dummy_dict)
        self.assertEqual(instance.id, 42)
        self.assertEqual(instance.width, 2)
        self.assertEqual(instance.height, 3)

    def test_create_square(self):
        obj = Square(1)  # Use Square as an example
        dummy_dict = {"id": 1, "size": 5}
        instance = obj.create(**dummy_dict)
        self.assertEqual(instance.id, 1)
        self.assertEqual(instance.size, 5)

    """
    def test_save_to_file(self):
        obj = Rectangle(1, 1)  # Use Rectangle as an example
        obj.save_to_file([obj.create(id=1, width=2, height=3)])
        with open("Rectangle.json", "r") as file:
            content = file.read()
        self.assertEqual(content, '[{"id": 1, "width": 2, "height": 3}]')

    def test_save_to_file_multiple(self):
        obj = Rectangle(1, 1)  # Use Rectangle as an example
        obj.save_to_file([
            obj.create(id=1, width=2, height=3),
            obj.create(id=2, width=4, height=5)
        ])
        with open("Rectangle.json", "r") as file:
            content = file.read()
        self.assertEqual(content, '[{"id": 1, "width": 2, "height": 3}, {"id": 2, "width": 4, "height": 5}]')
    """

    def test_save_to_file_empty(self):
        obj = Rectangle(1, 1)  # Use Rectangle as an example
        obj.save_to_file([])
        with open("Rectangle.json", "r") as file:
            content = file.read()
        self.assertEqual(content, "[]")

    """
    def test_load_from_file_nonexistent(self):
        obj = Rectangle(1, 1)  # Use Rectangle as an example
        instances = obj.load_from_file()
        self.assertEqual(len(instances), 0)
    """
    
    def test_load_from_file(self):
        obj = Rectangle(1, 1)  # Use Rectangle as an example
        obj.save_to_file([obj.create(**{"id": 1, "width": 2, "height": 3})])
        instances = obj.load_from_file()
        self.assertEqual(len(instances), 1)
        self.assertEqual(instances[0].id, 1)
        self.assertEqual(instances[0].width, 2)
        self.assertEqual(instances[0].height, 3)

    def test_load_from_file_multiple(self):
        obj = Rectangle(1, 1)  # Use Rectangle as an example
        obj.save_to_file([
            obj.create(**{"id": 1, "width": 2, "height": 3}),
            obj.create(**{"id": 2, "width": 4, "height": 5})
        ])
        instances = obj.load_from_file()
        self.assertEqual(len(instances), 2)
        self.assertEqual(instances[0].id, 1)
        self.assertEqual(instances[1].id, 2)
        self.assertEqual(instances[0].width, 2)
        self.assertEqual(instances[1].width, 4)
        self.assertEqual(instances[0].height, 3)
        self.assertEqual(instances[1].height, 5)


    def test_load_from_file_empty(self):
        obj = Rectangle(1, 1)  # Use Rectangle as an example
        obj.save_to_file([])
        instances = obj.load_from_file()
        self.assertEqual(len(instances), 0)

if __name__ == '__main__':
    unittest.main()

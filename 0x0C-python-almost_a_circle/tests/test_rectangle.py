# import unittest
# from models.rectangle import Rectangle
# from unittest.mock import patch

# class TestRectangle(unittest.TestCase):
#     def setUp(self):
#         self.rectangle = Rectangle(4, 6, 2, 3, 1)

#     def test_area(self):
#         self.assertEqual(self.rectangle.area(), 24)

#     def test_display(self):
#         expected_output = "  ##\n  ##\n  ##\n  ##\n  ##\n  ##\n"
#         with patch("builtins.print") as mock_print:
#             self.rectangle.display()
#             mock_print.assert_called_with(expected_output)

#     def test_str(self):
#         expected_output = "[Rectangle] (1) 2/3 - 4/6"
#         self.assertEqual(str(self.rectangle), expected_output)

#     def test_update_args(self):
#         self.rectangle.update(2, 8, 10, 5, 7)
#         self.assertEqual(self.rectangle.id, 2)
#         self.assertEqual(self.rectangle.width, 8)
#         self.assertEqual(self.rectangle.height, 10)
#         self.assertEqual(self.rectangle.x, 5)
#         self.assertEqual(self.rectangle.y, 7)

#     def test_update_kwargs(self):
#         self.rectangle.update(id=2, width=8, height=10, x=5, y=7)
#         self.assertEqual(self.rectangle.id, 2)
#         self.assertEqual(self.rectangle.width, 8)
#         self.assertEqual(self.rectangle.height, 10)
#         self.assertEqual(self.rectangle.x, 5)
#         self.assertEqual(self.rectangle.y, 7)

#     def test_to_dictionary(self):
#         expected_dict = {
#             'id': 1,
#             'width': 4,
#             'height': 6,
#             'x': 2,
#             'y': 3
#         }
#         self.assertEqual(self.rectangle.to_dictionary(), expected_dict)

#     def test_create_rectangle(self):
#         rectangle = Rectangle(4, 6, 2, 3, 1)
#         self.assertEqual(rectangle.width, 4)
#         self.assertEqual(rectangle.height, 6)
#         self.assertEqual(rectangle.x, 2)
#         self.assertEqual(rectangle.y, 3)
#         self.assertEqual(rectangle.id, 1)

#

# if __name__ == '__main__':
#     unittest.main()


import unittest
from tkinter.ttk import Widget


class MyTestCase(unittest.TestCase):
       def test_something(self):
        widget = Widget("The widget")
        assert widget.size() == (50, 50), 'incorrect default size'


if __name__ == '__main__':
    unittest.main()

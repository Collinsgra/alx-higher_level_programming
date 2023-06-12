#!/usr/bin/python3
"""this defines class MyInt which acquire from integer"""


class MyInt(int):
    """change integer operator == and !="""

    def __eq__(self, value):
        """rewrite == operator to != """
        return self.real != value

    def __ne__(self, value):
        """rewrite != operator to =="""
        return self.real == value

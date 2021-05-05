import csv
import change as change
import pandas as pd

class Customer:
    def __init__(self, name, password, discount_code, role):
        """

        :param name:
        :param password:
        :param discount_code:
        :param role:
        """
        self.name = name
        self.password = password
        self.discount_cod = discount_code
        self.role = role


    def __str__(self):
        return f"{self.name} is name"

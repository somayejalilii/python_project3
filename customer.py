import csv
import sys
from turtle import pd
import loger


class Customer:
    def __init__(self, name, password, discount_code, discount_percent, role):
        """
        Client class has name and password features of
        discount code and customer nature
        :param name:
        :param password:
        :param discount_code:
        :param role:
        """
        self.name = name
        self.password = password
        self.discount_cod = discount_code
        self.discount_percent = discount_percent
        self.role = role

    def buy_ticket(self, discount_percent, discount_code, role):
        """
        In this method, the ticket code and number of users are received from the user and,
         if having a discount code,
          is calculated with a discount percentage,
            and otherwise the price is calculated without discounts.
             The CSV file is updated after each purchase
        :param discount_percent:
        :param discount_code:
        :param role:
        :return:
        """
        self.role = role
        try:
            file_list = "list1.csv"
            location = 0
            row_n = int(input("To purchase tickets, enter the purchase code "))
            number_ticket = int(input("number ticket : "))
            change = pd.read_csv('list1.csv')
            with open(file_list, 'r') as csv_file:
                csv_reader = csv.DictReader(csv_file)
                for row in csv_reader:
                    if int(row['capacity_residual_event']) < int(number_ticket):
                        change_capacity = int(row['capacity_residual_event']) - int(number_ticket)
                        change.loc[location, 'capacity_residual_event'] = change_capacity
                        change.to_csv('list1.csv', index=False)
                    else:
                        print("The number entered is more than the ticket capacity ")
                        sys.exit()
                    location += 1
        except Exception:
            print("The number entered is more than the ticket capacity ")
            sys.exit()
        try:
            cod = int(input("If you have a discount code, 1 and otherwise, enter the number 2 :"))
            if cod == 2:
                dis_cod = int(input("If you have a discount code, enter it : "))
                with open('role.csv', 'r+') as event_file:
                    try:
                        csv_reader = csv.DictReader(event_file)
                        for row in csv_reader:
                            if dis_cod == row[discount_code]:
                                cost = row["cost_event"] * number_ticket
                                print("Latacia", cost, "Deposit")
                            else:
                                print("The entered code is not correct")
                                sys.exit()
                    except Exception:
                        print("The entered code is not correct")
                        sys.exit()
            elif cod == 1:
                cost = row_n["cost_event"] * number_ticket - (((row_n['cost_event'] * number_ticket) * discount_percent) / 100)
                print("Latacia", cost, "Deposit")
                return f"Your ticket amount by discounting", {self.role}, "is", cost
            loger.my_logger.info(f"{row_n}is created")
        except Exception:
            print("The entered option is not correct !!")
            sys.exit()

    def __str__(self):
        return

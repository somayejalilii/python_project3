import csv

import pandas as pd


class Ticket:
    def __init__(self, discount_code, name_event, expdate_event, time_event, cost_event, capacity_residual_event,
                 capacity_total_event, place_event):
        self.name_event = name_event
        self.expdate_event = expdate_event
        self.time_event = time_event
        self.capacity_total_event = capacity_total_event
        self.capacity_residual_event = capacity_residual_event
        self.place_event = place_event
        self.cost_event = cost_event
        self.discount_cod = discount_code


@staticmethod
def buy_ticket(obj_ticket, num_row):
    file_list = "list.csv"
    df_list = pd.read_csv(file_list)
    num_row = input("To purchase tickets, enter the purchase code ")
    with open('list.csv', 'a') as my_file:
        readData = [row for row in csv.DictReader(my_file)]
        df = pd.read_csv(df_list)
        df2 = df.iloc("capacity_residual_event")
        if df2 != 0:
            obj_ticket = input("number ticket")
            obj_ticket2 = (df2 - obj_ticket)
            readData[num_row]["capacity_residual_event"] = obj_ticket2
            csv_writer = csv.writer(my_file)
            csv_writer.writerows(obj_ticket2)
        else:
            print("The capacity is completed")
        df_cost = df.iloc("cost_event")
        cost = (df2 * df_cost)
        print("Latacia", cost, "Deposit")

import csv
import pandas as pd
import ticket
from ticket import Ticket


class Admin:
    def __init__(self, name_admin, password_admin):
        self.name_event = None
        self.exp_event = None
        self.time_event = None
        self.cost_event = None
        self.capacity_event = None
        self.place_event = None
        self.name_admin = name_admin
        self.password_admin = password_admin

def view_event():
    with open("list.csv", "r") as ticket_csv:
        ticket_r = csv.reader(ticket_csv)
        for row in ticket_r:
            print(row)

    def __str__(self):
        return

def create_event():
    file_list = 'list1.csv'
    file_list = pd.read_csv(file_list)
    name_event = input("enter name ticket ")
    expdate_event = input("enter Expiration date")
    time_event = input("enter time ticket")
    cost_event = input("enter cost_ticket")
    capacity_total_event = input("enter capacity total ticket ")
    capacity_residual_event = input("enter capacity residual ticket ")
    place_event = input("enter event place")
    obj_ticket = Ticket(name_event, expdate_event, time_event, cost_event, capacity_total_event,
                        capacity_residual_event, place_event)
    row_list = {[obj_ticket.name_event], [obj_ticket.expdate_event], [obj_ticket.time_event],
                [obj_ticket.cost_event], [obj_ticket.capacity_total_event],
                [obj_ticket.capacity_residual_event][obj_ticket.place_event]}
    row_list = [int(x.strip()) if x.isdigit() else x for x in row_list]
    with open(file_list, 'a', newline='') as csv_list:
        csv_writer = csv.writer(csv_list)
        csv_writer.writerows(row_list)



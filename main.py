import csv

from admin import Admin,view_event
from login import User, register
from ticket import Ticket, buy_ticket

shopping_list = []
menu = int(input("1-admin:\n"
                 "2-customer:\n"))


if menu == 1:
    User.log_in()
    menu5 = int(input("1-view list event:\n"
                      "2-create event:\n"))
    if menu5 == 1:
        Admin.veiw_event()
    else:
        Admin.create_event()

elif menu == 2:
    menu2 = int(input("1-log in:\n"
                      "2-Register:\n"))

    if menu2 == 1:
        User.log_in()
        with open("list.csv", "r") as ticket_csv:
            ticket_r = csv.reader(ticket_csv)
            for row in ticket_r:
                print(row)
            menu3 = int(input("hello welcome:\n"
                              "Please enter the option to purchase a ticket:\n"))
            if menu3 == 1:
                buy_ticket()
            else:
                print("The entered option is incorrect!")

    elif menu2 == 2:
        register()
        print("Your registration was successfully completed \n")
        menu2 = int(input("1-log in:\n"
                          "2-Register:\n"))

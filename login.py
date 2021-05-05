import pandas as pd
import hashlib
import csv


class User:
    def __init__(self, username, password):
        self.password = password
        self.username = username

    @staticmethod
    def log_in():
        file_path = "account.csv"
        def_account = pd.read_csv(file_path)
        lst_username = list(def_account["username"])
        username = input("enter your username")
        if username in lst_username:
            print("valid username")
            password = input("enter your password")
            hash_password = hashlib.sha256(password.encode("utf8")).hexdigest()
            if def_account.iloc[def_account.index[def_account['username'] == username].tolist()[0], 1] == hash_password:
                print("hello", username)


def register():
    file_path = "account.csv"
    def_account = pd.read_csv(file_path)
    lst_username = list(def_account["username"])
    username = input("enter your username")
    if username in lst_username:
        print("valid username")
    password = input("enter your password")
    hash_password = hashlib.sha256(password.encode("utf8")).hexdigest()
    obj_user = User(username, hash_password)
    row_account = [[obj_user.username, obj_user.password]]
    with open(file_path, 'a', newline='') as csv_account:
        csv_writer = csv.writer(csv_account)
        # writing the data row
        csv_writer.writerows(row_account)

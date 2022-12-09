import re
import streamlit as st
import sqlite3
from sqlite3 import Error
import hashlib

#settings
page_title = "Disney Management"
page_icon = ":european_castle:" #not working
layout = "centered"



st.set_page_config(page_title=page_title, page_icon=page_icon, layout=layout)
st.title("Disney Management :european_castle:")


#Drop downs
parks = ["Disneyland", "Disney World"]
locations = ["Anaheim", "Orlando"]
sections = ["Main Street U.S.A"]
restaurants = ["Jolly Holiday Bakery Cafe"]
utilities = ["restroom"]
shops = ["Adventureland Bazar"]
rides = ["Indiana Jones"]

#Input
# with st.form("entry_form1", clear_on_submit=True):
#     col1, col2, col3 = st.columns(3)
#     col1.selectbox("Park", parks, key="park")
#     col2.selectbox("Location", locations, key="location")
#     col3.selectbox("Section", sections, key="section")

#     submitted = st.form_submit_button("Commit")

# with st.form("entry_form2", clear_on_submit=True):
#     col4, col5, col6, col7 = st.columns(4)
#     col4.selectbox("Restaurant", restaurants, key="restaurant")
#     col5.selectbox("Utility", utilities, key="utility")
#     col6.selectbox("Shop", shops, key="shop")
#     col7.selectbox("Ride", rides, key="ride")

with st.form("entry_form", clear_on_submit=True):
    col1, col2, col3, col4, col5, col6, col7 = st.columns(7)
    col1.selectbox("Park", parks, key="park")
    col2.selectbox("Location", locations, key="location")
    col3.selectbox("Section", sections, key="section")
    col4.selectbox("Restaurant", restaurants, key="restaurant")
    col5.selectbox("Utility", utilities, key="utility")
    col6.selectbox("Shop", shops, key="shop")
    col7.selectbox("Ride", rides, key="ride")

    "---"

    submitted = st.form_submit_button("Search data")

    if submitted:
        restaurants = {restaurants: st.session_state[restaurants] for rest in restaurants}
        st.write(f"Restaurants {added_rest}")
        st.success("Data saved!")

# def create_connection(db_fn):
#     """ create a database connection to a SQLite database """
#     conn = None # so our program doesn't crash later on if the connection was unsuccessful
#     try:
#         conn = sqlite3.connect(db_fn) # the actual connection step 
#         print(sqlite3.version) # to check the version, not necessary 
#         print ("Opened database successfully\n") 
        
#     except Error as e:
#             print(e) # if something goes wrong, tell the user what happened

#     return conn


# def create_table(conn, create_table_sql):
#     """ create a table from the create_table_sql statement
#     :param conn: Connection object returned from create_connection
#     :param create_table_sql: a CREATE TABLE statement as a string
#     :return:
#     """
#     try:
#         c = conn.cursor()
#         c.execute(create_table_sql)
#     except Error as e:
#         print(e)

# def add_rest_record(conn, recordRest):
#     """
#     Create a new restaurant into the Restaurants table
#     :param conn:
#     :param recordRest:
#     :return: restID
#     """
#     sql = ''' INSERT INTO Restaurants(restID, sectionID, parkID, restName, restDescription, restTypeFood, isOpen, maxCapacity, isFull, waitTime)
#               VALUES(?,?,?,?,?,?,?,?,?,?) '''
#     cur = conn.cursor()
#     cur.execute(sql, recordRest)
#     conn.commit()

# def select_all_restaurants(conn):
#     """
#     Query tasks by priority
#     :param conn: the Connection object
#     :param priority:
#     :return:
#     """
#     cur = conn.cursor()
#     cur.execute("SELECT * FROM Restaurants")

#     rows = cur.fetchall() # to get the data back into a list 

#     for row in rows:
#         print(row)

# def search_restaurants_ID(conn, restID):
#     cur = conn.cursor()
#     cur.execute("SELECT * FROM Restaurants WHERE restID = ?;", restID)

#     rows = cur.fetchall()

#     for row in rows:
#         print(row[1])

# def search_restaurants(conn, contains):
#     cur = conn.cursor()
#     cur.execute("SELECT * FROM Restaurants WHERE restName LIKE ?;", contains)

#     rows = cur.fetchall()

#     for row in rows:
#         print(row[1])


# def delete_Restaurant_ID(conn, restID):
#     cur = conn.cursor()
#     search_restaurants_ID(conn,restID)
#     cur.execute("DELETE FROM Restaurants WHERE restID = ?;", restID)
#     conn.commit() # WITHOUT COMMIT NO CHANGES WILL BE MADE ON THE DB




# #main
# def main():
# 	# All SQL queries as strings 
#         sql_create_restaurants_table = """ CREATE TABLE IF NOT EXISTS Restaurants (
#                                             restID INT,
#                                             sectionID INT,
#                                             parkID INT,
#                                             restName VARCHAR(100),
#                                             restDescription VARCHAR(300),
#                                             restTypeFood VARCHAR(100),
#                                             restTypeService VARCHAR(100),
#                                             isOpen BIT,
#                                             maxCapacity INT,
#                                             isFull BIT,
#                                             waitTime TIME,

#                                             PRIMARY KEY (restID),
#                                             FOREIGN KEY (parkID) REFERENCES Parks(parkID),
#                                             FOREIGN KEY (sectionID) REFERENCES Sections(sectionID)
#                                         ); """

#         rest_jollyHolliday = (1,1,1,"Jolly Holiday Bakery Cafe", "In the morning, stop by Jolly Holiday Bakery Cafe on your way into Disneyland for fresh pastries, specialty coffees and a great view.", "Counter Service", "Cafe", 1, 190, 1, 45)
#         #accountY = ('Y','y.com','34kjfen9rhf','elia@email.com','elia')
#         #accountYY = ('YY','yy.com','34kjfen9rhf','r@email.com','rodrigo')
#         contains = ('%Jolly%',)
#         restName = ('%Cafe%',)
#         restID = ('%1%',)

# 		# create connection to our sqlite db file 
#         conn = create_connection(r"disney.sqlite")

#         if conn:
#             try:
#                 create_table(conn, sql_create_restaurants_table)
#                 print("Restaurants:")
#                 add_rest_record(conn, rest_jollyHolliday)
#                 #add_account(conn, accountY)
#                 #add_account(conn, accountYY)
#                 select_all_restaurants(conn)
#                 print("\nThe restaurants containing " + contains[0] + ":")
#                 search_restaurants(conn, contains)
#                 #print("\nThe usernames for urls LIKE "+ url_name[0] + ":")
#                 #UNameThruUrl(conn, url_name)
#                 print("\nLet's delete a restaurant with an restName like " + restName[0])
#                 delete_Restaurant_ID(conn, restID)
#                 print("\nCurrent accounts:")
#                 select_all_restaurants(conn)

#             #     inp = int(input("\n\tMenu\n1. Add an account\n2. Select all accounts\n3. Search an account via URL\n4. Look-up a username through URL\n\nPick a number to make a selection: "))
#             #     if inp == 1:
                    
#             #         appName = input("Type the app name: ")
#             #         url = input("Type a url: ")
#             #         password = input("Type a password: ")
#             #         email = input("Type a email: ")
#             #         user_name = input("Type a user name: ")
#             #         info_to_add = (appName, url, password, email, user_name)
#             #         add_account(conn, info_to_add)
#             #         print("Your accounts:")
#             #         select_all_accounts(conn)
#             #     elif inp == 2:
#             #         select_all_accounts(conn)
#             #     elif inp == 3:
#             #         urlInp = input("Type the URL of the account you are trying to look for\n")
#             #         print(urlInp)
#             #         search_urls(conn, (('%' + urlInp + '%'),))
#             #     elif inp == 4:
#             #         urlInp = input("Type the URL of the username you are trying to look for\n")
#             #         UNameThruUrl(conn, (('%' + urlInp + '%'),))
#             #     else:
#             #         print("Invalid input, bye! Hehe \n")


#             finally: 
#                 # delete_all_accounts(conn) # so next time we run this we won't get an issue for re-entering all the same data, REMOVE LATER
#                 # we want to always close connection at end of program
#                 conn.close() 
#                 print("connection closed")


# if __name__ == '__main__':
#     main()

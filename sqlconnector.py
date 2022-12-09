from select import select
import sqlite3
from sqlite3 import Error
import pandas as pd



# connecting to db
def create_connection(db_fn):
    """ create a database connection to a SQLite database """
    conn = None # so our program doesn't crash later on if the connection was unsuccessful
    try:
        conn = sqlite3.connect(db_fn) # the actual connection step 
        print(sqlite3.version) # to check the version, not necessary 
        print ("Opened database successfully") 
        
    except Error as e:
            print(e) # if something goes wrong, tell the user what happened

    return conn

def add_park(conn, project):
    """
    Create a new project into the projects table
    :param conn:
    :param project:
    :return: project id
    """
    sql = ''' INSERT INTO Parks(parkID,locationID,parkName,parksize,parkCapacity,numSectors,isOpen)
              VALUES(?,?,?,?,?,?,?) '''
    cur = conn.cursor()
    cur.execute(sql, project)
    conn.commit()

def add_section(conn, project):
    """
    Create a new project into the projects table
    :param conn:
    :param project:
    :return: project id
    """
    sql = ''' INSERT INTO Sections(sectionID,parkID,sectionName,sectionColorTheme,numAttractions)
              VALUES(?,?,?,?,?) '''
    cur = conn.cursor()
    cur.execute(sql, project)
    conn.commit()

def add_location(conn, project):
    """
    Create a new project into the projects table
    :param conn:
    :param project:
    :return: project id
    """
    sql = ''' INSERT INTO Locations(locationID,locationName,locationState,locationCity)
              VALUES(?,?,?,?) '''
    cur = conn.cursor()
    cur.execute(sql, project)
    conn.commit()

def add_restaurant(conn, project):
    """
    Create a new project into the projects table
    :param conn:
    :param project:
    :return: project id
    """
    sql = ''' INSERT INTO Restaurant(restID,sectionID,parkID,restName,restDescription,restTypeFood,restTypeService,isOpen,maxCapacity,isFull,waitTime)
              VALUES(?,?,?,?) '''
    cur = conn.cursor()
    cur.execute(sql, project)
    conn.commit()
# MISSING: add rides, utilities, shops


# QUERY ALL DATA
def select_all_accounts():
    """
    Query tasks by priority
    :param conn: the Connection object
    :param priority:
    :return:
    """
    conn = create_connection(r"disney.sqlite")
    cur = conn.cursor()
    cur.execute('''SELECT locationName, parkName, sectionName, rideName
FROM Location LEFT JOIN Parks P on Location.locationID = P.locationID LEFT JOIN Sections S on P.parkID = S.parkID LEFT JOIN Rides R on S.sectionID = R.sectionID
GROUP BY locationName;''')

    rows = cur.fetchall() # to get the data back into a list 

    # for row in rows:
    #     print(row)
    
    return rows

def parksFilter():
    conn = create_connection(r"disney.sqlite")
    cur = conn.cursor()
    cur.execute("SELECT DISTINCT parkName FROM Parks")

    rows = cur.fetchall() # to get the data back into a list 

    # for row in rows:
    #     print(row)
    
    return rows


# def main():
# 		# create connection to our sqlite db file 
#     conn = create_connection(r"disney.sqlite")

#     if conn:
#         try:
#             select_all_accounts(conn)
#             # result_df = pd.read_sql(select_all_accounts(conn), conn)`
#         finally:
#             conn.close()
#             print("connection closed")
        



if __name__ == '__main__':
    main()
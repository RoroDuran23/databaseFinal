# Core Pkgs
from itertools import groupby
from pickle import FALSE
from re import X
from select import select
import streamlit as st 
import pandas as pd

# DB Mgmt
import sqlite3 
conn = sqlite3.connect('data/disney2.sqlite')
c = conn.cursor()




# -------- QUERY EXECUTOR ----------------------------
def sql_executor(raw_code):
	c.execute(raw_code)
	data = c.fetchall()
	return data 
# ----------------------------------------------------



st.set_page_config(page_title="Disney Dashboard",
                    layout="wide")

##city = ['ID,', 'Name,', 'CountryCode,', 'District,', 'Population']

parks = ['parkID', 'locationID', 'parkName', 'parksize', 'parkCapacity', 'numSectors', 'isOpen']
sections = ['sectionID', 'parkID', 'sectionName', 'sectionColorTheme', 'numAttractions']
location = ['locationID', 'locationName', 'locationState', 'locationCity']
restaurants = ['restID', 'sectionID', 'restName', 'restDescription', 'restTypeFood', 'restTypeService', 'isOpen', 'maxCapacity', 'waitTime']
rides = ['rideID', 'sectionID', 'rideName', 'rideType', 'rideDescription', 'rideMinHeight', 'rideOpeningYear', 'waitTime']
utilities = ['utilityID', 'sectionID', 'utilityName', 'description', 'isAvailable']

run = False # will run query based on our filters

def main():
	# -------- DEFAULT QUERY FOR MAIN TABLE --------------
	# defaultQ = '''SELECT restName, restTypeFood, parkName, maxCapacity, restDescription, waitTime FROM Parks
	# 					INNER JOIN Sections
	# 					ON Parks.locationID = Sections.sectionID
	# 					INNER JOIN  Restaurants
	# 					ON Sections.sectionID = Restaurants.sectionID;'''

	defaultQ = '''SELECT Rides.rideName, Sections.sectionName, Parks.parkName, Location.locationName FROM Location
						INNER JOIN Parks
						ON Location.locationID = Parks.locationID
						INNER JOIN  Sections
						ON Parks.parkID = Sections.parkID
						INNER JOIN  Rides
						ON Sections.sectionID = Rides.sectionID;'''

	

	# ----------------------------------------------------

	st.title("Disney Park Manager")

	menu = ["Navigation","Common Views", "Add Record", "Delete Record", "Edit Record", "SQL Console"]
	choice = st.sidebar.selectbox("Menu",menu)

	
	if choice == "Navigation":
		st.caption("This page is meant for easily navigating through the whole database using filters")

		# ---- FILTERING DATA -------
		#with st.expander("Filter data"):
		#	col1, col2 = st.columns(2)
		#	with col1:
		#		parkFilter = st.selectbox(
		#			"Filter by park:",
		#			("Disneyland", "Magic Kingdom")
		#		)
		#	with col2:
		#		sectionFilter = st.selectbox(
		#			"Filter by section:",
		#			("Main Street, U.S.A.", "Adventureland", "New Orleans Square", "Frontierland", "Fantasyland", "Tomorrowland", "Critter Country", "Star Wars: Galaxys Edge", " Mickeys Toontown", "Pixar Pier")
		#		)
		
		st.subheader("Park Structure Navigation")
		colA, colB = st.columns(2)
		with colA:
			structSelect = st.selectbox(
				"Choose your filter:",
				("Default", "Location", "Park", "Section")
			)
		with colB:
			structID = st.number_input("Enter ID", step=1)
		
		structCode = '''SELECT * FROM [LocationMap]'''
		if structSelect == "Location":
			structCode = '''SELECT * FROM [LocationMap] WHERE locationID ='''+str(structID)
		elif structSelect == "Park":
			structCode = '''SELECT * FROM [LocationMap] WHERE parkID ='''+str(structID)
		elif structSelect == "Section":
			structCode = '''SELECT * FROM [LocationMap] WHERE sectionID ='''+str(structID)
		structureResults = sql_executor(structCode)
		structureDF = pd.DataFrame(structureResults)
		structureDF.columns = ["Location ID", "Location Name", "Park ID", "Park Name", "Section ID", "Section Name"]
		st.dataframe(structureDF)

		st.subheader("Amenity Search")
		col1, col2= st.columns(2)
		with col1:
			searchSelect = st.selectbox("Choose your filter:",
				("Location", "Park", "Section"))
		with col2:
			searchID = st.number_input("Enter Search ID", step=1)
		
		searchClause = '''WHERE '''+searchSelect+'''ID='''+str(searchID)

		with st.expander("Rides"):
			ridesCode = '''SELECT * FROM [Full Rides Path] ''' + searchClause
			ridesDF = pd.DataFrame(sql_executor(ridesCode))
			st.dataframe(ridesDF)

		with st.expander("Restaurants"):
			restCode = '''SELECT * FROM [Full Restaurant Path] ''' + searchClause
			restDF = pd.DataFrame(sql_executor(restCode))
			st.dataframe(restDF)

		with st.expander("Utilities"):
			utilCode = '''SELECT * FROM [Full Utilities Path] ''' + searchClause
			utilDF = pd.DataFrame(sql_executor(utilCode))
			st.dataframe(utilDF)

		with st.expander("Shops"):
			shopCode = '''SELECT * FROM [Full Shops Path] ''' + searchClause
			shopDF = pd.DataFrame(sql_executor(shopCode))
			st.dataframe(shopDF)

		query_results = sql_executor(defaultQ)


	elif choice == "SQL Console":
		st.subheader("SQL Console")
		st.caption("This section is designed to manipulate the entire database, any SQL operation can be executed here. Please use with caution.")
		# Columns/Layout
		col1,col2 = st.columns(2)

		with col1:
			with st.form(key='query_form'):
				raw_code = st.text_area("SQL Code Here")
				submit_code = st.form_submit_button("Execute")

			# Table of Info

			with st.expander("Table Info"):
				table_info = {'parks':parks,'sections':sections,'location':location, 'restaurants':restaurants, 'rides':rides}
				st.json(table_info)
			
		# Results Layouts
		with col2:
			if submit_code:
				st.info("Query Submitted")
				st.code(raw_code)

				# Results 
				query_results = sql_executor(raw_code)
				with st.expander("Results Table"):
					query_df = pd.DataFrame(query_results)
					st.dataframe(query_df)

#new new
	elif (choice == "Common Views"):
		st.header("Common Views")
		st.caption("This section has a collection of common views for easy visibility")
		ridesBY = 'SELECT * FROM [Rides by Year]'
		st.subheader("Rides by Year")
		ridesBYdf = pd.DataFrame(sql_executor(ridesBY))
		ridesBYdf.columns = ["rideName", "rideType", "rideOpeningYear"]
		st.dataframe(ridesBYdf)
		ridesBS = 'SELECT * FROM [Rides by Section]'
		st.subheader("Rides by Section")
		ridesBSdf = pd.DataFrame(sql_executor(ridesBS))
		ridesBSdf.columns = ["rideName", "rideType", "sectionName", "parkName"]
		st.dataframe(ridesBSdf)
		#new new
		ridesSubQ = 'SELECT parkName,(SELECT avg(rideOpeningYear) FROM Rides WHERE parkID = 1) AS AvgOpenYear FROM Parks WHERE parkID = 1'
		st.subheader("Average year...")
		subQdf = pd.DataFrame(sql_executor(ridesSubQ))
		subQdf.columns = ["parkName", "AvgOpenYear"]
		st.dataframe(subQdf)
		restosGroupBy = 'SELECT sectionID, COUNT(restName) AS NumRestaurants FROM Restaurants GROUP BY sectionID;'
		st.subheader("Group By Number of Restaurants per Section")
		groupByDF = pd.DataFrame(sql_executor(restosGroupBy))
		groupByDF.columns = ["sectionID", "NumRestaurants"]
		st.dataframe(groupByDF)





	elif (choice == "Add Record"):
		st.subheader("Add Record")
		st.caption("In this section you can add records to the bottom tiers of the database")
		with st.expander("Add Ride"):
			with st.form(key='AddRide', clear_on_submit=True):
				addRideID = st.number_input("rideID", step=0)
				addRideSecID = st.number_input("sectionID", step=0)
				addRideName = st.text_input("Ride Name")
				addRidetype = st.text_input("Ride Type")
				addRideDesc = st.text_input("Ride Description")
				addMinHeight = st.number_input("Ride Minimum Height")
				addRideOpeningYear = st.number_input("Opening year")
				waitTime = st.number_input("Wait Time")
				
				submitAddRide = st.form_submit_button(label='Add Ride')

			if submitAddRide:
			##ROLLBACK EXAMPLE !!! could implement everywhere but probably never gunna get tripped anyway
				try:
					query = '''INSERT INTO Rides(rideId, sectionID, rideName, rideType, rideDescription, rideMinHeight, rideOpeningYear, waitTime)
					VALUES(?,?,?,?,?,?,?,?)
						'''
					newRide = (addRideID, addRideSecID, addRideName, addRidetype, addRideDesc, addMinHeight, addRideOpeningYear, waitTime )
					c.execute(query, newRide)
					conn.commit()

				except conn.Error as error:
					conn.rollback()

				st.success("Function Sent")
		with st.expander("Add Utility"):
			with st.form(key='AddUtility', clear_on_submit=True):
				addUtilityID = st.number_input("Utility ID", step=0)
				addUtilitySecID = st.number_input("Section ID", step = 0)
				addUtilityName = st.text_input("Utility Name")
				addUtilityDescription = st.text_input("Utility Description")
				addUtilityAvailable = st.checkbox("Is Available")
				
				submitAddUtility = st.form_submit_button(label='Add Utility')

				if submitAddUtility:
				
					utilQuery = '''INSERT INTO Utilities(utilityID, sectionID, utilityName, description, isAvailable)
					VALUES(?,?,?,?,?)
						'''
					newUtil = (addUtilityID, addUtilitySecID, addUtilityName, addUtilityDescription, addUtilityAvailable)
					c.execute(utilQuery, newUtil)
					conn.commit()
					st.success("You have added a ride")

		with st.expander("Add Restaurant"):
			with st.form(key='AddRestaurant', clear_on_submit=True):
				addRestID = st.number_input("Restaurant ID", step = 0)
				addRestSecID = st.number_input("Section ID", step = 0)
				addRestName = st.text_input("Restaurant Name")
				addRestDescription = st.text_input("Description")
				addRestTypeFood = st.text_input("Type of Food")
				addRestTypeService = st.text_input("Type of Service")
				addIsOpen = st.checkbox("Is Open")
				addMaxCapacity = st.number_input("Maximum Capacity", step = 0)
				addWaitTime = st.number_input("Wait Time")
				## SQL SHIT HERE
				submitAddRest = st.form_submit_button(label='Add Ride')

				if submitAddRest:
					restQuery = '''INSERT INTO Restaurants(restID, sectionID, restName, restDescription, restTypeFood, restTypeService, isOpen, maxCapacity, waitTime)
					VALUES(?,?,?,?,?,?,?,?,?)
						'''
					newRest = (addRestID, addRestSecID, addRestName, addRestDescription, addRestTypeFood,addRestTypeService,addIsOpen,addMaxCapacity,addWaitTime)
					c.execute(restQuery, newRest)
					conn.commit()
					st.success("Added Restaurant")

	elif (choice == "Delete Record"):
		st.subheader("Delete Record")
		st.caption("In this section you can delete records from the bottom tiers of the database")
		with st.expander("Delete Ride"):
			with st.form(key = 'DeleteRide', clear_on_submit=True):
				delRideID = st.number_input("rideID", step = 0)
				submitDelRide = st.form_submit_button(label='Delete Ride')

				if submitDelRide:
					sDelRideID = str(delRideID)
					sql = 'DELETE FROM Rides WHERE rideID='+sDelRideID
					cur = conn.cursor()
					cur.execute(sql)
					conn.commit()
					st.success("Ride Deleted")
		with st.expander("Delete Utility"):
			with st.form(key = 'DeleteUtil', clear_on_submit=True):
				delUtilID = st.number_input("utilityID", step = 0)
				submitDelUtil = st.form_submit_button(label='Delete Utility')

				if submitDelUtil:
					sdelUtilID = str(delUtilID)
					sql = 'DELETE FROM Utilities WHERE utilityID='+sdelUtilID
					cur = conn.cursor()
					cur.execute(sql)
					conn.commit()
					st.success("Utility Deleted")
		with st.expander("Delete Restaurant"):
			with st.form(key = 'DeleteRest', clear_on_submit=True):
				delRideID = st.number_input("restID", step = 0)
				submitDelRest = st.form_submit_button(label='Delete Restaurant')

				if submitDelRest:

					sdelRestID = str(delRideID)
					sql = 'DELETE FROM Restaurants WHERE restID='+sdelRestID
					cur = conn.cursor()
					cur.execute(sql)
					conn.commit()
					
					st.success("Ride Deleted")

	elif (choice == "Edit Record"):
		st.subheader("Edit Records")
		st.caption("In this section you can edit records from the bottom tiers of the database")
		with st.expander("Edit Ride"):
			with st.form(key='EditRide', clear_on_submit=True):
				editRideID = st.number_input("rideID", step=0)
				editRideSecID = st.number_input("sectionID", step=0)
				editRideName = st.text_input("Ride Name")
				editRidetype = st.text_input("Ride Type")
				editRideDesc = st.text_input("Ride Description")
				editRideMinHeight = st.number_input("Ride Minimum Height")
				editRideOpeningYear = st.number_input("Ride Opening Year", step=0)
				editRideWaitTime = st.number_input("Wait Time")
				submitEditRide = st.form_submit_button(label='Edit Ride')

			if submitEditRide:

				
				# sql = "UPDATE Rides SET sectionID="+str(editRideSecID)+",rideName="+editRideName+", rideType="+editRidetype+", rideDescription="+editRideDesc+", rideMinHeight="+str(editRideMinHeight)+", rideOpeningYear="+str(editRideOpeningYear)+", waitTime="+str(editRideWaitTime)+"WHERE rideID="+str(editRideID)
				sql = '''UPDATE Rides 
						SET sectionID = ? , 
						rideName = ? , 
						rideType = ? , 
						rideDescription = ? , 
						rideMinHeight = ? , 
						rideOpeningYear = ? , 
						waitTime = ? , 
						WHERE rideID = ?'''
				task = (str(editRideSecID),editRideName,editRidetype,editRideDesc,str(editRideMinHeight),str(editRideOpeningYear),str(editRideWaitTime),str(editRideID))
				cur = conn.cursor()
				cur.execute(sql, task)
				conn.commit()
				st.success("You have edited the ride")

		with st.expander("Edit Utility"):
			with st.form(key='EditUtility', clear_on_submit=True):
				editUtilityID = st.number_input("Utility ID", step=0)
				editUtilitySecID = st.number_input("Section ID", step = 0)
				editUtilityName = st.text_input("Utility Name")
				editUtilityDescription = st.text_input("Utility Description")
				editUtilityAvailable = st.checkbox("Is Available")
				
				submitEditUtility = st.form_submit_button(label='Edit Utility')

				if submitEditUtility:
					#SQL SHIT
					st.success("You have Edited Utility")

		with st.expander("Edit Restaurant"):
			with st.form(key='EditRestaurant', clear_on_submit=True):

				editRestID = st.number_input("Edit ID", step = 0)
				editRestSecID = st.number_input("Section ID", step = 0)
				editRestName = st.text_input("Restaurant Name")
				editRestDescription = st.text_input("Description")
				editRestTypeFood = st.text_input("Type of Food")
				editRestTypeService = st.text_input("Type of Service")
				editIsOpen = st.checkbox("Is Open")
				editMaxCapacity = st.number_input("Maximum Capacity", step = 0)
				editWaitTime = st.number_input("Wait Time")
				
				submitEditRest = st.form_submit_button(label='Edit Restaurant')

				if submitEditRest:

					## SQL SHIT HERE

					st.success("Added Restaurant")





if __name__ == '__main__':
	main()
# Core Pkgs
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
	defaultQ = '''SELECT restName, restTypeFood, parkName, maxCapacity, restDescription, waitTime FROM Parks
						INNER JOIN Sections
						ON Parks.locationID = Sections.sectionID
						INNER JOIN  Restaurants
						ON Sections.sectionID = Restaurants.sectionID;'''
	# ----------------------------------------------------
	st.title("Disney Park Manager")

	menu = ["Query","Common Views", "Add Record", "Delete Record", "Edit Record", "SQL Console", "Version Control"]
	choice = st.sidebar.selectbox("Menu",menu)


	
	if choice == "Query":
		st.subheader("Searching by Filters")
		st.caption("This page is meant for easily navigating through the whole database using filters and straightforward options")

		# ---- FILTERING DATA -------
		with st.expander("Filter data"):
			col1, col2, col3 = st.columns(3)
			with col1:
				parkFilter = st.multiselect(
					"Park:",
					options=["Disneyland", "Magic Kingdom"],
					default = "Disneyland"
				)
				sectionFilter = st.multiselect(
					"Section:",
					options="M",
					default = "M"
				)
				locationFilter = st.multiselect(
					"Location:",
					options="M",
					default = "M"
				)
			with col2:
				restaurantFilter = st.multiselect(
					"Restaurant:",
					options=["Gibson Girl Ice Cream Parlor", "Jolly Holiday Bakery Cafe", 
							"Bengal Barbecue", "South Sea Traders", "The Tropical Hideaway", 
							"Tiki Juice Bar"],
					default = "Tiki Juice Bar"
				)
				rideFilter = st.multiselect(
					"Ride:",
					options="M",
					default = "M"
				)
				utilitiesFilter = st.multiselect(
					"Utilities:",
					options="M",
					default = "M"
				)
			with col3:
				shopsFilter = st.multiselect(
					"Shop:",
					options="M",
					default = "M"
				)
				shopsFilter = st.multiselect(
					"Filter:",
					options="M",
					default = "M"
				)
				shopsFilter = st.multiselect(
					"Filter2:",
					options="M",
					default = "M"
				)
			
			
			
		
	
		query_results = sql_executor(defaultQ)
		with st.expander("Results Table"):
			query_df = pd.DataFrame(query_results)
			st.dataframe(query_df)


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

	elif (choice == "Common Views"):
		st.header("Common Views")
		st.caption("This section has a collection of common views for easy visibility")
		ridesBY = 'SELECT * FROM [Rides by Year]'
		st.subheader("Rides by Year")
		st.dataframe(pd.DataFrame(sql_executor(ridesBY)))
		ridesBS = 'SELECT * FROM [Rides by Section]'
		st.subheader("Rides by Section")
		st.dataframe(pd.DataFrame(sql_executor(ridesBS)))



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
				addAvgAge = st.number_input("Ride Opening Year", step=0)
				addRideOpeningYear = st.number_input("Wait Time")
				
				submitAddRide = st.form_submit_button(label='Add Ride')

			if submitAddRide:
				
				query = '''INSERT INTO Rides(rideId, sectionID, rideName, rideType, rideDescription, rideMinHeight, rideAvgAge, rideOpeningYear, waitTime)
				VALUES(?,?,?,?,?,?,?,?)
					'''
				newRide = (addRideID, addRideSecID, addRideName, addRidetype, addRideDesc, addMinHeight, addAvgAge, addRideOpeningYear)
				c.execute(query, newRide)
				c.commit()
				st.success("You have added a ride")
		with st.expander("Add Utility"):
			with st.form(key='AddUtility', clear_on_submit=True):
				addUtilityID = st.number_input("Utility ID", step=0)
				addUtilitySecID = st.number_input("Section ID", step = 0)
				addUtilityName = st.text_input("Utility Name")
				addUtilityDescription = st.text_input("Utility Description")
				addUtilityAvailable = st.checkbox("Is Available")
				
				submitAddUtility = st.form_submit_button(label='Add Ride')

				if submitAddUtility:

					#SQL SHIT
					
					st.success("Added Utility")

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
					st.success("Added Restaurant")

	elif (choice == "Delete Record"):
		st.subheader("Delete Record")
		st.caption("In this section you can delete records from the bottom tiers of the database")
		with st.expander("Delete Ride"):
			with st.form(key = 'DeleteRide', clear_on_submit=True):
				delRideID = st.number_input("rideID", step = 0)
				submitDelRide = st.form_submit_button(label='Delete Ride')

				if submitDelRide:
					# SQL SHIT HERE
					st.success("Ride Deleted")
		with st.expander("Delete Utility"):
			with st.form(key = 'DeleteUtil', clear_on_submit=True):
				delRideID = st.number_input("utilityID", step = 0)
				submitDelRide = st.form_submit_button(label='Delete Utility')

				if submitDelRide:
					# SQL SHIT HERE
					st.success("Ride Deleted")
		with st.expander("Delete Restaurant"):
			with st.form(key = 'DeleteRest', clear_on_submit=True):
				delRideID = st.number_input("restID", step = 0)
				submitDelRide = st.form_submit_button(label='Delete Restaurant')

				if submitDelRide:

					# SQL SHIT HERE
					
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
				editRideName = st.number_input("Ride Minimum Height")
				editRideName = st.number_input("Ride Opening Year", step=0)
				editRideName = st.number_input("Wait Time")
				submitEditRide = st.form_submit_button(label='Edit Ride')

			if submitEditRide:

				## SQL SHIT HERE
				
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

	elif (choice == "Version Control"):
		st.subheader("Undo")
		if(st.button('Undo Previous Action')):
			rbq = 'ROLLBACK'
			c.execute(rbq)
		st.subheader("Return to Default")
			#will load a savepoint here





if __name__ == '__main__':
	main()
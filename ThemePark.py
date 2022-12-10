# Core Pkgs
import streamlit as st 
import pandas as pd

# DB Mgmt
import sqlite3 
conn = sqlite3.connect('data/disney2.sqlite')
c = conn.cursor()


# Fxn Make Execution
def sql_executor(raw_code):
	c.execute(raw_code)
	data = c.fetchall()
	return data 


##city = ['ID,', 'Name,', 'CountryCode,', 'District,', 'Population']

parks = ['parkID', 'locationID', 'parkName', 'parksize', 'parkCapacity', 'numSectors', 'isOpen']
sections = ['sectionID', 'parkID', 'sectionName', 'sectionColorTheme', 'numAttractions']
location = ['locationID', 'locationName', 'locationState', 'locationCity']
restaurants = ['restID', 'sectionID', 'restName', 'restDescription', 'restTypeFood', 'restTypeService', 'isOpen', 'maxCapacity', 'waitTime']
rides = ['rideID', 'sectionID', 'rideName', 'rideType', 'rideDescription', 'rideMinHeight', 'rideOpeningYear', 'waitTime']
utilities = ['utilityID', 'sectionID', 'utilityName', 'description', 'isAvailable']


def main():
	st.title("Theme Park Manager")

	menu = ["Query","Add Record", "Delete Record", "Edit Record", "Version Control"]
	choice = st.sidebar.selectbox("Menu",menu)

	if choice == "Query":
		st.subheader("HomePage")

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

	elif (choice == "Add Record"):
		st.subheader("Add Record")
		with st.expander("Add Ride"):
			with st.form(key='AddRide', clear_on_submit=True):
				addRideID = st.number_input("rideID", step=0)
				addRideSecID = st.number_input("sectionID", step=0)
				addRideName = st.text_input("Ride Name")
				addRidetype = st.text_input("Ride Type")
				addRideName = st.number_input("Ride Minimum Height")
				addRideName = st.number_input("Ride Opening Year", step=0)
				addRideName = st.number_input("Wait Time")
				submitAddRide = st.form_submit_button(label='Add Ride')

			if submitAddRide:
				
				## SQL SHIT HERE

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





if __name__ == '__main__':
	main()
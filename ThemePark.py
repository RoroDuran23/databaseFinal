# Core Pkgs
import streamlit as st 
import pandas as pd

# DB Mgmt
import sqlite3 
conn = sqlite3.connect('FinalDraft.sql')
c = conn.cursor()


# Fxn Make Execution
def sql_executor(raw_code):
	c.execute(raw_code)
	data = c.fetchall()
	return data 


##city = ['ID,', 'Name,', 'CountryCode,', 'District,', 'Population']

parks = ['parkID, ', 'locationID, ', 'parkName, ', 'parksize, ', 'parkCapacity, ', 'numSectors, ', 'isOpen']
sections = ['sectionID, ', 'parkID, ', 'sectionName, ', 'sectionColorTheme, ', 'numAttractions']
location = ['locationID, ', 'locationName, ', 'locationState, ', 'locationCity']
restaurants = ['restID, ', 'sectionID, ', 'restName, ', 'restDescription, ', 'restTypeFood, ', 'restTypeService, ', 'isOpen, ', 'maxCapacity, ', 'waitTime']
rides = ['rideID, ', 'sectionID, ', 'rideName, ', 'rideType, ', 'rideDescription, ', 'rideMinHeight, ', 'rideOpeningYear, ', 'waitTime']


def main():
	st.title("Theme Park Manager")

	menu = ["Home","Add Record", "Delete Record", "Edit Record", "Undo"]
	choice = st.sidebar.selectbox("Menu",menu)

	if choice == "Home":
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
				with st.expander("Results"):
					st.write(query_results)

				with st.expander("Pretty Table"):
					query_df = pd.DataFrame(query_results)
					st.dataframe(query_df)

	elif (choice == "Add Record"):
	    st.subheader("Add Record")

	elif (choice == "Delete Record"):
		st.subheader("Delete Record")

	elif (choice == "Edit Record"):
		st.subheader("Edit Record")

	elif (choice == "Undo"):
		st.subheader("Undo")





if __name__ == '__main__':
	main()
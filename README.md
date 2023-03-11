# web-scraping-challenge
<img width="1000" alt="Screen Shot 2023-03-11 at 12 15 47 PM" src="https://user-images.githubusercontent.com/44728723/224502506-99587731-f543-4c0a-9b79-59979fe482b3.png">


### Built an ETL pipeline using Python, Pandas, Python, Regex to extract, transform and load data into a SQL database.

## Approach

(1) After transforming the data, four CSV files were created and used to create an ERD and a table schema. Finally, CSV file data were uploaded into a Postgres database.

(2) The four dataframes (Category, Subcategory, Contacts and Campaigns) were created from data imported from two source data Excel files (contacts.xlsx and crowdfunding.xlsx).

(3) The data were transformed as follows:

    - CATEGORY & SUBCATEGORY DATAFRAMES:
        - Created numpy arrays from 1-9 for the categories and 1-24 for the subcategories
        - Used a list comprehension to add "cat" to each category_id and "subcat" to each subcategory_id
        - Exported the final dataframes to a CSV file 
        
    - CAMPAIGN DATAFRAME: 
        - Renamed columns blurb to description, launched_at to start_date, and deadline to end_date
        - Converted the goal and pledged columns to a 'float' data type from 'object' data type
        - Formatted launch_date and end_date columns to datetime format
        - Dropped unwanted columns
        - Merged the Campaign with the Category and the Subcategory dataframes
        - Exported the final dataframe to a CSV file
        
    - CONTACTS DATAFRAME was created using two approaches, Pandas and Regex
    
        - PANDAS:  Used pandas to convert the contacts CSV data from one column of values separated by commas into a dataframe, by doing the following:
            - Iterated through the Contact and convert each row to a dictionary
            - Iterated through each dictionary (row) and get the values for each row using list comprehension
            - Appended the list of values for each row to a list
            - Created a "first"name" and "last_name" column by splitting "name" column
            - Reordered the columns and exported final dataframe to a CSV file
            
        - REGEX: Used pandas to convert the contacts CSV data from one column of values separated by commas into a dataframe, by doing the following:
            - Extracted the contact_id with .str.extract
            - Converted the "contact_id" column to an int64 data type
            - Extracted the name of the contact using Regex and added it to a new column
            - Extract the email from the contacts using Regex and added the values to a new column
            - Dropped unwanted columns
            - Exported final dataframe to a CSV file

(4) Created a database in PostgreSQL with the exported CSV files

    - Created an ERD (entity relationship diagram) to depict the relationship between the tables
    
    - Created the tables and columns in SQL
    - Imported the values to the tables 
<p align="center">
<img width="580" alt="Screen Shot 2023-03-11 at 11 50 02 AM" src="https://user-images.githubusercontent.com/44728723/224497019-dc3d9f63-0cc2-4f16-b69d-c8d46350fd81.png">

## Technology
- pandas
- python
- JSON
- SQL
- PostgreSQL
- Regex

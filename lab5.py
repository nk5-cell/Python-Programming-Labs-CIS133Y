#*******************************************************************************
#Author:            Nidhi Kairon
#Description:       This is a program that fetches data about name "Anna" from
#                   the NAMES database, and creates a pandas dataframe, and
#                   plots the data using matplotlib
#Input:             NAMES database data
#Output:            2 plots using matplotlib
#*******************************************************************************

import pandas as pd
import pymssql
import matplotlib.pyplot as plt

name_connection = pymssql.connect(
    server='cisdbss.pcc.edu',
    database='NAMES',
    user='275student',
    password='275student'
)

sql = """
    SELECT Year, Name, Gender, NameCount
    FROM year_gender_totals y
    JOIN name_counts n ON n.FK_YearGenderTotalID = y.YearGenderTotalID
    JOIN names s ON s.NameID = n.FK_NameID
    WHERE Name = 'Anna';
"""

anna_data_long = pd.read_sql(sql, name_connection)

anna_data_wide = anna_data_long.pivot(index=["Year", "Name"], columns="Gender", values="NameCount")
anna_wide = anna_data_wide.reset_index()
anna_wide.columns.name = None

plt.figure(figsize=(12, 8), dpi=72)
plt.plot('Year', 'F', data=anna_wide)
plt.plot('Year', 'M', data=anna_wide)

plt.grid()
plt.title("Popularity of the Name Anna")
plt.xlabel("Year")
plt.ylabel("Number of Babies Named Anna")
plt.legend(['Female Babies', 'Male Babies'])

plt.show()

ld = anna_wide.melt(id_vars=['Year', 'Name'], value_vars=['M', 'F'], var_name='Gender', value_name="NameCount")

anna_wide['Percent Female'] = 100 * anna_wide['F'] / (anna_wide['F'] + anna_wide['M'])

plt.figure(figsize=(12, 8), dpi=72)
plt.plot('Year', 'Percent Female', data=anna_wide)

plt.grid()
plt.title("Is Anna a Female Name or a Male Name?")
plt.xlabel("Year")
plt.ylabel("Percent of Babies Named Anna Who Were Female")

plt.show()

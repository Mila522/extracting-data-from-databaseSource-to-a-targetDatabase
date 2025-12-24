ETL Pipeline with SQLite and Pandas
📌 Project Overview

This project demonstrates a simple ETL (Extract, Transform, Load) pipeline built using Python, SQLite, and Pandas.
The pipeline extracts user data from a source database, performs basic data cleaning and transformation, and loads the cleaned data into a target database.

It’s a beginner-friendly example of how data engineering workflows work in practice.

🛠️ Technologies Used

Python

SQLite

Pandas

🔄 ETL Process Breakdown
1️⃣ Extract

Connects to a SQLite database (source.db)

Reads data from the users table

Loads the data into a Pandas DataFrame

2️⃣ Transform

Removes duplicate records

Fills missing age values using the mean age

Creates a new column age_group:

"young" if age < 25

"adult" if age ≥ 25

3️⃣ Load

Writes the transformed data into a new SQLite database (target.db)

Saves the cleaned data into a table called users cleaned

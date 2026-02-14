🎓 Student Performance Analytics System

A web-based analytics dashboard built using Django, Pandas, NumPy, and Matplotlib that allows teachers to upload student marks and automatically generate statistical insights, rankings, and visual reports.

📌 Project Overview

The Student Performance Analytics System is designed to simplify academic data analysis. Instead of manually calculating averages, ranks, and failure percentages, this system processes a CSV,EXCEL or a JSON file and provides instant analytics through an interactive dashboard.

The project combines web development with data science tools to demonstrate full-stack and analytical capabilities in a single application.

🎯 Objectives

Automate student performance analysis

Generate statistical summaries

Visualize academic data using graphs

Rank students based on total marks

Calculate subject-wise averages and failure percentage

Provide a clean dashboard interface for teachers

🛠️ Technologies Used
1️⃣ Django

Used as the backend framework to:

Handle file uploads

Manage database records

Create dashboard views

Route URLs

Render templates

2️⃣ Pandas

Used for:

Reading files

Data cleaning

Data transformation

Calculating averages

Aggregating marks

Ranking students

3️⃣ NumPy

Used for:

Statistical calculations

Standard deviation

Performance analysis logic

Numeric computations

4️⃣ Matplotlib

Used to:

Generate subject average bar charts

Create visual representations of performance data

Convert graphs into images for web display

📂 Project Features
✅ CSV Upload System

Teachers can upload a file containing student marks in the following format:

Name,Maths,Science,English,Computer
Rahul,78,88,67,90
Priya,92,85,89,95
Amit,45,52,60,40


The system reads and stores the data automatically.

✅ Automatic Data Processing

After upload, the system:

Calculates subject-wise averages

Computes total marks per student

Assigns ranks based on total marks

Identifies the class topper

Calculates failure percentage (marks below 40)

✅ Dashboard Analytics

The dashboard displays:

Total number of students

Name of topper

Failure percentage

Ranking table

Subject average graph (bar chart)

✅ Ranking System

Students are ranked based on total marks using statistical sorting logic. The highest total receives Rank 1.

✅ Graphical Visualization

Matplotlib generates:

Subject-wise average bar chart

Visual representation embedded directly into dashboard

This enhances understanding through visual analysis instead of raw numbers.

🗃️ Database Structure

Model: StudentRecord

Fields:

name (CharField)

maths (IntegerField)

science (IntegerField)

english (IntegerField)

computer (IntegerField)

Methods:

total()

average()

⚙️ System Workflow

Teacher opens upload page

Uploads CSV file

Data is processed using Pandas

Records are stored in database

Dashboard generates:

Statistics

Rankings

Graphs

Results are displayed instantly

📊 Statistical Analysis Performed

Mean (Average)

Total Score Calculation

Failure Detection Logic

Percentage Calculation

Rank Assignment

Basic Statistical Aggregation

Standard Deviation (Optional Enhancement)

💡 Advantages of the System

Reduces manual calculation effort

Provides instant results

Visualizes performance trends

Improves academic data interpretation

Demonstrates integration of data science with web development

🚀 Future Enhancements

Student login system

Export report as PDF

Multi-class comparison

Subject performance trend over time

Search and filter functionality

Dark mode UI

AI-based performance prediction

🧠 Learning Outcomes

Through this project, the following skills were developed:

Backend development using Django

File handling and database management

Data manipulation using Pandas

Numerical computing using NumPy

Data visualization using Matplotlib

Integration of analytics with web applications

📈 Conclusion

The Student Performance Analytics System successfully demonstrates how data science libraries can be integrated into a web framework to create a practical, real-world solution. The project showcases both analytical processing and full-stack development capabilities, making it suitable for academic submission as well as portfolio presentation.
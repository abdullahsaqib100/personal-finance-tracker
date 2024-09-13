# personal-finance-tracker

𝐎𝐯𝐞𝐫𝐯𝐢𝐞𝐰:
The Personal Finance Tracker is a simple command-line tool built using Python that allows users to manage and track their personal expenses efficiently. The program provides options to add new expenses, view all recorded expenses, and calculate the total expenses. All data is stored in a CSV file (expenses.csv), making it easy to track and review financial records.

This project was developed with the goal of enhancing my Python skills while working on a real-world use case. Through this, I gained a deeper understanding of file handling in Python, especially working with CSV files.

𝐅𝐞𝐚𝐭𝐮𝐫𝐞𝐬:
1. Add New Expense: Allows users to input a date, category, description, and amount for a new expense. The data is then saved in the expenses.csv file.
2. View Expenses: Displays all the expenses in the CSV file.
3. Calculate Total Expenses: Sums up the total amount spent across all categories.
4. Persistent Storage: All data is stored in the expenses.csv file, which is created automatically if it doesn’t already exist.


𝐂𝐒𝐕 𝐅𝐢𝐥𝐞 - 𝒆𝒙𝒑𝒆𝒏𝒔𝒆𝒔.𝒄𝒔𝒗
The expenses.csv file serves as the storage for all the expenses you add while using the application. It contains the following columns:

Date: The date when the expense was made (format: DD-MM-YYYY).
Category: The category of the expense (e.g., Food, Bills, Transport).
Description: A brief description of the expense.
Amount: The amount spent.
The file is created automatically the first time you run the program and use the "Add a new expense" feature. As a sample, I have added an expenses.csv file in this repository to give you a clear understanding of how the data is structured and how the tracker works. Feel free to add new expenses and watch the file update in real-time as you use the application.


𝐂𝐡𝐚𝐥𝐥𝐞𝐧𝐠𝐞𝐬 𝐅𝐚𝐜𝐞𝐝:
Throughout this project, I encountered several challenges, especially with handling file operations efficiently. One particular issue I faced was ensuring that the expenses.csv file was both readable and writable without overwriting existing data. Understanding how to open the file in different modes (r+, a+) and ensuring proper validation of user inputs was a key learning experience. Additionally, working with CSV files to structure the data and ensure the program could calculate totals from these records required a clear understanding of how CSV data is structured.

Despite these hurdles, this project helped solidify my understanding of Python's file handling mechanisms, and I am proud of the final product.

𝐇𝐨𝐰 𝐭𝐨 𝐑𝐮𝐧 𝐭𝐡𝐞 𝐏𝐫𝐨𝐣𝐞𝐜𝐭?

𝟭. 𝗖𝗹𝗼𝗻𝗲 𝘁𝗵𝗲 𝗿𝗲𝗽𝗼𝘀𝗶𝘁𝗼𝗿𝘆:
git clone https://github.com/yourusername/personal-finance-tracker.git

𝟮. 𝗡𝗮𝘃𝗶𝗴𝗮𝘁𝗲 𝘁𝗼 𝘁𝗵𝗲 𝗽𝗿𝗼𝗷𝗲𝗰𝘁 𝗱𝗶𝗿𝗲𝗰𝘁𝗼𝗿𝘆:
cd personal-finance-tracker

𝟯. 𝗥𝘂𝗻 𝘁𝗵𝗲 𝗣𝘆𝘁𝗵𝗼𝗻 𝘀𝗰𝗿𝗶𝗽𝘁:
python3 finance_tracker.py



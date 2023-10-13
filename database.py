import sqlite3 # for database connection

""" Two tables to be created - 1) student information ( which will be accessed by ID number)
							   2) transactions ( will be used to strore the transaction performed in a shift) """
def get_data(id): # to get student data based on ID number
	pass

def write_transaction_db(filepath,data,amount): # to write a transaction to database
	pass
def get_transactions_db(filepath): # to get all the transactions performed
	connection = sqlite3.connect(filepath)
	cursor = connection.cursor()

	cursor.execute(f"SELECT * FROM Transactions ")
	rows = cursor.fetchall()
	print(rows)

	connection.close()
	return rows

 	
def update_data(filepath,data,amount): # for balance updating
    pass


if __name__ == "__main__":
	get_transactions_db("student_database.db")


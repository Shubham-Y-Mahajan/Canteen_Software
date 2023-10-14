import sqlite3 # for database connection

""" Two tables to be created - 1) student information ( which will be accessed by ID number)
							   2) transactions ( will be used to strore the transaction performed in a shift) """
def get_data(id): # to get student data based on ID number
    try:
        connection = sqlite3.connect("student_database.db")
        cursor = connection.cursor()

        cursor.execute(f"SELECT * FROM Student_Info WHERE ID='{id}'")
        rows = cursor.fetchall() # list of tuples now one id corresponds to one student only thus only one tuple in list
        # print(rows)  example = [(12241730, 'Shubham Mahajan', 1000)]
        data=list(rows[0])
        # print(data) exapmle = [12241730, 'Shubham Mahajan', 1000]
        connection.close()
        return data
    except IndexError:
        return 0
	
def write_transaction_db(filepath,data,amount): # to write a transaction to database
    data.pop()
    data.append(int(amount))
    connection = sqlite3.connect(filepath)
    cursor = connection.cursor()
    print(data)
    new_rows=[tuple(data),]
    print(new_rows)

    cursor.executemany("INSERT INTO Transactions VALUES(?,?,?)", new_rows)
    connection.commit()
    connection.close()
    
def get_transactions_db(filepath): # to get all the transactions performed
	connection = sqlite3.connect(filepath)
	cursor = connection.cursor()

	cursor.execute(f"SELECT * FROM Transactions ")
	rows = cursor.fetchall()
	print(rows)

	connection.close()
	return rows

 	
def update_data(filepath,data,amount): # for balance updating
    connection = sqlite3.connect(filepath)
    cursor = connection.cursor()
    balance_left=data[2]-amount
    if balance_left<0:
        return 0
    else:
        cursor.execute(f"UPDATE Student_Info SET Balance = {balance_left} WHERE ID='{data[0]}'")
        connection.commit()
        connection.close()
        return balance_left

def end_shift(filepath):
    connection = sqlite3.connect(filepath)
    cursor = connection.cursor()

    cursor.execute(f"SELECT * FROM Transactions ")
    rows = cursor.fetchall()
    cursor.execute(f"DELETE FROM Transactions ")
    connection.commit()
    connection.close()
    return rows

if __name__ == "__main__":
	pass


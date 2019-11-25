import mysql.connector
def test_mariadb_hdbpp_test():
	db_connection = mysql.connector.connect(
	host="archiver-maria-db",
	user="tango",
	passwd="tango"
	)
	db_cursor = db_connection.cursor()
	db_cursor.execute("SHOW DATABASES")
	print ("db cursor:", db_cursor)
	for db in db_cursor:
		print(db)
		if db == "hdbpp":
			print("yes it is")
	assert 0



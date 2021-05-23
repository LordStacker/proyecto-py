

def create_tables(cursor):
	with open('./basedatos.sql', 'r') as db_file:
		print('will run a migration')
		migration = db_file.read()
		cursor.execute(migration)
import sqlite3 as lite
def getLastDrawDate():
	"""Function to get the last draw date queried"""
	ret = ""
	con = None
	try:
		con = lite.connect('lib/euromillions.db')
		with con:
			cur = con.cursor()
			cur.execute('SELECT date FROM draws ORDER BY _id DESC LIMIT 1;')
			data = cur.fetchone()
			if data is not None:
				ret = data[0]
	except:
		raise
	return ret
	
def setLastDrawDate(day, game_numbers, game_stars, prize_amount):
	"""Function to set the last draw information got from the WS"""
	values =(day, game_numbers, game_stars, prize_amount)
	try:
		con = lite.connect('lib/euromillions.db')
		with con:
			cur = con.cursor()		
			cur.execute("INSERT INTO draws VALUES(null,?,?,?,?)", values)
			con.commit()
	except:
		raise
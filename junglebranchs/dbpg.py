from configs import *

def selectTable(table = '', names = '', where = '', order=[], pag=[]):
	conn = psycopg2.connect(host=pg_conn_data["host"],database=pg_conn_data["db"],user=pg_conn_data["user"],password=pg_conn_data["password"],port=pg_conn_data["port"])
	try:
		with conn.cursor() as cursor:
			if( names == "*"):
				StrN = "*"
			else:
				if isinstance(names, list):
					StrN = (','.join(names))
				else:
					StrN = names
			sql = "SELECT " + StrN + " FROM " + table
			if( len(where) > 0 ):
				sql += " WHERE " + where
			if( len(order) == 2 ):
				sql += " ORDER BY " + str(order[0]) + " " + str(order[1])
			if( len(pag) == 2 ):
				sql += " LIMIT " + str(pag[0]) + " OFFSET " +  str(pag[1])
			cursor.execute(sql)
			rows = cursor.fetchall()
			cursor.close()
			conn.close()
			if(len(rows)>0):
				for i, row in enumerate(rows):
					items = []
					for val in rows:
						items.append( val )
				return items	
			else:
				return []
	except psycopg2.Error as e:
		d = {}
		d["_error"] = "BASE_DATOS" + str(e)
		conn.close()
		return jsonify(d)
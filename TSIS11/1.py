import psycopg2
from config import config

def get_user(pattern):
    """get parts provided by a vendor specified by the vendor_id""" 
    conn = None
    try:
        #read database config
        params = config()
        #connect to the PostgreSQL database
        conn = psycopg2.connect(**params)
        # create a cursor object for execution
        cur = conn.cursor()
        # another way to call a function
        #cur.execute("SELECT * FROM get_parts_by_vendor( %s); ",(vendor_id,))
        if pattern == "phone":
            cur.callproc('phone', "")
        elif pattern == "name":
            cur.callproc("username", "")
        # process the result set
        rows = cur.fetchall()
        for row in rows:
            print(row)
        # close the communication with the PostgreSQL database server
        cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()

if __name__ == '__main__':
    pattern = input()
    get_user(pattern)
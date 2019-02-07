import sshtunnel
import MySQLdb


server = sshtunnel.SSHTunnelForwarder(
            ('206.189.190.150', 22),
            ssh_username= 'root',
            ssh_password= 'Summer201889$',
            remote_bind_address=('127.0.0.1', 3306))

server.start()
print(server.local_bind_port)

conn = MySQLdb.connect(host="127.0.0.1",port=server.local_bind_port,user="root",passwd="Summer201889$",db="amz_track")
x = conn.cursor()


x.execute("INSERT INTO productinventory (asin,seller,date,inventory) VALUES (%s,%s,%s,%s)",('0000000000','Test Seller','2019-02-03',999))
conn.commit()


conn.close()





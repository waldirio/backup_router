import telnetlib
import datetime

HOST = "192.168.56.120"
passLogin = "expasswd"
passEna = "inpasswd"

tn = telnetlib.Telnet(HOST)

tn.read_until("Password: ")
tn.write(passLogin + "\n")

tn.write("ena\n")
tn.read_until("Password: ")
tn.write(passEna + "\n")

tn.write("term length 0\n")
tn.write("show run \n")
tn.write("exit\n")

actualData=datetime.datetime.now()
aux = actualData.strftime("%B_%d_%Y")
print aux 

fileName = "config.dump_" + str(aux) + ".txt"
fileRef = open(fileName,'w')
#fileRef.write(tn.read_until('^end$'))
fileRef.write(tn.read_all())
fileRef.close()

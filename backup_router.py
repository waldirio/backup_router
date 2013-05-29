#!/usr/bin/env python

"""
Creation Data ..: 05/29/2013
Developer ......: Waldirio M. Pinheiro <waldirio.pinheiro@iesbrazil.com.br>
                  Luiz Cahue <luiz.cahue@iesbrazil.com.br>
Description ....: Connect to cisco equipment to collect config and generate a backup file.
Changelog ......: 
"""

import telnetlib
import datetime

def openList():
    file = open('list_router.txt','r')
    
    for b in file:
        backupRouter(b)

def backupRouter(server):
    print "Backup of Server " + server.rstrip()
    # Variables
    HOST = server.rstrip()
    passLogin = "expasswd"      # The External password
    passEna = "inpasswd"        # The Internal password
    
    tn = telnetlib.Telnet(HOST)
    
    tn.read_until("Password: ")
    tn.write(passLogin + "\n")
    
    tn.write("ena\n")
    tn.read_until("Password: ")
    tn.write(passEna + "\n")
    
    # To define the terminal size equal 0, removing the -- more --
    # option in show run
    tn.write("term length 0\n")
    tn.write("show run \n")
    tn.write("exit\n")
    
    # To get the date and add in the name file
    actualData=datetime.datetime.now()
    aux = actualData.strftime("%m_%d_%Y")
    
    # Generating a file named config.dump_<mm_dd_yyyy>.txt
    fileName = "config_" + HOST + ".dump_" + str(aux) + ".txt"
    fileRef = open(fileName,'w')
    fileRef.write(tn.read_all())
    fileRef.close()


openList()
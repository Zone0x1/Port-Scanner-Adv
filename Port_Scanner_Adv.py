#!/usr/bin/python3
"""
Python Port Scanner Threaded.py
Purpose : Python-based TCP Port Scanner 
Author : Mahmoud S.ALi :) 

Data : 27/3/2020
############
Version : 1.1
    Initial build
"""
# Import Meduols Threaded #
import argparse
import socket
import os
import sys
######################
# Ino Tools #
os.system("figlet Scanner-Port-Adv")
os.system("clear")
os.system("figlet Scanner-Started \n")
print ("Author   : Mahmoud S.ALi")
print ("Facebook : https://www.facebook.com/mody.saber.96343405")
print ("WhatsApp : 01117374028 \n")
def connection_Scan(target_ip , target_port):
    """
    Attempts to create a socket connection with the given ip addr and port.
    if succsseful , the port is open , if not , the port is closed 
    """
    try:
        conne_socket = socket.socket(socket.AF_INET , socket.SOCK_STREAM)
        conne_socket.connect((target_ip , target_port))
        conne_socket.send(b'Banner_query\r\n')
        result = conne_socket.recv(100)
        print ("[+] {}/tcp open ".format(target_port))
        print ("[+] {}".format(str(result)))
    except OSError:
        print ("[-] {}/tcp close ".format(target_port))
    finally:
        conne_socket.close()  # The Connection is CLosed #

def Port_Scan(target , port_num):
    """
    Scan indiceted prots for status.
    First , it attempts to resolve the ip addres of a provided hostname
    """
    try:
        target_ip = socket.gethostbyname(target)
        print ("[+] Scan Result For : {}".format( target_ip ))
        connection_Scan( target_ip , int ( port_num ) )
    except OSError:
        print ("[-] Cannot Resolve {} : Unknow Host :".format(target))
        return # Exit Port_Scan

def argument_parser():
    """
    Allow USer to specify target host and port 
    """
    parser = argparse.ArgumentParser(description="TCP port Scanner , Accepts a Hostname/IP Addres and list of ports to scan , attempts to identify the service running on a port ")

    parser.add_argument("-o", "--host"  , help="Host IP Address ")
    parser.add_argument("-p", "--ports"  , help="Comma-Separated Port List such as '25,80,8080'")
    
    var_args = vars(parser.parse_args()) #Convert argument 

    return var_args

if __name__ == '__main__':
    try:
        user_args = argument_parser()
        host = user_args["host"]
        port_list = user_args["ports"].split(",") # Make a List From Numbers Ports
        for port in port_list:
            Port_Scan(host , port)
    except AttributeError:
        print ("[-] Erorr , PLeasa Provide the COmmand-Line Arguments before running ")

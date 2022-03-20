#!/usr/bin/python
import os
import sys
from subprocess import Popen, PIPE, STDOUT
from proxy_txt_to_dict import proxy_txt_to_dict

def checkIfPortIsOpen(ip, port, timeout):
    """
        Parameters:
            ip [string]: ip address
            port [string]: port number
            timeout [string]: timeout in seconds
        Check if a port is open on a given ip using netcat command.
        Returns True if port is open, False otherwise.
    """
    p=Popen(["nc", "-zvw{timeout}".format(timeout=timeout), ip, port], stdout=PIPE, stderr=STDOUT)
    output = p.stdout.read().decode('utf-8')
    if("succeeded!" not in output):
        return False
    else:
        return True

def main():
    proxy_dict_ip_to_port = proxy_txt_to_dict()
    good_proxies = list()
    try:
        for proxy in proxy_dict_ip_to_port:
            ip = proxy
            port = proxy_dict_ip_to_port[proxy]
            if checkIfPortIsOpen(ip, port, 1):
                print("{ip}:{port} is open".format(ip=ip, port=port))
                good_proxies.append("{ip}:{port}".format(ip=ip, port=port))
            else:
                print("{ip}:{port} is closed".format(ip=ip, port=port))
    finally:
        file = open('good_proxies.txt', 'w')
        for proxy in good_proxies:
            file.write(proxy + '\n')
        file.close()


if __name__ == "__main__":
    main()

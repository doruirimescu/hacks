
def proxy_txt_to_dict():
    """
    Reads proxy.txt and returns a dictionary of ip:port
    """
    file=open('proxy_list.txt','r')
    proxy_list=file.readlines()
    file.close()

    proxy_dict = {}
    for line in proxy_list:
        #strip the newline character
        line=line.strip()
        line = line.split(':')
        proxy_dict[line[0]] = line[1]
    return proxy_dict

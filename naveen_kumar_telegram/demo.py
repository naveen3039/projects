from ping3 import ping

def myping(host):
    resp = ping(host)
    print(resp)

    if not resp :
        return False
    else:
        return True
        
print(myping("52.117.91.214"))
print(myping("192.168.1.1"))

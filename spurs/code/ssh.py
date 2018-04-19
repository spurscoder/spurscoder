import os, sys
import pexpect

msgs = {"GPU": ["spurs", "192.168.2.153", "1532"]}

def connectSSH(province):
    if province in msgs:
        msg = msgs[province]
        user, ip, password = msg
        child = pexpect.spawn('ssh %s@%s ' % (user, ip))
        child.expect('password:')
        child.sendline(password)
        child.interact()
    else:
        print('check your inputs!')


if __name__ == '__main__':

    connectSSH("GPU")

    pass
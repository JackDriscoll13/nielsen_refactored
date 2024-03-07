import random 
import time
import os
import socket

# original: 

def make_msgid(idstring=None, domain=None):
    """Returns a string suitable for RFC 2822 compliant Message-ID, e.g:

    <142480216486.20800.16526388040877946887@nightshade.la.mastaler.com>

    Optional idstring if given is a string used to strengthen the
    uniqueness of the message id.  Optional domain if given provides the
    portion of the message id after the '@'.  It defaults to the locally
    defined hostname.
    """
    timeval = int(time.time()*100)
    pid = os.getpid()
    randint = random.getrandbits(64)
    if idstring is None:
        idstring = ''
    else:
        idstring = '.' + idstring
    if domain is None:
        domain = socket.getfqdn()
    msgid = '<%d.%d.%d%s@%s>' % (timeval, pid, randint, idstring, domain)
    return msgid


# custom: 

def make_msgid_custom(idstring=None, domain=None):
    """Returns a string suitable for RFC 2822 compliant Message-ID, e.g:

    <142480216486.20800.16526388040877946887@nightshade.la.mastaler.com>

    Optional idstring if given is a string used to strengthen the
    uniqueness of the message id.  Optional domain if given provides the
    portion of the message id after the '@'.  It defaults to the locally
    defined hostname.
    """
    timeval = int(time.time()*100)
    pid = os.getpid()
    print(pid)
    randint = random.getrandbits(64)
    if idstring is None:
        idstring = ''
    else:
        idstring = '.' + idstring
    if domain is None:
        domain = socket.getfqdn()
        print(domain)
    msgid = '<%d.%d.%d%s@%s>' % (timeval, pid, randint, idstring, domain)
    print(msgid)
    return msgid


if __name__ == '__main__':
    make_msgid_custom(domain = 'NWNYMKNAL334CZ2.CORP.CHARTERCOM.com')

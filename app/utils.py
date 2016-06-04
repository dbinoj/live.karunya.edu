from app import app
import random
import scrypt
import re
from unidecode import unidecode

_punct_re = re.compile(r'[\t !"#$%&\'()*\-/<=>?@\[\\\]^_`{|},.]+')


def randstr(length):
    return ''.join(chr(random.randint(0,255)) for i in range(length))


def hash_password(password, maxtime=0.5, datalength=256):
    salt = randstr(datalength)
    hashed_password = scrypt.encrypt(salt, password.encode('utf-8'), maxtime=maxtime)
    return bytearray(hashed_password)


def verify_password(hashed_password, guessed_password, maxtime=300):
    try:
        scrypt.decrypt(hashed_password, guessed_password.encode('utf-8'), maxtime)
        return True
    except scrypt.error as e:
        print "scrypt error: %s" % e    # Not fatal but a necessary measure if server is under heavy load
        return False


def slugify(text, delim=u'-'):
    """Generates an ASCII-only slug."""
    result = []
    for word in _punct_re.split(text.lower()):
        result.extend(unidecode(word).split())
    return unicode(delim.join(result))

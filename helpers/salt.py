import random
import string
import hashlib
import hmac

#you should use bcrypt

secret = 'Yqueloque'

def make_salt(length = 5):
    salt = ''
    return salt.join(random.choice(string.ascii_letters) for x in xrange(length))

def make_pw_hash(name, pw, salt = None):
    if not salt:
        salt = make_salt()
    h = hashlib.sha256(name + pw + salt).hexdigest()
    return '%s,%s' % (salt, h)

def valid_pw(name, pw, h):
    salt = h.split(',')[0]
    return h == make_pw_hash(name, pw, salt)

def make_secure_val(val):
    salt = hmac.new(secret, val).hexdigest()
    return '%s|%s' % (val, salt)

def check_secure_val(secure_val):
    val = secure_val.split('|')[0]
    if secure_val == make_secure_val(val):
        return val

h = make_pw_hash('admin', 'pass')
print valid_pw('admin', 'pass', h)
import random
import string
import hashlib
import hmac

secret = 'Yqueloque'

def make_salt(length = 5):
    """Make a salt for hash any data
    Args:
        length (int): the value of usernamea
    Returns:
        string: random charaters, as default it return 5
    """
    salt = ''
    return salt.join(random.choice(string.ascii_letters) for x in xrange(length))

def make_pw_hash(name, pw, salt = None):
    """Make a hash with the user data
    Args:
        name (str): the value of username
        pw (str): password of the user
        salt (str): charaters for hash the user data
    Returns:
        string: value,hash of the value
    """
    if not salt:
        salt = make_salt()
    h = hashlib.sha256(name + pw + salt).hexdigest()
    return '%s,%s' % (salt, h)

def valid_pw(name, pw, h):
    """Validate password of the user
    Args:
        name (str): the value of username
        pw (str): password of the user
        h (str): hash of the user
    Returns:
        bool: if it match return true else false
    """
    salt = h.split(',')[0]
    return h == make_pw_hash(name, pw, salt)

def make_secure_val(val):
    """Make a hash with the value for more secure
    Args:
        val (str): the value to make secure
    Returns:
        string: value|hash of the value
    """
    salt = hmac.new(secret, val).hexdigest()
    return '%s|%s' % (val, salt)

def check_secure_val(secure_val):
    """Check if the secure val has not been changed
    Args:
        secure_val (str): a secure value
    Returns:
        string: The return value. the value if it's secure.
        None otherwise.
    """
    val = secure_val.split('|')[0]
    if secure_val == make_secure_val(val):
        return val

h = make_pw_hash('admin', 'pass')
print valid_pw('admin', 'pass', h)
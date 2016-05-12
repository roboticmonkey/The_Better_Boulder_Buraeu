"""Module for hashing"""

import uuid
import hashlib
 
def hash_password(password):
    """Takes a password and returns the hash"""
    # uuid is used to generate a random number
    salt = uuid.uuid4().hex
    # print "salt: %s" % (salt)
    # print len(salt)
    # return hashlib.sha256(salt.encode() + password.encode()).hexdigest() + ':' + salt
    return hashlib.sha256(salt + password).hexdigest() + ':' + salt
    
def check_password(hashed_password, user_password):
    """Checks entered password with stored hashed password, return T/F"""
    
    password, salt = hashed_password.split(':')
    # return password == hashlib.sha256(salt.encode() + user_password.encode()).hexdigest()
    return password == hashlib.sha256(salt + user_password).hexdigest()
 

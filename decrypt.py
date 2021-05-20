import os, random, struct, os
from Crypto.Cipher import AES

def decrypt_file(key, in_filename, out_filename=None, chunksize=24 * 1024):
    # Generation of the output file name
    if not out_filename:
        out_filename = os.path.splitext(in_filename)[0]
    # Decyphering section
    with open(in_filename, 'rb') as infile:
        origsize = struct.unpack('<Q', infile.read(struct.calcsize('Q')))[0]
        iv = infile.read(16)
        decryptor = AES.new(key, AES.MODE_CBC, iv)

        with open(out_filename, 'wb') as outfile:
            while True:
                chunk = infile.read(chunksize)
                if len(chunk) == 0:
                    break
                outfile.write(decryptor.decrypt(chunk))

            outfile.truncate(origsize)
    os.remove(in_filename)
    return out_filename
# Decrypt all the data from /data (can be changed to anything)
for subdir, dirs, files in os.walk(r'/home/kali/Desktop/POCcrypto/main'):
    for filename in files:
        filepath = subdir + os.sep + filename
        print (filepath)
        decrypt_file("dNkOxbUneW8vqw4uTsBWjnZGpUu72fnu",filepath)

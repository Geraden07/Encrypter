README
Author: Steven B.

DISCLAIMER: Please do not actually use this to encrypt sensitive information. This was written from the viewpoint of a student trying to get a better understanding of cryptology and may not necessarily be cryptographically secure.

Dependency: PyCrypto third party module

The script needs to be hardcoded with the hash of a password. It will prompt a user for a password, compare the hash of the inputed password to the hardcoded value, then if it matches, it will proceed to loop through the list of hardcoded file names. For each one it will try to encrypt it if the filename matches, or decrypt it if the filename has .AES appended to it. When it encyrpts, it will automatically append .AES to the file name.

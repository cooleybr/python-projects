## Hash Collision Detection

Using Python write a test to detect collisions from unique strings

Tested on Raspbian GNU/Linux 11 (bullseye)
Python Version: 3.9.2
tinydb==4.6.1

Hash Algorithms Available (hashlib):
{'sha3_384', 'shake_256', 'sha3_224', 'sha3_512', 'md5', 'ripemd160', 'sha3_256', 'shake_128', 'sha512', 'blake2b', 'sm3', 'sha512_224', 'sha256', 'sha384', 'sha224', 'whirlpool', 'sha1', 'md5-sha1', 'md4', 'blake2s', 'sha512_256'}

**Test Algorithm**: RIPEMD160

**Approach**: 

1. Generate random strings and calculate hash
2. Check hash value against stored values
3. If current hash matches existing hash, compare strings
4. If strings match -> Write to collisions.txt
5. Insert string and hash into database
6. Repeat

**TODO**:

 - TinyDB selected for ease of implementation - consider alternative
 - Probably a better methodology for generating strings
 - Include some timekeeping
 - String range and iterations

import hashlib
from random import choice
from string import printable
from tinydb import TinyDB, Query

#print (hashlib.algorithms_available)

# Instantiate database with tinydb for storing strings/hashes
db = TinyDB('db.json')
# Create a query object for reuse
entry = Query()

# Enter loop - infinite iterations until stopped
while(True):
  # Create a string with printable range of ascii characters
  # Arbitrary string length selected at 140 characters
  # Strings must be encoded for hashing - utf-8 chosen
  a = "".join(choice(printable) for i in range(140)).encode('utf-8')

  # create hashlib object for ripemd160
  h = hashlib.new('ripemd160')
  h.update(a)

  # generate hash of encoded string
  ahash = h.hexdigest()

  # Check db for existince of same hash, returns an array
  arr = db.search(entry.hash == ahash)

  # If the array is empty - same hash does not exist
  # If not empty - check to see if it's the same string or different
  # If different, then record as collision
  if(len(arr)>0):
    for item in arr:
      if(item['string']!=str(a)):
        print('strings match')
        line = 'Collision: '+ str(a) + ', ' + item['string']+'/n'
        f = open('collisions.txt','a')
        f.write(line)
        f.close()
  # Insert the record and restart loop.
  # This approach could insert duplicate string/hash entries
  db.insert({'string':str(a), 'hash':ahash})

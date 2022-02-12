import hashlib
from random import choice
from string import printable

print (hashlib.algorithms_available)

# Generate Strings
listy = ('hi','hi','hello','huh')
h = hashlib.new('ripemd160')

string_val = "".join(choice(printable) for i in range(140))
print(string_val)
collision=False
#for i in range(3000):
while(collision==False):
  a = "".join(choice(printable) for i in range(140)).encode('utf-8')
  b = "".join(choice(printable) for i in range(140)).encode('utf-8')
  h = hashlib.new('ripemd160')
  hi = hashlib.new('ripemd160')
  h.update(a) 
  ahash = h.hexdigest()
  hi.update(b)
  bhash = hi.hexdigest()
  print(str(a) + ' ' + ahash)
  print(str(b) + ' ' + bhash)
  if(ahash==bhash):
    print('Collision')
    collision=True

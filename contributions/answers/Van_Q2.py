# This code answers any prompt from question 2.

def result(c):
  #Here is a dictionary map to what the key of the prompt is:
  key = {
    'C' : 0,
    'E' : 1,
    'G' : 2,
    'I' : 3,
    'K' : 4,
    'M' : 5,
    'O' : 6,
    'Q' : 7,
    'S' : 8,
    'U' : 9,
    '!' : 1000,
    '%' : 100,
    '*' : 10,
    '#' : 1,
  }
  # Returns the value of the answer from the key
  return key.get(c)


string = input("Enter the crypted prompt: ")


ans = 0

i = 0
while i<len(string):
  while(string[i] == " "):
    i+=1
  temp = result(string[i])
  i+=1
  while(string[i] == " "):
    i+=1
  ans += (temp*result(string[i]))
  i+=1
  
print(ans)
   

def StringChallenge(strParam):
  aux=""
  for i in strParam:
    if i==" ":
      aux+=i 
    else:
      aux+=str(ord(i))

  # code goes here
  return aux

# keep this function call here 
print StringChallenge(raw_input())

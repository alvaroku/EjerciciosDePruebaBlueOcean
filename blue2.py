def StringChallenge(strParam):
  strParam = strParam.lower()
  aux=""
  for i in strParam:
    if i.isalpha():
      aux+=i 
    else:
      aux+="_"
   
  strParam=aux
  # code goes here
  return strParam

# keep this function call here 
print StringChallenge(raw_input())

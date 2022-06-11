def StringChallenge(strParam):

  # code goes here
  tresConjuntos=False
  tresDigitos=False
  sonDel1a9 = False
  primerConjuntoPar=False
  segundoConjuntoImpar=False
  ultimoDigitoMayor=False
  valido="false"
  strParam = strParam.split(".")
  if len(strParam)==3:
    tresConjuntos = True
    for i in strParam:
      if len(i)==3:
        tresDigitos=True
      else:
        tresDigitos=False
        break
    if tresDigitos:
      for i in strParam:
        for j in i:
          j=int(j)
          if j>0 and j<10:
            sonDel1a9=True
          else:
            sonDel1a9 = False
            break
      if sonDel1a9:
        suma=0
        for i in strParam[0]:
          suma+=int(i)
        if suma%2==0:
          primerConjuntoPar=True
        if primerConjuntoPar:
           suma=0
           for i in strParam[1]:
            suma+=int(i)
           if suma%2!=0:
            segundoConjuntoImpar=True
            for i in strParam:
              a = int(i[0])
              b = int(i[1])
              c = int(i[2])
              if c>a and c>b:
                
                ultimoDigitoMayor=True
              else:
                ultimoDigitoMayor=False
                break   
            if ultimoDigitoMayor:
              valido = "true"
            else:
              valido="false"   
        
  return valido
# keep this function call here 
print StringChallenge(raw_input())

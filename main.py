import random as ran
from math import gcd as bltin_gcd
import re


#///////////////////////////////////////////////////////////////
#//////////////////////FUNCIONES GENERALES///////////////////
#////////////////////////////////////////////////////////////////
def rela_primes():
  lista = []
  for i in range(26): 
    if bltin_gcd(26, i) == 1:
      lista.append(i)
  return lista 



def inver_primes():
  lista_primes = rela_primes()
  lista_inver = []
  for i in lista_primes:
    for j in range(30):
      if (i*j)%26 == 1:
        lista_inver.append(j)
        break
  return lista_inver

 
## agregar ignorar lo que no sean letras y pasar las mayus a minus 

def unify(palabra):
  palabralist = []
  palabra = palabra.replace(" ", "")
  palabra = palabra.lower()
  regex = re.compile('[^a-z]')
  palabra = regex.sub('', palabra)
  for i in range(len(palabra)):
    palabralist.append(palabra[i])
  return palabralist
  
def convert (list):
  lista = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l','m', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
  count = 0
  for i in list:
    for j in range(len(lista)):
      if i == lista[j]:
        list[count]= j
        continue

    count = count + 1
  return list

  
def deconvert(list):
  lista = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l','m', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
  string = ""
  for i in range(len(list)):
    list[i] = lista[int(list[i])]
    string = string + list[i]
  return string



#///////////////////////////////////////////////////////////////
#//////////////////////METODOS DE CODIFICACION///////////////////
#////////////////////////////////////////////////////////////////

####LIMPIO
def encode_despla(palabrast,key,count_falla):
  """
This codification method receives a message, and a key
From the message we remove all non alphabetical characters, remove spaces, and lower all characters that remain.
The key is required to be between 1 and 25.
If the user fails 3 times providing a valid key, the program chooses randomly a valid key and encrypts the message using it.
Understanding a<->0, b<->1, ..., z<->25 the codification method transforms each letter to its corresponding numerical value.
The codification method adds the key value to each number and transforms the result back to an alphabetical value.
Then returns the message encrypted
  """
  palabrals = unify(palabrast)
  if 1 <= key <= 26:
      palabrals = convert(palabrals)
      for i in range(len(palabrals)):
        palabrals[i] = (palabrals[i] + key)%26
      palabrast = deconvert(palabrals)
      print(palabrast)
      return palabrast, key
  elif count_falla == 2:
    key = ran.randint(1,26)
    palabrals = convert(palabrals)
    for i in range(len(palabrals)):
      palabrals[i] = (palabrals[i] + key)%26
    palabrast = deconvert(palabrals)
    print(palabrast)
    return palabrast, key
  else:
    return -1, -1

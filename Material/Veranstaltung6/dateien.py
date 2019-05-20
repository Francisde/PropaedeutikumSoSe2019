import numpy as np
import random as rd
import time
from datetime import datetime


def umfang(a, b):
  return 2*a +2*b
wobj = open("ausgabe.txt", "w")
fobj = open("liste.txt", "r")

for line in fobj:
  line=line.strip()
  print(line)
  werte=line.split(";")
  print(umfang(werte[0],werte[1]))
  wobj.write(umfang(werte[0],werte[1]))

fobj.close()
wobj.close()

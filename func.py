#Funções - Gerais -----------------------------------------------------
def Conf():
  OK = False
  while OK == False:
    a = ""
    a = input("\033[0;34;40mDigite ⌈ OK ⌋ para prosseguir ᚚ\x1B[0m ")
    if a == "OK" or a=="ok" or a=="Ok" or a=="oK":
      OK = True

es = 0
es1 = ""
es2 = ""
es3 = ""
es4 = ""
out1 = ""
out2 = ""
out3 = ""
out4 = ""

def Escolha2op():
  ESOK = False
  print("\n\n\n╭─────────────────────────────────╮\n (1)", es1,"\n (2)", es2,"\n╰─────────────────────────────────╯")
  while ESOK == False:
    es = int(input("» "))
    print("")
    if es == 1:
      print(out1)
      print("\n")
      ESOK = True
    elif es == 2:
      print(out2)
      print("\n")
      ESOK = True
    else:
      print("\033[0;31;40m Argumento inválido (Digite 1 ou 2)\x1B[0m")

def Escolha3op():
  ESOK = False
  print("\n\n\n╭─────────────────────────────────╮\n (1)", es1,"\n (2)", es2,"\n╰─────────────────────────────────╯")
  while ESOK == False:
    es = int(input("» "))
    print("")
    if es == 1:
      print(out1)
      print("\n")
      ESOK = True
    elif es == 2:
      print(out2)
      print("\n")
      ESOK = True
    elif es == 3:
      print(out3)
      print("\n")
      ESOK = True
    else:
      print("\033[0;31;40m Argumento inválido (Digite 1 ou 2)\x1B[0m")

def Escolha4op():
  ESOK = False
  print("\n\n\n╭─────────────────────────────────╮\n (1)", es1,"\n (2)", es2,"\n╰─────────────────────────────────╯")
  while ESOK == False:
    es = int(input("» "))
    print("")
    if es == 1:
      print(out1)
      print("\n")
      ESOK = True
    elif es == 2:
      print(out2)
      print("\n")
      ESOK = True
    elif es == 3:
      print(out3)
      print("\n")
      ESOK = True
    elif es == 4:
      print(out4)
      print("\n")
      ESOK = True
    else:
      print("\033[0;31;40m Argumento inválido (Digite 1 ou 2)\x1B[0m")

def Clear():
  es = 0
  es1 = ""
  es2 = ""
  es3 = ""
  es4 = ""
  out1 = ""
  out2 = ""
  out3 = ""
  out4 = ""
#Funções - Ataques--------------------------------------------------


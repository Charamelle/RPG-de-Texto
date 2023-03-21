# \
import time
import random
import sys

#Listas
esc = ["esc","Esc","eSc","esC","ESc","ESC","eSC"]
info = ["Info","info","INFO"]
rc = ["1","2","2.1","2.2","2.3","3","4","5"]
cposs = ["",False, False, False, False, False, False]
tipos_sk = ["of","def","sum","buff","debuff"]
frskills = ["Você toca seu pianinho com todo o ódio que você tem guardado dentro do seu corpinho de rato.", "Você mete a pata no pianinho, estourando os tímpanos de seus inimigos.", "Você toca seu pianinho, expressando toda a sua dor através da música, machucando fisicamente seus inimigos... talvez esteja na hora de ir pra terapia..."]
failini = ["Os dois vêm furiosos para cima de você, mas você desvia dos ataques.", "Seus inimigos se preparam para te atacar, mas se distraem brevemente com uma borboleta","O grande demônio sopra fogo em sua direção, mas você foge", "O bandido e a criatura vão te atacar, mas trombam em si mesmos."]
skills = ["Invocar Vespuccio - Invoca uma criatura aliada com 10 HP e 1d2 de dano [Pode usar 1 vez por batalha]", "Bola de Fogo - Dano: 1d8 [Cooldown: 2 turnos]", "Spikes de Gelo - Dano: 1d4 [Cooldown: 1 turno]", "Jato de Água Fervente - Dano: 1d4 [Cooldown: 1 turno]", "Afincar das Raízes - Pula o turno do inimigo", "Ataque Ousado - Dá 1d3 de dano bônus por 5 rodadas [Pode usar 1 vez por batalha]", "Ragnarok - Fica inalvejável por 2 rodadas [Pode usar 1 vez por batalha]", "Invocar Aberração - Invoca uma criatura aliada com 10 de HP e 1d2 de dano [Pode usar 1 vez por batalha]", "Hemorragia - Dano: 1d6 [Cooldown: 1 turnos]", "Ataque Rápido - Dano: 1d5 [Cooldown: 1 turno]", "Golpe Misericordioso - Dano: 1d12 [Cooldown: 3 turnos]", "Prece para Nossa Senhora das Graças - Cura 1d5 [Cooldown: 3 turnos]", "Fúria Divina - Dano: 1d10 [Cooldown: 3 turnos]", "Uma Longa História - Diminuí a chance de acerto dos inimigos em 30% por 1 round [Cooldown: 2 turnos]", "Poesia de Amor - Cura 1d3 [Cooldown: 1 turno]", "Melodia do Coração - Diminuí a chance de acerto dos inimigos em 30% por 1 round [Cooldown: 2 turnos]", "Cacofonia - Dano: 1d8 [Cooldown: 2 turnos]", "Heal Bem Vegano - Cura 1d5 [Cooldown: 3 turnos]"]
Morto = [False]
Escolha = [0]
# --- Dados do personagem
nome = ""
raca = ""
classe = ""

ap = ""
bonus = 0
bonusB = 0

sk1 = ""
sk2 = ""

# --- Valores ini-pts
HPbase = 20
if raca == "FADA" or raca == "RATO":
  HPbase = 15

sau = 0
frc = 0
pod = 0
des = 0
pts = 240-(sau+frc+pod+des)
HP1 = HPbase + (sau/10)
ptsok = False

# --- Outras variáveis
Bard = False
Kpt = False

#Funções - Gerais -----------------------------------------------------
def Conf():
  OK = False
  while OK == False:
    a = ""
    a = input("\033[0;34;48mDigite ⌈ OK ⌋ para prosseguir ᚚ\x1B[0m ")
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
    Escolha[0] = es
    print("")
    if Escolha[0] == 1:
      print(out1)
      print("\n")
      ESOK = True
    elif Escolha[0] == 2:
      print(out2)
      print("\n")
      ESOK = True
    else:
      print("\033[0;31;48m Argumento inválido (Digite 1 ou 2)\x1B[0m")

def Escolha3op():
  ESOK = False
  print("\n\n\n╭─────────────────────────────────╮\n (1)", es1,"\n (2)", es2,"\n (3)", es3,"\n╰─────────────────────────────────╯")
  while ESOK == False:
    es = int(input("» "))
    Escolha[0] = es
    print("")
    if Escolha[0] == 1:
      print(out1)
      print("\n")
      ESOK = True
    elif Escolha[0] == 2:
      print(out2)
      print("\n")
      ESOK = True
    elif Escolha[0] == 3:
      print(out3)
      print("\n")
      ESOK = True
    else:
      print("\033[0;31;48m Argumento inválido (Digite 1 ou 2)\x1B[0m")

def Escolha4op():
  ESOK = False
  print("\n\n\n╭─────────────────────────────────╮\n (1)", es1,"\n (2)", es2,"\n (3)", es3,"\n (4)", es4,"\n╰─────────────────────────────────╯")
  while ESOK == False:
    es = int(input("» "))
    Escolha[0] = es
    print("")
    if Escolha[0] == 1:
      print(out1)
      print("\n")
      ESOK = True
    elif Escolha[0] == 2:
      print(out2)
      print("\n")
      ESOK = True
    elif Escolha[0] == 3:
      print(out3)
      print("\n")
      ESOK = True
    elif Escolha[0] == 4:
      print(out4)
      print("\n")
      ESOK = True
    else:
      print("\033[0;31;48m Argumento inválido (Digite 1 ou 2)\x1B[0m")

#Funções - Ataques--------------------------------------------------


# FUNÇÃO: BATALHA --------------------------------------------------

def batalha():
  global Kpt
  FF = False
  CD1 = 0
  CD2 = 0
  turn = 1
  
  Summon_Cr = False
  AtkO = False #Atk Ousado
  RA = False #Afinc. das Raízes
  RAG = False #Ragnarok
  Kpt = False
  Att1 = 0
  Att2 = 0

  HP = HP1
  HPb = 2
  HPc = 10
  if Kpt == True:
    HPi = 30
  if Kpt == False:
    HPi = 25  
  print("\n\033[0;37;44m ◄ BATALHA INICIADA ► \x1B[0m")
  while FF == False:
    CA = 80
    if raca == "ELFO MACONHEIRO":
      CA -= 5
    print("\n\n\033[0;30;47m Round", turn,"\x1B[0m")
    print("\n» Qual sua ação?\n(1)", sk1,"\n(2)",sk2,"\n(3) Espada - Dano: 1d3 [Sem cooldown]")
    mov = int(input(""))
    ESCS = False
    #PLAYER ----------------------------------------------------------
    while ESCS == False:
      if mov == 1 and CD1<turn:
        if sk1 == skills[0]:
          Summon_Cr = True
          print("Você invoca seu amiguinho Vespuccio, uma incrivel vespa de 4 metros de altura, para te ajudar nessa batalha.")
          CD1 = 10000000
          ESCS = True
        if sk1 == skills[5]:
          AtkO = True
          Att1 = 5 + turn
          CD1 = 10000000
          ESCS = True
          print("Você fica revoltado e começa atacar com todo seu ódio. Cada ataque seu dará 1d3 de dano bônus nas próximas 5 rodadas.")
        if sk1 == skills[1]:
          roll = random.randint(1,100)
          if roll<=pod:
            dam = random.randint(1,8) + bonus
            HPi = HPi - dam
            ESCS = True
            CD1 = 2 + turn
          print("Fogo nelas!!! Você arremessa uma bola de fogo, dando",dam,"de dano!")
          if roll>pod:
            ESCS = True
            print("Você lança uma bolona de fogo, mas erra seu alvo.")
        if sk1 == skills[7]:
          Summon_Cr = True
          print("Você invoca sua criação para lutar ao seu lado na batalha!")
          CD1 = 10000000
          ESCS = True
        if sk1 == skills[9]:
          roll = random.randint(1,100)
          if roll<=frc:
            dam = random.randint(1,5)+ bonus
            HPi = HPi - dam
            ESCS = True
            CD1 = 1 + turn
          print("Você avança em seu inimigo em alta velocidade com sua faca, dando",dam,"de dano!")
          if roll>frc:
            ESCS = True
            print("Você avança em seu inimigo em alta velocidade, mas sua mira é terrível. Você errou, passando reto por ele.")
        if sk1 == skills[11]:
          roll = random.randint(1,100)
          if roll<=pod:
            dam = random.randint(1,5)+ bonus
            ESCS = True
            CD1 = 3 + turn
            HP = HP + dam
            if Bard == True:
              qm = int(input("Quem você quer curar?\n(1) Você mesmo\n(2) Bardo"))
              if qm == 1:
                HP = HP + dam
              print("Você cura", dam,"pontos de vida.")
              if qm == 2:
                HPb = HPb + dam
                print("Você cura", dam,"pontos de vida do bardo.")
            else:
              HP = HP + dam
              print("Você cura", dam,"pontos de vida.")
          if roll>pod:
            ESCS = True
            print("Suas preces foram ignoradas.")
        if sk1 == skills[13]:
          roll = random.randint(1,100)
          if roll<=pod:
            CA = CA + 30
            ESCS = True
            print("Ah, que belas palavras... seus inimigos ficaram mais calmos agora e terão mais dificuldade de te atacar nesse turno.")
            if roll>pod:
              ESCS = True
              print("Ninguém gostou da sua poesia :(")
        if sk1 == skills[15]:
          roll = random.randint(1,100)
          if roll<pod:
            CA = CA + 30
            ESCS = True
            print("Você se sente possuído pelo ritmo ragatanga e toca uma musiquinha, acalmando seus inimigos.")
            if roll>pod:
              print("Ninguém gostou da sua música :(")
              ESCS = True
      elif mov == 2 and CD2<turn:
        if sk2 == skills[1]:
          roll = random.randint(1,100)
          if roll<pod:
            dam = random.randint(1,8)+ bonus
            ESCS = True
            CD2 = 2 + turn
            HPi = HPi - dam
          print("Fogo nelas!!! Você arremessa uma bola de fogo, dando",dam,"de dano!")
          if roll>pod:
            ESCS = True
            print("Você lança uma bolona de fogo, mas erra seu alvo.")
        if sk2 == skills[2]:
          roll = random.randint(1,100)
          if roll<=pod:
            dam = random.randint(1,4)+ bonus
            HPi = HPi - dam
            ESCS = True
            CD2 = 1 + turn
          print("Você é possuído pelo ritmo da Lerigou e joga espinhos de gelo no inimigo. Você dá", dam,"de dano.")
          if roll>pod:
            ESCS = True
            print("Você erra os espinhos de gelo.")
        if sk2 == skills[3]:
          roll = random.randint(1,100)
          if roll<=pod:
            dam = random.randint(1,4)+ bonus
            HPi = HPi - dam
            ESCS = True
            CD2 = 1 + turn
          print("Você, furioso, cria um jato de água fervente e dá um banho nas vagabundas te batendo. Você dá", dam,"de dano.")
          if roll>pod:
            ESCS = True
            print("Você erra o jato.")
        if sk2 == skills[4]:
          ESCS = True
          RA = True
          CD2 = 3 + turn
        if sk2 == skills[17]:
          roll = random.randint(1,100)
          if roll<=pod:
            dam = random.randint(1,5)+ bonus
            ESCS = True
            CD2 = 3 + turn
            if Bard == True:
              qm = int(input("Quem você quer curar?\n(1) Você mesmo\n(2) Bardo"))
              if qm == 1:
                HP = HP + dam
              print("Você cura", dam,"pontos de vida.")
              if qm == 2:
                HPb = HPb + dam
                print("Você cura", dam,"pontos de vida do bardo.")
            else:
              HP = HP + dam
              print("Você cura", dam,"pontos de vida.")
          if roll>pod:
            ESCS = True
            print("Você falhou.")
        if sk2 == skills[6]:
          RAG = True
          Att2 = 2 + turn
          print("Você fica inalvejável")
        if sk2 == skills[8]:
          roll = random.randint(1,100)
          if roll<pod:
            dam = random.randint(1,6) + bonus
            HPi = HPi - dam
            ESCS = True
            CD2 = 1 + turn
          print("Você causa uma hemorragia interna em seu inimigo, rompendo suas veias e causando", dam,"de dano.")
          if roll>pod:
            ESCS = True
            print("Você erra o jato.")
        if sk2 == skills[10]:
          roll = random.randint(1,100)
          if roll<frc:
            dam = random.randint(1,12) + bonus
            HPi = HPi - dam
            ESCS = True
            CD2 = 3 + turn
          print("Você pula em seu inimigo, ferindo-o rapidamente, inflingindo", dam,"de dano.")
          if roll>frc:
            ESCS = True
            print("Você erra o ataque.")
        if sk2 == skills[12]:
          roll = random.randint(1,100)
          if roll<=pod:
            dam = random.randint(1,10) + bonus
            HPi = HPi - dam
            ESCS = True
            CD2 = 3 + turn
          print("- Você chama teu daddy deus pra dar um tapa neles... e ele dá!", dam,"de dano.")
          if roll>pod:
            ESCS = True
            print("Suas preces foram ignoradas.")
        if sk2 == skills[14]:
          roll = random.randint(1,100)
          if roll<pod:
            dam = random.randint(1,3) + bonus
            ESCS = True
            CD2 = 1 + turn
            if Bard == True:
              qm = int(input("Quem você quer curar?\n(1) Você mesmo\n(2) Bardo"))
              if qm == 1:
                HP = HP + dam
              print("Você cura", dam,"pontos de vida.")
              if qm == 2:
                HPb = HPb + dam
                print("Você cura", dam,"pontos de vida do bardo.")
            else:
              HP = HP + dam
              print("Você cura", dam,"pontos de vida.")
          if roll>pod:
            ESCS = True
            print("Ninguém gostou da sua poesia :(")
        if sk2 == skills[16]:
          roll = random.randint(1,100)
          if roll<=pod:
            dam = random.randint(1,8) + bonus
            HPi = HPi - dam
            ESCS = True
            CD2 = 2 + turn
            print(frskills[random.randint(0,3)], "Você deu", dam, "de dano.")
          if roll>pod:
            ESCS = True
            print("Você toca a pior música que consegue imaginar... mas por algum motivo, eles gostaram.")
      elif mov == 3:
        roll = random.randint(1,100)
        if roll<=frc:
          dam = random.randint(1,3) + bonus
          print("Você dá uma espadada nele, dando", dam,"de dano.")
          ESCS = True
        if roll>frc:
          ESCS = True
          print("Você erra seu golpe.")
      elif CD1>=turn or CD2>=turn:
        print("\033[0;31;48m Habilidade em cooldown\x1B[0m")
        mov = int(input(""))
      else:
        print("\033[0;31;48mArgumento inválido - Digite uma das três opções acima (1, 2 ou 3)\x1B[0m")
        mov = int(input(""))
    time.sleep(1)
    #INIMIGO() -----------------------------------------------------------
    if RA == False:
      if Kpt == True:
        roll = random.randint(1,100)
        rollp = random.randint(1,des) + 20
        if roll<CA and roll<rollp:
          dam = random.randint(1,6)
          rand = random.randint(1,2)
          if rand == 1 and Summon_Cr == True:
            HPc = HPc - dam
            print("Eles atacam sua criatura, dando", dam, "de dano.")
          else:
            HP = HP - dam
            print("Eles te atacam, dando", dam, "de dano.")
        else:
          print(failini[random.randint(0,3)])
      if Kpt == False:
        roll = random.randint(1,100)
        rollp = random.randint(1,des) + 15
        if roll<CA and roll<rollp:
          dam = random.randint(1,6)
          rand = random.randint(1,3)
          if rand == 1 and Summon_Cr == True:
            HPc = HPc - dam
            print(ap,"ataca sua criatura, dando", dam, "de dano.")
          elif rand == 2 and Bard == True:
            HPb = HPb - dam
            print(ap,"ataca o bardo, dando",dam,"de dano.")
          else:
            HP = HP - dam
            print(ap,"te ataca, dando", dam, "de dano.")
        else:
          print(failini[random.randint(0,3)])
    #Ataque - Criatura
    if Summon_Cr == True:
      dam = random.randint(1,2)
      HPi = HPi - dam
      print("Sua criatura ataca o inimigo, dando", dam,"de dano.")
    if Bard == True and Morto[0]!=True:
      dam = random.randint(1,2) + bonusB
      HPi = HPi - dam
      print("Seu aliado ataca o inimigo, dando", dam,"de dano.")
    if HP <= 0:
      print("\n\033[0;37;41m〤 Você morreu 〤\x1B[0m")
      sys.exit()
    if Bard == True and HPb <= 0 and Morto[0]!=True:
      Morto[0] = True
      print("\033[0;33;48m> Seu aliado (bardo) morreu.")
    if Summon_Cr == True and HPc <= 0:
      print("\033[0;33;48m> Sua criatura morreu")
      Summon_Cr = False
    print("\n\033[0;36;48mHP (",nome,") -",HP,"\x1B[0m")
    if Bard == True and Morto[0]!=True:
      print("\033[0;36;48mHP (Bardo) -",HPb,"\x1B[0m")
    if Bard == True and Morto[0] == True:
      print("\033[0;36;48mHP (Bardo) - MORTO\x1B[0m")
    if Summon_Cr == True:
      print("\033[0;36;48mHP (Criatura) -",HPc,"\x1B[0m")
    if RA == True:
      print("Turno inimigo pulado (time inimigo preso nas Raízes)")
    
    turn = turn + 1
    if Att1>turn:
      AtkO = False
    if Att2>turn:
      RAG = False
    if HPi <= 0:
      FF = True

#Intro--------------------------------------------------------------

print("\x1B[3mBem-vindo!\x1B[0m\n\nVocê se deparará com escolhas, para quais serão fornecidas opções de ação, para selecionar uma delas, selecione o número dentro do parênteses referente a opção escolhida.\n\n")

Conf()
print("\n")
for x in range (0,4):  
    b = "\033[1;35;48mEntrando em criação de personagem" + "." * x
    print (b, end="\r")
    time.sleep(0.3)
print("\033[1;35;48mEntrando em criação de personagem...\x1B[0m")

# --- Criação de personagem

nome = input("\nQual o seu nome?\033[3;37;48m ")

print("\n\n\033[1;35;48mEscolha de RAÇA")
time.sleep(0.3)

print("\n\x1B[0mCada raça recebe um atributo e um “defeito” (quirk) e poderá selecionar determinadas classes. Para ver as informações de uma raça digite info + o número referente à ela no index a seguir (Ex. info 3).\n1. Humano\n2. Elfo\n3. Anão\n4. Fadinha\n5. Rato Pianista\n\nPara escolher sua raça, digite ESC {index da raça escolhida}. (Ex. ESC 5)")

while raca == "":
  cmd, r = input("\033[3;37;48m").split()
  
  if cmd in info:
    if r == "1":
      print("\n\033[1;35;48m《 RAÇA - HUMANO 》\n\x1B[0m› Descrição: Caso você queira algo mais “vanilla” - não tem atributos ou quirks\n\033[0;32;48mPossíveis classes: Druida, Bárbaro, Mago, Assassino, Crente, Bardo\x1B[0m")
    if r == "2":
      print("\n\033[1;35;48m《 RAÇA - ELFO 》\n\x1B[0m› Essa raça é subdividida em duas, cada uma tendo seus próprios atributos.\n\n» Elfo Dark (2.1)\n› Atributo: Em ambientes escuros, sua chance de acerto aumenta em 10%\n› Quirk: Ao lutarem debaixo da luz solar, se sentem cansados, perdendo 5% da chance de acerto de todas suas ações\n\n» Elfo Maconheiro (2.2)\n› Atributo: Você é praticamente uma maconha ambulante, então, ao entrarem em contato com você inimigos ficaram relaxados, tendo uma queda de 5% de chance de acerto de ações ofensivas\n› Quirk: -5 pontos de força\n\n\033[0;32;48mPossíveis classes: Druida, Mago, Assassino, Crente, Bardo\x1B[0m")
    if r == "3":
      print("\n\033[1;35;48m《 RAÇA - ANÃO 》\n\x1B[0m› Atributos: +10% de chance de acerto e 1d2 de dano bônus em combates corpo-a-corpo \n› Quirks: -10% de chance de acerto em rolagens de DESTREZA \n\033[0;32;48mPossíveis classes: Bárbaro, Mago, Crente, Bardo\x1B[0m")
    if r == "4":
      print("\n\033[1;35;48m《 RAÇA - FADINHA 》\n\x1B[0m› Atributos: +20% de Chance de Acerto em qualquer magia\n› Quirks: -5 HP base (15)\n\033[0;32;48mPossíveis classes: Druida, Bárbaro, Mago, Crente, Bardo\x1B[0m")
    
    if r == "5":
      print("\n\033[1;35;48m《 RAÇA - RATO PIANISTA 》\n\x1B[0m› Atributos: +10% em rolagens de destreza\n› Quirks: -5 de HP base (15)\n\033[0;32;48mPossíveis classes: Rato Pianista\x1B[0m")

  if cmd in esc: #ESCOLHA DE RAÇA -------------------+
    if r == "1":
      print("Raça selecionada: Humano")
      cposs[1:6] = [True, True, True, True, True, True]
      raca = "HUMANO"
      
    if r == "2.1":
      print("Raça selecionada: Elfo (Dark)")
      cposs[1:6] = [True, False, True, True, True, True]
      raca = "ELFO DARK"
      
    if r == "2.2":
      print("Raça selecionada: Elfo (Maconheiro)")
      cposs[1:6] = [True, False, True, True, True, True]
      raca = "ELFO MACONHEIRO"
      
    if r == "3":
      print("Raça selecionada: Anão")
      desc = 10
      cposs[1:6] = [False, True, True, False, True, True]
      raca = "ANÃO"
      
    if r == "4":
      print("Raça selecionada: Fada")
      cposs[1:6] = [True, True, True, False, True, True]
      raca = "FADA"
      
    if r == "5":
      print("Raça selecionada: Rato Pianista")
      cposs[-1] = True
      raca = "RATO"
      
    if r == "2": 
      print("\033[0;31;48m Index de raça inválido.\x1B[0m")
      
  if cmd not in info and cmd not in esc:
    print("\033[0;31;48m Comando inválido. Possíveis comandos: info, esc.\x1B[0m")
  if r not in rc:
    print("\033[0;31;48m Index de raça inválido.\x1B[0m")

print("\n\n\033[1;35;48mEscolha de CLASSE")
time.sleep(1)
print("\n\n\x1B[0mCada classe recebe duas habilidades. Para ver as informações de uma classe digite info + o número referente à ela no index a seguir (Ex. info 6)\n1. Druída\n2. Bárbaro\n3. Mago\n4. Assassino\n5. Crente\n6. Bardo\n7. Rato Pianista\n\nPara escolher sua raça, digite ESC {index da classe escolhida}. (Ex. esc 7) - \033[0;32;48mVocê só poderá escolher uma classe que condiz com a sua raça (", raca,")\x1B[0m\n")

while classe == "": #ESCOLHA DE CLASSE ---------
  cmd, c = input("\033[3;37;48m").split()

  if cmd in info:
    if c == "1":
      print("\n\033[1;35;48m《 CLASSE - DRUIDA 》\n\x1B[0m\n› Invocar Vespuccio: invoca uma vespa gigante para lutar ao seu lado [10 HP, dano 1d2] - Só pode ser usada uma vez por batalha\n› Poderá ser escolhida um dos seguintes feitiços:\n- Bola de Fogo [dano 1d8] - Cooldown: 2 turnos\n- Spikes de Gelo [dano 1d4] - Cooldown: 1 turno\n- Jato d'água fervente [dano 1d4] - Cooldown: 1 turno\n- Afincar das raízes [imobiliza completamente o inimigo durante um turno] - Cooldown: 3 turnos\n- Heal bem vegano [cura 1d5] - Cooldown: 3 turnos")
      if cposs[1] == True:
        print("\033[0;32;48mVocê pode escolher essa classe.")
      else:
        print("\033[0;31;48mEssa classe está indisponível.")
    
    if c == "2":
      print("\n\033[1;35;48m《 CLASSE - BÁRBARO 》\n\x1B[0m\n› Ataque Ousado [dá 1d3 de dano bônus durante 5 turnos, mas se tornará 10% mais fácil de ser atingido] - Pode ser usado 1 vez por batalha\n› Ragnarok [fica inalvejável por 2 rodadas] - Só pode ser usado 1 vez por batalha")
      if cposs[2] == True:
        print("\033[0;32;48mVocê pode escolher essa classe.")
      else:
        print("\033[0;31;48mEssa classe está indisponível.")
        
    if c == "3":
      print("\n\033[1;35;48m《 CLASSE - MAGO 》\n\x1B[0m\n» Escolha uma dupla de magias (natureza ou sangue).\n\n› Natureza:\n- Bola de Fogo [dano 1d8] - Cooldown: 1 turno\n- Afincar das raízes [imobiliza completamente o inimigo durante um turno] - Cooldown: 2 turnos\n\n› Sangue:\n- Invocar aberração: invoca uma aberração de sangue para lutar ao seu lado [HP 10, dano 1d2] - Pode ser usada 1 vez por batalha\n- Hemorragia [dano 1d6] - Cooldown: 1 turno")
      if cposs[3] == True:
        print("\033[0;32;48mVocê pode escolher essa classe.")
      else:
        print("\033[0;31;48mEssa classe está indisponível.")
        
    if c == "4":
      print("\n\033[1;35;48m《 CLASSE - ASSASSINO 》\n\x1B[0m\n› Ataque Rápido [dano 1d5] - Cooldown: 1 turno\n› Golpe Misericordioso [1d12] - Cooldown: 3 turnos")
      if cposs[4] == True:
        print("\033[0;32;48mVocê pode escolher essa classe.")
      else:
        print("\033[0;31;48mEssa classe está indisponível.")
        
    if c == "5":
      print("\n\033[1;35;48m《 CLASSE - CRENTE 》\n\x1B[0m\n› Prece para Nossa Senhora das Graças: cura você ou um aliado [cura de 1d5] - Cooldown: 3 turnos\n› Fúria Divina [dano 1d10] - Cooldown: 3 turnos")
      if cposs[5] == True:
        print("\033[0;32;48mVocê pode escolher essa classe.")
      else:
        print("\033[0;31;48mEssa classe está indisponível.")
        
    if c == "6":
      print("\n\033[1;35;48m《 CLASSE - BARDO 》\n\x1B[0m\n› Uma Longa História: acalma seus inimigos, diminuindo suas chances de acertarem seus ataques em 30% - Cooldown: 2 turnos\n› Poesia de Amor [cura 1d3] - Cooldown: 2 turnos")
      if cposs[6] == True:
        print("\033[0;32;48mVocê pode escolher essa classe.")
      else:
        print("\033[0;31;48mEssa classe está indisponível.")
        
    if c == "7":
      print("\n\033[1;35;48m《 CLASSE - RATO PIANISTA 》\n\x1B[0m\n› Melodia do Coração: acalma seus inimigos, diminuindo suas chances de acertarem seus ataques em 30% - Cooldown: 2 turnos\n› Cacofonia [dano 1d8] - Cooldown: 2 turnos")
      if cposs[7] == True:
        print("\033[0;32;48mVocê pode escolher essa classe.")
      else:
        print("\033[0;31;48mEssa classe está indisponível.")


  
  if cmd in esc:
    if c == "1":
      sk1 = skills[0]
      classe = "druida"
      print("Escolha um dos seguintes feitiços (digite apenas o número):\n(1) Bola de Fogo\n(2) Spikes de Gelo\n(3) Jato d'água fervente\n(4) Afincar das raízes\n(5) Heal bem vegano")
      ch = int(input("» "))
      if ch == 1:
        sk2 = skills[1]
      if ch == 2:
        sk2 = skills[2]
      if ch == 3:
        sk2 = skills[3]
      if ch == 4:
        sk2 = skills[4]
      if ch == 5:
        sk2 = skills[17]
    if c == "2":
      classe = "barbaro"
      sk1 = skills[5]
      sk2 = skills[6]
    if c == "3":
      classe = "mago"
      print("Escolha uma dupla de poderes abaixo:\n(1) Natureza:\n- Bola de fogo\n- Afincar das raízes\n(2) Sangue:\n- Invocar aberração\n- Hemorragia")
      ch = int(input("» "))
      if ch == 1:
        sk1 = skills[1]
        sk2 = skills[4]
      if ch == 2:
        sk1 = skills[7]
        sk2 = skills[8]
    if c == "4":
      classe = "assassino"
      sk1 = skills[9]
      sk2 = skills[10]
    if c == "5":
      classe = "crente"
      sk1 = skills[11]
      sk2 = skills[12]
    if c == "6":
      classe = "bardo"
      sk1 = skills[13]
      sk2 = skills[14]
    if c == "7":
      classe = "rato"
      sk1 = skills[15]
      sk2 = skills[16]
print("Classe selecionada: ", classe)

print("")
time.sleep(1)
print("")
time.sleep(1)

#DISTRIBUIÇÃO DE PONTOS ------------------------------

print("\n\n\033[1;35;48mDistribuição de Pontos")
time.sleep(1)
print("\n\n\x1B[0mQuanto maior a quantidade de pontos você tiver em certa área, maior será sua chance de ter sucesso em suas ações durante batalhas, com exceção de SAÚDE, que irá apenas auxiliar na quantidade de vida do personagem. FORÇA é utilizado para combates corpo-a-corpo, PODER para lançar feitiços e DESTREZA para desviar de ataques. Escolha entre uma das disposições disponíveis:\n\n\n")
time.sleep(1)
print("\033[1;35;48m《 DISTRIBUIÇÃO 1 》\n\x1B[0m\n› SAÚDE: 60\n› FORÇA: 60\n› PODER: 60\n› DESTREZA: 60\n\n")
time.sleep(0.3)
print("\033[1;35;48m《 DISTRIBUIÇÃO 2 》\n\x1B[0m\n› SAÚDE: 50\n› FORÇA: 50\n› PODER: 90\n› DESTREZA: 50\n\n")
time.sleep(0.3)
print("\033[1;35;48m《 DISTRIBUIÇÃO 3 》\n\x1B[0m\n› SAÚDE: 60\n› FORÇA: 80\n› PODER: 60\n› DESTREZA: 70\n\n")
time.sleep(0.3)
print("\033[1;35;48m《 DISTRIBUIÇÃO 4 》\n\x1B[0m\n› SAÚDE: 80\n› FORÇA: 70\n› PODER: 70\n› DESTREZA: 40\n\n")
time.sleep(0.2)
print("Selecione uma das opções (1, 2, 3 ou 4)")

while ptsok == False:
  lero = int(input("» "))
  if lero == 1:
    sau = 60
    frc = 60
    pod = 60
    des = 60
    ptsok = True
  elif lero == 2:
    sau = 50
    frc = 50
    pod = 90
    des = 50
    ptsok = True
  elif lero == 3:
    sau = 60
    frc = 80
    pod = 60
    des = 70
    ptsok = True
  elif lero == 4:
    sau = 80
    frc = 70
    pod = 70
    des = 40
    ptsok = True
  else:
    print("\033[0;31;48m Argumento inválido, selecione uma das opções dadas")

if raca == "ELFO DARK":
  pod = pod + 10
  des = des + 10
elif raca == "ANÃO":
  frc = frc + 10
  des = des - 10
elif raca == "FADA":
  pod = pod + 20
elif raca == "RATO":
  des = des + 10
  
print("") #espacinho pra deixar bonitinho

for x in range (0,4):  
    b = "\033[1;35;48mIniciando. narrativa" + "." * x
    print (b, end="\r")
    time.sleep(0.3)
print("\033[1;35;48mIniciando narrativa...\x1B[0m")

#EVENTO 1
print("Você se encontra na Taverna do Nei, um grande estabelecimento, que nesta noite fria e seca, está muito movimentado. Você foi contratado por um senhor notório por sua grande riqueza para encontrar e recuperar uma relíquia de sua família, um grande medalhão dourado com finos detalhes esculpidos em sua superfície. Essa taverna teria sido o último local em que o bandido teria sido visto.\nVocê olha ao redor da sala e em meio de pessoas que conversavam alto, bebiam e jogavam, você avista quem procurava, o ladrão do medalhão, um homem magro e alto, com uma postura curvada, que carregava em si uma adaga com uma lâmina trabalhada, com detalhes em vermelho. Como o bar está muito movimentado, é meio arriscado iniciar uma perseguição, já que é mais fácil se misturar em meio às pessoas e fugir, mas, caso pegá-lo agora, você poderá voltar para casa mais cedo, assim podendo descansar. Portanto, você irá…")
es1 = "Arriscar e iniciar uma perseguição"
es2 = "Esperar que ele saia da taverna para segui-lo"
out1 = "Você se aproxima rapidamente do procurado, que corre entre as pessoas, empurrando todos em seu caminho, causando uma comoção. Uma briga se inicia e você o perde de vista, perdendo sua chance de capturá-lo.\n\n\033[0;37;41m〤 Fim de Jogo 〤\x1B[0m"
out2 = "Horas se passam e nada acontece. Por conta do tédio, você decide apelidar o bandido carinhosamente de:"
Escolha2op()

if Escolha[0] == 1:
  sys.exit()

else:
  ap = input("Digite o nome que você deu a ele: ")
  print("\nJá é madrugada, quando você nota uma movimentação diferente vinda de", ap, "que está indo para o lado de fora. Você o segue de longe, passando despercebido, e o vê se aproximando de um bardo e de um senhor que conversavam do lado de fora. O malfeitor se aproxima andando lentamente dos homens enquanto toca uma pequena flauta, cuja música é baixa demais para você ouví-la de onde você está. Subitamente ambos os senhores colapsam no chão, sendo então amarrados, vendados e colocados em uma carruagem por", ap,"Então, você se apressa para montar em sua montaria, que é…")

es1 = "Só um cavalo normal"
es2 = "Uma grande besta peluda com quatro olhos"
es3 = "Uma pulga do tamanho de um elefante"
es4 = "Um grande cachorro vestido de cenoura"
out1 = ""
out2 = ""
out3 = ""
out4 = ""
Escolha4op()

#EVENTO 2
print("Seguindo o",ap,"você se depara com uma pequena entrada para uma caverna, onde você entra e vê um longo corredor de pedras. Ao seguir este caminho, você se encontra em um pequeno espaço repleto de caixotes e potes de madeira, pedaços de roupas rasgadas e algumas armas empilhadas em um canto. Encostado em uma das paredes está um dos reféns, sentado, amarrado a uma estaca de madeira, ainda vendado. Do outro lado da sala há uma passagem. Você…")

es1 = "Liberta o refém"
es2 = "Segue o caminho em busca do bandido"
out1 = "Você se aproxima do refém, corta a corda que estava o amarrando e retira o saco que estava cobrindo sua cabeça, que revela um pequeno bardo de cabelos azuis longos e olhos acinzentados, que te olha assustado. Você sinaliza para que fique quieto e aponta com a cabeça para a pilha de armas, sugerindo-o a pegar uma. Ele se aproxima da pilha e pega um arco e algumas flechas e te olha. Você sinaliza para que ele te siga e entra na passagem."
out2 = ""
Escolha2op()

# EVENTO 3.1 (ROTA COM BARDO)
if Escolha[0] == 1:
  Bard = True
  print("Ao atravessar a passagem, você se depara com um grande salão com grandes pilares de pedra. Na parede, há uma enorme escultura de uma besta humanóide com quatro grandes chifres em sua cabeça, braços extremamente musculares e enormes garras. Logo na frente da estátua há um grande círculo detalhado com espirais trinchado no chão. Logo no centro está o", ap ,"segurando sua adaga contra a garganta do outro refém, que está de joelhos, enquanto ele recita algo em uma língua que você não entende. Perto de você há uma entrada para uma pequena sala que aparenta ter seu interior mais trabalhado, que parece um local digno de se guardar o medalhão. Você…")

  es1 = "Fica apenas observando a cena"
  es2 = "Tenta impedir o sacrifício"
  es3 = "Vai em busca do medalhão pela caverna"
  out1 = ""
  out2 = ""
  out3 = ""
  Escolha3op()
  if Escolha[0] == 1:
    print(ap,"puxa sua adaga, cortando a traquéia do refém. O sangue se espalha pelas mini-trincheiras em formatos circulares desenhados no chão, começando a brilhar levemente.", ap ,"fica quieto, se ajoelha e abaixa a cabeça.\n\nVocê utiliza dessa oportunidade para entrar na sala e ir em busca do medalhão. Você se depara com uma sala com suas paredes polidas, com alguns pequenos desenhos entalhados, ao centro há três pedestais. No pedestal da esquerda há uma manopla dourada, com diversos desenhos em prata, no do meio há um cajado de madeira escura, com desenhos de astros em seu cabo e em sua ponta traz um belo cristal azul. No último pedestal, à direita, você vê… nada. Se aproximando dos pedestais, você percebe que há uma nota em cada um. Pegando-as, você lê:")
    print("\nPEDESTAL À ESQUERDA\n・Manopla de Kian\n╰ Essa poderosa manopla canaliza a força dos deuses em quem vesti-la, aumentando sua força.\n\nPEDESTAL AO CENTRO\n・Cajado de Mona\n╰ Fabricado pela prestigiosa feiticeira, Mona, este cajado têm o poder de significamente fortalecer os poderes de qualquer tipo de magia de quem possuí-lo.\n\nPEDESTAL À DIREITA:\n・Medalhão de Araghornn\n╰ Forjado no submundo, este poderoso artefato é capaz de trazer ao plano superficial a grande besta demoníaca, Araghornn. Porém, para que funcione o ritual deverá ser carregado em frente à grande estátua, na caverna oculta.\n\nVocê pode pegar um dos artefatos a sua frente para se fortalecer, você pega…")
    
    es1 = "Manopla de Kian"
    es2 = "Cajado de Mona"
    es3 = "Nenhum"
    Escolha3op()
    if Escolha[0] == 1:
      print("Você pega a Manopla de Kian e o bardo pega o Cajado de Mona\n\033[0;32;48mVocê dará +2 de dano.\x1B[0m")
      bonus += 2
    elif Escolha[0] == 2:
      print("Você pega a Manopla de Kian e o bardo pega a Manopla de Kian\n\033[0;32;48mVocê dará +2 de dano.\x1B[0m")
      bonus += 2
    elif Escolha[0] == 3:
      print("Você deixa ambos os artefatos em seus postos. O bardo pega o Cajado de Mona")
      bonusB += 2
    print("Percebendo que o medalhão não está na vitrine, você sai da pequena sala, indo para o grande salão. Você olha para o ritual e vê, bem ao centro, um pequeno pedestal, ao olhar um pouco mais para ele, você percebe que o medalhão está em cima dele. Você então decide confrontar", ap,". Você se direciona ao grande salão, onde se encontra com ele.")
    Escolha[0] = 0
    batalha()
    if Morto[0] == True:
      print("\n\nAo derrotar",ap,", você lentamente se levanta e se arrasta até o medalhão e o pega. Porém, antes que pudesse cantar sua vitória, ao virar para ajudar seu aliado, você o vê no chão, imóvel, suas tentativas de reanimá-lo são falhas e você se encontra fraco demais para carregá-lo para fora do local. Cabisbaixo, você caminha, lentamente, até a entrada da caverna, onde você sobe em sua montaria novamente e parte para vila para ser propriamente tratado e finalizar sua missão.")
    else:
      print("\n\nAo derrotar ",ap,", você lentamente se levanta com a ajuda de seu aliado e se arrasta até o medalhão e o pega. Lentamente vocês caminham até a entrada da caverna, onde sobem em sua montaria novamente e partem para vila para ser propriamente tratados e para que você possa finalizar sua missão.")
  elif Escolha[0] == 2:
    print("Você corre até o ritual, atacando", ap)
    Escolha[0] = 0
    batalha()
    if Morto[0] == True:
      print("\n\nAo derrotar",ap,", você lentamente se levanta e se arrasta até o medalhão e o pega. Porém, antes que pudesse cantar sua vitória, ao virar para ajudar seu aliado, você o vê no chão, imóvel, suas tentativas de reanimá-lo são falhas e você se encontra fraco demais para carregá-lo para fora do local. Cabisbaixo, você caminha, lentamente, até a entrada da caverna, onde você sobe em sua montaria novamente e parte para vila para ser propriamente tratado e finalizar sua missão.")
    else:
      print("\n\nAo derrotar ",ap,", você lentamente se levanta com a ajuda de seu aliado e se arrasta até o medalhão e o pega. Lentamente vocês caminham até a entrada da caverna, onde sobem em sua montaria novamente e partem para vila para ser propriamente tratados e para que você possa finalizar sua missão.")
  elif Escolha[0] == 3:
    print("Enquanto",ap, "estava ocupado, você rapidamente entra na pequena passagem. Você se depara com uma sala com suas paredes polidas, com alguns pequenos desenhos entalhados, ao centro há três pedestais. No pedestal da esquerda há uma manopla dourada, com diversos desenhos em prata, no do meio há um cajado de madeira escura, com desenhos de astros em seu cabo e em sua ponta traz um belo cristal azul. No último pedestal, à direita, você vê… nada. Se aproximando dos pedestais, você percebe que há uma nota em cada um. Pegando-as, você lê:")
    print("\nPEDESTAL À ESQUERDA\n・Manopla de Kian\n╰ Essa poderosa manopla canaliza a força dos deuses em quem vesti-la, aumentando sua força.\n\nPEDESTAL AO CENTRO\n・Cajado de Mona\n╰ Fabricado pela prestigiosa feiticeira, Mona, este cajado têm o poder de significamente fortalecer os poderes de qualquer tipo de magia de quem possuí-lo.\n\nPEDESTAL À DIREITA:\n・Medalhão de Araghornn\n╰ Forjado no submundo, este poderoso artefato é capaz de trazer ao plano superficial a grande besta demoníaca, Araghornn. Porém, para que funcione o ritual deverá ser carregado em frente à grande estátua, na caverna oculta.\n\nVocê pode pegar um dos artefatos a sua frente para se fortalecer, você pega…")
    
    es1 = "Manopla de Kian"
    es2 = "Cajado de Mona"
    es3 = "Nenhum"
    Escolha3op()
    if Escolha[0] == 1:
      print("Você pega a Manopla de Kian e o bardo pega o Cajado de Mona\n\033[0;32;48mVocê dará +2 de dano.\x1B[0m")
      bonus += 2
    elif Escolha[0] == 2:
      print("Você pega a Manopla de Kian e o bardo pega a Manopla de Kian\n\033[0;32;48mVocê dará +2 de dano.\x1B[0m")
      bonus += 2
    elif Escolha[0] == 3:
      print("Você deixa ambos os artefatos em seus postos. O bardo pega o Cajado de Mona")
      bonusB += 2
    print("Percebendo que o medalhão não está na vitrine, você sai da pequena sala, indo para o grande salão. Você olha para o ritual e vê, bem ao centro, um pequeno pedestal, ao olhar um pouco mais para ele, você percebe que o medalhão está em cima dele. Você então decide confrontar", ap,". Você se direciona ao grande salão, onde se encontra com ele.")
    Escolha[0] = 0
    batalha()
    if Morto[0] == True:
      print("\n\nAo derrotar",ap,", você lentamente se levanta e se arrasta até o medalhão e o pega. Porém, antes que pudesse cantar sua vitória, ao virar para ajudar seu aliado, você o vê no chão, imóvel, suas tentativas de reanimá-lo são falhas e você se encontra fraco demais para carregá-lo para fora do local. Cabisbaixo, você caminha, lentamente, até a entrada da caverna, onde você sobe em sua montaria novamente e parte para vila para ser propriamente tratado e finalizar sua missão.")
    else:
      print("\n\nAo derrotar ",ap,", você lentamente se levanta com a ajuda de seu aliado e se arrasta até o medalhão e o pega. Lentamente vocês caminham até a entrada da caverna, onde sobem em sua montaria novamente e partem para vila para ser propriamente tratados e para que você possa finalizar sua missão.")


        

# EVENTO 3.2 (ROTA SEM BARDO)

if Escolha[0] == 2:
  Kpt = True
  print("Ao atravessar a passagem, você se depara com um grande salão com grandes pilares de pedra. Na parede, há uma enorme escultura de uma besta humanóide com quatro grandes chifres em sua cabeça, braços extremamente musculares e enormes garras. Logo na frente da estátua há um grande círculo detalhado com espirais trinchado no chão. Logo no centro está o", ap ,"segurando sua adaga contra a garganta do outro refém, que está de joelhos, enquanto ele recita algo em uma língua que você não entende. Perto de você há uma entrada para uma pequena sala que aparenta ter seu interior mais trabalhado, que parece um local digno de se guardar o medalhão. Você…")
  
  es1 = "Fica apenas observando a cena"
  es2 = "Tenta impedir o sacrifício"
  es3 = "Vai em busca do medalhão pela caverna"
  out1 = ""
  out2 = ""
  out3 = ""
  Escolha3op()

  
  if Escolha[0] == 1:
    print(ap,"puxa sua adaga, cortando a traquéia do refém. O sangue se espalha pelas mini-trincheiras em formatos circulares desenhados no chão, começando a brilhar levemente.", ap ,"fica quieto, se ajoelha e abaixa a cabeça.\n\nVocê utiliza dessa oportunidade para entrar na sala e ir em busca do medalhão. Você se depara com uma sala com suas paredes polidas, com alguns pequenos desenhos entalhados, ao centro há três pedestais. No pedestal da esquerda há uma manopla dourada, com diversos desenhos em prata, no do meio há um cajado de madeira escura, com desenhos de astros em seu cabo e em sua ponta traz um belo cristal azul. No último pedestal, à direita, você vê… nada. Se aproximando dos pedestais, você percebe que há uma nota em cada um. Pegando-as, você lê:")
    print("\nPEDESTAL À ESQUERDA\n・Manopla de Kian\n╰ Essa poderosa manopla canaliza a força dos deuses em quem vesti-la, aumentando sua força.\n\nPEDESTAL AO CENTRO\n・Cajado de Mona\n╰ Fabricado pela prestigiosa feiticeira, Mona, este cajado têm o poder de significamente fortalecer os poderes de qualquer tipo de magia de quem possuí-lo.\n\nPEDESTAL À DIREITA:\n・Medalhão de Araghornn\n╰ Forjado no submundo, este poderoso artefato é capaz de trazer ao plano superficial a grande besta demoníaca, Araghornn. Porém, para que funcione o ritual deverá ser carregado em frente à grande estátua, na caverna oculta.\n\nVocê pode pegar um dos artefatos a sua frente para se fortalecer, você pega…")
    
    es1 = "Manopla de Kian"
    es2 = "Cajado de Mona"
    es3 = "Nenhum"
    if Escolha[0] == 1:
      print("Você pega a Manopla de Kian e o bardo pega o Cajado de Mona\n\033[0;32;48mVocê dará +2 de dano.\x1B[0m")
      bonus += 2
    elif Escolha[0] == 2:
      print("Você pega a Manopla de Kian e o bardo pega a Manopla de Kian\n\033[0;32;48mVocê dará +2 de dano.\x1B[0m")
      bonus += 2
    elif Escolha[0] == 3:
      print("Você deixa ambos os artefatos em seus postos.")
    print("Percebendo que o medalhão não está na vitrine, você sai da pequena sala, indo para o grande salão. Você olha para o ritual e vê, bem ao centro, um pequeno pedestal, ao olhar um pouco mais para ele, você percebe que o medalhão está em cima dele. Você então decide confrontar", ap,". Você se direciona ao grande salão, onde se encontra com ele.\n\nO chão começa a tremer violentamente, o medalhão começa a brilhar intensamente. A enorme estátua de pedra começa a quebrar e, uma enorme besta, aparece de dentro da estátua, como se as pedras que formam o monumento fossem apenas uma pele externa da grande besta. Ela se solta e, com um olhar furioso, olha em sua direção.")
    Escolha[0] = 0
    batalha()
  elif Escolha[0] == 2:
    print("Você corre até o ritual, atacando", ap)
    Escolha[0] = 0
    batalha()
    print("Ao ver a besta cair, você lentamente se levanta e se arrasta até o medalhão e o pega. Lentamente você caminha até a entrada da caverna, onde você sobe em sua montaria novamente e parte para vila para ser propriamente tratado e finalizar sua missão.")
  elif Escolha[0] == 3:
    print("Enquanto",ap, "estava ocupado, você rapidamente entra na pequena passagem. Você se depara com uma sala com suas paredes polidas, com alguns pequenos desenhos entalhados, ao centro há três pedestais. No pedestal da esquerda há uma manopla dourada, com diversos desenhos em prata, no do meio há um cajado de madeira escura, com desenhos de astros em seu cabo e em sua ponta traz um belo cristal azul. No último pedestal, à direita, você vê… nada. Se aproximando dos pedestais, você percebe que há uma nota em cada um. Pegando-as, você lê:")
    print("\nPEDESTAL À ESQUERDA\n・Manopla de Kian\n╰ Essa poderosa manopla canaliza a força dos deuses em quem vesti-la, aumentando sua força.\n\nPEDESTAL AO CENTRO\n・Cajado de Mona\n╰ Fabricado pela prestigiosa feiticeira, Mona, este cajado têm o poder de significamente fortalecer os poderes de qualquer tipo de magia de quem possuí-lo.\n\nPEDESTAL À DIREITA:\n・Medalhão de Araghornn\n╰ Forjado no submundo, este poderoso artefato é capaz de trazer ao plano superficial a grande besta demoníaca, Araghornn. Porém, para que funcione o ritual deverá ser carregado em frente à grande estátua, na caverna oculta.\n\nVocê pode pegar um dos artefatos a sua frente para se fortalecer, você pega…")
    
    es1 = "Manopla de Kian"
    es2 = "Cajado de Mona"
    es3 = "Nenhum"
    Escolha3op()
    
    if Escolha[0] == 1:
      print("Você pega a Manopla de Kian e o bardo pega o Cajado de Mona\n\033[0;32;48mVocê dará +2 de dano.\x1B[0m")
      bonus += 2
    elif Escolha[0] == 2:
      print("Você pega a Manopla de Kian e o bardo pega a Manopla de Kian\n\033[0;32;48mVocê dará +2 de dano.\x1B[0m")
      bonus += 2
    elif Escolha[0] == 3:
      print("Você deixa ambos os artefatos em seus postos.")
    print("Percebendo que o medalhão não está na vitrine, você sai da pequena sala, indo para o grande salão. Você olha para o ritual e vê, bem ao centro, um pequeno pedestal, ao olhar um pouco mais para ele, você percebe que o medalhão está em cima dele. Você então decide confrontar", ap,". Você se direciona ao grande salão, onde se encontra com ele.\nO chão começa a tremer violentamente, o medalhão começa a brilhar intensamente. A enorme estátua de pedra começa a quebrar e, uma enorme besta, aparece de dentro da estátua, como se as pedras que formam o monumento fossem apenas uma pele externa da grande besta. Ela se solta e, com um olhar furioso, olha em sua direção.")
    Escolha[0] = 0
    batalha()
    print("\nAo ver a besta cair, você lentamente se levanta e se arrasta até o medalhão e o pega. Lentamente você caminha até a entrada da caverna, onde você sobe em sua montaria novamente e parte para vila para ser propriamente tratado e finalizar sua missão.")

time.sleep(1)
print("\033[1;35;48m ~fim\x1B[0m")
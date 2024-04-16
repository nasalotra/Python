def Xpow (x , y) :
    val = 1
    for i in range(y) :
        val = x * val
    return val

def BaseToDec (base , toHexa , tab) :
    toHexa = str(toHexa)
    lenght = len(toHexa)
    value = 0
    for i in range(lenght) :
        one = Xpow(base , i) * int(( 10 + tab.index(int(toHexa[(lenght - 1) - i]))) if int(toHexa[(lenght - 1) - i]) in tab else int(toHexa[(lenght - 1) - i]))
        value += one
    return value


def DecToBase (base , toHexa , tab ) :
    quotient = toHexa
    hexa = ""
    while  True :
        modulo = quotient % base
        quotient  = int(quotient / base)
        hexa = str(( tab[ (modulo%10)]  if modulo >= 10  else modulo )) + hexa
        if quotient == 0 :
            break
    return hexa




def toInto(InputBase , Value , OutputBase):
    tab = ["A", "B" , "C" , "D" , "E" , "F"]
    return str(DecToBase(OutputBase , BaseToDec(InputBase , Value , tab) , tab))




"""
    [
        [1,0,0],
        [0,1,0]
    ]
"""


def countVar(toCalc):
    variables = []
    toCalc = str(toCalc).lower()
    i = 0
    for x in toCalc:
        if not(str(x).isspace()):
            if (x <= "z" and x >= "a") and ((((i == len(toCalc) - 1) or not(toCalc[i + 1] <= "z" and toCalc[i + 1] >= "a")) and toCalc[i - 1] == " ") or ((i == 0 or not(toCalc[i - 1] <= "z" and toCalc[i - 1] >= "a")) and toCalc[i + 1] == " ") or (toCalc[i - 1] == "(" and toCalc[i + 1] == ")")):
                    if not(x in variables):
                        variables.append(x)
        i += 1
    return variables

def indexReplace(chaine , index , car):
    return f"{chaine[:index]}{car}{chaine[index + 1:]}"


def AentreZ(x):
    return (x <= "z" and x >= "a")

def analyse(toCalc , line , variables):
    toCalc = str(toCalc).lower()
    i = 0
    for x in toCalc:
        if not(str(x).isspace()):
            if (x <= "z" and x >= "a") and ((((i == len(toCalc) - 1) or not(toCalc[i + 1] <= "z" and toCalc[i + 1] >= "a")) and toCalc[i - 1] == " ") or ((i == 0 or not(toCalc[i - 1] <= "z" and toCalc[i - 1] >= "a")) and toCalc[i + 1] == " ") or (toCalc[i - 1] == "(" and toCalc[i + 1] == ")")):
                toCalc = indexReplace(toCalc , i , line[variables.index(x)])
        i += 1
    return int(eval(toCalc))



def TrulyTable(generator):
    generator = str(generator).lower()
    # print(generator)
    table = []
    max = ""
    variables = countVar(generator)
    print("\n")
    for x in variables:
        max += "1"
    max = int(max)
    max = toInto(2 , max , 10)
    for x in range(int(max) + 1):
        add = []
        res = toInto(10, x, 2)
        for y in res:
            add.append(int(y))
        if len(add) < len(variables):
            for y in range(len(variables) - len(add)):
                add.insert(0 , 0)
        table.append(add)

    funcRes = []
    lines = ""
    for k in variables:
        lines += f"| {k} "
    lines += f"| f({generator}) |" 
    hr = ""
    for k in range(len(lines)):
        hr += "-"
    print(hr)
    print(lines)
    print(hr)
    for line in table:
        lines = ""
        ok = analyse(generator , line , variables)
        for k in line:
            lines += f"| {k} "
        leng = int((len(f"| f({generator}) |") - 3)/2)
        coco = ""
        for k in range(leng):
            coco += " "
        lines += f"|{coco}{' ' if len(coco) % 2 != 0 else ''}{ok}{coco}|"
        funcRes.append(ok)
        print(lines)

    hr = ""
    for k in range(len(lines)):
        hr += "-"
    print(hr+"\n")
    return [table , funcRes, variables]

Start = input("Veuillez entrer l'expression de la fonction logique\n>>")
All = TrulyTable(Start.strip())

##############################################################################

valeur = All[0]

func = All[1]

var = All[2]


variable = ""
x = len(valeur[0])
y = len(func)

Pforme = ""
Sforme = ""
tabP = []
tabS = []

def FormeCConjonctive(tab, var, x):
    j = 0
    if x == 0:
        return NULL
    solution = ""
    while j < x:
        if tab[j] == 0:
            solution += var[j] + "'"
        elif tab[j] == 1:
            solution += var[j]
        if j < x - 1:
            solution += " . "
        j += 1
    return solution

def FormeCDisjonctive(tab, var, x):
    j = 0
    if x == 0:
        return NULL
    solution = ""
    while j < x:
        if tab[j] == 1:
            solution += var[j] + "'"
        elif tab[j] == 0:
            solution += var[j]
        if j < x - 1:
            solution += " + "
        j += 1
    solution = "(" + solution + ")"
    return solution

i = 0
numP = 0
numS = 0
while i < y:
    if func[i] == 1:
        tabP.append(i)
        numP += 1
    if func[i] == 0:
        tabS.append(i)
        numS += 1
    i += 1

j = 0
while j < numP:
    Pforme += FormeCConjonctive(valeur[tabP[j]], var, x)
    if j < numP - 1:
        Pforme += " + "
    j += 1

j = 0
while j < numS:
    Sforme += FormeCDisjonctive(valeur[tabS[j]], var, x)
    if j < numS - 1:
        Sforme += " . "
    j += 1

k = 0
while k < x:
    variable += var[k]
    if k < x - 1:
        variable += ","
    k += 1
 
print(f"Premiere forme canonique: \n f({variable}) = " + Pforme + "\n")
print(f"Deuxieme forme canonique: \n  f({variable}) = " + Sforme + "\n")

# ~~~~~~~~ Latihan & Oretan ~~~~~~~~
# Vincent
def segitigaKata(param):
    newList = list(param)
    count = 0
    rowCount = 0
    for i in range(0, int(len(newList)/2)):
        for j in range(0, i+1):
            print(newList[count], end = ' ')
            count += 1
        rowCount += 1
        print()
        if(count == len(newList)):
            break

    count = 0
    for i in range(rowCount, 0, -1):
        for j in range(i, 0, -1):
            if count == len(newList):
                break
            print(newList[count], end = ' ')
            count += 1
        print()

userInput = str(input('Masukkan kata yang ingin dijadikan segitiga: ')).replace(' ', '')
if len(userInput) < 10:
    print('Mohon maaf, jumlah karakter tidak memenuhi syarat membentuk pola.')
else:
    segitigaKata(userInput)


# ----------------------------------------------------------------------------------------
# Diawali dengan angka 4, 5 atau 6.
# Terdiri atas tepat 16 digit angka.
# Hanya mengandung angka 0-9.
# Boleh dituliskan berupa grup 4 digit yang dipisahkan dengan tanda hubung "-"
# Tidak boleh terdapat 1 angka yang diulang >3x & tertulis secara beruntun, misal: 3333.

import json

# Adapun kriteria nomor kartu kredit yang valid adalah sebagai berikut:

# Diawali dengan angka 4, 5 atau 6.
# Terdiri atas tepat 16 digit angka.
# Hanya mengandung angka 0-9.
# Boleh dituliskan berupa grup 4 digit yang dipisahkan dengan tanda hubung "-"
# Tidak boleh terdapat 1 angka yang diulang >3x & tertulis secara beruntun, misal: 3333.
                
def checkFFS(param):
    print(param[0])
    if int(param[0]) == 4 or int(param[0]) == 5 or int(param[0]) == 6:
        return True
    else:
        return False

def checkDot(param):
    dot = '.'
    if dot in str(param):
        return False
    else:
        return True

def checkLength(param):
    if len(str(param).replace('-', '')) == 16:
        return True
    else:
        return False

def checkNumeric(param):
    if str(param).replace('-', '').isnumeric():
        return True
    else:
        return False

def checkRepetition(param):
    newList = list(str(param).replace('-', ''))
    print(newList)
    count = 0

    for i in range(len(newList)-1):
        print(count, end= "")
        if newList[i] == newList[i+1]:
            count += 1
        else: 
            count = 0
        if count >= 3:
            return False

    return True

def checkDash(param):
    dash = "-"
    if dash in str(param):
        param = param.split(dash)
        for i in param:
            if len(i) == 4:
                return True
            else:
                return False
    else:
        return True

inside = open("ccNasabah.json", "r")
out = json.load(inside)
print(out[0]['nama'])

validDict = {}
count = 0

for i in out:
    booleanList = []
    booleanList.append(checkFFS(i['noCreditCard']))
    booleanList.append(checkLength(i['noCreditCard']))
    booleanList.append(checkNumeric(i['noCreditCard']))
    booleanList.append(checkRepetition(i['noCreditCard']))
    booleanList.append(checkDash(i['noCreditCard']))
    booleanList.append(checkDot(i['noCreditCard']))
    print(booleanList)
    boolCount = 0

    for i in booleanList:
        if i == True:
            boolCount += 1
        if boolCount == 6:
            validDict[count] = 1
        else:
            validDict[count] = 0
    count += 1

print(validDict)

validData = []
invalidData = []

for i in range(len(validDict)):
    if validDict[i] == 1:
        validData.append({
            'nama': out[i]['nama'],
            'noCreditCard': out[i]['noCreditCard']
        })
    else:
        invalidData.append({
            'nama': out[i]['nama'],
            'noCreditCard': out[i]['noCreditCard']
        })

with open('ccValid.json', 'w') as outfile:
    json.dump(validData, outfile)

with open('ccInvalid.json', 'w') as outfile:
    json.dump(invalidData, outfile)



# ----------------------------------------------------------------------------------------
# Dimas

kata = ('kode python').replace (' ', '')
katList = list(kata)


rules = []
for a in range(len(katList)):
    X = int((a*(a+1))/2)
    rules.append (X)
print (rules)

n=0
if len(katList) not in rules:
    print ('Mohon maaf, jumlah karakter tidak memenuhi syarat membentuk pola.')
else:
    n= rules.index(len(katList))
def kiki(n):   
    num = 0
    for i in range(0, n): 
        for j in range(0, i+1): 
            print(katList[num], end=" ")  
            num = num + 1
        print("\r") 
def kuku(n):   
    num = 0
    for i in range(n, 0, -1): 
        for j in range(1, i+1): 
            print(katList[num], end=" ")  
            num = num + 1
        print("\r") 
       
kiki(n)
kuku(n)


# ----------------------------------------------------------------------------------------
import json

with open('ccNasabah.json','r') as x:
    out = json.load(x)

letter = ['a','b','c','d','e','f','g','h','i',
        'j','k','l','m','n','o','p','q','r','s','t','u',
        'v','w','x','y','z'
]
valid = []
invalid = []
for i in range(len(out)):
    nomor = out[i]['noCreditCard']
    nomor = nomor.split('-')
    nomor = ''.join(nomor)
    # print(nomor[0])
    if nomor[0]=='4' and len(nomor) == 16:
        # for j in range(len(nomor)):
        #     if nomor[j].isalpha():
        #         invalid.append(out[i])
            
        if ' ' in nomor:
            invalid.append(out[i])
        elif nomor[i].isalpha():
            invalid.append(out[i])
        elif '-' in nomor:
            invalid.append(out[i])
        elif '44444' in nomor:
            invalid.append(out[i])
        else: 
            valid.append(out[i])
    elif nomor[0] == '5' and len(nomor) == 16:
        # for j in range(len(nomor)):
        #     if nomor[j].isalpha():
        #         invalid.append(out[i])
        
        if ' ' in nomor:
            invalid.append(out[i])
        elif nomor[i].isalpha():
            invalid.append(out[i])
        elif '-' in nomor:
            invalid.append(out[i])
        elif '9999' in nomor:
            invalid.append(out[i])
        else:
            valid.append(out[i])
    elif nomor[0] == '6' and len(nomor) == 16:
        # for j in range(len(nomor)):
        #     if nomor[j].isalpha():
        #         invalid.append(out[i])
        if ' ' in nomor:
            invalid.append(out[i])
        elif nomor[i].isalpha():
            invalid.append(out[i])
        elif '-' in nomor:
            invalid.append(out[i])
        elif '61234' in nomor:
            invalid.append(out[i])
        else: 
            valid.append(out[i])
    else:
        invalid.append(out[i])

with open('ccValid.json','w') as y:
    json.dump(valid,y)
with open('ccInvalid.json','w') as yy:
    json.dump(invalid,yy)



# ----------------------------------------------------------------------------------------
# Nadya
def segitigaKata (kata):
    kata = kata.replace (' ', '')
    x = len (kata)
    y = 0
    bisa = False
    for i in range (1,round(x/2)+1):
        y = y + i
        if y == x:
            bisa = True
            index = i  
            break
    if bisa == False:
        print ('Mohon maaf, jumlah karakter tidak memenuhi syarat membentuk pola')
    elif bisa == True:
        segitiga = ''
        n = 0
        for m in range (index):
            for j in range (m+1):
                segitiga += kata[n]
                segitiga += ' '
                n +=1
            segitiga += '\n'
        n = 0
        for a in range (index):
            for j in range (a, index):
                segitiga += kata [n]
                segitiga += ' '
                n += 1 
            segitiga += '\n'
        print (segitiga)

segitigaKata('Purwadhika')
segitigaKata('Purwadhika Startup and Coding School @BSD')
segitigaKata('kode')
segitigaKata('kode python')
segitigaKata('lintang')


# ----------------------------------------------------------------------------------------
import json
valid = []
invalid = []
angka = '0123456789'
with open ('ccNasabah.json', 'r') as file_nasabah:
    load_nasabah = json.load(file_nasabah) ## bentuknya list of dict 
for i in range(len(load_nasabah)):
    isvalid = True
    x = load_nasabah[i]['noCreditCard']
    if int(x[0]) != 4 and  int(x[0]) != 5 and int(x[0]) != 6:
        isvalid=False
    nodash  = x.replace('-', '')
    if len (nodash) != 16:
        isvalid = False
    for k in nodash:
        benar = k in angka
        if not benar:
            isvalid = False
            break
    for p in range(len(nodash)-3):
        if nodash [p] == nodash [p+1] and nodash [p] == nodash [p+2] and nodash [p] == nodash [p+3]:
            isvalid = False  
    dash = '-' in x
    if dash:    
        split = x.split('-')
        for l in split:
            if len(l) != 4:
                isvalid = False
                break
    
    if isvalid == True:
        valid.append(load_nasabah[i])
    if isvalid == False:
        invalid.append(load_nasabah[i])

with open ('ccValid.json', 'w') as ccvalid:
    dump_ccvalid = json.dump(valid, ccvalid)

with open ('ccInvalid.json', 'w') as ccinvalid:
    dump_ccinvalid = json.dump(invalid, ccinvalid)
eng_upper='ABCDEFGHIJKLMNOPQRSTUVWXYZ'
eng_lower='abcdefghijklmnopqrstuvwxyz'
eng_len=len(eng_lower)

ru_upper='АБВГДЕЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ'
ru_lower=ru_upper.lower()
ru_len=len(ru_lower)

print ('Выберите тип: шифровка/расшифровка. s-шифровка, p-расшифровка')
vibor=input()
text=input()
shag=int(input())
itog=''



def shifr(text, shag, itog):
    for i in range (len(text)):
        if text[i] in eng_upper:
            itog+= eng_upper[(eng_upper.find(text[i])+shag)%26]
        elif text[i] in eng_lower:
            itog+= eng_lower[(eng_lower.find(text[i])+shag)%26]
        elif text[i] in ru_upper:
            itog+= ru_upper[(ru_upper.find(text[i])+shag)%32]
        elif text[i] in ru_lower:
            itog+= ru_lower[(ru_lower.find(text[i])+shag)%32]
        else:
            itog+=text[i]
    return itog

def deshifr(text, shag, itog):
    for i in range (len(text)):
        if text[i] in eng_upper:
            itog+= eng_upper[(eng_upper.find(text[i])-shag)%26]
        elif text[i] in eng_lower:
            itog+= eng_lower[(eng_lower.find(text[i])-shag)%26]
        elif text[i] in ru_upper:
            itog+= ru_upper[(ru_upper.find(text[i])-shag)%32]
        elif text[i] in ru_lower:
            itog+= ru_lower[(ru_lower.find(text[i])-shag)%32]
        else:
            itog+=text[i]
    return itog


if vibor=='s':
    print (shifr(text, shag, itog))
elif vibor=='p':
    print (deshifr(text, shag, itog))

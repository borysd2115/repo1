napis = input("Podaj napis: ")
dlg = len(napis)

#a)
ile_d=0
for litera in napis:
    if(litera=="d"):
        ile_d+=1
print("Ilosc d:",ile_d)

#b)
dlg_b = len(napis)
for litera in napis:
    if(litera=="a"):
        dlg_b-=1
print("Znaki rożne od a:",dlg_b)

#c)
napis_2=""
for i in range(0,dlg):
    if(napis[i]!="b" and napis[i]!="B"):
        napis_2=napis_2+"a"
    else:
        napis_2=napis_2+napis[i]
print("Znaki rozne od b i B zamienione na a:",napis_2)

#d)
napis_3=""
for i in range(0,dlg):
    if(napis[i]!="s"):
        napis_3=napis_3+napis[i]
print("Znaki rozne od s:",napis_3)

#e)
ile_z=0
for i in range(0,dlg):
    if(napis[i]!="d" and i%3==0):
       ile_z+=1
print("Ilosc znaków róznych od d, które mają numer podzielny przez 3:",ile_z)

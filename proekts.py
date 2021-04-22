from math import *
print("!!!Picas ir pieredzetas uz 45 cm diametru!!!")
print("")  
print("Mervienibas: ml un g - 1, karotes un glazes - 2")
print("Miklas: plana mikla - 1, gaisiga mikla - 2")
print("")  
print("Izveleto mervienibu un miklu atdali ar punktu") 
print("Piemers: 1.1")
print("")
mervienibamikla=float(input("Kada mervieniba un ar kadu miklu tu velies pagatavot picu - "))
print("")  
if mervienibamikla==1.1:
         print("Lai izcept planu miklu:") 
         print(" olas - 1 gabals,")
         print(" sals - 4 g,")
         print(" augu ella - 20 ml,")
         print(" udens - 60 ml,")
         print(" milti - 165 g")         
elif mervienibamikla==1.2: 
         print("Lai izcept gaisigu miklu:")      
         print(" sausais raugs - 10 g,")
         print(" cukurs - 30 g,")
         print(" sals - 3.5 g,")
         print(" augu ella - 40 ml,")
         print(" udens - 280 ml")
elif mervienibamikla==2.1: 
         print("Lai izcept planu miklu:") 
         print(" olas - 1 gabals,")
         print(" sals - 1 tejkarotes,")
         print(" augu ella - 20 ml,")  
         print(" udens - 3 edamkarotes,")
         print(" milti - 1.5 glaze")
elif mervienibamikla==2.2: 
         print("Lai izcept gaisigu miklu:")      
         print(" sausais Raugs - 2 tejkarotes,")
         print(" cukurs - 1.5 edamkarotes,")
         print(" sals - 0.5 tejkarotes,")
         print(" augu ella - 2 edamkarotes,")
         print(" udens - 1.5 glazes")
else:
         print("Sadas atbildes nav.") 
         
print("___________________________________________________________")
print(" ")

print("Mervienibas: ml un g - 1, karotes un glazes - 2")
print("Picas veidi: siera pica - 1, desu pica - 2, vistas pica - 3")
print(" ")
print("Izveleto mervienibu un miklu atdali ar punktu")
print("Piemers: 1.1")
print(" ")
pizza=float(input("Kada mervieniba un kadu picu tu velies pagatavot - "))
print(" ")
if pizza==1.1: 
         print("Lai izcept Siera picu:")
         print(" mozzarella siers - 250 g,")
         print(" parmezana siers - 100 g,")
         print(" kiploks - 10 g")
         print(" sviests - 30 g")
elif pizza==1.2: 
         print("Lai izcept Desu picu:")
         print(" siers - 100 g,")
         print(" kupinata desa - 200 g,")
         print(" tomati - 250 g")
         print(" tomatu merce - 90 g")
elif pizza==1.3: 
         print("Lai izcept Vistas picu:")
         print(" vistas fileja - 330 g,")
         print(" sipoli - 46 g,")
         print(" majoneze - 17 g,")
         print(" augu ella - 13 ml,")
         print(" siers - 133 g")
elif pizza==2.1: 
         print("Lai izcept Siera picu:")
         print(" mozzarella siers - 250 g,")
         print(" parmezana siers - 100 g,")
         print(" kiploks - 2 daivinas")
         print(" sviests - 1.5 edamkarotes")
elif pizza==2.2:
         print("Lai izcept Desu picu:")
         print(" siers - 100 g,")
         print(" kupinata desa - 200 g,")
         print(" tomati - 2,5 gabali")
         print(" tomatu merce - 4 edamkarotes")
elif pizza==2.3: 
         print("Lai izcept Vistas picu:")
         print(" vistas fileja - 330 g,")
         print(" sipoli - 0.5 gabals,")
         print(" majoneze - 1 edamkarote,")
         print(" augu ella - 1 edamkarote,")
         print(" siers - 133 g")
else:
         print("Sadas atbildes nav.")
         
print("___________________________________________________________")
print(" ")

print("Ja - 1, ne - 2")
print("Merces: kiploku - 1, saldskaba - 2, tomatu - 3, BBQ - 4 ")
print(" ")
print("Izveleto atbildi un merci atdali ar punktu")
print("Piemers: 1.1")
print(" ")
merces=float(input("Vai jus velaties izmantot merci? Ja velaties, tad kadu? - "))
print(" ")
if merces==1.1:
         print("Kiploku merces cena ir 2 eiro")
elif merces==1.2:
         print("Saldskaba merces cena ir 1 eiro")
elif merces==1.3:
         print("Tomatu merces cena ir 1 eiro")
elif merces==1.4:
         print("BBQ merces cena ir 3 eiro")
elif merces==2:
         print("Bez merzes ari ir garsigi:)")
else: 
         print("Sadas atbildes nav.")
         
print("___________________________________________________________")
print(" ")

cilveki=float(input("Cik cilveku edis picu? - "))
skaits=cilveki/4
print("Uz", "%.0f"%cilveki, "cilvekiem ir paredzetas", "%.0f"%(ceil(skaits)) ,"picas")

print("___________________________________________________________")
print(" ")

print("Miklas: plana mikla - 1, gaisiga mikla - 2")
miklucena=int(input("Kadas picas miklu cenu tu gribi uzzinat? - "))
print(" ")
if miklucena==1:
         def plana_mikla_cena(olas,sals,ella,udens,milti):
                  return olas+sals+ella+udens+milti
         olas=1.50
         sals=1.65
         ella=2.00
         udens=0.50
         milti=1.00
         cena=plana_mikla_cena(olas,sals,ella,udens,milti)
         print("Viena olu paka maksa 1.50 eiro")
         print("Viens kilograms sals paka maksa 1.65 eiro")
         print("Viens litrs augu ellas iepakojums maksa 2.00 eiro")
         print("Viena 0.5l udens pudele maksa 0.50 eiro ")
         print("Viens kilograms miltu pakas maksa 1.00 eiro")
         print("")
         print("Planu mikla cena ir", "%.2f"%cena , "eiro")
elif miklucena==2:
         def gaisiga_mikla_cena(raugs,cukurs,sals,ella,udens):
                  return raugs+cukurs+sals+ella+udens
         raugs=0.23
         cukurs=0.70
         sals=1.65
         ella=2.00
         udens=0.50
         cena=gaisiga_mikla_cena(raugs,cukurs,sals,ella,udens)
         print("Viena 14 g sausu rauga paka maksa 0.23 eiro")
         print("Viens kilograms cukura paka maksa 0.70 eiro")
         print("Viens kilograms sals paka maksa 1.65 eiro")
         print("Viens litrs augu ellas iepakojums maksa 2.00 eiro")
         print("Viena 0.5l udens pudele maksa 0.50 eiro ")
         print("")
         print("Gaisiga mikla cena ir", "%.2f"%cena , "eiro")
else:
         print("Sadas atbildes nav.")
         
print("___________________________________________________________")
print(" ")

print("Picas veidi: siera pica - 1, desu pica - 2, vistas pica - 3")
picascena=int(input("Kadas picas cenu tu gribi uzzinat? - "))
print("")
if picascena==1:
         def sieras_picas_cena(mozzarella,parmezans,kiploks,sviests):
                  return mozzarella+parmezans+kiploks+sviests
         mozzarella=2.00
         parmezans=2.00
         kiploks=0.05
         sviests=1.50
         cena=sieras_picas_cena(mozzarella,parmezans,kiploks,sviests)
         print("Divas 125 g mozzarella paka maksa 2.00 eiro")
         print("Viena parmezana paka maksa 2.00 eiro")
         print("Viens kiploks maksa 0.05 eiro")
         print("Viena 250 g sviesta paka maksa 1.50 eiro")
         print("")
         print("Sieras picas cena ir", "%.2f"%cena , "eiro")
elif picascena==2:
         def desas_picas_cena(siers,desa,tomati,merce):
                  return siers+desa+tomati+merce
         siers=1.50
         desa=2.00
         tomati=0.40
         merce=1.00
         cena=desas_picas_cena(siers,desa,tomati,merce)
         print("Viena 250 g siera paka maksa 1.50 eiro")
         print("200 g kupinetas desas maksa 2.00 eiro")
         print("250 g tomatu maksa 0.40 eiro")
         print("500 g tomatu merce maksa 1.00 eiro")
         print("")
         print("Desas picas cena ir", "%.2f"%cena , "eiro")
elif picascena==3:
         def vistas_picas_cena(vista,sipoli,majoneze,ella,siers):
                  return vista+sipoli+majoneze+ella+siers
         vista=2.00
         sipoli=0.23
         majoneze=0.60
         ella=2.00
         siers=1.50
         cena=vistas_picas_cena(vista,sipoli,majoneze,ella,siers)
         print("Viens vistas filejas iepakojums maksa 2.00 eiro")
         print("Viens 26 g sipols maksa 0.23 eiro")
         print("Viena 250 g majonezes paka maksa 0.60 eiro")
         print("Viena litrs augu ellas iepakojums maksa 2.00 eiro")
         print("Viena 133g siera gabals maksa 1.50 eiro")
         print("")
         print("Vistas picas cena ir", "%.2f"%cena , "eiro")
else: 
         print("Sadas atbildes nav.")
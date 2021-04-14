from math import *
print("")  
print("Mervienibas: ml un g - 1, karotes un glazes - 2")
print("Miklas: plana mikla - 1, gaisiga mikla - 2")
print("")  
print("Izveleto mervienibu un miklu atdali ar punktu") 
print("Piemers: 1.1")
print("")  
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
         print(" sausais Raugs - 10 g,")
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
else:  
         print("Lai izcept gaisigu miklu:")      
         print(" sausais Raugs - 2 tejkarotes,")
         print(" cukurs - 1.5 edamkarotes,")
         print(" sals - 0.5 tejkarotes,")
         print(" augu ella - 2 edamkarotes,")
         print(" udens - 1.5 glazes")
print(" ")
print(" ")
print("Mervienibas: ml un g - 1, karotes un glazes - 2")
print("Picas veidi: siera pica - 1, desu pica - 2, vistas pica - 3")
print(" ")
print("Izveleto mervienibu un miklu atdali ar punktu")
print("Piemers: 1.1")
print(" ")
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
else: 
         print("Lai izcept Vistas picu:")
         print(" vistas fileja - 330 g,")
         print(" sipoli - 0.5 gabals,")
         print(" majoneze - 1 edamkarote,")
         print(" augu ella - 1 edamkarote,")
         print(" siers - 133 g")
print(" ")
print(" ")
cilveki=float(input("Cik cilveku edis picu? - "))
skaits=cilveki/4
print("Uz", "%.0f"%cilveki, "cilvekiem ir paredzetas", "%.0f"%(ceil(skaits)) ,"picas")
print(" ")
print(" ")

print("Miklas: plana mikla - 1, gaisiga mikla - 2")
miklucena=float(input("Kadas picas miklu cenu tu gribi uzzzinat? - "))
print("")
def plana_mikla_cena(olas,sals,ella,udens,milti):
         return olas+sals+ella+udens+milti
olas=1.50
sals=1.65
ella=2.00
udens=0.50
milti=1.00
cena=plana_mikla_cena(olas,sals,ella,udens,milti)
if miklucena==1:
         print("Viena olu paka maksa 1.50 eiro")
         print("Viens kilograms sals paka maksa 1.65 eiro")
         print("Viens litrs augu ellas iepakojums maksa 2.00 eiro")
         print("Viena 0.5l udens pudele maksa 0.50 eiro ")
         print("Viens kilograms miltu pakas maksa 1.00 eiro")
         print("Planu mikla cena ir", "%.2f"%cena , "eiro")
         
def gaisiga_mikla_cena(olas,sals,ella):
         return olas+sals+ella
olas=1.50
sals=1.65
ella=2.00

         

#https://courses.cs.ut.ee/2023/programmeerimine/fall/Main/Praks13 Ülesanne 1

#alampunkt 1, loo klass jne

class Isik:
    def __init__(self, nimi, vanus, pikkus, kaal):
        self.nimi   = nimi
        self.vanus  = vanus
        self.pikkus = pikkus
        self.kaal   = kaal

#teen funkstiooni kmi, jagan pikkuse sajaga, sest pikkust peba selle arvutamsieks olema meetrites, mitte sentimeetrites
    def kmi(self):
        return(round((self.kaal)/((self.pikkus/100)**2), 1 ))
    

#Punkt 2, võrdle kahe isiku kaalu/pikkust

# isik1 = Isik('Anne',   21, 1.87, 60)
# isik2 = Isik('Peeter', 32, 1.99, 80)

# print(isik2.nimi + (' On raskem 'if isik2.kaal>isik1.kaal else 'On kergem ') + 'kui '  + isik1.nimi)
# print(isik2.nimi +' '+  ('On pikem 'if isik2.pikkus>isik1.pikkus else 'On lühem ') + 'kui '  + isik1.nimi)
    
##Punkt 3, võta failist tervisekontroll andmed ning tagasta nende BMI
    
fail = open('Documents/tervisekontroll.txt', 'r')
for line in fail:
    #võtan iga rea lõpus ära newline characteri
    line = line.strip('\n')
    #splitin saadud rea komade kohtade pealt listiks
    rida = line.split(',')
    #võtan listielemndid ning sisesstan need Isiku objekti
    inimene = Isik(rida[0], int(rida[1]), float(rida[2]), float(rida[3]))
    bmi = inimene.kmi()
    #annan vastava väärtuse, mis sobib nende kehakaalga, kas on tervisliku või mitte
    if 19 < bmi < 25:
        print(inimene.nimi + ', ' + str(inimene.vanus) +', sinu bmi on ' + str(bmi) + ', oled normaalkaalus')
    elif bmi > 25:
        print(inimene.nimi + ', ' + str(inimene.vanus)  +', sinu bmi on ' + str(bmi) +  ', oled paks')
    else: 
         print(inimene.nimi + ', ' + str(inimene.vanus) +', sinu bmi on ' +  str(bmi) +  ', oled kõhn')
fail.close()

from module1 import*
print("Regestreerimne ja Autoriseerimine".center(50,"+"))
users=["Andrei"]
pswords=["12345"]
while True:
    sign=input("Regestreerimne- R, Autoriseerimine- A, Välja- E")
    if sign.upper()=="R":
        log=input("Login: ")
        pswrd1=input("sulle valida automaatne parooli? Y- jah, N- ei")
        if pswrd1.upper()=="Y":
            psword=autopsword()
            print("sinu parool: "+psword)
            pswords.append(psword) #dobovlayem k spisku
            if log not in users:
                users.append(log)
        elif pswrd1.upper()=="N":
            psword=""
            while len(psword)!=12:
               try:
                   psword=input("Siseta parool 12 sümboolid suurus: ")
               except:
                    ValueError
            if ans != True:
                print ("Parool ei sobi")
            else:
                print("Regestreerimne on edukas")
                users.append(log)
                pswords.append(psword)

    elif sign.upper()=="A":
        login=input("Siseta login: ")
        if login not in users:
            print("Kasutaja ei ole olema")
            print("Kas sa tahad regestreerida?")
            reg=input("Y= jah, N= ei")
            if reg.upper() =="Y":
                log=input("Login: ")
                pswrd1=input("sulle valida automaatne parooli? Y- jah, N- ei")
                if pswrd1.upper()=="Y":
                    psword=autopsword()
                    print("sinu parool: "+psword)
                    pswords.append(psword) 
                    if log not in users:
                        users.append(log)
                elif pswrd1.upper()=="N":
                    psword=""
                    while len(psword)!=12:
                       try:
                           psword=input("Siseta parool 12 sümboolid suurus: ")
                       except:
                            ValueError
                    ans=psword_check(psword) 
                    if ans != True:
                        print ("Parool ei sobi")
                    else:
                        print("Regestreerimne on edukas")
                        users.append(log)
                        pswords.append(psword)
            else:
                pass
        else:
            psword=input("Siseta parool: ")
            if psword not in pswords:
                print("Vale parool")
            else:
                print("Autoriseerimine on edukas")
    elif sign.upper()=="E":
        break
    else:
        print("See funktsioon ei ole")

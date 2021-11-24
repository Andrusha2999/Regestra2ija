from module1 import*
users=["Andrei"]
passwords=["12345"]
password=passauto()
print(password)
while True:
    print("Regestreerimine - 1, Autriseerimine - 2, Välja - 3")
    v=int(input())
    if v==1:
        login=input("Sisestage nimi: ")
        pswrd=input("Sisestage salasõnu: ")
        while len(pswrd)>12:
            try:
                pswrd=input("Sisesta salasõna: ")
            except:
                ValueError
        t=passcontrol(pswrd)
        if t!=True:
            print("Salasõna ei sobib.") 
        else:
            print("Salasõna sobib, regestreerimine lõpub.")
            users.append(login)
            passwords.append(pswrd)
    elif v==2:
        login=input("Sisesta nimi: ")
        if login in users:
            pswrd=input("Sisestage salasõna: ")
            if pswrd not in passwords:
                print("Vale salasõna")
            else:
                print("Autoriseerimine lõpub")
        else:
            print("Viga! Soovite registreeruda?")
            reg=input("1 - Jah, 2 - Ei.")
            if reg=="1":
               login=input("Sisestage nimi: ")
        pswrd=input("Sisestage salasõnu: ")
        while len(pswrd)>12:
            try:
                pswrd=input("Sisesta salasõna: ")
            except:
                ValueError
        t=passcontrol(pswrd)
        if t!=True:
            print("Salasõna ei sobib.") 
        else:
            print("Salasõna sobib, regestreerimine lõpub.")
            users.append(login)
            passwords.append(pswrd)
            break
    elif v==3:
        print("Head aega!")
        break
    else:
        print("On vaja valida 1,2 või 3.")

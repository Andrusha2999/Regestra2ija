def autopsword()->str:
    """automaatseltloomatud parool
    """
    str0=".,:;!_*-+()/#¤%&"
    str1 = "0123456789"
    str2 = "qwertyuiopasdfghjklzxcvbnm"
    str3 = str2.upper()
    #print(str3) # 'QWERTYUIOPASDFGHJKLZXCVBNM'
    str4 = str0+str1+str2+str3 
    ls = list(str4) 
    shuffle(ls) 
    psword = "".join([choice(ls) for x in range(12)]) # Извлекаем из списка 12 произвольных значений
    # 
    return psword
def pswordcheck(psword:str)->bool:
    digit="d"
    alpha="a"
    upper="e"
    lower="f"
    symbl="w"
    psword=list(psword)
    for i in psword:
        if i.isdigit()== True: #string index out of range
            digit="True"
        if i.isalpha()== True:
            alpha="True"
        if i.isupper()== True:
            upper="True"
        if i.islower()==True:
            lower="True"
        if i in [".","_","/","@"]:
            symbl="True"
    if digit=="True" and upper=="True" and alpha=="True" and lower=="True" and symbl=="True": 
        ans=True
    else:
        ans=False
    return ans

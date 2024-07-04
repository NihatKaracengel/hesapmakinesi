operatorler = ["+","-","*","/","çıkış"]

tekrar = False

def hesapmakinesi(sayi1 ,sayi2, operator):
    if operator not in operatorler:
        return("Hatalı Operatör Seçimi")
    if operator == "+":
        return(sayi1 + sayi2)
    elif operator == "-":
        return(sayi1 - sayi2)
    elif operator == "*":
        return(sayi1 * sayi2)
    elif operator == "/":
        return(sayi1 / sayi2)
    elif operator == "çıkış".lower():
        global tekrar
        tekrar = True
        return("Çıkış yaptınız.")
    else:
        print("Hatalı işlem")

while not tekrar:
    sayi1 = int(input("1. sayıyı gir: "))
    sayi2 = int(input("2. sayıyı gir: "))
    operator = input("İşlemi seçin: + - * / ").lower()
    print(hesapmakinesi(sayi1,sayi2,operator))





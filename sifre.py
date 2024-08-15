import random

karakterler = "+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"
sayi = int(input("şifreniz kaç karakterden oluşsun istersiniz?"))

password = ""
for i in range(sayi):
    password += random.choice(karakterler)
print("şifreniz =",password)

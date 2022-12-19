toplam=0
derssaati=3
hafta=14
toplam=derssaati*hafta
print(toplam)
x=10
print("x'in değeri...:\n"+str(x))
y=6
print("y'nin değeri:\n"+str(y))
strvar="Python"
print(strvar)
print(strvar[-6])
print(strvar)
print(strvar[:3])
print(strvar[-6:-3])
print(strvar[::3])
print(strvar[2::3])
print(strvar[::-1])
print(strvar.upper())
print(strvar.lower())
ceo_mu= True
kıvırcık_mı, sarışın_mı=True, True
güzel_mi=sarışın_mı and kıvırcık_mı
print(güzel_mi)
if güzel_mi:
    print("well done" )
else:
    print("olsun")
print(type(güzel_mi))
elma=9
muz=True
çilek=False
meyveler=['elma',elma,muz,çilek,1,5]
print(meyveler)
print(meyveler[3])
print(meyveler[:3])
(meyveler.append(7))
print(meyveler)
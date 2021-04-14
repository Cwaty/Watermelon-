
numara = 7
sherwoodcrypto = 1

if numara < 0:
   print("0 dan küçük bir sayı kullanamazsın , Geçerli bir sayı gir ve tekrardan dene! \n\n Örnek : 1-2-3-4-5-6-7-8")
if numara == 0:
   print("Seçmeye çalıştıştığınız sayı 0 olamaz.")
else:
   for i in range(1,numara + 1):
       sherwoodcrypto = sherwoodcrypto*i
   print("faktöriyeli numaran",numara,"-",sherwoodcrypto)

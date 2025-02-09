
notes = int(input("enter n.o of notes"))

n100 = notes//100
n50 = (notes%100)//50
n10 = (notes%100%50)//10

print ("notes of 100 :" , n100)
print ("notes of 50 :" , n50)
print ("notes of 10 :" , n10)
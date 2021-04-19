#Question 1
#Ek program likhiye jisse ki niche di hui dictionaries ek hi dictionary me aa 
# jaaye jaise ki niche Expected result me diya gaya hain or jisski bhi keys same hai 
# unki values add ho jai.


dic1={1:10,2:20}
dic2={3:30,2:40}
dic3={5:50,6:60}
dic4={}

dic1.update(dic2)
dic1.update(dic3)
print(dic1)

for d in (dic1,dic2,dic3):
    dic4.update(d)

print(dic4)
#Nested Dictionary:-
Dic= {
 1: 'NAVGURUKUL',
 2: 'IN',  
 3:{
     'A' : 'WELCOME',
     'B' : 'To', 
     'C' : 'DHARAMSALA'
     }
}
print(Dic) 
#Output :- {1: 'NAVGURUKUL', 2: 'IN', 3: {'A': 'WELCOME', 'B': 'To', 'C': 'DHARAMSALA'}}
for x in Dic:
    print(Dic[x])

for a in Dic:
    for x in Dic[3[A]]:
        print(Dic[x])

dic={
    1:"Navgurukul",
    2:"banglore",
    3:"campus",
    4:{
        "i":"Navgurukul",
        "ii":"Banglore",
        "iii":"Campus",
        "iv":{
            "I":"navgurukul",
            "II":"banglore",
            "III":"campus"
        }
    }
}

print(dic)

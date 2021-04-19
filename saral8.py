#Removing Elements from a Dictionary:-
#Hum dictionary ke elements ko kahin tareeko se remove kar sakte hain.
#  Jaisa ki niche dikhaya gaya hain. Hum pop( ) method ka use karke specified 
# element ko remove kar sakte hain :

 
CAR_DETAILS={
    "brand": "Ford",
    "model": "jason",
    "year": 1964
}
CAR_DETAILS.pop("model")
print(CAR_DETAILS) 
#Output:-  {'brand': 'Ford', 'year': 1964} The popitem() method removes the last inserted item:

dic={
    1:'Reena',
    2:'Amrita',
    3:'Sana',
    4:'shanti',
    5:'anzum'
}
dic.pop(2)
print(dic)
dic.popitem()
print(dic)
del dic(1)
print(dic) 

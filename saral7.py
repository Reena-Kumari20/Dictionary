#Updating Dictionary :-
#Hum dictionary ko update karne ke liye usme ek entry kar sakte hai ya fir
#  key-value pair add kar sakte hai aur jo key pehle se present hai uski value 
# change kar sakte hai. Jaisa ki niche example me dikhaya gaya hain. Example 1:-
person= {'1': 'RAM', '2': 17,}
person[3] = 'male'
print(person) 
#Output:-  {'1': 'RAM', '2': 17,'3':'male'} Example 2-

details={
    'Name': 'RAM',
     'Age': 17, 
     'student': {
      'id': 22,
      'place': 'dharamsala'
      }
     } 
details['student']['id']=35
print(details);  
#Output:- {'Name': 'RAM', 'Age': 17, 'student': {'id': 35, 'place': 'dharamsala'}}

dic={'name1':'Reena','name2':'sana','name3':'shanti'}
dic['name4']='Deepti'
print(dic)

dic1={
    101:"notebook",
    102:'pen',
    103:'pencil',
    104:{
        1:"colour",
        2:'marker',
        3:'whilte board'
    }
}
dic1[104][4]='black board'
print(dic1)

#Copy of Dictionary :-
#Hum dictionary ko 2 tarike se copy kar sakte hai,phela method copy() and
#  second method by using built-in function dict(). Example 1 :-

classes ={
    "room1":  "6th",
    "room2":  "7th",
    "room3":  "8th"
        }
mydict=classes.copy()
print(mydict) 
#Ouput:- {'room2': '7th', 'room3': '8th', 'room1': '6th'}

dic2={
    'a':"reena",
    'b':"amrita",
    'c':'sana'
}

dic3=dic2.copy()
print(dic3)
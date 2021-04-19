#Keys Case Sensitive :-
#Dictionary ki keys case sensitive hoti hain , matlab hum same name ki keys 
# ko alag alag case me likh sakte hai aur python usko alag alag keys ki tarah treat 
# karega. Example:-
"""Dict = {
       'ball' : 'green',
       'Ball': 'red'
     }
print(Dict['ball'])
print(Dict['Ball'])
print(Dict['bat']) 
Dict me “ball” ek key hai aur “green” uski value hai. Isi tarah “Ball” dusri key hai 
aur “red” uski value hain."""

dic={
    "ball":"green",
    "ball":"red",
    }
print(dic["ball"])
print(dic)
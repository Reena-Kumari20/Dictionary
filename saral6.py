#Adding Elements to a Dictionary:-
#Python dictionary me hum ek baar me ek hi key-value add kar sakte hai aur add karne ke liye humein key ko square brackets “[ ]” me likhte hain aur uski value ko “=” operator ka use karke assign kar dete hain. Example 1:-

 
dic= {
    'Name': 'RAM', 
    'Age': 17,
    }

dic['ORGANIZATION'] = "NAV GURUKUL"

dic['place'] = 'dharamsala'
dic['name1']="Reena"
dic['name2']="amrita"
dic['name3']={
    101:"sana",
    102:"anzum",
    103:"shanti",
    104:"ujala"
}
print(dic) 

#Key Exists or not
#Dictionary mai key exists karti hai ya nahi check karne ke liye hum in keyword ka use karte hai.

"""car ={
    "brand":  "ford",
    "model":  "mustang",
    "year":  1964
}
if "model" in car:
    print("Yes, 'model' is one of the keys in the car dictionary.")

else:
    print("No, 'model' key dictionary mai nahi hai.") 
Output :-  Yes, 'model' is one of the keys in the thisdict dictionary."""

dic={
    "name1":"Reena",
    "name2":"amrita",
    "name3":"sana",
    "name4":"priyanka"
}
if "name1" in dic:
    print("yes,this key in dictionary")
else:
    print()
#Question 2
#Ek program likhiye jisse ki agar di hui key pehle se dictionary me exist karti ho 
#toh “exists “ print kare aur agar nahi karti ho toh “not exists” print kare. Example :-

user=int(input("enter the key: "))

dic={
    101:'Reena',
    102:'Sana',
    103:'Amrita',
    104:'Shanti'
}
if user in dic:
    print('exists')
else:
    print('not exists')

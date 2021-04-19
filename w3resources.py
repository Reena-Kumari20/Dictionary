#1. Write a Python script to sort (ascending and descending) a dictionary by value.
"""d={
    1:2,4:2,6:3,2:5
}
#a=d.sort()
print(d)

#2. Write a Python script to add a key to a dictionary
#Sample Dictionary : {0: 10, 1: 20}
#Expected Result : {0: 10, 1: 20, 2: 30}

dic={
    0:10,
    1:20,
}
dic[2]=30
print(dic)
dic.update({3:40})
print(dic)"""


#3. Write a Python script to concatenate following dictionaries to create a new one. Go to the editor

"""Sample Dictionary :
dic1={1:10, 2:20}
dic2={3:30, 4:40}
dic3={5:50,6:60}
Expected Result : {1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}"""

dic1={1:10,2:20}
dic2={3:30,4:40}
dic3={5:50,6:60}
dic1.update(dic2)
dic1.update(dic3)
print(dic1)

#dic4={}
#dic5={
#     "dic1":dic1,
#     "dic2":dic2,
#     "dic3":dic3
# }
# for d in (dic1,dic2,dic3):
#     dic4.update(d)
# print(dic4)
# print(dic5)


stu={101:"Reena",102:"Sana",103:"Amrita",104:"Shanti",105:"Sweta"}
print(stu[101])
print(stu[102])
print(stu[103])
print(stu[104])
print(stu[105])
 
# length of dictionary(len(dictionary_name))
print(len(stu))

#Dictionaries are written with curly brackets, and have keys and values:

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(thisdict)

#Dictionary Items
#Dictionary items are ordered, changeable, and does not allow duplicates.
#Dictionary items are presented in key:value pairs, and can be referred to by using the key name.
#Example
#Print the "brand" value of the dictionary:

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(thisdict["brand"])

#Duplicates Not Allowed
#Dictionaries cannot have two items with the same key:

#Example
#Duplicate values will overwrite existing values:

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964,
  "year": 2020
}
print(thisdict)
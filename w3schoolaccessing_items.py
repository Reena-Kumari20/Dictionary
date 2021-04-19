#creating a dictionary

thisdict={
  "brand":"ford",
  "model":"mustang",
  "year":1964
}

print(thisdict["brand"])
print(thisdict.get("brand"))

#dictionary_length
#to determine how many items a dictinary has,use the len()function.
print(len(thisdict))

#dictionary items-data types

thisdict={
  "brand":"ford",
  "electric":False,
  "year":1964,
  "colors":["red","while","blue"]
}

print(type(thisdict))

#accessing items

d={
  "brand":"ford",
  "model":"mustang",
  "year":1964
}
x=d["model"]
print(x)
a=d.get("model")
print(a)

print(d["model"])
print(d.get("model"))

#get keys
print(d.keys())
print(d.values())

#add a new items
car={
  "brand":"ford",
  "model":"mustang",
  "year":1964
}
car["color"]="write"
print(car)

#get values

print(car.values())

print(car.items())

if "model" in car:
  print("Yes,'model' is one of the keys in the car dictionary")


#Iterate through all keys:-
 
states_capitals = {
  'Gujarat' : 'Gandhinagar',
  'Maharashtra' : 'Mumbai',
  'Rajasthan' : 'Jaipur',
  'Bihar' : 'Patna'
  }
#for state in states_capitals:
#    print(state) 

#for state in states_capitals:
#    print(state,states_capitals[state])

for state in states_capitals.keys():
    print(state)

for state in states_capitals.values():
    print(state)

for x,y in states_capitals.items():
    print(x,y)

print(len(states_capitals))


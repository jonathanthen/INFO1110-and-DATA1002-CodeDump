name = 'Iris' 
age = 23 
message = 'Hi ' + name + ', you are ' + str(age) + ' years old.' 
print(message)

##comparing the two different ways

message = 'Hi {}, you are {} years old.'.format(name, age)
print(message)
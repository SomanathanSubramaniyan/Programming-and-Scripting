#Somu 13-Feb-2018
#Convert your name into Hexadecimal Value

Name = input("Name:  ")
value = "Ox  :"
Binary = "Ob  :"
i = 0
while  i < len(Name):
    position = Name[i]
    string = (str(hex(ord(position))))[2:]
    value = value + " " + string
    Binary = Binary + " " + str((bin(ord(position))))[2:]
    i = i+1

print (value)
print (Binary)

print (hex(1903))

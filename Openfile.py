# somu  26 Feb 2018

# f = open("data/iris.csv")
# print (f)
# print(f.read())
# f.close()

with open("data/iris.csv") as f:
    for line in f:
        print(line.split(',')[4], end='')
    #contents = f.read()
    #print(contents)
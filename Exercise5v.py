#somu 27 Feb 2018
#References : https://en.wikipedia.org/wiki/Iris_flower_data_set
#Data  http://archive.ics.uci.edu/ml/machine-learning-databases/iris/
#   Open Iris data set petal length, petal width, sepal length and sepal width, 
#   and these values should have the decimal places aligned, with a space between the column


# Read first line from the data file 
# Read the petal/Sepal length and width 

counter1, counter2,counter3 = 1,1,1
Gplen,Gpwid,Gslen,Gswid = 0.0,0.0, 0.0,0.0
Gname,Gnamei,Gnameo = '','',''

# Function to print the name, petel length, petal width, Sepal length and sepal width
def printiris(line):
        Gplen = float(str(line.split(',')[0]))
        Gpwid = float(str(line.split(',')[1]))
        Gslen = float(str(line.split(',')[2]))
        Gswid = float(str(line.split(',')[3]))
        print ("{:04.2f}  {:04.2f}  {:04.2f}  {:04.2f}".format (Gplen,Gpwid,Gslen,Gswid))

# Store all the distinct flower names 
flowers = set()
with open("data/iris.csv") as f:
        for line in f:
            Gname   = str(line.split(',')[4]).rstrip()
            flowers.add(Gname)

#Read the file and print the petel /Sepal details for each flower 
with open("data/iris.csv") as f:
        for line in f:
            Gnameo   = str(line.split(',')[4]).rstrip()
            if Gnameo == 'Iris-virginica':
                if counter1 == 1: 
                    print ("{:^20}".format(Gnameo))
                    printiris(line)
                    counter1 += 1
                else:
                   printiris(line)
            if Gnameo == 'Iris-versicolor':
                if counter2 == 1: 
                    print ("{:^20}".format(Gnameo))
                    printiris(line)
                    counter2 += 1
                else:
                   printiris(line)
            if Gnameo == 'Iris-setosa':
                if counter3 == 1: 
                    print ("{:^20}".format(Gnameo))
                    printiris(line)
                    counter3 += 1
                else:
                   printiris(line)                    

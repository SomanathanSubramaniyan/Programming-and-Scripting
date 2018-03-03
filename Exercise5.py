#somu 27 Feb 2018
#References : https://en.wikipedia.org/wiki/Iris_flower_data_set
#Data  http://archive.ics.uci.edu/ml/machine-learning-databases/iris/
#   Open Iris data set petal length, petal width, sepal length and sepal width, 
#   and these values should have the decimal places aligned, with a space between the column


# Read first line from the data file 
# Read the petal/Sepal length and width 

counter = 1
Gplen,Gpwid,Gslen,Gswid = '','', '', ''
Gname,Gnamei,Gnameo = '','',''

# Function to print the name, petel length, petal width, Sepal length and sepal width
def printiris(name,plen,pwid,slen,swid):
    print ('\n',name) 
    print ("{0:12} ==> {1:2}".format("Petal Length", (plen) ))
    print ("{0:12} ==> {1:2}".format("Petal Width",  (pwid) ))
    print ("{0:12} ==> {1:2}".format("Sepal Length", (slen) ))
    print ("{0:12} ==> {1:2}".format("Sepal Width",  (swid) ))

flowers = set()
with open("data/iris.csv") as f:
        for line in f:
            Gname   = str(line.split(',')[4]).rstrip()
            flowers.add(Gname)
print (flowers)

with open("data/iris.csv") as f:
        for line in f:
            Gnameo   = str(line.split(',')[4])
            if Gnameo == 'Iris-virginica':
            Gplen = Gplen + " " + str(line.split(',')[0])
            Gpwid = Gpwid + " " + str(line.split(',')[1])
            Gslen = Gslen + " " + str(line.split(',')[2])
            Gswid = Gswid + " " + str(line.split(',')[3])
            #   printiris(Gnameo,Gplen,Gpwid,Gslen,Gswid)
            #  Gplen,Gpwid,Gslen,Gswid = '','', '', ''
            Gnamei   = str(line.split(',')[4])
            counter += 1
                    


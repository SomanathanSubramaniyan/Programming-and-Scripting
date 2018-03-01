#somu 27 Feb 2018
#References : https://en.wikipedia.org/wiki/Iris_flower_data_set
#Data  http://archive.ics.uci.edu/ml/machine-learning-databases/iris/
#   Open Iris data set petal length, petal width, sepal length and sepal width, 
#   and these values should have the decimal places aligned, with a space between the column


# Read first line from the data file 
# Read the petal/Sepal length and width 
counter = 1
Petal_length = 1.0
Petal_width = 1.0
Sepal_length = 1.0
Sepal_width = 1.0

with open("data/iris.csv") as f:
        for line in f:
            if counter == 2:
                break
            else:
                Petal_length = line.split(',')[0]
                Petal_width  = line.split(',')[1]
                Sepal_length = line.split(',')[2]
                Sepal_width  = line.split(',')[3]
                Flowername   = line.split(',')[4]
               
                counter += 1

print ("{0:15} ==> {1:10f}".format("Petal Length", float(Petal_length) ))
print ("{0:15} ==> {1:10f}".format("Petal Width", float(Petal_width) ))
print ("{0:15} ==> {1:10f}".format("Sepal Length", float(Sepal_length) ))
print ("{0:15} ==> {1:10f}".format("Sepal Width", float(Sepal_width) ))


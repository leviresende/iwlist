import statistics
# import numpy as np
# import matplotlib.pyplot as plt
# from sklearn.linear_model import LinearRegression
# from sklearn.preprocessing import PolynomialFeatures
import numpy as np
from numpy.polynomial.polynomial import polyfit
import matplotlib.pyplot as plt


# sequence of distance read in processing in string and float
distance = ["1m", "5m", "10m", "20m", "30m"]
distanceFloat = [1.0, 5.0, 10.0, 20.0, 30.0]

# list to receive each read
read = []

# matrix to storage all the reads
matrix = []

# iterating in the directory 
for dist in distance:
    
    # update file to catch the reads
    file = "./results2/" + dist + ".txt"
    
    # get the values and convert them to float
    with open(file) as f:
        for line in f: 
            line = float(line.strip()) 
            read.append(line) 
    
    # storage the read in the matrix
    matrix.append(read)

    # reset the list of reads
    read = []


# get the size of the matrix to iterate there
length = len(matrix)

# list to receive the median
values = []

# iterating in the matrix to get the median of each read
for i in range(length):
    values.append(statistics.median(matrix[i]))

print(values)

# # preparing data for linear regression
# x = np.array(distanceFloat).reshape((-1,1))
# y = np.array(values)

# x_ = PolynomialFeatures(degree=2, include_bias=False).fit_transform(x)

# model = LinearRegression().fit(x_, y)

# r_sq = model.score(x_, y)
# print('coefficient of determination:', r_sq)
# print('intercept:', model.intercept_)
# print('slope:', model.coef_)

# plt.figure(1)
# plt.plot(x_,y, 'o')
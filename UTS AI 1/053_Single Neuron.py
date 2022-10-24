
#insialisasi numpy
import numpy as np

#inisialisasi variable
inputs = [3, 5, 4, 4.5, 2, 6, 3.5, 8, 9, 1]

#inisialisasi bobot variable
weights = [-3.4, 1.4, 0.8, 2.9, 2.4, -1.6, 0.6, 2.2, 5.6, 1.5]

#inisialisasi bias
bias = 7

#penghitungan output = (input*weight)+bias
output = np.dot(weights, inputs) + bias

#cetak ouput
print(output)
#inisialisasi numpy
import numpy as np

#inisialisasi variable
inputs = [3, 5, 4, 4.5, 2, 6, 3.5, 8, 9, 1]

#inisialisasi bobot variable 
weights =   [[-3.4, 1.4, 0.8, 2.9, 2.4, -1.6, 0.6, 2.2, 5.6, 1.5],
            [1.5, 3.2, 4.5, 7.8, -2.3, 6.7, 8.3, 9.7, -1.2, 4.5],
            [7.1, -0.3, 6.5, 0.8, 1.3, 6.2, 6.7, 9.8, 4.6, -5.4],
            [1.5, -3.2, 4.2, 5.1, 6.4, -7.5, 0.2, 8.6, 9.4, 6.7],
            [3.5, 5.6, -0.7, 8.5, -1.2, 4.6, 8.9, 5.3, 2.9, 0.3]]

#inisialisasi bias
bias = [8, 4, 1.7, -2.4, 3.5]

#penghitungan output = (input*weight)+bias
output = np.dot(weights, inputs)+bias

#cetak output
print(output)


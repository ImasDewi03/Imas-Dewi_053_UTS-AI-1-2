#instalasi numpy
import numpy as np

#inisialisasi variable
inputs = [[1.2, 2.3, 3.4, 5.6, 7.8, 8.9, 1.4, 2.9, 3.7, 4.9],
        [0.5, 0.7, 1.3, 2.5, 3.6, 4.6, 1.5, 3.9, 6.9, 5.7],
        [0.3, 8.5, 7.6, 9.8, 4.5, 5.8, 4.7, 0.9, 8.8, 7.7],
        [1.1, 3.2, 4.1, 5.1, 6.2, 7.2, 5.9, 9.1, 4.3, 6.5],
        [3.3, 4.4, 5.3, 1.7, 0.3, 0.6, 7.3, 8.2, 6.2, 3.1],
        [4.8, 0.5, 0.4, 0.8, 0.1, 0.2, 6.3, 6.9, 7.9, 5.8]]

#panjang weights
weights1 = [[1.2, 2.3, 3.4, 4.5, 5.6, 6.7, 9.5, 7.6, 9.1, 8.2],
            [7.8, 8.9, 9.1, 2.4, 2.5, 3.5, 3.3, 1.7, 2.5, 6.5],
            [5.3, 5.2, 4.2, 1.9, 9.8, 8.7, 1.4, 2.1, 5.6, 7.7],
            [7.6, 7.5, 5.4, 4.3, 3.2, 2.1, 5.7, 6.1, 2.2, 1.1],
            [8.4, 6.4, 5.9, 7.1, 9.2, 8.3, 3.6, 6.3, 2.1, 0.3]]

#jumlah biases pada layer1
biases1 = [4.4, 1.3, 3.5, 4.6, 7.9]

#inisialisasi bobot variable 2
weights2 =  [[0.1, 3.2, 2.4, 5.4, 4.6],
            [4.2, 1.1, 2.5, 7.8, 6.5],
            [2.6, 3.4, 9.8, 8.7, 6.4]]

#jumlah biases pada layer2
biases2= [2.4, 5.1, 7.7]

#menghitung layer1 menggunakan inputs, weights1, dan biases1
layer1_outputs = np.dot(inputs, np.array(weights1).T) + biases1

#menghitung layer2 dari hasil perhitungan layer1
layer2_outputs = np.dot(layer1_outputs, np.array(weights2).T) + biases2

#print output layer2
print(layer2_outputs)



matrix_33 = [[3,4,5],[-4,5,8], [6,7,9]]
# resultado = 13

positivo =     matrix_33[0][0] * matrix_33[1][1] * matrix_33[2][2] +\
               matrix_33[0][1] * matrix_33[1][2] * matrix_33[2][0] +\
               matrix_33[0][2] * matrix_33[1][0] * matrix_33[2][1]


negativo =     -1* (matrix_33[0][2] * matrix_33[1][1] * matrix_33[2][0] +\
               matrix_33[0][0] * matrix_33[1][2] * matrix_33[2][1] +\
               matrix_33[0][1] * matrix_33[1][0] * matrix_33[2][2])

determinante = positivo + negativo

print(determinante)
#Exercices

#importing NUmpy
import numpy as np
print('numpy:', np.__version__)
print(dir(np))

#creating numpy array using
python_list = [1, 2, 3, 4, 5]
print('type:', type(python_list))
print(python_list)
two_dimensionel_list = [[0,1,2], [3,4,5], [6,7,8]]
print(two_dimensionel_list)
numpy_array_from_list = np.array(python_list)
print(type(numpy_array_from_list))
print(numpy_array_from_list)

#creating float numpy arrays
numpy_array_from_list2 = np.array(python_list, dtype=float)
print(numpy_array_from_list2)

#creating boolean numpy arrays
numpy_bool_array = np.array([0, 1, -1, 0, 0], dtype=bool)
print(numpy_bool_array)

#creating multidimensional array using numpy
numpy_two_dimensionel_list = np.array(two_dimensionel_list)
print(type(numpy_two_dimensionel_list))
print(numpy_two_dimensionel_list)

#converting numpy array to list
np_to_list = numpy_array_from_list.tolist()
print(type(np_to_list))
print('one dimensional array:', np_to_list)
print('two dimensional array:', numpy_two_dimensionel_list.tolist())

python_tuple = (1,2,3,4,5)
print(type(python_tuple))
print('python tuple:', python_tuple)
numpy_array_from_tuple = np.array(python_tuple)
print(type(numpy_array_from_tuple))
print(numpy_array_from_tuple)

#shape of numpy array
nums = np.array([1,2,3,4,5])
print(nums)
print('shape of nums:', nums.shape)
print(numpy_two_dimensionel_list)
print('shape of numpy two dimensional list :', numpy_two_dimensionel_list.shape)
three_by_four_array = np.array([[0, 1, 2, 3], [4, 5, 6, 7], [8, 9, 10, 11]])
print(three_by_four_array.shape)

#data type of numpy array
int_lists = [-3, -2, -1, 0, 1, 2,3]
int_array = np.array(int_lists)
float_array = np.array(int_lists, dtype=float)
print(int_array)
print(int_array.dtype)
print(float_array)
print(float_array.dtype)

#size of numpy array
numpy_array_from_list = np.array([1, 2, 3, 4, 5])
two_dimensional_list = np.array([[0, 1, 2],
[3, 4, 5],
[6, 7, 8]])
print('The size:', numpy_array_from_list.size)
print('The size:', two_dimensional_list.size)

#mathematical operation using numpy
#addition
print('original array: ', numpy_array_from_list)
ten_plus_original = numpy_array_from_list + 10
print(ten_plus_original)

#substraction
print('original array: ', numpy_array_from_list)
ten_minus_original = numpy_array_from_list - 10
print(ten_minus_original)

#multiplication
print('original array: ', numpy_array_from_list)
ten_times_original = numpy_array_from_list * 10
print(ten_times_original)

#division
print('original array: ', numpy_array_from_list)
ten_times_original = numpy_array_from_list / 10
print(ten_times_original)

#modulus
print('original array: ', numpy_array_from_list)
ten_times_original = numpy_array_from_list % 3
print(ten_times_original)

#floor division
print('original array: ', numpy_array_from_list)
ten_times_original = numpy_array_from_list // 10
print(ten_times_original)

#Exponential
print('original array: ', numpy_array_from_list)
ten_times_original = numpy_array_from_list ** 2
print(ten_times_original)

#checking data types
numpy_int_arr = np.array([1,2,3,4])
numpy_float_arr = np.array([1.1, 2.0,3.2])
numpy_bool_arr = np.array([-3, -2, 0, 1,2,3], dtype='bool')
print(numpy_int_arr.dtype)
print(numpy_float_arr.dtype)
print(numpy_bool_arr.dtype)

#converting types
#int to float
numpy_int_arr = np.array([1,2,3,4], dtype = 'float')
print(numpy_int_arr)

#float to int
numpy_int_arr = np.array([1., 2., 3., 4.], dtype = 'int')
print(numpy_int_arr)

#int to boolean
print(np.array([-3, -2, 0, 1,2,3], dtype='bool'))

#int to str
print(np.array(['1', '2', '3'], dtype='<U21'))

#multi-dimensional arrays
two_dimension_array = np.array([(1,2,3),(4,5,6), (7,8,9)])
print(type (two_dimension_array))
print(two_dimension_array)
print('Shape: ', two_dimension_array.shape)
print('Size:', two_dimension_array.size)
print('Data type:', two_dimension_array.dtype)

#Getting items from a numpy array
two_dimension_array = np.array([[1,2,3],[4,5,6], [7,8,9]])
first_row = two_dimension_array[0]
second_row = two_dimension_array[1]
third_row = two_dimension_array[2]
print('First row:', first_row)
print('Second row:', second_row)
print('Third row: ', third_row)

first_column= two_dimension_array[:,0]
second_column = two_dimension_array[:,1]
third_column = two_dimension_array[:,2]
print('First column:', first_column)
print('Second column:', second_column)
print('Third column: ', third_column)
print(two_dimension_array)

#slicing numpy array
two_dimension_array = np.array([[1,2,3], [4,5,6], [7,8,9]])
first_two_rows_and_columns = two_dimension_array[0:2, 0:2]
print(first_two_rows_and_columns)

#reverse the rows and the whole array
print(two_dimension_array[::])

#Reverse the row and column positions
two_dimension_array = np.array([[1,2,3], [4,5,6], [7,8,9]])
print(two_dimension_array[::-1,::-1])

#represent missing values
print(two_dimension_array)
two_dimension_array[1,1] = 55
two_dimension_array[1,2] =44
print(two_dimension_array)

numpy_zeroes = np.zeros((3,3),dtype=int,order='C')
print(numpy_zeroes)

numpy_ones = np.ones((3,3),dtype=int,order='C')
print(numpy_ones)

first_shape = np.array([(1,2,3), (4,5,6)])
print(first_shape)
reshaped = first_shape.reshape(3,2)
print(reshaped)

np_list_one = np.array([1,2,3])
np_list_two = np.array([4,5,6])
print(np_list_one + np_list_two)
print('Horizontal Append:', np.hstack((np_list_one, np_list_two)))

print('Vertical Append:', np.vstack((np_list_one, np_list_two)))

#generate random numbers
random_float = np.random.random()
print(random_float)

random_floats = np.random.random(5)
print(random_floats)

random_int = np.random.randint(0, 11)
print(random_int)

random_int = np.random.randint(2,10, size=4)
print(random_int)

random_int = np.random.randint(2,10, size=(3,3))
print(random_int)

normal_array = np.random.normal(79, 15, 80)
print(normal_array)

#numpy and statistics
'''import matplotlib.pyplot as plt
import seaborn as sns
sns.set()
plt.hist(normal_array, color="grey", bins=50)'''

#matrix in numpy
four_by_four_matrix = np.matrix(np.ones((4,4), dtype=float))
print(four_by_four_matrix)

np.asarray(four_by_four_matrix)[2] = 2
print(four_by_four_matrix)

#numpy.arrange()
lst = range(0, 11, 2)
for l in lst:
    print(l)

whole_numbers = np.arange(0, 20, 1)
print(whole_numbers)

natural_numbers = np.arange(1, 20, 1)
print(natural_numbers)

odd_numbers = np.arange(1, 20, 2)
print(odd_numbers)

even_numbers = np.arange(2, 20, 2)
print(even_numbers)

#Creating sequence of numbers using linspace
print(np.linspace(1.0, 5.0, num=10))

print(np.linspace(1.0, 5.0, num=5, endpoint=False))

print(np.logspace(2, 4.0, num=4))

x = np.array([1,2,3], dtype=np.complex128)
print(x)

print(x.itemsize)

np_list = np.array([(1,2,3), (4,5,6)])
print(np_list)
print('First row: ', np_list[0])
print('Second row: ', np_list[1])
print('First column: ', np_list[:,0])
print('Second column: ', np_list[:,1])
print('Third column: ', np_list[:,2])

#numpy statistical function
np_normal_dis = np.random.normal(5, 0.5, 100)
np_normal_dis
print('min: ', two_dimension_array.min())
print('max: ', two_dimension_array.max())
print('mean: ',two_dimension_array.mean())
print('sd: ', two_dimension_array.std())

print(two_dimension_array)
print('Column with minimum: ',
np.amin(two_dimension_array,axis=0))
print('Column with maximum: ',
np.amax(two_dimension_array,axis=0))
print('=== Row ==')
print('Row with minimum: ',
np.amin(two_dimension_array,axis=1))
print('Row with maximum: ',
np.amax(two_dimension_array,axis=1))

#create repeating sequences
a = [1,2,3]
# Repeat whole of 'a' two times
print('Tile: ', np.tile(a, 2))
# Repeat each element of 'a' two times
print('Repeat: ', np.repeat(a, 2))

#generate random numbers
# One random number between [0,1)
one_random_num = np.random.random()
one_random_in = np.random
print(one_random_num)

# Random numbers between [0,1) of shape 2,3
r = np.random.random(size=[2,3])
print(r)

## Random numbers between [0, 1] of shape 2, 2
rand = np.random.rand(2,2)
print(rand)

rand2 = np.random.randn(2,2)
print(rand2)

# Random integers between [0, 10) of shape 2,5
rand_int = np.random.randint(0, 10, size=[5,3])
print(rand_int)

from scipy import stats
np_normal_dis = np.random.normal(5, 0.5, 1000) # mean,standard deviation, number of samples
np_normal_dis
## min, max, mean, median, sd
print('min: ', np.min(np_normal_dis))
print('max: ', np.max(np_normal_dis))
print('mean: ', np.mean(np_normal_dis))
print('median: ', np.median(np_normal_dis))
print('mode: ', stats.mode(np_normal_dis))
print('sd: ', np.std(np_normal_dis))

#Linear Algebra
### Dot product: product of two arrays
f = np.array([1,2,3])
g = np.array([4,5,3])
### 1*4+2*5 + 3*6
np.dot(f, g)

#NumPy Matrix Multiplication with np.matmul()
### Matmul: matruc product of two arrays
h = [[1,2],[3,4]]
i = [[5,6],[7,8]]
### 1*5+2*7 = 19
np.matmul(h, i)
np.array([[19, 22],[43, 50]])
## Determinant 2*2 matrix
### 5*8-7*6np.linalg.det(i)
np.linalg.det(i)

Z = np.zeros((8,8))
Z[1::2,::2] = 1
Z[::2,1::2] = 1
print(Z)

new_list = [ x + 2 for x in range(0, 11)]
print(new_list)

np_arr = np.array(range(0, 11))
print(np_arr + 2)

temp = np.array([1,2,3,4,5])
pressure = temp * 2 + 5
print(pressure)

'''plt.plot(temp,pressure)
plt.xlabel('Temperature in oC')
plt.ylabel('Pressure in atm')
plt.title('Temperature vs Pressure')
plt.xticks(np.arange(0, 6, step=0.5))
plt.show()'''

'''mu = 28
sigma = 15
samples = 100000
x = np.random.normal(mu, sigma, samples)
ax = sns.distplot(x);
ax.set(xlabel="x", ylabel='y')
plt.show()'''
import numpy as np
import matplotlib.pylab as plt

arr = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9], [0, 11, 12]])
# print(arr.shape)
# print(arr.size)
# print(arr.dtype)
# print(arr[0:2])
# print(arr[:, 0:2])
# print(arr[0:2:, 0:2])
# print(arr[::-1])
# print(arr[:, ::-1])
# print(arr[::-1, ::-1])

# arr1 = arr.reshape((12,))  # 多维数组变成一维
# arr2 = arr1.reshape((1, 12))
# arr3 = arr.reshape((4, -1))

# print(np.concatenate((arr, arr), axis=1))

# print(arr.sum(axis=0))

print(np.sort(arr, axis=0))

# print(np.array([1, 2, 3]))
# img_arr = plt.imread("./computer.jpg")
# print(img_arr)
# plt.imshow(img_arr[400:800, 50:650, :])
# plt.show()

# print(np.linspace(0, 100, 20))

# print(np.arange(0, 100, 2))

# np.random.seed(100)
# print(np.random.randint(0, 100, (4, 5)))

# print(np.random.random((4, 5)))

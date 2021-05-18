import numpy as np

#get file object
file1 = open("quantable_class\\sample.txt", "r+")
# for line in file:
line = file1.readlines()
#luminace values from file
lumline = line[2:9]


#chrominace values from file
chromline = line[11:19]
# chrom = [x[:-1] for x in chromline]

file1.close
lumin = np.array([x[:-1] for x in lumline])
# an_array = np.array([i for i in chrom])
# chrom = np.array([x[:-1] for x in chromline])

print(np.append(lumin, lumin[0].strip('[]')))
# print(chrom)

# inputchrom = chrom
# # an_array = np.array([[1, 2], [3, 4]])
# # another_array = np.array([[1, 2], [3, 4]])

# comparison = chrom == inputchrom
# equal_arrays = comparison.all()

# print(equal_arrays)
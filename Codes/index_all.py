# Your goal is to implement a function, index_all(), that takes a list of objects and the item to search 
# for as input arguments and returns a list of indices for where that item exists within the list.
# NOTE: Since the input argument could be a list of lists, your function should be able to traverse 
# multidimensional lists to find all instances of the item, and the elements of the returned list 
# should also be lists to indicate multidimensional indices.

def index_all(search_list, target):
  indices = []
  for i, item in enumerate(search_list):
    if item == target:
      indices.append([i])
    elif isinstance(item, list):
      for index in index_all(item, target):
        indices.append([i] + index)
  return indices

# [[[1, 2, 3], 2, [1, 3]], [1, 2, 3]]
# 0:[[1, 2, 3], 2, [1, 3]]
#   0:[1, 2, 3]
#     0:1
#     1:2
#     2:3
#   1:2
#   2:[1, 3]
#     0:1
#     1:3
# 1:[1, 2, 3]
#   0:1
#   1:2
#   2:3

example = [[[1, 2, 3], 2, [1, 3]], [1, 2, 3]]
print(index_all(example, 2)) # [[0, 0, 1], [0, 1], [1, 1]] 
print(index_all(example, [1, 2, 3])) # [[0, 0], [1]]
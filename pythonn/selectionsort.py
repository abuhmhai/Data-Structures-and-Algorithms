def selection_sort(array):

  for i in range(len(array)):
    min_index = i
    for j in range(i + 1, len(array)):
      if array[j] < array[min_index]:
        min_index = j
    array[i], array[min_index] = array[min_index], array[i]

  return array

if __name__ == "__main__":
  array = [10, 5, 2, 1, 8, 7,9, 6, 3, 4]
  sorted_array = selection_sort(array)
  print(sorted_array)

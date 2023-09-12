def insertion_sort(a):
  for i in range(1, len(a)):
    j = i
    while j > 0 and a[j] < a[j - 1]:
      a[j], a[j - 1] = a[j - 1], a[j]
      j -= 1

  return a
if __name__ == "__main__":
  a = [35, 7, 64, 52, 32, 22] 
  print("Unsorted array:", a)
  sorted_array = insertion_sort(a)
  print("Sorted array:", sorted_array)

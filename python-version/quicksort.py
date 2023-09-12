def swap(a, b):
  temp = a
  a = b
  b = temp

def partition(arr, low, high):
  pivot = arr[high]
  i = (low - 1)

  for j in range(low, high):
    if arr[j] <= pivot:
      i += 1
      swap(arr[i], arr[j])

  swap(arr[i + 1], arr[high])
  return (i + 1)

def quickSort(arr, low, high):
  if low < high:
    pi = partition(arr, low, high)

    quickSort(arr, low, pi - 1)
    quickSort(arr, pi + 1, high)

def main():
  arr = [10, 8, 7, 6, 5, 4, 3, 2, 1]
  n = len(arr)

  quickSort(arr, 0, n - 1)

  for i in range(n):
    print(arr[i])

if __name__ == "__main__":
  main()

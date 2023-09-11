while True:
    n = int(input("Nhập số phần tử của mảng: "))
    if n >0:
        break
    else:
        print("Nhập lại.")
array = []
for i in range(n):
    gia_tri = int(input(f'Nhập phần tử thứ {i+1}: '))
    array.append(gia_tri)
print(array)


# array.insert(3,8) # Chèn vào vị trí thứ 3 giá trị 8
# print("Mảng sau khi chèn phần tử là: ", array)

# while True:
#     index=int(input("Nhap vi tri can xoa: "))
#     if index<n:
#         del array[index]      
#         print("Mảng sau khi xóa phần tử ở vị trí xác định là: ", array)
#         break
#     else:
#         print("Nhap lai")


# array.remove(21)  # Xóa phần tử có giá trị là 21
# print("Mảng sau khi xóa phần tử có giá trị xác định là: ", array)

while True:
    e=int(input("Nhap gia tri muon xd vt: "))
    if e not in array:
        print("khong co trong mang")
    else:
        vi_tri=array.index(e)
        print(f"Vi tri cua {e} la: {vi_tri}")

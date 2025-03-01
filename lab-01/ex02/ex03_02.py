def daonguoclist(lst):
    return lst[::-1]
input_list = input("Nhap danh sach cac so, cach nhau bang dau phay: ")
numbers = list(map(int, input_list.split(',')))
listdaonguoc= daonguoclist(numbers)
print("List sau khi dao nguoc:", listdaonguoc)
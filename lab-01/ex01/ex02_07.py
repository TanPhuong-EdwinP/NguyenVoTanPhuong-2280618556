print("Nhập các dòng vănbanr(Nhập 'done' để kết thúc):")
lines = []
while True:
    line = input()
    if line.lower() =='done':
        break
    lines.append(line)
print("\n Các dòng đã nhập sau khi chuyêmr thành chữ in hoa:")
for line in lines:
    print(line.upper())    
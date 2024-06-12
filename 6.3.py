value=int(input("Введіть значення\n"))

while True:
    value_str = str(value)
    value=1
    for char in value_str:
        value=value*int(char)
    print(value)
    if value<=9:
        break
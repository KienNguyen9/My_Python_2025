# Variable 
Python is a dynamic variable language 

To get the type of any variable 
```Py
    a = 1000
    str_a =  "ABCD"

    print(type(a))
    print(type(str_a))

```

# Datatype 
    Interger
    Floating-point number
    complex-number

# Giới hạn lưu trữ của các kiểu dữ liệu

## Kiểu int
Với C/C++ giới hạn là khoảng 19 chứ số
Nhưng với python, thì ko có giới hạn cho kiểu dữ liệu `int` (trong python có thể xử lí kiểu số nguyên lớn)

## Kiểu float
Có giới hạn, nếu như sau khi tính toán vượt quá giới hạn này thì 
    Nếu lớn hơn giới hạn trên sẽ nhận chuối `inf`
    Nếu nhỏ hơn giới hạn dưới sẽ nhận giá trị `0`


## Kiểu bool

```
a = 123
b = 0
bool(a) # true
bool(b) # false
```

## Kiểu string

A = "string abcd"

## Ép kiểu - casting 

Dùng các hàm sau:

```py
a = 12345

str_a = string(a) 
```
cần chứ ý khi ép kiểu từ `string` sang `số nguyên` hoặc `số thực`

VD: dòng lệnh sau đây là không thể

```py
a = "123345.123aaa"
b = int(a) # là ko thể vì có kí tự "aaa" bên trong chuỗi

# Tương tự với khi ép sang float
```


# 1：ASCII码转换
# 给出一个string，你需要把他反转reverse，然后按照他的数字转换成英文字母
# 由于只会出现英文字母和空格，所以ASCII码肯定是两位数或者1开头的三位数，
# 所以反转之后只要判断读的第一位是不是1就可以确定读几位了，一遍O(n)遍历完即可出结果


#ASCII to string
print(chr(107))

# string ASCII
print(ord('h'))

code = '701011792823411101701997927'

code = code[::-1]

index = 0
res = []
while (index < len(code)):
    if code[index] == '1':
        letter = chr(int(code[index:index+3]))
        index += 3
    else:
        letter = chr(int(code[index:index+2]))
        index += 2
    res.append(letter)

print(''.join(res))




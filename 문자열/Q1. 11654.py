# 문자를 아스키코드로 : ord

def convert(data):
    if type(data) == str:
        print(ord(data))
    else:
        print(ord(str(data)))
        
data = input()
convert(data)


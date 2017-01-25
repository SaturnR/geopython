'''
import random
rnd = random.randint(0,100)
# ზემოთ დაწერილი ნაწილი ჯერ არ ამიხსნია, ამიტომ ბევს ნუ იფიქრებთ უბრალოდ გამოიყენეთ

while True:
    
    number = input('gamoicani ricxvi:')
    
    number = int(number)

    # ამ ადგილას შეადარეთ rnd  შემთხვევითი რიცხვი, თქვენს მიერ შეყვანილ number რიცხვს
    # ეკრანზე დაწერეთ შესაბამისი შედეგი, "metia", "naklebia" ან  'tqven gamoicanit ricxvi'
    if rnd > number:
        print('metia')
    elif rnd < number:
        print('naklebia')
    else:
        print('gilocavt Tqven gamoicanit')
        break
'''


'''
n = 0

while n < 10:
    print(str(n)+' is less then 10')
    n = n + 1
    if n == 5:
        break

'''
'''
n = 0

for n in range(10):
    print(str(n)+' is less then 10')
    n = n + 1
    if n > 5:
        break
    print('number is less then 5')


'''
n = 0

while n < 10:
    print(str(n)+ 'is less then 10')
    n = n + 1

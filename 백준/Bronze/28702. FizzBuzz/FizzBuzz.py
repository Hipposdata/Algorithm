# 입력된 세 수중 적어도 하나이상은 숫자일듯 
import sys
for i in range(3):
    tmp = sys.stdin.readline().strip()
    if tmp.isdigit():
        dap = int(tmp) + (3-i)
        if dap %5 == 0 and dap%3 == 0:
            print('FizzBuzz')
        elif dap%3 == 0 and dap %5 != 0:
            print('Fizz')
        elif dap%3 != 0 and dap %5 == 0:
            print('Buzz')
        else:
            print(dap)
        break

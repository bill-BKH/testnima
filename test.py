import random
import time


x = random.randint(1,6)

print('you are in wild west')
time.sleep(1)
print('you see bastardo!!!')
time.sleep(1)
print('he slowly reaches to his gun')

time.sleep(random.randint(1,5))
start = time.time()
print('DRAW')
input()
end  = time.time()


print('your speed is '+str(round(end-start)))
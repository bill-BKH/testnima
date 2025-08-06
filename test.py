import random
import time
import vars
from art import bastardo,revolver
x = random.randint(1,6)
health = 3
while health >0: 
    print('you are in wild west')
    time.sleep(1)
    print('you see bastardo!!!')
    time.sleep(1)
    print('he slowly reaches to his gun')

print('you are in wild west')
time.sleep(1)
print(bastardo)
print('you see bastardo!!!')
time.sleep(1)
print('he slowly reaches to his gun')

time.sleep(random.randint(1,3))
start = time.time()
print(revolver)
print('DRAW')
input()
end  = time.time()

elapsed_time = round(end-start,2)
if elapsed_time < vars.minimum_speed:
    print('you are the fastest gun drawer in wild west!!!')
else:
    print('bastardo kills you!')


print('end')
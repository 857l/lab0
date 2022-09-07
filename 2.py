import time

t_start = time.perf_counter()

f = open('input.txt', 'r')
x = int(f.readline())

a = 0
b = 1
for i in range(x - 1):
    a, b = b, a + b

f = open('output.txt', 'w')
f.write(str(b))
f.close()

print("Время работы: %s секунд " % (time.perf_counter() - t_start))
print(b)

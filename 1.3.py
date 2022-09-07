import time

t_start = time.perf_counter()

f = open('input.txt', 'r')
a, b = f.readline().split()

f = open('output.txt', 'w')
f.write(str(int(a) + int(b)**2))
f.close()

print(int(a) + int(b))
print("Время работы: %s секунд " % (time.perf_counter() - t_start))
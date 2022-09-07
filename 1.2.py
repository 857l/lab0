import time

t_start = time.perf_counter()

a, b = map(int, input().split())

print(a + b**2)
print("Время работы: %s секунд " % (time.perf_counter() - t_start))
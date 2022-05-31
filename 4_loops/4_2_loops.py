import random
import resource
import psutil

initial_memory_usage = 0
initial_cpu_usage = 0
final_memory_usage = 0
final_cpu_usage = 0

scope_start = 0
scope_end = 100000

test_value = 0
test_values = []

for i in range(scope_start, scope_end):

    if i == scope_start:
        initial_memory_usage = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
        initial_cpu_usage = psutil.cpu_percent(1)

    if i == (scope_end - 1):
        final_memory_usage = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
        final_cpu_usage = psutil.cpu_percent(1)

    test_value = test_value * random.randint(1, 1000)
    test_values.append(test_value)


print('Initial memory usage: ', initial_memory_usage, ', initial CPU usage: ', initial_cpu_usage)
print('Final memory usage: ', final_memory_usage, ', final CPU usage: ', final_cpu_usage)

import time
start_time = time.perf_counter ()
for x in range(1, 100):
    print(x)
end_time = time.perf_counter ()
print(end_time - start_time, "seconds")
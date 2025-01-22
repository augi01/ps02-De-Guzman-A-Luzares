# Join Method
start = time.time()
result = "".join(str(i) for i in range(1, 100001))
print("Join Method Time:", time.time() - start)

import time
count = 0
while True and count < 1000:
    count = count + 1
    print ("count: " + str(count))
    time.sleep(1)

print("end of 10s_process")
import requests
import sys
import time

requestNumber = 1

if len(sys.argv) > 1:
    requestNumber = sys.argv[1]

timeForRequests = []

timeToEnd = time.time() + 60 * requestNumber

while time.time() < timeToEnd:
    start = time.time()
    for i in range(10):
        r = requests.get('http://localhost:8080/pie')

    end = time.time()

    timeForRequests.append(end-start)

averageRequest = 0

for i in timeForRequests:
    averageRequest += i

averageRequest /= len(timeForRequests)

print(averageRequest)




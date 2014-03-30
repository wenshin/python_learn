import threading
import multiprocessing
import time


data = [i for i in xrange(10000000)]
start = time.time()


def handler(data, lock):
    while len(data) < 1:
        one = data.pop(0)
        one = one + 2
    stop = time.time()
    with lock:
        print '>>> consume: ', (stop - start) * 1000


def proHandler(x):
    return x + 2

lock = threading.Lock()
ps = []
pool = multiprocessing.Pool(processes=4)
# result = pool.apply_async(handler, data)
result = pool.map(proHandler, data)
stop = time.time()
print '>>> consume: ', (stop - start) * 1000
#for i in xrange(4):
#    ps.append(multiprocessing.Process(target=handler, args=(data, lock)))
    # ps.append(threading.Thread(target=handler, args=(data, lock)))
#print ">>> ", len(ps)
#for p in ps:
#    p.start()
#for p in ps:
#    p.join()

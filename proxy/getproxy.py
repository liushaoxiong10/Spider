import threads
import Queue

queue = Queue.Queue()
url='http://www.xicidaili.com/nt/'
for i in range(1, 5):
    url_o = url + str(i)
    queue.put(url_o)
thread_count = 10
thread_all = []
for i in range(thread_count):
    thread_all.append(threads.threads(queue))
for t in thread_all:
    t.start()
for t in thread_all:
    t.join()


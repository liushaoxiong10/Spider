#-*- coding:utf-8-*-
import threading
import  spider

class threads(threading.Thread):
    def __init__(self,queue):
        threading.Thread.__init__(self)
        self._queue=queue
    def run(self):
        while not self._queue.empty():
            url=self._queue.get_nowait()
            spider.spider(url)

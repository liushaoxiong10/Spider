import threads
import Queue
import sys

def main(key):
    queue=Queue.Queue()
    url_frist = 'https://www.baidu.com/s?wd='
    url_pn =  '&oq='
    url_last ='&ie=utf-8&rsv_idx=1&pn='
    string=str(key)
    for i in range(0,20,10):
        url=url_frist+string+url_pn+string+url_last+str(i)
        queue.put(url)
    thread_count=10
    thread_all =[]
    for i in range(thread_count):
        thread_all.append(threads.threads(queue))
    for t in thread_all:
        t.start()
    for t in thread_all:
        t.join()
if __name__=='__main__':
    if len(sys.argv)!=2:
        print "baidu.py 'Your Seach content'"
    else :
        main(sys.argv[1])

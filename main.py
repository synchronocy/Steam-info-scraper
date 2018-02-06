#!usr/bin/env python3

# Date: 02-07-18, Feb ~ 7th 2018 | Synchronocy
# Project: SteamID Info grabber
# Pretty bad way of doing things, nonetheless simple.
# IDLE Python 3.6 64-bit

# Added possible pooling for those who bulk search.


#import sys
#import string
import requests
import json
#from lxml import html
#from threading import Thread
#from queue import Queue

apikey = ""
'''
class Worker(Thread):
    """
    Pooling
    """

    def __init__(self, tasks):
        Thread.__init__(self)
        self.tasks = tasks
        self.daemon = True
        self.start()

    def run(self):
        while True:
            func, args, kargs = self.tasks.get()
            try:
                func(*args, **kargs)
            except Exception as ex:
                pass
            finally:
                self.tasks.task_done()

class ThreadPool:
    """
    Pooling
    """

    def __init__(self, num_threads):
        self.tasks = Queue(num_threads)
        for _ in range(num_threads):
            Worker(self.tasks)

    def add_task(self, func, *args, **kargs):
        """
        Add a task to be completed by the thread pool
        """
        self.tasks.put((func, args, kargs))

    def map(self, func, args_list):
        """
        Map an array to the thread pool
        """
        for args in args_list:
            self.add_task(func, args)

    def wait_completion(self):
        """
        Await completions
        """
        self.tasks.join()
'''     
def scrape(uname):
    src = requests.get("https://steamid.eu/api/request.php?api=" + apikey + "&player=" + uname + "&request_type=1&format=json").text
    src = src.replace("steamid.eu","steamcommunity.com")
    print(src)
    try:
        with open("output.txt","a") as handle:
            handle.write(src)
        print("Output Saved!")
    except:
        print("failed!")

def main():
    #pool = ThreadPool(20)
    uname = input("Custom URL / SteamID64 / SteamID32: ")
    #pool.add_task(scrape(uname))
    scrape(uname)
    
if __name__ == '__main__':
    main()

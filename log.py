import time 

def timestamp(func):
    def wrapper():
      print(f"{time.ctime()}")
      func()
      
    return wrapper

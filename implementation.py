def go(callback):
  pass
def run():
  pass
def make():
  pass
def len(channel):
  pass
def cap(channel):
  pass
def send(channel, value, callback):
  pass
def recv(channel, callback):
  pass
def close(channel):
  pass
def select(cases, callback):
  pass
# used in select
default = object() 

class Channel:
    def __init__(self):
        self.closed = False
        self.waiting_to_send = 

class WaitingQueue(list):
    total = 0

    def enqueue(self, x):
        WaitingQueue.total += 1
        self.append(x)

    def dequeue(self, x=None):
        if x is None:
            x = self.pop(0)
            WaitingQueue.total -= 1
        else:
            idx = self.index(x)
            if idx is not None:
                self.pop(idx)
                WaitingQueue.total -= 1
        return x
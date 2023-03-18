execution_queue = []

def go(callback):
    if callback:
        execution_queue.append(callback)
    pass

def run():
    while execution_queue:
        f = execution_queue.pop(0)
        f()
    if WaitingQueue.total > 0:
        raise Exception("<----- fatal error: all goroutines are asleep")
    pass

def make():
    return Channel()

def len(channel):
    return 0

def cap(channel):
    return 0

def send(channel, value, callback):
    # "A send on a nil channel blocks forever."
    if channel is None:
        WaitingQueue.total += 1
        return

    # "A send on a closed channel proceeds by causing a run-time panic."
    if  channel.closed:
        raise Exception("<----- send on closed channel")

    # "A send on an unbuffered channel can proceed if a receiver is ready."
    if channel.waiting_to_recv:
        receiver = channel.waiting_to_recv.dequeue()
        go(callback)
        go(lambda: receiver(value, True))
        return 

    channel.waiting_to_send.enqueue((value, callback))

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
        self.waiting_to_send = WaitingQueue()
        self.waiting_to_recv = WaitingQueue()

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
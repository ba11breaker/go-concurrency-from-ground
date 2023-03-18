const execution_queue = [];

function go(callback) {
  if (callback) execution_queue.push(callback);
}

function run() {
  while (execution_queue.length > 0) {
    f = execution_queue.pop(0);
    f();
  }
  if (WaitingQueue.total > 0) {
    throw new Exception("<----- fatal error: all goroutines are asleep")
  }
}

function make() {

}

function len() {

}

function cap() {

}

function send(channel, value, callback) {

}

function recv(channel, callback) {

}

function close(channel) {

}

function select() {

}

_default = new Object();

class Channel {
  closed = false;
  waiting_to_send = null;
  waiting_to_recv = null;

  constructor() {
    this.waiting_to_recv = new WaitingQueue();
    this.waiting_to_send = new WaitingQueue();
  }
}

class WaitingQueue {
  static total = 0;
  list = [];

  constructor() {
    this.list = [];
  }

  enqueue(x) {
    WaitingQueue.total += 1;
    this.list.push(x);
  }

  deuqeue(x = null) {
    if (!x) {
      x = this.list.pop(0);
      WaitingQueue.total -= 1;
    } else {
      idx = this.list.findIndex(x);
      if (idx >= -1) {
        this.list.pop(idx);
        WaitingQueue.total -= 1;
      }
    }
  }
}

// const channel = new Channel();
// channel.waiting_to_recv.enqueue(5);
// console.log(WaitingQueue.total);
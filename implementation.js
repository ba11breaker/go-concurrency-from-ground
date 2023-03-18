function go(callback) {
  
}

function run() {

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
  total = 0;
  list = [];

  enqueue(x) {
    this.total += 1;
    this.list.push(x);
  }

  deuqeue(x = null) {
    if (!x) {
      x = this.list.pop(0);
      this.total -= 1;
    } else {
      idx = this.list.findIndex(x);
      if (idx >= -1) {
        this.list.pop(idx);
        this.total -= 1;
      }
    }
  }
}
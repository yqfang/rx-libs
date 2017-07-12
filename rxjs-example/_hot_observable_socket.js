/**
 * Created by yqfang on 2017/7/10.
 */
var { Observable } = require('rxjs/Rx');


/** A really, really, really fake websocket */
class FakeWebSocket {
    constructor(url) {
        this.url = url;
        console.log('connecting to ' + url);
        let i = 0;
        this.id = setInterval(() => this.triggerMessage(i++), 500);
    }

    close() {
        console.log('closing connection to ' + this.url);
        clearInterval(this.id);
    }

    addEventListener(name, handler) {
        const listeners = this.listeners = this.listeners || {};
        const handlers = listeners[name] = listeners[name] || [];
        handlers.push(handler);
    }

    addEventListener(name, handler) {
        const listeners = this.listeners = this.listeners || {};
        const handlers = listeners[name] = listeners[name] || [];
        handlers.push(handler);
    }

    triggerMessage(msg) {
        const listeners = this.listeners;
        if (listeners) {
            const handlers = listeners['message'];
            handlers.forEach(handler => handler({ target: this, data: JSON.stringify(msg) }))
        }
    }
}



// Notice we've moved the creation of the WebSocket
// *outside* of the observable.
const socket = new FakeWebSocket('ws://someurl');

const source = new Observable((observer) => {
    // here our observable is "closing over" the producer
    // the producer (socket) is a shared reference for
    // every call/subscription
    socket.addEventListener('message', (e) => observer.next(e));

    //NOTICE: no returned teardown. :(
});


/**
 * Notice in console that ONE connection is made
 * and shared.
 */

// first connection
source.subscribe((e) => console.log('s1', e));

// second connection one second later
setTimeout(() => {
    source.subscribe((e) => console.log('s2', e));
}, 1000);


// since it's a "hot" observable, a new connection is created
// only once for all subscriptions to the same observable.e just functions)
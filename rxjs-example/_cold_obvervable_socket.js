/**
 * Created by yqfang on 2017/7/10.
 */
var { Observable } = require('rxjs/Rx');
//The example below is “cold” because it creates and listens to the WebSocket inside of the subscriber function that is called when you subscribe to the Observable:
// So anything that subscribes to `source` above, will get its own WebSocket instance, and when it unsubscribes, it will `close()` that socket. This means that our source is really only ever unicast, because the producer can only send to one observer.
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

    triggerMessage(msg) {
        const listeners = this.listeners;
        if (listeners) {
            const handlers = listeners['message'];
            handlers.forEach(handler => handler({ target: this, data: JSON.stringify(msg) }))
        }
    }
}



const source = new Observable((observer) => {
    const socket = new FakeWebSocket('ws://someurl');
    socket.addEventListener('message', (e) => observer.next(e));
    return () => socket.close();
});


/**
 * Notice in console that two connections are made
 */

// first connection
source.subscribe((e) => console.log('s1', e));

// second connection one second later
setTimeout(() => {
    source.subscribe((e) => console.log('s2', e));
}, 3000);


// since it's a "cold" observable, a new connection is created
// each time you subscribe to the same observable.
// (aka, each time you call the function,
//       since observables are just functions)
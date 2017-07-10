from rx import Observable, Observer



def subscribe(observer):
    observer.on_next('hello')
    observer.on_next('world')
    observer.on_completed()


# act as a comsumer(receive data)
class PrintObserver(Observer):
    def on_next(self, value):
        print("Received {0}".format(value))
    def on_completed(self):
        print("Done")
    def on_error(self, error):
        print("Error Occurred: {0}".format(error))

# act as a producer(push data)
source = Observable.create(subscribe)


source.subscribe(PrintObserver())
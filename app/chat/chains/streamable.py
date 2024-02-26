from langchain.chains import LLMChain
from threading import Thread
from queue import Queue

from app.chat.callbacks.stream import StreamingHandler

class StreamableChain(LLMChain):
    def stream(self, input):
        queue = Queue()
        handler = StreamingHandler(queue)
        def task():
            self(input, callbacks=[handler])
        
        Thread(target=task).start()
            
        while True:
            token = queue.get()
            if token is None:
                break 
            yield token
import uvicorn
from fastapi import FastAPI
import endpoints
from container import Container

from eventwatcher import EventWatcher

import threading

def create_app() -> FastAPI:
    container = Container()
    container.wire(modules=[endpoints])

    app = FastAPI()
    app.container = container
    app.include_router(endpoints.router)

    return app


app = create_app()

if __name__ == '__main__':
    event_thread = threading.Thread(target=EventWatcher)
    event_thread.start()
    uvicorn.run('main:app', host='0.0.0.0', port=8000)

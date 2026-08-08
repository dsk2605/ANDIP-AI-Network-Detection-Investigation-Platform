from fastapi import WebSocket


class ConnectionManager:

    def __init__(self):

        self.connections: list[WebSocket] = []

    async def connect(
        self,
        websocket: WebSocket,
    ):

        await websocket.accept()

        self.connections.append(websocket)

    def disconnect(
        self,
        websocket: WebSocket,
    ):

        if websocket in self.connections:
            self.connections.remove(websocket)

    async def broadcast(
        self,
        message: dict,
    ):

        disconnected = []

        for websocket in self.connections:

            try:

                await websocket.send_json(message)

            except Exception:

                disconnected.append(websocket)

        for websocket in disconnected:

            self.disconnect(websocket)


manager = ConnectionManager()
import asyncio
import websockets

async def handle_client(websocket, path):
    print("Cliente conectado.")

    message = await websocket.recv()
    print(f"Mensagem recebida: {message}")

    if message == "hello":
        response = "world"
        await websocket.send(response)
        print(f"Resposta Enviada: {response}")

start_server = websockets.serve(handle_client, "localhost", 12300)

asyncio.get_event_loop().run_until_complete(start_server)
print("Servidor WebSocket ouvindo em localhost:12300...")
asyncio.get_event_loop().run_forever()

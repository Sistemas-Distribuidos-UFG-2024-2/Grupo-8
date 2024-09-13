const WebSocket = require('ws');

const serverUrl = 'ws://localhost:12300';

const ws = new WebSocket(serverUrl);

ws.on('open', () => {
	console.log('Conectado ao servidor WebSocket.');
	 ws.send('hello');
});

ws.on('message', (message) => {
	console.log(`Resposta do servidor: ${message}`);
	ws.close();
});

ws.on('close', () => { 
	console.log('Conexão fechada.'); 
});


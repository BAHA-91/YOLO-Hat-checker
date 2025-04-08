const { contextBridge, ipcRenderer } = require('electron');

contextBridge.exposeInMainWorld('electronAPI', {
  startStream: () => ipcRenderer.send('start-stream')
});

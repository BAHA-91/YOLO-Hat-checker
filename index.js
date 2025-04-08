const { app, BrowserWindow } = require('electron');

function createWindow () {
  const win = new BrowserWindow({
    width: 900,
    height: 600,
    frame: false,
    transparent: true,
    hasShadow: false,
    backgroundColor: '#00000000',
    webPreferences: {
      contextIsolation: false,
      nodeIntegration: true
    }
  });

  win.loadFile('index.html');
}

app.whenReady().then(() => {
  createWindow();
});

const http = require("http"); // http modul importálása

// Szerver létrehozása
const server = http.createServer((req, res) => {
  res.statusCode = 200;
  res.setHeader("Content-Type", "text/plain");
  res.end("Hello, Node.js!");
});

// A szerver a 3000-es porton figyel
server.listen(3000, () => {
  console.log("A szerver fut a http://localhost:3000 címen");
});

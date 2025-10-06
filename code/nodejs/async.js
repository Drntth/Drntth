const fs = require("fs");
console.log("1");
fs.readFile("data/async.txt", "utf-8", (err, data) => {
  if (err) throw err;
  console.log(data);
});
console.log("2");
console.log("3");

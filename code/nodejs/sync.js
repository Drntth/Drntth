const fs = require("fs");
console.log("1");
const result = fs.readFileSync("data/sync.txt", "utf-8");
console.log(result);
console.log("2");
console.log("3");

const fs = require("fs");

fs.readFile("./tweet.js", "utf-8", (err, jsonString) => {
  if (err) {
    console.log(err);
  } else {
    try {
      const data = jsonString;
      const jsonData = JSON.stringify(data).replace(/\\n/g, "");
      fs.writeFile("./tweet.json", jsonData, (err, jsData) => {
        if (err) {
          console.log("uh oh", err);
        } else {
          console.log("success bro");
        }
      });
    } catch (err) {
      console.log("Error parsing JSON", err);
    }
  }
});

const fs = require("fs");
const { parse } = require("path");

//choose the filename of the archive and use it for first argument
//make sure you put the archive in this same dir
fs.readFile("./tweet.js", "utf-8", (err, jsonString) => {
  const parsedJSON = JSON.parse(jsonString);

  const errorHandler = (e) => console.log(".");
  Object.values(parsedJSON).forEach((val) => {
    if (
      val.tweet.id < 1217132453917147136 &&
      val.tweet.id != 700808989886382080
    ) {
      const listOfIDs = val.tweet.id + ", ";
      console.log(typeof listOfIDs);

      try {
        fs.appendFile("yes.txt", listOfIDs, (err) => {
          console.log("updated");
        });
      } catch (e) {
        errorHandler();
      }
    }
  });
});

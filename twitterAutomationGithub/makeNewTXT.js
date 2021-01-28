const fs = require("fs");
const { parse } = require("path");

fs.readFile("./tweet.js", "utf-8", (err, jsonString) => {
  const parsedJSON = JSON.parse(jsonString);

  const errorHandler = (e) => console.log(".");
  Object.values(parsedJSON).forEach((val) => {
    if (
      val.tweet.id < 1217132453917147136 &&
      val.tweet.id != 700808989886382080
    ) {
      const listOfIDs = val.tweet.id + " " + val.tweet.created_at + ", ";

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

// fs.readFile("./tweet.js", "utf-8", (err, jsonString) => {
//   const parsedJSON = JSON.parse(jsonString);
//   Object.values(parsedJSON).forEach((val) => {
//     if (
//       val.tweet.id < 1177329553653370880 &&
//       val.tweet.id != 700808989886382080
//     ) {
//       const listOfIDs = val.tweet.id + ", ";
//       fs.appendFile("yes.txt", listOfIDs, (err) => {
//         if (err) throw err;
//         console.log("updated");
//       });
//     }
//   });
// });

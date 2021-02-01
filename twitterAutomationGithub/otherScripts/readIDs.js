const fs = require("fs");

fs.readFile("listOfIDs.txt", "utf-8", (err, listOfIDs) => {
  if (err) throw err;
  const IDs = listOfIDs.split(",");
  console.log(typeof IDs);
  IDs.forEach((id) => console.log(id));
});

//not sure if this one works, so I'll just leave it commented
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

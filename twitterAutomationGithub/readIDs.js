const fs = require("fs");

fs.readFile("listOfIDs.txt", "utf-8", (err, listOfIDs) => {
  if (err) throw err;
  const IDs = listOfIDs.split(",");
  console.log(typeof IDs);
  IDs.forEach((id) => console.log(id));
});

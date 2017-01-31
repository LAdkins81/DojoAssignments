var contact = {
  fName: "Laura",
  lName: "Adkins",
  age: 35,
};
function printObj(object){
  for (var cat in object){
  console.log(object[cat]);
  }
}
printObj(contact);

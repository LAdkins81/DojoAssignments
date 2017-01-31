function numOnly(arr){
  newArr = [];
  for(var i=0; i<arr.length; i++){
    if (typeof arr[i] === "number"){
      newArr.push(arr[i]);
    }
  }
  return newArr;
}
var check = numOnly([1, 7, "hi", "blue", 44]);
console.log(check);

function zipIt(arr1, arr2){
  var combArr = {};
  for (var x=0; x<arr1.length; x++){
    combArr[arr1[x]]=arr2[x];
  }
  return combArr;
}
var zippedObj = zipIt([1,2,3], ["hi", "bye", "later"]);
console.log(zippedObj);

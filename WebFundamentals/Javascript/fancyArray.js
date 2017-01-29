function fancyArray(symbol, arr, reversed){
  var count = 0;
  if(reversed === false){ //prints the array in order if false
  for (var i = 0; i < arr.length; i++){ //loops through the array
    console.log(count++ + symbol + arr[i]); //returns the array in order
    }
  }
  if (reversed === true){ //prints the array in reverse if true
     var revArr = arr.reverse(); //reverses the array
     for (var x = 0; x < arr.length; x++){ //loops through the array
     console.log(count++ + symbol + revArr[x]); //returns the reversed array
    }
  }
}
fancyArray("==>",["Jim", "Jack", "Rob", "Bob"], false);

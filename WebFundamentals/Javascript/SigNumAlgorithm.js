function sigNum(num){
  if (num < 1){
    while(num < 1){
      num=num*10;
    }
  }
  else if (num > 9){
    while (num > 10){
      num=num/10;
    }
  } else {
    num = num;
  }
  return Math.trunc(num);
}
var answer = sigNum(901212);
console.log(answer);

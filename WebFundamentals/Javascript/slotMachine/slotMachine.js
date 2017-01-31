function slotMachine(quarters){
  while(quarters > -1){
    var bonus = Math.floor(Math.random()*51 + 50);
    quarters--;
     var win = bonus + quarters;
    if(Math.trunc(Math.random()*100) === Math.trunc(Math.random()*100)){
      return win;
    }
    if (quarters === 0){
      return 0;
    }
  }
}
var winnings = slotMachine(50);
console.log(winnings);

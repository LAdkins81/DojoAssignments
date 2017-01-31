function slotMachine(quarters, goal){
  while(quarters > -1){
    quarters--;
    console.log(quarters);
    var bonus = Math.floor(Math.random()*51 + 50);
    var win = bonus + quarters;
    if(Math.trunc(Math.random()*100) === Math.trunc(Math.random()*100)){
      console.log(win);
    } else if (quarters > goal){
      console.log(quarters);
      break;
    }
    else if (quarters === 0){
        return 0;
      }
    }
  }
var winnings = slotMachine(100, 10);
console.log(winnings);

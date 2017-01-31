function bDayCountdown(daysUntilMyBday){

  if (daysUntilMyBday > 61){
   console.log("Did you start with 60 or fewer days?");
  }

while (daysUntilMyBday < 61 && daysUntilMyBday > 0){
  daysUntilMyBday--;

  if (daysUntilMyBday < 61 && daysUntilMyBday > 29){
  console.log(daysUntilMyBday + " days until my birthday...so sad!");
} else if (daysUntilMyBday < 30 && daysUntilMyBday > 5){
  console.log(daysUntilMyBday + " days left!! I can't wait! *squeal*")
}
else if (daysUntilMyBday < 6 && daysUntilMyBday > 0){
  console.log(daysUntilMyBday + " DAYS UNTIL MY BIRTHDAY! WOOT!");
} else if (daysUntilMyBday === 0){
  console.log("Happy Birthday!");
}
}
}
var countDown = bDayCountdown(102);
console.log(countDown);

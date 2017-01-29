
function tellTime(hour, minute, period){
  var late = Number(hour) + 1;
  if(minute > 30 && period === "AM"){
    console.log("It's almost " + late + " in the morning");
  } else if(minute < 30 && period === "AM"){
    console.log("It's just past " + hour + " in the morning");
  }else if(minute > 30 && period === "PM"){
    console.log("It's almost " + late + " in the evening");
  } else if (minute < 30 && period === "PM"){
    console.log("It's just past " + hour + " in the evening");
  } else {
    console.log("Time to buy a proper clock!")
  }
}
tellTime(4, 45, "AM");

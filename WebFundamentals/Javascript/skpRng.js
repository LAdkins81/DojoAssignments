function skpRng(start, end, skipBy){
    Number(start);
    Number(skipBy);
  for (var i = start; i < end; i=i+skipBy){
    console.log(i);
  }
}
skpRng(4,56,8);

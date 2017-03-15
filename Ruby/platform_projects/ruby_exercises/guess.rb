def guess_number num
  number = 25
  if num == 25
    puts "You got it right!"
  elsif num > 25
    puts "Too high!"
  else
    puts "Too low!"
  end
end

guess_number 25

def guess_number_2 num
  unless num == 25
    puts "Nope!"
  else
    puts "You got it!"
  end
end

guess_number_2 25

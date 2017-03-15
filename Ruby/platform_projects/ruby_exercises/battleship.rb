BEGIN{
  puts "this is in the beginning"
}

END {
  puts "this is the end"
}

board = Array.new (5) { Array.new(5, 0) }

def pretty_print board
  board.each_cons(5) {|a| "\n"}
  print board
end

puts "Let's play battleship"
pretty_print board

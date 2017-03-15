test1 = ["ant", "bear", "cat"].any? { |word| word.length >= 3 }
puts "____________", test1

test2 = (1..4).collect {|i| i*i}
puts "____________", test2

test3 = (1..4).collect { "dog" }
puts "____________", test3

test4 = (1..10).detect { |i| i %5 == 0 and i % 7 == 0 }
puts "____________", test4

test5 = (1..100).detect { |i| i %5 == 0 and i % 7 == 0 } # => 35
puts "____________", test5

test6 = (1..10).find_all { |i| i % 3 == 0 }
puts "____________", test6

test7 = (1..10).reject { |i| i % 3 == 0 }
puts "____________", test7

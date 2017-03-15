x = (1..55)

sum = 0
x.each do |n|
  puts "The number is #{n}"
  sum += n
  puts "The sum is #{sum}"
end

x.each do |n|
  puts n
end

x.each do |n|
  puts n if n % 2 == 1
end

arr = [1, 5, 6, 22]
arr.each do |v|
  puts v
end
puts arr.max

sum = 0
arr.each { |a| sum+=a }
avg = sum/arr.length.to_f
puts avg

def odd rng
  y = rng.step(2).to_a
  puts y
end
puts odd (1..255)

def greater_than arr, y
  arr.count{|x|x>y}
end
puts greater_than [5, 2, 7, 9, 4, 5], 3

def sqr_array arr
  newarr = []
  arr.each { |i| newarr << i ** 2 }
  puts newarr.class
end

sqr_array [5, 9, 11, 3]

def no_neg arr
  arr.collect! { |v| (v < 0) ? 0 : v }
end
puts no_neg [1, 4, -3, 5, -1]

def max_min_avg arr
  max = arr.max
  min = arr.min
  avg = arr.inject{ |sum, el| sum+el }.to_f / arr.size
  newarr = [] << max << min << avg
  puts newarr
end

max_min_avg [4, 3, 11, 55, -7]

def shift_arr arr
  arr.shift
  arr.insert(arr.length, 0)
  puts arr
end

shift_arr [5, 6, 8, 11, 4]

def dojo arr
  arr.collect! {|v| (v < 0) ? "Dojo" : v }
end
puts dojo [1, 4, -3, 5, -1]

def greater_than array
  sum = 0
  array.each { |v| sum+=v }
  puts sum
  array.reject! { |v| v < 10 }
  print array
end

puts greater_than [3,5,1,2,7,9,8,13,25,32]

def shuff array
  newarr = array.shuffle
  puts newarr
  five = array.delete_if {|x| x.length < 5}
  puts five
end

shuff ['John', 'KB', 'Oliver', 'Cory', 'Matthew', 'Christopher']

def alpha
  arr = Array ('a'..'z')
  newarr = arr.shuffle
  puts newarr.last
  puts newarr.first
  if newarr.first == 'a' || newarr.first == 'e' || newarr.first == 'i' || newarr.first == 'o' || newarr.first == 'u'
    puts "Oops! You printed a vowel!"
  end
end

alpha

def randarr
  randomarray = (55..100).to_a.sort{ rand() - 0.5 }[0..9]
  print randomarray.sort
  puts randomarray.max
  puts randomarray.min
end

randarr

str = ""
5.times { str << rand(65..90).chr }
puts str

string_array = []
10.times do
  str = ""
  5.times { str << rand(65..90).chr }
  string_array << str
end
puts string_array

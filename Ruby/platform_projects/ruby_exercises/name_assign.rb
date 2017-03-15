a = {first_name: "Laura", last_name: "Adkins"}
b = {first_name: "Terry", last_name: "Adkins"}
c = {first_name: "Sara", last_name: "Boehm"}
d = {first_name: "Julie", last_name: "Hellebusch"}
e = {first_name: "Katie", last_name: "Booth"}
names = [a, b, c, d, e]

def people a = {first_name: "Laura", last_name: "Adkins"}
  puts "Your name is #{a[:first_name]} #{a[:last_name]}!"
end

people
people b
people c
people d
people e

puts "You have #{names.length} names in the 'names' array."
names.each do |name|
  puts "The name is #{name[:first_name]} #{name[:last_name]}"
end

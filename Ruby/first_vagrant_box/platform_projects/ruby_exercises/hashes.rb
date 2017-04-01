x = {'first_name' => 'Laura', 'last_name' => 'Adkins'}
x.delete('last_name')
puts x
puts x.empty?
puts x.has_key?('first_name')
puts x.has_value?('first_name')

# def new_user user = {greeting: "Welcome", first_name: "Laura", last_name: "Adkins"}
#   puts "#{user[:greeting]}, #{user[:first_name]} #{user[:last_name]}!"
# end
# our_user = {greeting: 'Hey', first_name: 'Terry', last_name: "Adkins"}
# new_user
# new_user our_user

def new_user first_name: "first", last_name: "last"
  puts "Welcome to our site, #{first_name} #{last_name}!"
end

new_user

def new_user greeting="Welcome", first_name: "first", last_name: "last"
    puts "#{greeting}, #{first_name} #{last_name}"
end
our_user = {first_name: "Bob", last_name: "Smith"}
new_user "Hey", {first_name: "Terry", last_name: "Adkins"}
new_user "Hello", our_user

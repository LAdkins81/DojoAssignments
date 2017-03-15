def hello_world
  puts "hello world"
end
hello_world

def say_hello name1, name2
  puts "hello #{name1} and #{name2}"
end

say_hello "Laura","Katie"

def are_you_there name1, name2
  if name1.empty? or name2.empty
    return "Who are you?"
  end
end

puts are_you_there "",""

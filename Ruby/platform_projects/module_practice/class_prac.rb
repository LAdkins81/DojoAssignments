class CodingDojo
  @@no_of_branches = 0
  def initialize(id, name, address)
    @branch_id = id
    @branch_name = name
    @branch_address = address
    @@no_of_branches += 1
    puts "Created branch #{@@no_of_branches}"
  end
  def hello
    puts "Hello CodingDojo!"
  end
  def display_all
    puts "Branch ID: #{@branch_id}"
    puts "Branch Name: #{@branch_name}"
    puts "Branch Address: #{@branch_address}"
  end
end
# now using above class to create objects
branch = CodingDojo.new(117, "Chicago CodingDojo", "Chicago IL")
branch.display_all
branch2 = CodingDojo.new(333, "Seattle CodingDojo", "Seattle WA")
branch2.display_all

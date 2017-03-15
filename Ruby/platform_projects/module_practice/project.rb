class Project

  def initialize(name,descrip)
    @proj_name = name
    @proj_descrip = descrip
  end

  def name
    puts @proj_name
  end

  def elevator_pitch
    puts "The #{@proj_name} project is great! #{@proj_descrip}"
  end

end

project1 = Project.new("Main", "We will rock you!")
puts project1.name
project1.elevator_pitch

project2 = Project.new("Secondary", "Another option is dancing until dawn!")
project2.elevator_pitch

require_relative 'mammal'

class Dog < Mammal

  def pet
    @health = @health + 5
    self
  end

  def walk
    @health = @health - 1
    self
  end

  def run
    @health = @health - 10
    self
  end

end

fido = Dog.new
puts fido.walk.walk.walk.run.run.pet.health

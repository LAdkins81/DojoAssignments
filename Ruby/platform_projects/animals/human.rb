require_relative 'mammal'

class Human < Mammal
  def subclass_method
    breath
  end

  def another_method
    self.eat
  end
end
human = Human.new
puts human

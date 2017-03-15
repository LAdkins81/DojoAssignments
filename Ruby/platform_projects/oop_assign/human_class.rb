class Human
  attr_accessor :strength, :intelligence, :stealth, :health

  def initialize
    @strength = 3
    @intelligence = 3
    @stealth = 3
    @health = 100
  end

  def attack target
    target.health -= 10 if target.class.ancestors.include?(Human)
  end

end

person1 = Human.new
person2 = Human.new

person1.attack(person2)
puts person2.health

require_relative 'human_class'

class Warrior < Human

  def initialize
    @health = 50
    @intelligence = 25
  end

  def heal
    @health += 10
  end

  def fireball target
    if target.class.ancestors.include?(Human)
      target.health -= 20
      true
    else
      false
    end
  end

end

warrior1 = Warrior.new
warrior2 = Warrior.new

warrior1.fireball(warrior2)

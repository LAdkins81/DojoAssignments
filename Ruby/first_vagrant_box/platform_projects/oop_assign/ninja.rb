require_relative 'human_class'

class Ninja < Human

  def initialize
    @stealth = 175
  end

  def steal target
    attack(target)
    @health += 10
  end

  def get_away
    @health -= 15
  end

end

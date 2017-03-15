require_relative 'human_class'

class Samurai < Human

@@samurais = 0

  def initialize
    @health = 200
    @@samurais +=1
  end

  def death_blow target
    if target.class.ancestors.include?(Human)
      target.health = 0
      true
    else
      false
    end
  end

  def mediate
    @health = 200
  end

  def how_many
    puts @@samurais
  end

end

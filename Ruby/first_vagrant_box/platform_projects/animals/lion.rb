require_relative 'mammal'

class Lion < Mammal
  def initialize
    @health = 170
  end

  def fly
    @health = @health - 10
    self
  end

  def attack_town
    @health = @health - 50
    self
  end

  def eat_human
    @health = @health + 20
    self
  end

  def display_health
    puts "This is a lion... His health is #{@health}"
  end

end

roar = Lion.new
puts roar.attack_town.attack_town.attack_town.eat_human.eat_human.fly.fly.display_health

bob = Mammal.new
puts bob.health

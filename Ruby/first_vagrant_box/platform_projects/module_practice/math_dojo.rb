class MathDojo
  attr_accessor :num1

  def initialize
    @num1 = 0
  end

  def add *values
    @num1 += values.flatten.reduce(:+)
    self
  end

  def subtract *values
    @num1 -= values.flatten.reduce(:+)
    self
  end

end

challenge1 = MathDojo.new.add(2).add(2, 5).subtract(3, 2).num1
puts challenge1
challenge2 = MathDojo.new.add(1).add([3, 5, 7, 8], [2, 4.3, 1.25]).subtract([2,3], [1.1, 2.3]).num1
puts challenge2
# def multi_args *values
#  values
# end
# puts multi_args(1).inspect # => [1]
# puts multi_args(1, 2, 3, 4, 5).inspect # => [1, 2, 3, 4, 5]

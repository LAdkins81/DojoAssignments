module MyEnumerable
  def my_each
    for i in 0..self.length
      yield(self[i])
    end
  end
end
class Array
   include MyEnumerable
end

test1 = [1,2,3,4].my_each {|i| puts i}
test2 = [1,2,3,4].my_each {|i| puts i*10}
puts test1
puts test2

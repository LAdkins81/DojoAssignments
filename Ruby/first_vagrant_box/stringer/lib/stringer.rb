require "stringer/version"

module Stringer
  def self.spacify *strings
    strings.join(" ")
  end

  def self.minify string, len
    if len > string.length
      return string
    end
     "#{string[0..len]}..."
  end

  def self.replacify string, word, replace
    str = string.split
    str.map{ |x| x = word }
  end

end

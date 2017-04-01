require "spec_helper"

RSpec.describe Stringer do
  # it "has a version number" do
  #   expect(Stringer::VERSION).not_to be nil
  # end
  #
  # it "does something useful" do
  #   expect(false).to eq(true)
  # end
  it "concatenates undefined number of strings with a space" do
   expect(Stringer.spacify "Laura", "Terry", "Bob", "Katie", "Joe", "Yuka", "Louis", "Meredith").to eq("Laura Terry Bob Katie Joe Yuka Louis Meredith")
  end
  context "minify string" do
    it "returns the string to the length specified with ... at the end" do
      expect(Stringer.minify "I love to code", 7).to eq("I love t...")
    end
    it "returns the string if the string is less than the number specified" do
      expect(Stringer.minify "hello", 7).to eq("hello")
    end
  end
  it "replaces a word in a string with a different word" do
    expect(Stringer.replacify "I can't do this", "can't", "can").to eq("I can do this")
  end
end

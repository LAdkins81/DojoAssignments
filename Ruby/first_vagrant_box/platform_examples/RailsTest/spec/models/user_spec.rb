require 'rails_helper'

RSpec.describe User, type: :model do
  context "With valid attributes" do
    it "should save" do
      user = User.new(
      first_name:'Laura',
      last_name:'Adkins',
      email:'laura@adkins.com'
      )
      expect(user).to be_valid
    end
  end
  context "With invalid attributes" do
    it "should not save if first_name field is blank" do
      user = User.new(
        first_name:'',
        last_name:'adkins',
        email:'laura@adkins.com'
        )
        expect(user).to be_invalid
      end
    it "should not save if last_name field is blank" do
      user = User.new(
        first_name:'Laura',
        last_name:'',
        email:'laura@adkins.com'
        )
        expect(user).to be_invalid
      end
    it "should not save if email is not unique" do
      user = User.create(
        first_name:"Katie",
        last_name:"Booth",
        email:"katie@booth.com"
      )
      user = User.new(
        first_name:"Katie",
        last_name:"Booth",
        email:"katie@booth.com"
      )
      expect(user).to be_invalid
    end
    it "should not save if email is invalid" do
      user = User.new(
        first_name:"David",
        last_name:"Wolgemuth",
        email:"davidw"
      )
      expect(user).to be_invalid
    end
  end
end

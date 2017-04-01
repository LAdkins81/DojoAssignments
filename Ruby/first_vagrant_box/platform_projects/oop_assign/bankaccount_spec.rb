require_relative 'bankaccount'
RSpec.describe BankAccount do
  before(:each) do
    @user1 = BankAccount.new()
    @user1.deposit('checking', 150)
    @user1.deposit('savings', 25)
    @user1.total_balance
  end
  it 'has a getter method for retrieving the checking account balance' do
    expect{@user1.check_balance}.to output("Your checking account balance is 150\n").to_stdout
  end
  it 'has a getter method that retrieves the total balance' do
    expect{@user1.total_balance}.to output("Your total balance is 175\n").to_stdout
  end
  context "withdrawing money" do
    it 'has a function that raises and error if a user tries to withdraw more cash than is in checking account' do
    expect{ @user1.withdraw("checking", 500) }.to raise_error("Insufficient funds")
   end
   it 'has a function that raises and error if a user tries to withdraw more cash than is in savings account' do
   expect{ @user1.withdraw("savings", 500) }.to raise_error("Insufficient funds")
  end
 end
  it 'cannot set interest rate' do
    expect{@user1.interest_rate}.to raise_error{NoMethodError}
  end
  it 'cannot retrieve number of accounts' do
    expect{@user1.number_of_accts}.to raise_error{NoMethodError}
  end
end

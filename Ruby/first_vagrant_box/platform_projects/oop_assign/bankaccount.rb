require 'securerandom'

class BankAccount
  attr_reader :checking
  attr_reader :savings
  attr_reader :account_num
  attr_reader :int_rate

@@bank_accounts = 0

  def initialize
    @checking = 0
    @savings = 0
    @int_rate = 0.01
    @account_num = create_acct_num
    @@bank_accounts += 1
  end

  def display_acct_num
    puts @account_num
  end

  def deposit acct, amt
    if acct == 'checking'
      @checking += amt
    end
    if acct == 'savings'
      @savings += amt
    end
  end

  def withdraw acct, amt
    if acct == 'checking'
      if @checking - amt < 0
        raise "Insufficient funds"
      else
        @checking -= amt
      end
    else
      if @savings - amt < 0
        raise "Insufficient funds"
      else
        @savings -= amt
      end
    end
  end

  def check_balance
    puts "Your checking account balance is #{@checking}"
  end

  def save_balance
    puts "Your savings account balance is #{@savings}"
  end

  def total_balance
    puts "Your total balance is #{@checking + @savings}"
  end

  def account_information
    puts "Account number = #{@account_num}"
    puts "Total balance = #{@checking + @savings}"
    puts "Checking account balance = #{@checking}"
    puts "Savings account balance = #{@savings}"
    puts "Interest rate = #{@int_rate}"
  end

  private
    def create_acct_num
      @account_num = SecureRandom.random_number * 100000000000
      @account_num = @account_num.floor
    end

  private
    def number_of_accts
      puts @@bank_accounts 
    end

end

user2 = BankAccount.new
user2.deposit('checking', 55)
user2.account_information

class User < ActiveRecord::Base
  validates :first_name, :last_name, :email_address, :age, presence: true
  validates :first_name, :last_name, :email_address, length: { in: 2..20 }
  validates :age, numericality: { greater_than: 10, less_than: 150 }
end

class Blog < ActiveRecord::Base
  validates :name, :description, presence: true

  has_many :owners
  has_many :posts

  has_many :users, through: :owners
  has_many :user_posts, through: :posts, source: :user
  has_many :comments, as: :commentable, dependent: :destroy
end

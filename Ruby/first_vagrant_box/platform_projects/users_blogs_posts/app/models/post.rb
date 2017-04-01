class Post < ActiveRecord::Base
  validates :title, :content, presence: true
  validates :title, length: {minimum: 7}

  belongs_to :blog
  belongs_to :user
  has_many :messages
  has_many :comments, as: :commentable, dependent: :destroy
end

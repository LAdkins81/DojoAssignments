class UsersController < ApplicationController
  def index
    render json: User.all
  end

  def count
    user_count = User.count
    render text: "There are #{user_count} users!"
  end

  def new
    render 'users/new.html'
  end

  def create
    User.create( name: params[:name])
    redirect_to action: :index
  end

  def show
    render json: User.find(params[:id])
  end

  def edit
    @user = User.find(params[:id])
    render 'users/edit.html'
  end

end

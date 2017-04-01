class UsersController < ApplicationController
  skip_before_action :require_login, only: [:new, :create]
  before_action :require_correct_user, only: [:edit, :show, :update, :destroy]

  def new
    @user = User.new
  end

  def create
    @user = User.new(user_params)
    if @user.save
      redirect_to '/sessions/new'
    else
      flash[:errors] = @user.errors.full_messages
      redirect_to '/users/new'
    end
  end

  def show
    @user = User.find(params[:id])
    @secrets = Secret.where('user_id=?', session[:user_id])
  end

  def edit
    @user = User.find(params[:id])
  end

  def update
    user = User.find(params[:id])
    user.update(user_params)
    if user.save
      redirect_to "/users/#{user.id}"
    else
      flash[:errors] = user.errors.full_messages
    end
  end

  def destroy
    user = User.find(params[:id])
    session.clear
    user.destroy
    redirect_to '/users/new'
  end

  private
  def user_params
    params.require(:user).permit(:name, :email, :password, :password_confirmation)
  end

  def require_correct_user
    if current_user != User.find(params[:id])
      redirect_to "/users/#{session[:user_id]}"
    end
  end

end

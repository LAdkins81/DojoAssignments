class SessionsController < ApplicationController
  skip_before_action :require_login, except: [:destroy]

  def new
  end

  def create
    user = User.find_by_email(params[:email])
    if user.nil?
      flash[:errors] = ["Invalid Combination"]
      redirect_to '/sessions/new'
    else
      if user.authenticate(params[:password])
        session[:user_id] = user.id
        redirect_to "/users/#{user.id}"
      else
        flash[:errors] = ["Invalid Combination"]
        redirect_to "/sessions/new"
      end
    end
  end

  def destroy
    reset_session
    redirect_to "/sessions/new"
  end
end

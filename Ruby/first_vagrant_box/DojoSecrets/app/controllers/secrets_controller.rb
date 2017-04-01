class SecretsController < ApplicationController

  def index
    @secrets = Secret.all
    @likes = Like.all
  end

  def create
    @secret = Secret.new(content:params[:content], user_id:session[:user_id])
    if @secret.save
      redirect_to :back
    else
      flash[:errors] = @secret.errors.full_messages
      redirect_to :back
    end
  end

  def destroy
    secret = Secret.find(params[:id])
    secret.destroy if secret.user = current_user
    redirect_to "/users/#{current_user.id}"
  end

end

class SurveyController < ApplicationController
  def index
    if session[:counter].nil?
      session[:counter] = 0
    end
  end

  def create
    Student.create(name:params[:name], location:params[:location], language:params[:language], comment:params[:comment])
    redirect_to action: 'result'
  end

  def result
    @students = Student.last
    session[:counter] += 1
    times = session[:counter]
    flash[:notice] = "Thank you! You have submitted this form #{times} times!"
  end

end

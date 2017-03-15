class SayController < ApplicationController
  def index
    if session[:counter].nil?
      session[:counter] = 0
      puts 'hello'
    end
    render text: "What do you want me to say?"
  end

  def hello
    render text: "Saying hello!"
  end

  def hello_joe
    render text: "Saying hello to Joe!"
  end

  def hello_michael
    redirect_to action: :hello_joe
  end

  def count
    session[:counter] += 1
    times = session[:counter]
    render text: "You have visited this page #{times} time(s)!"
  end

  def restart
    session.clear
    render text: "Destroyed the session!"
  end
end

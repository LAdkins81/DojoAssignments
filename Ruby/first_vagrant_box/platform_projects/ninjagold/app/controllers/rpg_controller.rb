class RpgController < ApplicationController
  def index
    if session[:gold].nil?
      session[:gold] = 0
    end
  end

  def farm
    current_time = Time.now.strftime("%l:%M on %m-%d-%Y")
    farmgold = rand(10..20)
    session[:gold] += farmgold
    session[:farm] = "You have earned #{farmgold} from the farm! #{current_time}"
    redirect_to action: "index"
  end

  def cave
    current_time = Time.now.strftime("%l:%M on %m-%d-%Y")
    cavegold = rand(5..10)
    session[:gold] += cavegold
    session[:cave] = "You have earned #{cavegold} from the cave! #{current_time}"
    redirect_to action: "index"
  end

  def house
    current_time = Time.now.strftime("%l:%M on %m-%d-%Y")
    housegold = rand(2..5)
    session[:gold] += housegold
    session[:house] = "You have earned #{housegold} from the house! #{current_time}"
    redirect_to action: "index"
  end

  def casino
    current_time = Time.now.strftime("%l:%M on %m-%d-%Y")
    casinogold = rand(-50..50)
    session[:gold] += casinogold
    if casinogold > 0
      session[:casino] = "You have earned #{casinogold} from the casino! #{current_time}"
    else
      session[:casino] = "You have lost #{casinogold} from the casino! #{current_time}"
    end
    redirect_to action: "index"
  end

end

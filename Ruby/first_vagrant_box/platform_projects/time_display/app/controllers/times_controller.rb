class TimesController < ApplicationController
  config.time_zone = 'Central Time (US & Canada)'
  def main
    @time_date = Time.now.utc.in_time_zone.strftime("%l:%M on %a, %m-%d-%Y")
  end
end

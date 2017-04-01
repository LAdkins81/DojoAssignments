class DojoController < ApplicationController
  def index
    @dojos = Dojo.all
  end

  def new
    @dojo = Dojo.new
  end

  def create
    @dojo = Dojo.new(dojo_params)

    if @dojo.save
      flash[:success] = "Congratulations! You've added a new dojo!"
      redirect_to action: 'index'
    else
      flash[:errors] = @dojo.errors.full_messages
      redirect_to action: 'new'
    end
  end

  def show
    @dojo = Dojo.find(params[:id])
    @students = @dojo.students
  end

  def update
    @dojo = Dojo.find(params[:id])

    if @dojo.update(dojo_params)
      redirect_to root_path, notice: "You have successfully updated the dojo!"
    else
      flash[:errors] = @mydojo.errors.full_messages
    end
  end

  def edit
    @dojo = Dojo.find(params[:id])
  end

  def destroy
    dojo = Dojo.find(params[:id])
    dojo.destroy
    redirect_to :root
  end

  private
  def dojo_params
    params.require(:dojo).permit(:branch, :street, :city, :state)
  end

end

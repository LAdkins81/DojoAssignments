require_relative 'project'

RSpec.describe Project do
  before(:each) do
    @project1 = Project.new('Project 1', 'description 1', 'Laura Adkins')
    @project2 = Project.new('Project 2', 'description 2', 'Katie Booth')
  end
  it 'has a getter and setter for name attribute' do
    @project1.name = "Changed Name"
    expect(@project1.name).to eq("Changed Name")
  end
  it 'has a getter and setter for owner attribute' do
    @project1.owner = "Ruby Rails"
    expect(@project1.owner).to eq("Ruby Rails")
  end
  it 'has a method elevator_pitch to explain name, description, and owner' do
    expect(@project1.elevator_pitch).to eq("Project 1, description 1, Laura Adkins")
    expect(@project2.elevator_pitch).to eq("Project 2, description 2, Katie Booth")
  end
  describe 'project tasks' do
    it 'has a method add_tasks that pushes a single task into the tasks attribute array and a tasks method that prints all the tasks' do
    1.upto(4) { |n| @project1.add_tasks("Task # #{n}") }
    expect(@project1.tasks).to eq(["Task # 1", "Task # 2", "Task # 3", "Task # 4"])
  end
    it 'has method print_tasks that prints every task in the project' do
      1.upto(2) { |n| @project1.add_tasks("Task # #{n}") }
      expect{ @project1.print_tasks }.to output("Task # 1\nTask # 2\n").to_stdout
    end
  end
end

require 'rails_helper'
RSpec.describe UsersController, type: :controller do
  before do
    @user = create(:user)
    @user2 = create(:user2)
  end
  context "when not logged in" do
    before do
      session[:user_id] = nil
    end
    it "cannot access show" do
      get :show, id: @user
      expect(response).to redirect_to("/sessions/new")
    end
    it "cannot access edit"
      get :edit, id: @user
      expect(response).to redirect_to("/sessions/new")
    end
    it "cannot access update"
      get :update, id: @user
      expect(response).to redirect_to("/sessions/new")
    end
    it "cannot access destroy"
      get :destroy, id: @user
      expect(response).to redirect_to("/session/new")
    end
  end
  context "when signed in as the wrong user" do
    before do
      session[:user_id] = @user.id
    end
    it "cannot access profile page another user"
      get :show, id: @user2
      expect(response).to redirect_to("/users/#{session[:user_id]}")
    end
    it "cannot access the edit page of another user"
      get :edit, id: @user2
      expect(response).to redirect_to("/users/#{session[:user_id]}")
    end
    it "cannot update another user"
      get :update, id: @user2
      expect(response).to redirect_to("/users/#{session[:user_id]}")
    end
    it "cannot destroy another user"
      get :destroy, id: @user2
      expect(response).to redirect_to("/users/#{session[:user_id]}")
    end
  end
end

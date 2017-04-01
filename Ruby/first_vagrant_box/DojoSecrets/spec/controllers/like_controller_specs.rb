require 'rails_helper'
RSpec.describe LikesController, type: :controller do
  before do
    @user = create(:user)
    @secret = create(:secret, user: @user)
    @like = create(:like, secret: @secret, user: @user)
  end
  context "when not logged in " do
    before do
      session[:user_id] = nil
    end
    it "cannot create a like"
      get :create, id: @user
      expect(response).to redirect_to("/sessions/new")
    end
    it "cannot destroy a like"
      get :destroy, id: @user
      expect(response).to redirect_to("/sessions/new")
    end
  end
  context "when signed in as the wrong user" do
    before do
      @wrong_user = create(:user, email:"wrong@user.com")
      session[:user_id] = @wrong_user.id
    end
    it "shouldn't be able to destroy a like"
      delete :destroy, id: @like.id
      expect(Like.last).to eq(@like)
    end
  end
end

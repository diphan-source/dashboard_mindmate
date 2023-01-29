import React from "react";

const Login = () => {
  return (
    <div className="container-fluid p-0">
      <div className="row">
        <div className="col-12">
          <div className="login-card">
            <form className="theme-form login-form">
              <h4>Login</h4>
              <h6>Welcome back! Log in to your account.</h6>
              <div className="form-group">
                <label>Email Address</label>
                <div className="input-group">
                  <span className="input-group-text">
                    <i className="icon-email"></i>
                  </span>
                  <input
                    className="form-control"
                    type="email"
                    required=""
                    placeholder="Test@gmail.com"
                  />
                </div>
              </div>
              <div className="form-group">
                <label>Password</label>
                <div className="input-group">
                  <span className="input-group-text">
                    <i className="icon-lock"></i>
                  </span>
                  <input
                    className="form-control"
                    type="password"
                    name="login[password]"
                    required=""
                    placeholder="*********"
                  />
                </div>
              </div>
              <div className="form-group">
                <button className="btn btn-primary btn-block" type="submit">
                  Sign in
                </button>
              </div>
            </form>
          </div>
        </div>
      </div>
    </div>
  );
};

export default Login;

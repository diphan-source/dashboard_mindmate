import React from 'react'

export const Login = () => {
  return (
    <section>
  <div class="container-fluid p-0">
    <div class="row m-0">
      <div class="col-12 p-0">
        <div class="login-card ">
          <form class="theme-form login-form theme-login-form" method="post">
            <h4>Login</h4>
            <h6>Welcome back! Log in to your account.</h6>
            <input type="hidden" name="csrfmiddlewaretoken" value="voRxoLCLTVLBxAoYsyJGLV76igA79f1l3rZ1w79LTnrqRlgNwQ9Zhn0fLbvhB4SR" />
            <tr>
    <th><label for="id_username">Username:</label></th>
    <td>
      
      <input type="text" name="username" autofocus autocapitalize="none" autocomplete="username" maxlength="150" required id="id_username" />
      
      
    </td>
  </tr>

  <tr>
    <th><label for="id_password">Password:</label></th>
    <td>
      
      <input type="password" name="password" autocomplete="current-password" required id="id_password" />
      
      
        
      
    </td>
  </tr>
            
              <div class="form-group">
                <button class="btn btn-primary btn-block" type="submit">Sign in</button>
              </div>
              <p>Don't have account?<a class="ms-2" href="register_simple.htm">Create Account</a></p>
          </form>
        </div>
      </div>
    </div>
  </div>
</section>
  )
}

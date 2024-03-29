import MuiThemeProvider from 'material-ui/styles/MuiThemeProvider';
import RaisedButton from 'material-ui/RaisedButton';
import TextField from 'material-ui/TextField';
import "./Login.css"
import "../App"
import React from 'react';
import axios from 'axios'

class Login extends React.Component {
constructor(props){
  super(props);
  this.state={
    username: this.props.username,
    password:this.props.password
  }
 }

 validateForm() {
  return this.state.username.length > 0 && this.state.password.length > 0;
}

userHasAuthenticated() {
  this.props.userHasAuthenticated(true);
}


 handleClick(event){
   var self = this;
   //TODO: Change apiBaseURL to the actual URL
  // var apiBaseUrl = "http://68.82.219.27:8080/login";
  var apiBaseUrl = "http://httpbin.org/post";
	var payload={
    "message_type" : 3,
    "body" : {    
      "username":this.state.username,
      "password":this.state.password
    }
  }
	axios.post(apiBaseUrl, payload)
	.then(function (response) {
		console.log(response);
		if(response.status === 200){
			console.log("Login successfull");
      self.userHasAuthenticated();
      localStorage.setItem("username", self.state.username)
      self.props.history.push("/");
      window.location.reload();
      
		}
		else if(response.status === 204){
			console.log("username password do not match");
			alert("username password do not match")
    }
	})
	.catch(function (error) {
		console.log(error);
	});
}

render() {
  return (
    <div class="wrapper fadeInDown">
      <div id="formContent">
        <div>
            <h3>Login</h3>
        </div>
        <MuiThemeProvider>
          <div>
          <TextField
            hintText="Enter your Username"
            type="username"
            floatingLabelText="Username"
            onChange = {(event,newValue) => this.setState({username:newValue})}
          />
          <br/>
            <TextField
              type = "password"
              hintText="Enter your Password"
              floatingLabelText="Password"
              onChange = {(event,newValue) => this.setState({password:newValue})}
            />
            <br/>
            <RaisedButton label="Submit" primary={true} style={style} onClick={(event) => this.handleClick(event)}/>
          </div>
        </MuiThemeProvider>
      </div>
    </div>
  );
}
}
const style = {
 margin: 15,
};
export default Login;
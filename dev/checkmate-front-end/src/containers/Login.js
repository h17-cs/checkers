import MuiThemeProvider from 'material-ui/styles/MuiThemeProvider';
import RaisedButton from 'material-ui/RaisedButton';
import TextField from 'material-ui/TextField';
import "./Login.css"
import "../App"
import React from 'react';
import axios from 'axios'
import {withRouter} from "react-router"
//TODO: change to actual screen redirect after successful login

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
	var apiBaseUrl = "http://68.82.219.27:8080/addUser";
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
			// var uploadScreen=[];
			// uploadScreen.push(<Register appContext={self.props.appContext}/>)
      // self.props.appContext.setState({loginPage:[],uploadScreen:uploadScreen})
      self.userHasAuthenticated();
      // self.props.push({
      //   state: { username: self.state.username,
      //            password: self.state.password }
      //     })
      self.setState({
          state: { username: self.state.username,
                    password: self.state.password }
             })
      self.props.history.push("/");
		}
		else if(response.status === 204){
			console.log("username password do not match");
			alert("username password do not match")
    }
    //TODO: Uncomment when database is ready
		// else{
		// 	console.log("username does not exists");
		// 	//alert("username does not exist");
		// }
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
// const TestRouter = withRouter(Login);
export default Login;
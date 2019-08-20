import MuiThemeProvider from 'material-ui/styles/MuiThemeProvider';
import AppBar from 'material-ui/AppBar';
import RaisedButton from 'material-ui/RaisedButton';
import TextField from 'material-ui/TextField';
import React from 'react';
import axios from 'axios'

import index from './index'
//TODO: change to actual screen redirect after successful login
class Login extends React.Component {
constructor(props){
  super(props);
  this.state={
  email:'',
  password:''
  }
 }

 handleClick(event){
   //TODO: Change apiBaseURL to the actual URL
	var apiBaseUrl = "lol";
	var self = this;
	var payload={
    "message_type" : 3,
    "body" : {    
      "email":this.state.email,
      "password":this.state.password
    }
  }
	axios.post(apiBaseUrl, payload)
	.then(function (response) {
		console.log(response);
		if(response.data.code === 200){
			console.log("Login successfull");
			var uploadScreen=[];
			uploadScreen.push(<index appContext={self.props.appContext}/>)
			self.props.appContext.setState({loginPage:[],uploadScreen:uploadScreen})
		}
		else if(response.data.code === 204){
			console.log("email password do not match");
			alert("email password do not match")
		}
		else{
			console.log("email does not exists");
			alert("email does not exist");
		}
	})
	.catch(function (error) {
		console.log(error);
	});
}

render() {
    return (
      <div>
        <MuiThemeProvider>
          <div>
          <AppBar
             title="Login"
           />
           <TextField
             hintText="Enter your Email"
             floatingLabelText="Email"
             onChange = {(event,newValue) => this.setState({email:newValue})}
             />
           <br/>
             <TextField
               type="password"
               hintText="Enter your Password"
               floatingLabelText="Password"
               onChange = {(event,newValue) => this.setState({password:newValue})}
               />
             <br/>
             <RaisedButton label="Submit" primary={true} style={style} onClick={(event) => this.handleClick(event)}/>
         </div>
         </MuiThemeProvider>
      </div>
    );
  }
}
const style = {
 margin: 15,
};
export default Login;
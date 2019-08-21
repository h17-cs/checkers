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
  username:'',
  password:''
  }
 }

 handleClick(event){
   //TODO: Change apiBaseURL to the actual URL
	var apiBaseUrl = "http://httpbin.org/post";
	var self = this;
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
			var uploadScreen=[];
			uploadScreen.push(<index appContext={self.props.appContext}/>)
			self.props.appContext.setState({loginPage:[],uploadScreen:uploadScreen})
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
      <div>
        <MuiThemeProvider>
          <div>
          <AppBar
             title="Login"
           />
           <TextField
             hintText="Enter your Username"
             floatingLabelText="Username"
             onChange = {(event,newValue) => this.setState({username:newValue})}
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
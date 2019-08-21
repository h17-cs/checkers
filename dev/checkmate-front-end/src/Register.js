import React, { Component } from 'react';
import MuiThemeProvider from 'material-ui/styles/MuiThemeProvider';
import AppBar from 'material-ui/AppBar';
import RaisedButton from 'material-ui/RaisedButton';
import TextField from 'material-ui/TextField';
import axios from 'axios';

import Login from './Login'


//TODO: Change payload to what charles sent to front end discord. For login and register

class Register extends Component {
  constructor(props){
    super(props);
    this.state={
      first_name:'',
      last_name:'',
      username:'',
      password:''
    }
  }

  handleClick(event){
    //TODO: Change apiBaseURL to the actual URL
    var apiBaseUrl = "http://httpbin.org/get";
    console.log("values",this.state.first_name,this.state.last_name,this.state.username,this.state.password);
    //To be done:check for empty values before hitting submit
    var payload={
      "message_type" : 3,
      "body" : {
        "first_name": this.state.first_name,
        "last_name":this.state.last_name,
        "username":this.state.username,
        "password":this.state.password
      }
    }
    axios.post(apiBaseUrl, payload)
   .then(function (response) {
     console.log(response);
     if(response.data.code === 200){
      //  console.log("registration successfull");
       var loginscreen=[];
       loginscreen.push(<Login parentContext={this}/>);
       var loginmessage = "Not Registered yet.Go to registration";
       this.props.parentContext.setState({loginscreen:loginscreen,
       loginmessage:loginmessage,
       buttonLabel:"Register",
       isLogin:true
        });
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
             title="Register"
           />
           <br/>
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
    );
  }
}
const style = {
  margin: 15,
};
export default Register;
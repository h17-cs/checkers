import React, { Component } from 'react';
import MuiThemeProvider from 'material-ui/styles/MuiThemeProvider';
import RaisedButton from 'material-ui/RaisedButton';
import TextField from 'material-ui/TextField';
import axios from 'axios';
import "./containers/Login.css"

import Login from './containers/Login'


class Register extends Component {
  constructor(props){
    super(props);
    this.state={
      username:'',
      password:''
    }
  }

  handleClick(event){
    //TODO: Change apiBaseURL to the actual URL
    var apiBaseUrl = "http://68.82.219.27:8080/addUser";
    console.log("values",this.state.username,this.state.password);
    //To be done:check for empty values before hitting submit
    var payload={
      "message_type" : 3,
      "body" : {
        "username":this.state.username,
        "password":this.state.password
      }
    }
    axios.post(apiBaseUrl, payload, {headers: {'Access-Control-Allow-Origin': '*', 'Content-Type': 'application/json'}, timout: 15000})
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
      <div class="wrapper fadeInDown">
        <div id="formContent">
          <div>
              <h3>Register</h3>
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
export default Register;
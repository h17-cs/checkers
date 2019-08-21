import React, { Component } from 'react';
import './App.css';
import LoginScreen from './Loginscreen';
import { Router, Route, Link, Switch } from 'react-router-dom';

import Routes from "./Routes";


class App extends Component {
  constructor(props){
    super(props);
    this.state={
      loginPage:[],
      uploadScreen:[]
    }
  }
  // componentWillMount(){
  //   var loginPage =[];
  //   loginPage.push(<LoginScreen appContext={this} key={"login-screen"}/>);
  //   this.setState({
  //                 loginPage:loginPage
  //                   })
  // }
  render() {
    return (
      <div className="App">
      <Link to="/">Home Page</Link>
      <Link to="/login">Login</Link>
      <Link to="/register">Register</Link>
      <Routes/>
      </div>
   
    );
  }
}

export default App;
import React, { Component, Fragment } from 'react';
import './App.css';
import { Navbar, Nav, NavItem} from "react-bootstrap";
import { LinkContainer } from "react-router-bootstrap";

import Routes from "./Routes";


class App extends Component {
  constructor(props){
    super(props);
    this.state={
      // loginPage:[],
      // uploadScreen:[]
      isAuthenticated:  false
    };
  }

  userHasAuthenticated = authenticated => {
    this.setState({
      isAuthenticated : authenticated
    });
  }

  handleLogout = event => {
    this.userHasAuthenticated(false);
  }
  // componentWillMount(){
  //   var loginPage =[];
  //   loginPage.push(<LoginScreen appContext={this} key={"login-screen"}/>);
  //   this.setState({
  //                 loginPage:loginPage
  //                   })
  // }
  render() {

    const childProps = {
      isAuthenticated: this.state.isAuthenticated,
      userHasAuthenticated: this.userHasAuthenticated
    };
    return (

      <div className="App">
        <Navbar fluid collapseOnSelect>
          <Navbar.Header>
            <Nav pullLeft>
              <LinkContainer to="/">
                <NavItem>Home</NavItem>
              </LinkContainer>
              <LinkContainer to="/game">
                <NavItem>Game</NavItem>
              </LinkContainer>
              <LinkContainer to="/chat">
                <NavItem>Chat</NavItem>
              </LinkContainer>
            </Nav>
            <Navbar.Toggle />
          </Navbar.Header>
          <Navbar.Collapse>
          <Nav pullRight>
            {this.state.isAuthenticated ? 
              <NavItem onClick={this.handleLogout}>Logout</NavItem> : 
              <Fragment>
                <LinkContainer to="/register">
                <NavItem>Register</NavItem>
                </LinkContainer>
                <LinkContainer to="/login">
                <NavItem>Login</NavItem>
                </LinkContainer>
              </Fragment>
            }
          </Nav>
          </Navbar.Collapse>
        </Navbar>
        <Routes childProps= {childProps}/>     
      </div>
    );
  }
}

export default App;
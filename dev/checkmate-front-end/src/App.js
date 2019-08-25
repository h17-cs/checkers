import React, { Component, Fragment } from 'react';
import './App.css';
import { Navbar, Nav, NavItem} from "react-bootstrap";
import { LinkContainer } from "react-router-bootstrap";

import Routes from "./Routes";


class App extends Component {
  constructor(props){
    super(props);
    this.state={
      username:'',
      password:'',
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

  render() {

    const childProps = {
      userHasAuthenticated: this.userHasAuthenticated,
      username: this.username,
      password: this.password
    };
    return (

      <div className="App">
        <Navbar fluid collapseOnSelect>
          <Navbar.Header>
            <Nav pullLeft>
              <LinkContainer to="/">
                <NavItem>Home</NavItem>
              </LinkContainer>
            </Nav>
            <Navbar.Toggle />
          </Navbar.Header>
          <Navbar.Collapse>
          <Nav pullRight>
            {this.state.isAuthenticated ? 
              <Fragment>
                <LinkContainer to="/">
                  <NavItem onClick={this.handleLogout}>Logout</NavItem>
                </LinkContainer>
                <LinkContainer to="/game">
                  <NavItem>Game</NavItem>
                  </LinkContainer>
              </Fragment> : 
              <Fragment>
                <LinkContainer to="/register">
                <NavItem>Register</NavItem>
                </LinkContainer>
                <LinkContainer to="/login">
                <NavItem Component={this.userHasAuthenticated}>Login</NavItem>
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
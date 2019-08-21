import React, { Component } from 'react';
import './App.css';
import { Navbar, Nav, NavItem} from "react-bootstrap";
import { LinkContainer } from "react-router-bootstrap";
import { Link } from 'react-router-dom';



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
            </Nav>
            <Navbar.Toggle />
          </Navbar.Header>
          <Navbar.Collapse>
          <Nav pullRight>
            <LinkContainer to="/register">
            <NavItem >Register</NavItem>
            </LinkContainer>
            <LinkContainer to="/login">
            <NavItem>Login</NavItem>
            </LinkContainer>
          </Nav>
        </Navbar.Collapse>
        </Navbar>
        <Routes childProps= {childProps}/>     
      </div>
    );
  }
}

export default App;
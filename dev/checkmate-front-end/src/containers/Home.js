import React, { Component, Fragment } from "react";
import "./Home.css"
import {NavItem} from "react-bootstrap";
import { LinkContainer } from "react-router-bootstrap";

export default class Home extends Component {
  
 
  render() {
      
    return (
        <div className="Home">
          <div className="lander">
            <h1>CheckMate</h1>
            <p>A simple Checkers app</p>
          </div>
            <div className="centerMenu">  
              {window.localStorage.getItem("username") ?
                <Fragment>
                  <div class="col-md-3 col-sm-6 hero-feature">
                    <div class="thumbnail">
                    <LinkContainer to="/game"> 
                      <NavItem>
                        <img src="https://icon-library.net/images/multiple-people-icon/multiple-people-icon-10.jpg" alt="" className="publicImage"/>
                        <div class="caption">
                            <h3>Public Game</h3>
                            <p>Jump on queue with random players!</p>
                        </div>
                      </NavItem>
                      </LinkContainer>
                    </div>
                  </div>

                
                <div class="col-md-3 col-sm-6 hero-feature">
                  <div class="thumbnail">
                  <LinkContainer to="/game"> 
                    <NavItem>
                      <img src="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQYHVOKAjjrBHSCPiEqGoscxboPP6s_fGK5NFUk6JZJJ5LcAXzE" alt="" className="privateImage"/>
                      <div class="caption">
                          <h3>Private Game</h3>
                          <p>Share your unique link with a friend and play!</p>
                      </div>
                    </NavItem>
                  </LinkContainer>
                  </div>
                </div>
                </Fragment> :
                <div></div>
              }
            </div>
        </div>
        
    );
  }
}
import React, { Component } from "react";
import "./Home.css"

export default class Home extends Component {
  render() {
      
    return (
        <div className="Home">
        <div className="lander">
          <h1>Home Page</h1>
          <p>A simple Checkers app</p>
        </div>
      
          
        <div class="col-md-3 col-sm-6 hero-feature">
        <div class="thumbnail">
            <img src="https://icon-library.net/images/multiple-people-icon/multiple-people-icon-10.jpg" alt=""/>
            <div class="caption">
                <h3>Lobby</h3>
                <p>Jump on queue with random players!.</p>
            </div>
        </div>
        </div>

        <div class="col-md-3 col-sm-6 hero-feature">
        <div class="thumbnail">
            <img src="https://www.nicepng.com/png/detail/80-802325_could-you-recommend-some-fun-2-player-tabletop.png" alt=""/>
            <div class="caption">
                <h3>Private Game</h3>
                <p>Share your unique link with a friend and play!</p>
            </div>
        </div>
        </div>
        </div>
        
    );
  }
}
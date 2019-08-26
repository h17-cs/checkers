
import React, { Component } from 'react';
import './About.css'

class About extends Component {
    render() {
      
        return (
            <div className="aboutDiv">
                <h1>We Are CheckMate!</h1>
                <br/>
                
                <h4>CS451-001</h4>
                <h4>Group 2</h4>
                
                <h2 className="title"> Team Members: </h2>
                <div className="members">
                    <h5>Idan Hershcovich</h5>
                    <h5>Charles Hill</h5>
                    <h5>Brendan McFadden</h5>
                    <h5>Nicholas Wegfahrt</h5>
                </div>
                <br/>
                <div>
                    <p> We're a group of soon to be seniors, who have created this checkers app as a term long project for our CS451 class. </p>
                </div>

                
            </div>
        )
    }
}

export default About;
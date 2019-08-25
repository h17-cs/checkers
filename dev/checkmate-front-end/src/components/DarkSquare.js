
import '../Game.css'
import React, { Component } from 'react';
import LightPiece from './LightPiece'

class DarkSquare extends Component {
    render() {
        return(
            <div className ="darkSquare">
                <LightPiece/>
            </div>
        );
    }
}

export default DarkSquare;
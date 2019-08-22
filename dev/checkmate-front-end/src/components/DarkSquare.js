
import '../Game.css'
import React, { Component } from 'react';
import LightPiece from './LightPiece'
import DarkPiece from './DarkPiece'

class DarkSquare extends Component {
    
    decideOccupation(){
        if(this.props.pieceInfo != null) {
            if(this.props.pieceInfo[0] === 0){
                return <LightPiece/>
            }
            else if(this.props.pieceInfo[0] === 1){
                return <DarkPiece/>
            }
        }
    }
    
    render() {
        return(
            <div className ="darkSquare">
                {this.decideOccupation()}
            </div>
        );
    }
}

export default DarkSquare;
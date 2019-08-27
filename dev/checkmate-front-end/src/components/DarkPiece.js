import React, { Component } from 'react';
import piece from "../imgs/man_dark.png";
import king from "../imgs/king_dark.png";
import "../Game.css"

class DarkPiece extends Component {
    
    pieceType(){
        if(this.props.pieceType === 0)
        {
            return <img src={piece} className="pieceImg"></img>
        }
        else {
            return <img src={king} className="pieceImg"></img>
        }
    }
    
    render() {
        return(
            this.pieceType()
        );
    }
}

export default DarkPiece;
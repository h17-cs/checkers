import '../Game.css'
import React, { Component } from 'react';
import LightPiece from './LightPiece';
import DarkPiece from './DarkPiece';

class GameTrackBox extends Component {

    renderLightPlayer(){
        if (this.props.gameTrackBox.currentTurn == 0){
            return <LightPiece/>
       }
    }

    renderDarkPlayer(){
        if (this.props.gameTrackBox.currentTurn == 1){
            return <DarkPiece/>
       }
    }

    render() {
        return(
            <div className = "gameTrackBox">
            <div>
                <div className = "pieceNameSep">
                    {this.renderLightPlayer()}
                    <h1 className = "nameSpacing"> {this.props.gameTrackBox.playerOne} </h1>
                </div>
            </div>
            <div>
                <div className = "pieceNameSep">
                    {this.renderDarkPlayer()}
                    <h1 className = "nameSpacing"> {this.props.gameTrackBox.playerTwo} </h1>
                </div>
            </div>
            </div>
        );
    }
}

export default GameTrackBox;
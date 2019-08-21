import '../Game.css'
import Board from "./BoardComponent";
import GameInfo from "./GameInfo";
import React, { Component } from 'react';

class Game extends Component {
    render() {
        return(
            <div>
                <div className="holdingSpacer">
                    <Board/>
                    <GameInfo/>
                </div>
            </div>
        );
    }
}

export default Game;
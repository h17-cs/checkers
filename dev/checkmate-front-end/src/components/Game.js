import '../Game.css'
import Board from "./BoardComponent";
import GameInfo from "./GameInfo";
import React, { Component } from 'react';

class Game extends Component {
   constructor(props){
       super(props);

       this.state = {
           gameTimer:"2:00",
           gameInfo:{
               gameTrackBox: {
                    playerOne: "Idan",
                    playerTwo: "Nick",
                    currentTurn: 0
               }  
           }
       }
   }
   
    render() {
        return(
            <div className="topMargin">
                <h1>{this.state.gameTimer}</h1>
                <div className="holdingSpacer">
                    <Board/>
                    <div>
                        <GameInfo gameInfo = {this.state.gameInfo}/>
                        <div className="formatButtons">
                            <input type ="button" value= "Forfeit" className="actionButton"/>
                            <input type ="button" value= "Save Game" className="actionButton"/>
                            <input type ="button" value= "Main Menu" className="actionButton"/>
                            
                        </div>
                    </div>
                </div>
            </div>
        );
    }
}

/*

*/

export default Game;
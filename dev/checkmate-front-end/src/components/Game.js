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
           },
           gameState: {
            "zero": [0 , 0],
            "one": [0 , 0],
            "two": [0 , 0],
            "three": [0 , 0],
            "four": [0 , 0],
            "five": [0 , 0],
            "six": [0 , 0],
            "seven": [0 , 0],
            "eight": [0 , 0],
            "nine": [0 , 0],
            "ten": [0 , 0],
            "eleven": [0 , 0],
            "twelve": null,
            "thirteen": null,
            "fourteen":  null,
            "fifteen":  null,
            "sixteen":  null,
            "seventeen":  null,
            "eighteen":  null,
            "nineteen":  null,
            "twent": [1 , 0],
            "twentOne": [1 , 0],
            "twentTwo": [1 , 0],
            "twentThree": [1 , 0],
            "twentFour": [1 , 0],
            "twentFive": [1 , 0],
            "twentSix": [1 , 0],
            "twentSeven": [1 , 0],
            "twentEight": [1 , 0],
            "twentNine": [1 , 0],
            "thirt": [1, 0],
            "thirtOne": [1 , 0],
            "thirtTwo": [1 , 0],
        }
       }
   }
   
    render() {
        return(
            <div className="topMargin">
                <h1>{this.state.gameTimer}</h1>
                <div className="holdingSpacer">
                    <Board gameState = {this.state.gameState}/>
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
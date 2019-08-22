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
               },
               gameState: {
                   "1": (0 , 0),
                   "2": (0 , 0),
                   "3": (0 , 0),
                   "4": (0 , 0),
                   "5": (0 , 0),
                   "6": (0 , 0),
                   "7": (0 , 0),
                   "8": (0 , 0),
                   "9": (0 , 0),
                   "10": (0 , 0),
                   "11": (0 , 0),
                   "12": (0 , 0),
                   "13": (0 , 0),
                   "14": (0 , 0),
                   "15": (0 , 0),
                   "16": (0 , 0),
                   "17": (0 , 0),
                   "18": (0 , 0),
                   "19": (0 , 0),
                   "20": (0 , 0),
                   "21": (0 , 0),
                   "22": (0 , 0),
                   "23": (0 , 0),
                   "24": (0 , 0),
                   "25": (0 , 0),
                   "26": (0 , 0),
                   "27": (0 , 0),
                   "28": (0 , 0),
                   "29": (0 , 0),
                   "30": (0 , 0),
                   "31": (0 , 0),
                   "32": (0 , 0),
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
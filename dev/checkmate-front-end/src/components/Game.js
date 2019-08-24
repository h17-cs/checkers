import '../Game.css'
import Board from "./BoardComponent";
import GameInfo from "./GameInfo";
import React, { Component } from 'react';

class Game extends Component {
   constructor(props){
       super(props);

    this.setMoveOrder = this.setMoveOrder.bind(this)

       this.state = {
           timestamp:1566344113915,
           clock_expire:1566344113915,
           gameTimer:"2:00",
           gameInfo:{
                playerOne: "Idan",
                playerTwo: "Nick",
            },
           screenOwner: 0,
           playerTurn: 0,
           valid_moves: new Array(),
           moveOrder: new Array(),
           possible_moves: {
            "zero": null,
            "one": null,
            "two": null,
            "three": null,
            "four": null,
            "five": null,
            "six": null,
            "seven": null,
            "eight": [12, 13],
            "nine": [13,14],
            "ten": [14, 15],
            "eleven": [15],
            "twelve": null,
            "thirteen": null,
            "fourteen":  null,
            "fifteen":  null,
            "sixteen":  null,
            "seventeen":  null,
            "eighteen":  null,
            "nineteen":  null,
            "twent": [16],
            "twentOne": [16, 17],
            "twentTwo": [17, 18],
            "twentThree": [18, 19],
            "twentFour": null,
            "twentFive": null,
            "twentSix": null,
            "twentSeven": null,
            "twentEight": null,
            "twentNine": null,
            "thirt": null,
            "thirtOne": null,
            "thirtTwo": null,
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

//    gameTimer:"2:00",
//            gameInfo:{
//                 playerOne: "Idan",
//                 playerTwo: "Nick",
//             },
//            playerTurn: 0,
//            moveOrder: [],
//            gameState: {
   
   setMoveOrder( newData ){
       this.setState({moveOrder: newData[0],
            valid_moves: newData[1]
        })
       
   }

    render() {
        return(
            <div className="topMargin">
                <h1>{this.state.gameTimer}</h1>
                <div className="holdingSpacer">
                    <Board gameState = {[this.state.gameState, this.state.moveOrder, this.state.possible_moves, this.state.valid_moves, this.state.screenOwner]}  setMoveOrder = {this.setMoveOrder}/>
                    <div>
                        <GameInfo gameInfo = {[this.state.gameInfo, this.state.playerTurn]}/>
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
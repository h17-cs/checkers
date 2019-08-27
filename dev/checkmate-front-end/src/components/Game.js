import Board from "./BoardComponent";
import GameInfo from "./GameInfo";
import React, { Component } from 'react';
import MuiThemeProvider from 'material-ui/styles/MuiThemeProvider';


class Game extends Component {
   constructor(props){
       super(props);

    this.setMoveOrder = this.setMoveOrder.bind(this)
    this.forfeit = this.forfeit.bind(this)
    this.timer = this.timer.bind(this)
    //this.componentDidMount = this.componentDidMount(this)
       this.state = {
           timestamp:1566344113915,
           clock_expire:1566344113915,
           floatTimer: 60,
           gameInfo:{
                playerOne: window.localStorage.getItem("username"),
                playerTwo: "Nick",
            },
           screenOwner: 0,
           playerTurn: 0,
           valid_moves: new Array(),
           moveOrder: new Array(),
           isGameOver:0,
           didForfeit:0,
           timeExpire:0,
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

   componentDidMount(){
       this.interval = setInterval(() => this.timer(), 1000)
   }

   componentWillMount(){
       clearInterval(this.interval);
   }
   
   timer(){
        this.setState({floatTimer: (this.state.floatTimer - 1)})
        if(this.state.floatTimer === 0){
            this.setState({timeExpire: 1})
        }
   }
   setMoveOrder( newData ){
       this.setState({moveOrder: newData[0],
            valid_moves: newData[1]
        })
   }

   forfeit(){
       this.setState({isGameOver: 1})
   }

   formatGameTime(){
       var totalSecs= this.state.floatTimer
       if(this.state.floatTimer > 0) {
            var minutes = Math.floor( totalSecs / 60)
            var seconds = totalSecs - (minutes * 60)
            var strSeconds;
            if(seconds < 10){
                strSeconds = "0"+ seconds.toString()
            }
            else {
                 strSeconds = seconds.toString()
             }
            return minutes.toString().concat(":", strSeconds)
        }
        else{
            return "0:00"
        }

   }

    render() {
        return(
            <MuiThemeProvider>
            <div className = "gameViewColor">
                <div className="topMargin">
                    <div>
                    <h1>{this.formatGameTime()}</h1>
                    </div>
                    <div className="gameViewCont">
                        <div>
                        <Board gameState = {[this.state.gameState, this.state.moveOrder, this.state.possible_moves, this.state.valid_moves, this.state.screenOwner]}  setMoveOrder = {this.setMoveOrder}/>
                        </div>
                        <div className="sidebar">

                            <div>
                            <GameInfo gameInfo = {[this.state.gameInfo, this.state.playerTurn]}/>
                            </div>
                            <div>
                            
                                <input type="button" value= "Forfeit" id="overrideButtons" onClick={this.forfeit}/>
                                
                                <input type ="button" value= "Save Game" id="overrideButtons"/>
                                
                                <input type ="button" value= "Main Menu" id="overrideButtons"/>
                                
                                
                            </div>
                        </div>
                    </div>
                </div>
            </div>
            </MuiThemeProvider>
        );
    }
}


export default Game;
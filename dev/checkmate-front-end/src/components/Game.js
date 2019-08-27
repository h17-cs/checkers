import Board from "./BoardComponent";
import GameInfo from "./GameInfo";
import React, { Component } from 'react';
import MuiThemeProvider from 'material-ui/styles/MuiThemeProvider';

const URL = 'ws://localhost:3030'

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
            "sqr_1": null,
            "sqr_2": null,
            "sqr_3": null,
            "sqr_4": null,
            "sqr_5": null,
            "sqr_6": null,
            "sqr_7": null,
            "sqr_8": null,
            "sqr_9": [12, 13],
            "sqr_10": [13,14],
            "sqr_11": [14, 15],
            "sqr_12": [15],
            "sqr_13": null,
            "sqr_14": null,
            "sqr_15":  null,
            "sqr_16":  null,
            "sqr_17":  null,
            "sqr_18":  null,
            "sqr_19":  null,
            "sqr_20":  null,
            "sqr_21": [16],
            "sqr_22": [16, 17],
            "sqr_23": [17, 18],
            "sqr_24": [18, 19],
            "sqr_25": null,
            "sqr_26": null,
            "sqr_27": null,
            "sqr_28": null,
            "sqr_29": null,
            "sqr_30": null,
            "sqr_31": null,
            "sqr_32": null
           },
           gameState: {
            "sqr_1": [0 , 0],
            "sqr_2": [0 , 0],
            "sqr_3": [0 , 0],
            "sqr_4": [0 , 0],
            "sqr_5": [0 , 0],
            "sqr_6": [0 , 0],
            "sqr_7": [0 , 0],
            "sqr_8": [0 , 0],
            "sqr_9": [0 , 0],
            "sqr_10": [0 , 0],
            "sqr_11": [0 , 0],
            "sqr_12": [0 , 0],
            "sqr_13": null,
            "sqr_14": null,
            "sqr_15":  null,
            "sqr_16":  null,
            "sqr_17":  null,
            "sqr_18":  null,
            "sqr_19":  null,
            "sqr_20":  null,
            "sqr_21": [1 , 0],
            "sqr_22": [1 , 0],
            "sqr_23": [1 , 0],
            "sqr_24": [1 , 0],
            "sqr_25": [1 , 0],
            "sqr_26": [1 , 0],
            "sqr_27": [1 , 0],
            "sqr_28": [1 , 0],
            "sqr_29": [1 , 0],
            "sqr_30": [1 , 0],
            "sqr_31": [1, 0],
            "sqr_32": [1 , 0]
        }
       }
   }

   ws = new WebSocket(URL)

   componentDidMount(){
       this.interval = setInterval(() => this.timer(), 1000)

       this.ws.onopen = () => {
        // on connecting, do nothing but log it to the console
        console.log('connected')
      }
  
      this.ws.onmessage = evt => {
        // on receiving a message, add it to the list of messages
        const message = JSON.parse(evt.data)
        this.addMessage(message)
      }
  
      this.ws.onclose = () => {
        console.log('disconnected')
        // automatically try to reconnect on connection loss
        this.setState({
          ws: new WebSocket(URL),
        })
      }
   }

   componentWillMount(){
       clearInterval(this.interval);
   }

   addMessage = message =>
    this.setState(state => ({ messages: [message, ...state.messages] }))

    submitMessage = messageString => {
        // on submitting the ChatInput form, send the message, add it to the list and reset the input
        // const message = { 
        //     name: this.state.name, 
        //     message: messageString 
        // }
        const message = { 
            turn: this.state.playerTurn,
            isGameOver:this.state.timeExpire,
            didForfeit:this.state.didForfeit,
            timeExpire:this.state.didForfeit,
            moveMade: this.state.moveOrder
        }
        this.ws.send(JSON.stringify(message))
        this.addMessage(message)
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
import '../Game.css'
import React, { Component } from 'react';
import GameTrackBox from './GameTrackBox';
// import ChatBox from './ChatBox'
import Chat from './Chat/Chat'
import BoardComponent from './BoardComponent.css'



class GameInfo extends Component {
    render() {
        return(
            <div className = "gameInfo">
                <GameTrackBox gameTrackBox = {this.props.gameInfo}/>
                <hr className="hrLine"/>
                <Chat/>
                {/* <div className="formatButtons"> */}
                    <div class="btn-group" role="group">
                        <input type ="button" value= "Forfeit" className="actionButton" onClick={this.forfeit}/>
                        <input type ="button" value= "Save Game" className="actionButton"/>
                        <input type ="button" value= "Main Menu" className="actionButton"/>         
                    </div>
                {/* </div> */}
            </div>
        );
    }
}

export default GameInfo;
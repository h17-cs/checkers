import '../Game.css'
import React, { Component } from 'react';
import GameTrackBox from './GameTrackBox';
// import ChatBox from './ChatBox'
import Chat from './Chat/Chat'



class GameInfo extends Component {
    render() {
        return(
            <div className = "gameInfo">
                <GameTrackBox gameTrackBox = {this.props.gameInfo.gameTrackBox}/>
                <hr className="hrLine"/>
                <Chat/>
               
            </div>
        );
    }
}

export default GameInfo;
import '../Game.css'
import React, { Component } from 'react';
import GameTrackBox from './GameTrackBox';
// import ChatBox from './ChatBox'
import Chat from './Chat/Chat'
import BoardComponent from './BoardComponent.css'



class GameInfo extends Component {
    render() {
        return(
            <div className = "containter">
                <GameTrackBox gameTrackBox = {this.props.gameInfo.gameTrackBox}/>
                <hr className="hrLine"/>
                <Chat/>
               
            </div>
        );
    }
}

export default GameInfo;
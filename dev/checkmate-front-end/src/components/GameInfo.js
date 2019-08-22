import '../Game.css'
import React, { Component } from 'react';
import GameTrackBox from './GameTrackBox';
import ChatBox from './ChatBox'

class GameInfo extends Component {
    render() {
        return(
            <div className = "gameInfo">
                <GameTrackBox gameTrackBox = {this.props.gameInfo.gameTrackBox}/>
                <hr className="hrLine"/>
                <ChatBox/>
                <div>
                    <div className="vertSpacer">
                        <input type ="text" placeholder="Message Here"  />
                        <input type ="button" value= "Send" className="sendButton"/>
                    </div>
                </div>
            </div>
        );
    }
}

export default GameInfo;
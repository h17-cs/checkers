import '../Game.css'
import React, { Component } from 'react';
import GameTrackBox from './GameTrackBox';
import ChatBox from './ChatBox'
import { w3cwebsocket as W3CWebSocket } from "websocket";

const client = new W3CWebSocket('wss://echo.websocket.org/');

class GameInfo extends Component {
    componentWillMount() {
        client.onopen = () => {
          console.log('WebSocket Client Connected');
        };
        client.onmessage = (message) => {
          console.log(message);
        };
      }

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
import React, { Component } from 'react';
import GameTrackBox from './GameTrackBox';
// import ChatBox from './ChatBox'
import Chat from './Chat/Chat'
import BoardComponent from './BoardComponent.css'



class GameInfo extends Component {
    render() {
        return(
            <div>
                <div>
                <GameTrackBox gameTrackBox = {this.props.gameInfo}/>
                </div>
                <hr className="hrLine"/>
                <Chat names= {this.props.gameInfo}/>
               
            </div>
        );
    }
}

export default GameInfo;
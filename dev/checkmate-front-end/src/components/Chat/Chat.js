import React, { Component } from 'react'
import ChatInput from './ChatInput'
import '../../Game.css'
import ChatMessage from './ChatMessage'



//address to test on a local server for testing.
const URL = 'ws://localhost:3030'

class Chat extends Component {
  state = {
    name: window.localStorage.getItem("username"),
    messages: [],
  }
  ws = new WebSocket(URL)
  username = window.localStorage.getItem("username");

  componentDidMount() {
    this.ws.onopen = () => {
      // on connecting, do nothing but log it to the console
      console.log('connected')
    }
    

    this.ws.onmessage = (evt) => {
      // on receiving a message, add it to the list of messages
      console.log(evt)
      const message = JSON.parse(evt.data)
      this.addMessage(message.body)
      return false;
    }

    this.ws.onclose = () => {
      console.log('disconnected')
      // automatically try to reconnect on connection loss
      this.setState({
        ws: new WebSocket(URL),
      })
    }
  }

  addMessage = message =>
    this.setState(state => ({ messages: [message, ...state.messages] }))

  submitMessage = messageString => {
    // on submitting the ChatInput form, send the message, add it to the list and reset the input
    const message = { name: this.state.name, message: messageString }
    this.ws.send(JSON.stringify({
      "message_type": 0,
      "body" : 
      {
        "name" : this.username,
        "message" : message.message,
      }
    }))
    // this.ws.send(JSON.stringify(message))
    this.addMessage(message)
  }

  render() {
    return (
      <div>        
        <div className="chatBox">
            {this.state.messages.map((message, index) =>
            <ChatMessage
                key={index}
                message={message.message}
                name={message.name}
            />,
            )}
        </div>
        <ChatInput
          ws={this.ws}
          onSubmitMessage={messageString => this.submitMessage(messageString)}
        />
      </div>
    )
  }
}

// constructor(props) {
//   super(props)

//   this.state = {
//     board: Array(6).fill(0).map(x => Array(8).fill('white')),
//     socket: openSocket('http://localhost:1337'),
//     message: 'Waiting for another player...',
//     yourTurn: false
//   }
//   let self = this
//     this.state.socket.on('color', color => {
//       this.setState(...self.state, {color: color})
//     });
//     this.state.socket.on('turn', player => {
//       if (player === this.state.color) {
//         this.setState(...self.state, 
//                       {message: "You're up. What's your move?", 
//                        yourTurn: true})
//       } else {
//         this.setState(...self.state, 
//                       {message: player + ' is thinking...', 
//                        yourTurn: false})
//       }
//     });
// }
 
//   render() {
//     return (
//       <div>
//         {/* <label htmlFor="name">
//           Name:&nbsp;
//           <TextField
//             type="text"
//             id={'name'}
//             placeholder={'Enter your name...'}
//             value={this.state.name}
//             onChange={e => this.setState({ name: e.target.value })}
//           />
//         </label> */}
        
//         <div className="chatBox">
//             {/* {this.state.messages.map((message, index) => */}
//             <ChatMessage
//                   color={this.state.color} 
//                   message={this.state.message} 
//                 // key={index}
//                 // message={message.message}
//                 // name={this.props.names[0].playerOne}


//             />,
//             )}
//         </div>
//         {/* <ChatInput
//           ws={this.ws}
//           onSubmitMessage={messageString => this.submitMessage(messageString)}
//         /> */}
//       </div>
//     )
//   }

// }


export default Chat
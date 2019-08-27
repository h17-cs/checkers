import React, { Component } from 'react'
import PropTypes from 'prop-types'
import '../../Game.css'
import { TextField } from 'material-ui';

class ChatInput extends Component {
  static propTypes = {
    onSubmitMessage: PropTypes.func.isRequired,
  }
  state = {
    message: '',
  }

  render() {
    return (
      <form
        action="."
        onSubmit={e => {
          e.preventDefault()
          this.props.onSubmitMessage(this.state.message)
          this.setState({ message: '' })
        }}
      >
        <div id="msgInputs">
         
            <TextField
              type="text"
              placeholder={'Enter message...'}
              value={this.state.message}
              onChange={e => this.setState({ message: e.target.value })}
              className="msgTextBox"
            />
         
            <input type="submit" value={'Send'} id="overrideSendButton" />
        </div>
       
      </form>
    )
  }
}

export default ChatInput
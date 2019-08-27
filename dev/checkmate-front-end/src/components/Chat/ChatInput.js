import React, { Component } from 'react'
import PropTypes from 'prop-types'
import '../../Game.css'

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
        <TextField
          type="text"
          placeholder={'Enter message...'}
          value={this.state.message}
          onChange={e => this.setState({ message: e.target.value })}
          className="msgTextBox"
        />
        <input type="submit" value={'Send'} />
      </form>
    )
  }
}

export default ChatInput
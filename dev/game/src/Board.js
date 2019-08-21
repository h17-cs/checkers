import React from 'react';
import LightSquare from './components/LightSquare';
import DarkSquare from './components/DarkSquare';
import LightPiece from './components/LightPiece';
import DarkPiece from './components/DarkPiece';

class Board extends React.Component {
  onClick(id) {
    if (this.isActive(id)) {
      this.props.moves.clickCell(id);
      this.props.events.endTurn();
    }
  }

  isActive(id) {
    if (!this.props.isActive) return false;
    if (this.props.G.cells[id] !== null) return false;
    return true;
  }

  render() {
    let winner = '';
    if (this.props.ctx.gameover) {
      winner =
        this.props.ctx.gameover.winner !== undefined ? (
          <div id="winner">Winner: {this.props.ctx.gameover.winner}</div>
        ) : (
          <div id="winner">Draw!</div>
        );
    }

    const cellStyle = {
      border: '1px solid #555',
      width: '50px',
      height: '50px',
      lineHeight: '50px',
      textAlign: 'center',
    };

    let tbody = [];
    for(let i = 0; i<8; i++){
      let cells = []
      for (let j = 0; j< 8; j++){
          if( i % 2 === 0){
              if(j%2 === 0){
              cells.push(<td> {<LightSquare> </LightSquare>} </td>);
              }
              else{
              cells.push(<td> {<DarkSquare> </DarkSquare>} </td>);
              }
          }
          else{
              if(j%2 === 0){
                  cells.push(<td> {<DarkSquare/>} </td>);
              }
              else{
                  cells.push(<td> {<LightSquare/>} </td>);
              }
          }
      }
      tbody.push(<tr> {cells} </tr>)
  }


    return (
      <div>
        <table id="board">
          <tbody>{tbody}</tbody>
        </table>
        {winner}
      </div>
    );
  }
}

export default Board
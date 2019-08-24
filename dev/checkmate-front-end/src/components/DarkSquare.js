
import '../Game.css'
import React, { Component } from 'react';
import LightPiece from './LightPiece'
import DarkPiece from './DarkPiece'


class DarkSquare extends Component {

    constructor(props){
        super(props);

        this.state = {
            clicked: false,
            squareId: this.props.squareId,
            pieceInfo: this.props.pieceInfo,
            valid_moves: this.props.valid_moves
        }
    }
    
    decideOccupation(){
        if(this.state.pieceInfo != null) {
            if(this.state.pieceInfo[0] === 0){
                return <LightPiece/>
            }
            else if(this.props.pieceInfo[0] === 1){
                return <DarkPiece/>
            }
        }
    }

    clickedSquare(e, pieceInfo, selectedSquares, possible_moves, valid_moves){
    
        let id =this.state.squareId
            if(pieceInfo != null && selectedSquares.length === 0) {
                console.log("First Piece Selected for moving");
                this.setState({clicked: true})
                return new Array( [id], possible_moves);
            }
            else if(pieceInfo === null && selectedSquares.length === 1){
                console.log("I get In");
                if(id === selectedSquares[0]){
                    console.log("Unselect First Square");
                    this.setState({clicked: false})
                    return new Array(new Array(), new Array())
                }
                else if ( valid_moves != null && valid_moves.includes(id)){
                    console.log("Attempt Second Square");
                    this.setState({clicked: true})
                    return new Array( new Array(selectedSquares[0], id), new Array());
                }
           }

           return new Array(selectedSquares, valid_moves)

    }
    
    render() {
        return(
            <div className = { (this.state.clicked ?  "highlightSquare" : "darkSquare" )} onClick = {(e) => {this.props.setMoveOrder(this.clickedSquare(e, this.props.pieceInfo, this.props.selectedSquares, this.props.possible_moves, this.props.valid_moves))}}>
                {this.decideOccupation()}
            </div>
        );
    }
}

export default DarkSquare;
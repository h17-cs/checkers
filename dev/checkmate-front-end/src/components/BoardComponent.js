import React, {Component} from 'react';
import LightSquare from './LightSquare';
import DarkSquare from './DarkSquare';
import '../App.css';
import './BoardComponent.css'
//import LightPiece from './LightPiece';
//import DarkPiece from './DarkPiece';

class BoardComponent extends Component {

    generateSquares(){
        let redSquares = [];
        redSquares.push(<DarkSquare key = {'0'} squareId = {0} pieceInfo={this.props.gameState[0].sqr_1} selectedSquares = {this.props.gameState[1]} possible_moves={this.props.gameState[2].zero} valid_moves={this.props.gameState[3]} screenOwner={this.props.gameState[4]} setMoveOrder = {this.props.setMoveOrder}/>);
        redSquares.push(<DarkSquare key = {'1'} squareId = {1} pieceInfo={this.props.gameState[0].sqr_2} selectedSquares = {this.props.gameState[1]} possible_moves={this.props.gameState[2].one} valid_moves={this.props.gameState[3]} screenOwner={this.props.gameState[4]} setMoveOrder = {this.props.setMoveOrder}/>);
        redSquares.push(<DarkSquare key = {'2'} squareId = {2} pieceInfo={this.props.gameState[0].sqr_3} selectedSquares = {this.props.gameState[1]} possible_moves={this.props.gameState[2].two} valid_moves={this.props.gameState[3]}  screenOwner={this.props.gameState[4]} setMoveOrder = {this.props.setMoveOrder}/>);
        redSquares.push(<DarkSquare key = {'3'} squareId = {3} pieceInfo={this.props.gameState[0].sqr_4} selectedSquares = {this.props.gameState[1]} possible_moves={this.props.gameState[2].three} valid_moves={this.props.gameState[3]} screenOwner={this.props.gameState[4]} setMoveOrder = {this.props.setMoveOrder}/>);
        redSquares.push(<DarkSquare key = {'4'} squareId = {4} pieceInfo={this.props.gameState[0].sqr_5} selectedSquares = {this.props.gameState[1]} possible_moves={this.props.gameState[2].four} valid_moves={this.props.gameState[3]} screenOwner={this.props.gameState[4]} setMoveOrder = {this.props.setMoveOrder}/>);
        redSquares.push(<DarkSquare key = {'5'} squareId = {5} pieceInfo={this.props.gameState[0].sqr_6} selectedSquares = {this.props.gameState[1]}  possible_moves={this.props.gameState[2].five} valid_moves={this.props.gameState[3]} screenOwner={this.props.gameState[4]} setMoveOrder = {this.props.setMoveOrder}/> );
        redSquares.push(<DarkSquare key = {'6'} squareId = {6} pieceInfo={this.props.gameState[0].sqr_7} selectedSquares = {this.props.gameState[1]} possible_moves={this.props.gameState[2].six} valid_moves={this.props.gameState[3]} screenOwner={this.props.gameState[4]} setMoveOrder = {this.props.setMoveOrder}/> );
        redSquares.push(<DarkSquare key = {'7'} squareId = {7} pieceInfo={this.props.gameState[0].sqr_8} selectedSquares = {this.props.gameState[1]} possible_moves={this.props.gameState[2].seven} valid_moves={this.props.gameState[3]} screenOwner={this.props.gameState[4]} setMoveOrder = {this.props.setMoveOrder}/>);
        redSquares.push(<DarkSquare key = {'8'} squareId = {8} pieceInfo={this.props.gameState[0].sqr_9} selectedSquares = {this.props.gameState[1]} possible_moves={this.props.gameState[2].eight} valid_moves={this.props.gameState[3]} screenOwner={this.props.gameState[4]} setMoveOrder = {this.props.setMoveOrder}/> );
        redSquares.push(<DarkSquare key = {'9'} squareId = {9} pieceInfo={this.props.gameState[0].sqr_10} selectedSquares = {this.props.gameState[1]} possible_moves={this.props.gameState[2].nine} valid_moves={this.props.gameState[3]} screenOwner={this.props.gameState[4]} screenOwner={this.props.gameState[4]} setMoveOrder = {this.props.setMoveOrder}/>);
        redSquares.push(<DarkSquare key = {'10'} squareId = {10} pieceInfo={this.props.gameState[0].sqr_11} selectedSquares = {this.props.gameState[1]} possible_moves={this.props.gameState[2].ten} valid_moves={this.props.gameState[3]} screenOwner={this.props.gameState[4]} setMoveOrder = {this.props.setMoveOrder}/>);
        redSquares.push(<DarkSquare key = {'11'} squareId = {11} pieceInfo={this.props.gameState[0].sqr_12} selectedSquares = {this.props.gameState[1]} possible_moves={this.props.gameState[2].eleven} valid_moves={this.props.gameState[3]} screenOwner={this.props.gameState[4]} setMoveOrder = {this.props.setMoveOrder}/>);
        redSquares.push(<DarkSquare key = {'12'} squareId = {12} pieceInfo={this.props.gameState[0].sqr_13} selectedSquares = {this.props.gameState[1]} possible_moves={this.props.gameState[2].twelve} valid_moves={this.props.gameState[3]} screenOwner={this.props.gameState[4]} setMoveOrder = {this.props.setMoveOrder}/>);
        redSquares.push(<DarkSquare key = {'13'} squareId = {13} pieceInfo={this.props.gameState[0].sqr_14} selectedSquares = {this.props.gameState[1]} possible_moves={this.props.gameState[2].thirteen} valid_moves={this.props.gameState[3]} screenOwner={this.props.gameState[4]} setMoveOrder = {this.props.setMoveOrder}/> );
        redSquares.push(<DarkSquare key = {'14'} squareId = {14} pieceInfo={this.props.gameState[0].sqr_15} selectedSquares = {this.props.gameState[1]} possible_moves={this.props.gameState[2].fourteen} valid_moves={this.props.gameState[3]} screenOwner={this.props.gameState[4]} setMoveOrder = {this.props.setMoveOrder}/>);
        redSquares.push(<DarkSquare key = {'15'} squareId = {15} pieceInfo={this.props.gameState[0].sqr_16} selectedSquares = {this.props.gameState[1]} possible_moves={this.props.gameState[2].fifteen} valid_moves={this.props.gameState[3]} screenOwner={this.props.gameState[4]} setMoveOrder = {this.props.setMoveOrder}/>);
        redSquares.push(<DarkSquare key = {'16'} squareId = {16} pieceInfo={this.props.gameState[0].sqr_17} selectedSquares = {this.props.gameState[1]} possible_moves={this.props.gameState[2].sixteen} valid_moves={this.props.gameState[3]} screenOwner={this.props.gameState[4]} setMoveOrder = {this.props.setMoveOrder}/>);
        redSquares.push(<DarkSquare key = {'17'} squareId = {17} pieceInfo={this.props.gameState[0].sqr_18} selectedSquares = {this.props.gameState[1]} possible_moves={this.props.gameState[2].seventeen} valid_moves={this.props.gameState[3]} screenOwner={this.props.gameState[4]} setMoveOrder = {this.props.setMoveOrder}/>);
        redSquares.push(<DarkSquare key = {'18'} squareId = {18} pieceInfo={this.props.gameState[0].sqr_19} selectedSquares = {this.props.gameState[1]} possible_moves={this.props.gameState[2].eighteen} valid_moves={this.props.gameState[3]} screenOwner={this.props.gameState[4]} setMoveOrder = {this.props.setMoveOrder}/>);
        redSquares.push(<DarkSquare key = {'19'} squareId = {19} pieceInfo={this.props.gameState[0].sqr_20} selectedSquares = {this.props.gameState[1]} possible_moves={this.props.gameState[2].nineteen} valid_moves={this.props.gameState[3]} screenOwner={this.props.gameState[4]} setMoveOrder = {this.props.setMoveOrder}/>);
        redSquares.push(<DarkSquare key = {'20'} squareId = {20} pieceInfo={this.props.gameState[0].sqr_21} selectedSquares = {this.props.gameState[1]} possible_moves={this.props.gameState[2].twent} valid_moves={this.props.gameState[3]} screenOwner={this.props.gameState[4]} setMoveOrder = {this.props.setMoveOrder}/>);
        redSquares.push(<DarkSquare key = {'21'} squareId = {21} pieceInfo={this.props.gameState[0].sqr_22} selectedSquares = {this.props.gameState[1]} possible_moves={this.props.gameState[2].twentOne} valid_moves={this.props.gameState[3]} screenOwner={this.props.gameState[4]} setMoveOrder = {this.props.setMoveOrder}/>);
        redSquares.push(<DarkSquare key = {'22'} squareId = {22} pieceInfo={this.props.gameState[0].sqr_23} selectedSquares = {this.props.gameState[1]} possible_moves={this.props.gameState[2].twentTwo} valid_moves={this.props.gameState[3]} screenOwner={this.props.gameState[4]} setMoveOrder = {this.props.setMoveOrder}/>);
        redSquares.push(<DarkSquare key = {'23'} squareId = {23} pieceInfo={this.props.gameState[0].sqr_24} selectedSquares = {this.props.gameState[1]} possible_moves={this.props.gameState[2].twentThree} valid_moves={this.props.gameState[3]} screenOwner={this.props.gameState[4]} setMoveOrder = {this.props.setMoveOrder}/>);
        redSquares.push(<DarkSquare key = {'24'} squareId = {24} pieceInfo={this.props.gameState[0].sqr_25} selectedSquares = {this.props.gameState[1]} possible_moves={this.props.gameState[2].twentFour} valid_moves={this.props.gameState[3]} screenOwner={this.props.gameState[4]} setMoveOrder = {this.props.setMoveOrder}/>);
        redSquares.push(<DarkSquare key = {'25'} squareId = {25} pieceInfo={this.props.gameState[0].sqr_26} selectedSquares = {this.props.gameState[1]} possible_moves={this.props.gameState[2].twentFive} valid_moves={this.props.gameState[3]} screenOwner={this.props.gameState[4]} setMoveOrder = {this.props.setMoveOrder}/>);
        redSquares.push(<DarkSquare key = {'26'} squareId = {26} pieceInfo={this.props.gameState[0].sqr_27} selectedSquares = {this.props.gameState[1]} possible_moves={this.props.gameState[2].twentSix} valid_moves={this.props.gameState[3]} screenOwner={this.props.gameState[4]} setMoveOrder = {this.props.setMoveOrder}/>);
        redSquares.push(<DarkSquare key = {'27'} squareId = {27} pieceInfo={this.props.gameState[0].sqr_28} selectedSquares = {this.props.gameState[1]} possible_moves={this.props.gameState[2].twentSeven} valid_moves={this.props.gameState[3]} screenOwner={this.props.gameState[4]} setMoveOrder = {this.props.setMoveOrder}/>);
        redSquares.push(<DarkSquare key = {'28'} squareId = {28} pieceInfo={this.props.gameState[0].sqr_29} selectedSquares = {this.props.gameState[1]} possible_moves={this.props.gameState[2].twentEight} valid_moves={this.props.gameState[3]}screenOwner={this.props.gameState[4]}  setMoveOrder = {this.props.setMoveOrder}/>);
        redSquares.push(<DarkSquare key = {'29'} squareId = {29} pieceInfo={this.props.gameState[0].sqr_30} selectedSquares = {this.props.gameState[1]} possible_moves={this.props.gameState[2].twentNine} valid_moves={this.props.gameState[3]} screenOwner={this.props.gameState[4]} setMoveOrder = {this.props.setMoveOrder}/> );
        redSquares.push(<DarkSquare key = {'30'} squareId = {30} pieceInfo={this.props.gameState[0].sqr_31} selectedSquares = {this.props.gameState[1]} possible_moves={this.props.gameState[2].thirt} valid_moves={this.props.gameState[3]} screenOwner={this.props.gameState[4]} setMoveOrder = {this.props.setMoveOrder}/>);
        redSquares.push(<DarkSquare key = {'31'} squareId = {31} pieceInfo={this.props.gameState[0].sqr_32} selectedSquares = {this.props.gameState[1]} possible_moves={this.props.gameState[2].thirtOne} valid_moves={this.props.gameState[3]} screenOwner={this.props.gameState[4]} setMoveOrder = {this.props.setMoveOrder}/>);
        return  redSquares;
    }

    render(){
        let tbody = [];
        let redsSpent = 0;
        let reds = this.generateSquares();

        for(let i = 0; i<8; i++){
            let cells = []
            for (let j = 0; j< 8; j++){
                if( i % 2 === 0){
                    if(j%2 === 0){
                    cells.push(<td key = { i.toString().concat('_', j.toString() ) } > {<LightSquare key = { i.toString().concat('_', j.toString() ) } />} </td>);
                    }
                    else{
                        cells.push(<td key = { redsSpent.toString()}> {reds[redsSpent]} </td>);
                        redsSpent++;
                    }
                }
                else{
                    if(j%2 === 0){
                        cells.push(<td key = { redsSpent.toString()}> {reds[redsSpent]} </td>);
                        redsSpent++;
                    }
                    else{
                        cells.push(<td key = { i.toString().concat('_', j.toString() ) }> {<LightSquare key = { i.toString().concat('_', j.toString() ) }/>} </td>);
                    }
                }
            }
            tbody.push(<tr> {cells} </tr>)
        }

        return(
            <div >
                <div className="woodBase">
                    <div className="boardBackground">
                        <table>
                            <tbody>
                                {tbody}
                            </tbody>
                        </table>
                    </div>
                </div>
            </div>
        )
    }
}

export default BoardComponent;
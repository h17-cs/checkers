import React, {Component} from 'react';
import LightSquare from './LightSquare';
import DarkSquare from './DarkSquare';
import '../App.css';
//import LightPiece from './LightPiece';
//import DarkPiece from './DarkPiece';

class BoardComponent extends Component {

    generateSquares(){
        let redSquares = [];
        redSquares.push(<DarkSquare key = {'0'} pieceInfo={this.props.gameState.zero}/>);
        redSquares.push(<DarkSquare key = {'1'} pieceInfo={this.props.gameState.one}/>);
        redSquares.push(<DarkSquare key = {'2'} pieceInfo={this.props.gameState.two}/>);
        redSquares.push(<DarkSquare key = {'3'} pieceInfo={this.props.gameState.three}/>);
        redSquares.push(<DarkSquare key = {'4'} pieceInfo={this.props.gameState.four}/>);
        redSquares.push(<DarkSquare key = {'5'} pieceInfo={this.props.gameState.five}/> );
        redSquares.push(<DarkSquare key = {'6'} pieceInfo={this.props.gameState.six}/> );
        redSquares.push(<DarkSquare key = {'7'} pieceInfo={this.props.gameState.seven}/>);
        redSquares.push(<DarkSquare key = {'8'} pieceInfo={this.props.gameState.eight}/> );
        redSquares.push(<DarkSquare key = {'9'} pieceInfo={this.props.gameState.nine}/>);
        redSquares.push(<DarkSquare key = {'10'} pieceInfo={this.props.gameState.ten}/>);
        redSquares.push(<DarkSquare key = {'11'} pieceInfo={this.props.gameState.eleven}/>);
        redSquares.push(<DarkSquare key = {'12'} pieceInfo={this.props.gameState.twelve}/>);
        redSquares.push(<DarkSquare key = {'13'} pieceInfo={this.props.gameState.thirteen}/> );
        redSquares.push(<DarkSquare key = {'14'} pieceInfo={this.props.gameState.fourteen}/>);
        redSquares.push(<DarkSquare key = {'15'} pieceInfo={this.props.gameState.fifteen}/>);
        redSquares.push(<DarkSquare key = {'16'} pieceInfo={this.props.gameState.sixteen}/>);
        redSquares.push(<DarkSquare key = {'17'} pieceInfo={this.props.gameState.seventeen}/>);
        redSquares.push(<DarkSquare key = {'18'} pieceInfo={this.props.gameState.eighteen}/>);
        redSquares.push(<DarkSquare key = {'19'} pieceInfo={this.props.gameState.nineteen}/> );
        redSquares.push(<DarkSquare key = {'20'} pieceInfo={this.props.gameState.twent}/>);
        redSquares.push(<DarkSquare key = {'21'} pieceInfo={this.props.gameState.tewntOne}/>);
        redSquares.push(<DarkSquare key = {'22'} pieceInfo={this.props.gameState.twentTwo}/>);
        redSquares.push(<DarkSquare key = {'23'} pieceInfo={this.props.gameState.twentThree}/>);
        redSquares.push(<DarkSquare key = {'24'} pieceInfo={this.props.gameState.twentFour}/>);
        redSquares.push(<DarkSquare key = {'25'} pieceInfo={this.props.gameState.twentFive}/>);
        redSquares.push(<DarkSquare key = {'26'} pieceInfo={this.props.gameState.twentSix}/>);
        redSquares.push(<DarkSquare key = {'28'} pieceInfo={this.props.gameState.twentEight}/>);
        redSquares.push(<DarkSquare key = {'29'} pieceInfo={this.props.gameState.twentNine}/>);
        redSquares.push(<DarkSquare key = {'30'} pieceInfo={this.props.gameState.thirt}/> );
        redSquares.push(<DarkSquare key = {'31'} pieceInfo={this.props.gameState.thirtOne}/>);
        redSquares.push(<DarkSquare key = {'32'} pieceInfo={this.props.gameState.thirtTwo}/>);
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
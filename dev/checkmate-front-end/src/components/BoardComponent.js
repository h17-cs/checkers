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
        for ( let i = 1; i < 33; i++ )
        {
            redSquares.push(<td> <DarkSquare key = {i.toString()}/> </td>);
        }
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
                        cells.push(<td key = { redsSpent.toString()}> {reds[i]} </td>);
                        redsSpent++;
                    }
                }
                else{
                    if(j%2 === 0){
                        cells.push(<td key = { redsSpent.toString()}> {<DarkSquare key = { i.toString() }/>} </td>);
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
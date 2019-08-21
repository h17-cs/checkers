import React, {Component} from 'react';
import LightSquare from './LightSquare';
import DarkSquare from './DarkSquare';
import LightPiece from './LightPiece';
import DarkPiece from './DarkPiece';

class BoardComponent extends Component {

    render(){
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

        return(
            <div >
                <table>
                    <tbody>
                        {tbody}
                    </tbody>
                </table>
            </div>
        )
    }
}

export default BoardComponent;
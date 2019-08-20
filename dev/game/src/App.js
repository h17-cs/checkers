import { Client } from 'boardgame.io/react';
import { Game } from 'boardgame.io/core';
import Board from './Board'

// Return true if `cells` is in a winning configuration.
function IsVictory(cells) {
  
}

// Return true if all `cells` are occupied.
function IsDraw(cells) {
  return cells.filter(c => c === null).length == 0;
}

const TicTacToe = Game({
  setup: () => ({ cells: Array(9).fill(null) }),

  moves: {
    clickCell(G, ctx, id) {
      // Ensure that we can't overwrite cells.
      if (G.cells[id] === null) {
        G.cells[id] = ctx.currentPlayer;
      }
    },
  },

  flow: {
    endGameIf: (G, ctx) => {
      if (IsVictory(G.cells)) {
        return { winner: ctx.currentPlayer };
      }
      if (IsDraw(G.cells)) {
        return { draw: true };
      }
    },
  },
});

const App = Client({ 
  game: TicTacToe,
  board: Board
 });

export default App;
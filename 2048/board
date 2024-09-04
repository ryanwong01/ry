import javax.swing.JPanel;

public class Board extends JPanel {
	public Tile[][] board;

	public Board() {
		board = new Tile[4][4];
		for (int i = 0; i < board.length; i++) {
			for (int j = 0; j < board[i].length; j++) {
				board[i][j] = new Tile();
			}
		}
	}

	public Tile[][] getBoard() {
		return board;
	}
	
	public int getBoardLength()
	{
		return board.length;
	}

	public int getHighTile() {
		int highest = board[0][0].getTileValue();
		for (int i = 0; i < board.length; i++) {
			for (int j = 0; j < board[i].length; j++) {
				if (board[i][j].getTileValue() > highest) {
					highest = board[i][j].getTileValue();
				}
			}
		
		return highest;
	}

	public String toString() {
		String s = "";
		for (int i = 0; i < board.length; i++) {
			for (int j = 0; j < board[i].length; j++) {
				s += board[i][j].toString() + " ";
			}
			s += "\n";
		}
		return s;
	}

	public void spawnNewTile()
    {
        boolean empty = true;
        while ( empty )
        {
            int row = (int)( Math.random() * 4 );
            int col = (int)( Math.random() * 4 );
            int x = (int)(Math.random() * 10) + 1;
            if ( board[row][col].getTileValue() == 0 )
            {
                if ( x <= 2 )
                {
                    board[row][col] = new Tile( 4 );
                    empty = false;
                }
                else
                {
                    board[row][col] = new Tile( 2 );
                    empty = false;
                }
            }

        }

    }
	
}

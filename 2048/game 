public class Game {

    private Board board;
    private Score score;

    public Game() {
        this.board = new Board();
        this.score = new Score();
    }

    public Board getBoard() {
        return board;
    }

    public Score getScore() {
        return score;
    }
    
    public boolean blackOut() {
        int count = 0;
        Tile[][] boardArray = board.getBoard(); // Get the board array from the Board object
        for (int i = 0; i < boardArray.length; i++) {
            for (int j = 0; j < boardArray[i].length; j++) {
                if (boardArray[i][j].getTileValue() > 0) {
                    count++;
                }
            }
        }
        if ( count == 16 )
        {
            return true;
        }
        return false;
    }   
    
    public boolean gameOver() {
        int count = 0;
        Tile[][] boardArray = board.getBoard();
        for (int i = 0; i < boardArray.length; i++) {
            for (int j = 0; j < boardArray[i].length; j++) {
                if (boardArray[i][j].getTileValue() > 0) {
                    if (i == 0 && j == 0) {
                        if (boardArray[i][j].getTileValue() != boardArray[i + 1][j].getTileValue()
                                && boardArray[i][j].getTileValue() != boardArray[i][j + 1].getTileValue()) {
                            count++;
                        }
                    } else if (i == 0 && j == 3) {
                        if (boardArray[i][j].getTileValue() != boardArray[i + 1][j].getTileValue()
                                && boardArray[i][j].getTileValue() != boardArray[i][j - 1].getTileValue()) {
                            count++;
                        }
                    } else if (i == 3 && j == 3) {
                        if (boardArray[i][j].getTileValue() != boardArray[i - 1][j].getTileValue()
                                && boardArray[i][j].getTileValue() != boardArray[i][j - 1].getTileValue()) {
                            count++;
                        }
                    } else if (i == 3 && j == 0) {
                        if (boardArray[i][j].getTileValue() != boardArray[i - 1][j].getTileValue()
                                && boardArray[i][j].getTileValue() != boardArray[i][j + 1].getTileValue()) {
                            count++;
                        }
                    } else if (i == 0 && (j == 1 || j == 2)) {
                        if (boardArray[i][j].getTileValue() != boardArray[i + 1][j].getTileValue()
                                && boardArray[i][j].getTileValue() != boardArray[i][j + 1].getTileValue()
                                && boardArray[i][j].getTileValue() != boardArray[i][j - 1].getTileValue()) {
                            count++;
                        }
                    } else if (i == 3 && (j == 1 || j == 2)) {
                        if (boardArray[i][j].getTileValue() != boardArray[i - 1][j].getTileValue()
                                && boardArray[i][j].getTileValue() != boardArray[i][j + 1].getTileValue()
                                && boardArray[i][j].getTileValue() != boardArray[i][j - 1].getTileValue()) {
                            count++;
                        }
                    } else if (j == 0 && (i == 1 || i == 2)) {
                        if (boardArray[i][j].getTileValue() != boardArray[i][j + 1].getTileValue()
                                && boardArray[i][j].getTileValue() != boardArray[i - 1][j].getTileValue()
                                && boardArray[i][j].getTileValue() != boardArray[i + 1][j].getTileValue()) {
                            count++;
                        }
                    } else if (j == 3 && (i == 1 || i == 2)) {
                        if (boardArray[i][j].getTileValue() != boardArray[i][j - 1].getTileValue()
                                && boardArray[i][j].getTileValue() != boardArray[i - 1][j].getTileValue()
                                && boardArray[i][j].getTileValue() != boardArray[i + 1][j].getTileValue()) {
                            count++;
                        }
                    } else {
                        if (boardArray[i][j].getTileValue() != boardArray[i][j - 1].getTileValue()
                                && boardArray[i][j].getTileValue() != boardArray[i][j + 1].getTileValue()
                                && boardArray[i][j].getTileValue() != boardArray[i - 1][j].getTileValue()
                                && boardArray[i][j].getTileValue() != boardArray[i + 1][j].getTileValue()) {
                            count++;
                        }
                    }
                }
            }
        }
        if (count == 16) {
            return true;
        }
        return false;
    }
}

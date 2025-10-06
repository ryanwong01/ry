class Game {
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
        Tile[][] boardArray = board.getBoard();
        for (int i = 0; i < boardArray.length; i++) {
            for (int j = 0; j < boardArray[i].length; j++) {
                if (boardArray[i][j].getTileValue() > 0) {
                    count++;
                }
            }
        }
        return count == 16;
    }

    public boolean gameOver() {
        Tile[][] boardArray = board.getBoard();
        for (int i = 0; i < boardArray.length; i++) {
            for (int j = 0; j < boardArray[i].length; j++) {
                int value = boardArray[i][j].getTileValue();
                if (value == 0 ||
                    (i > 0 && boardArray[i - 1][j].getTileValue() == value) ||
                    (i < boardArray.length - 1 && boardArray[i + 1][j].getTileValue() == value) ||
                    (j > 0 && boardArray[i][j - 1].getTileValue() == value) ||
                    (j < boardArray[i].length - 1 && boardArray[i][j + 1].getTileValue() == value)) {
                    return false;
                }
            }
        }
        return true;
    }
}
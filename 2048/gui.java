import javax.swing.*;
import java.awt.*;
import java.awt.event.*;

public class GUI extends JFrame implements KeyListener {
    private JFrame frame;
    private Game game;
    private Board board;

    public GUI(Game game) {
        this.game = game;
        this.board = game.getBoard();
        this.board.addKeyListener(this);
    }

    public void createAndShowGUI() {
        frame = new JFrame("2048");
        frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        frame.setSize(400, 400);
        frame.setResizable(false);

        frame.getContentPane().setLayout(new BorderLayout());
        frame.getContentPane().add(board, BorderLayout.CENTER);

        frame.setVisible(true);
        board.requestFocusInWindow(); // Request focus for keyboard input
    }

    @Override
    public void keyPressed(KeyEvent e) {
        int keyCode = e.getKeyCode();
        if (keyCode == KeyEvent.VK_UP) {
            // Handle up key
        } else if (keyCode == KeyEvent.VK_DOWN) {
            // Handle down key
        } else if (keyCode == KeyEvent.VK_LEFT) {
            // Handle left key
        } else if (keyCode == KeyEvent.VK_RIGHT) {
            // Handle right key
        }
    }

    @Override
    public void keyTyped(KeyEvent e) {
        // Not used
    }

    @Override
    public void keyReleased(KeyEvent e) {
        // Not used
    }
}


import javax.swing.*;
import java.awt.*;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;

public class GUI extends JFrame {
    private JFrame frame;
    private Game game;
  
    //private FileHandler fileHandler;

    /**
    public GUI(Game game, FileHandler fileHandler) {
        this.game = game;
        this.fileHandler = fileHandler;
    }
    **/
    
    //test con
    public GUI(Game game) {
        this.game = game;
    }
   

    public void createAndShowGUI() {
        frame = new JFrame("2048");
        frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        frame.setSize(400, 400);
        frame.setResizable(false);

        Board board = game.getBoard();
        frame.add(board);

        /**
        JMenuBar menuBar = new JMenuBar();
        JMenu fileMenu = new JMenu("File");
        
        JMenuItem highScoresItem = new JMenuItem("High Scores");
        highScoresItem.addActionListener(new ActionListener() {
            public void actionPerformed(ActionEvent e) {
                String highScores = fileHandler.getHighScores();
                JOptionPane.showMessageDialog(frame, highScores, "High Scores", JOptionPane.PLAIN_MESSAGE);
            }
        });
        fileMenu.add(highScoresItem);
        menuBar.add(fileMenu);
        frame.setJMenuBar(menuBar);

        frame.setVisible(true);
        **/
    }
}

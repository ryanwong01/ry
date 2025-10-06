import javax.swing.*;
import java.awt.*;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;

public class Main {
    public static void main(String[] args) {
        Game game = new Game();
        GUI gui = new GUI(game);
        gui.createAndShowGUI();
    }
}
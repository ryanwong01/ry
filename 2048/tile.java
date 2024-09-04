
import javax.swing.*;
import java.awt.*;

public class Tile extends JPanel {
    private int value;
    private Color tileColor;

    public Tile() {
        this.value = 0;
    }

    public Tile(int number) {
        this.value = number;
    }

    public int getTileValue() {
        return value;
    }

    public void setTileValue(int value) {
        this.value = value;
    }

    public void setColor() {
        if (this.getTileValue() == 2) {
            tileColor = new Color(238, 228, 218);
        } else if (this.getTileValue() == 4) {
            tileColor = new Color(237, 224, 200);
        } else if (this.getTileValue() == 8) {
            tileColor = new Color(242, 177, 121);
        } else if (this.getTileValue() == 16) {
            tileColor = new Color(245, 149, 99);
        } else if (this.getTileValue() == 32) {
            tileColor = new Color(246, 124, 96);
        } else if (this.getTileValue() == 64) {
            tileColor = new Color(246, 94, 59);
        } else if (this.getTileValue() == 128) {
            tileColor = new Color(237, 207, 115);
        } else if (this.getTileValue() == 256) {
            tileColor = new Color(237, 204, 98);
        } else if (this.getTileValue() == 512) {
            tileColor = new Color(237, 200, 80);
        } else if (this.getTileValue() == 1024) {
            tileColor = new Color(237, 197, 63);
        } else {
            tileColor = new Color(237, 194, 45);
        }
    }

    public Color getTileColor() {
        setColor();
        return tileColor;
    }

    @Override
    protected void paintComponent(Graphics g) {
        super.paintComponent(g);
        g.setColor(getTileColor());
        g.fillRect(0, 0, getWidth(), getHeight());
    }
}

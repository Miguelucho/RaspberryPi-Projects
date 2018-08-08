//La clase Rectangle tendrá el siguiente código:
package geometry;
/**
 * @author Mario Pérez Esteso <mario@geekytheory.com>
 * @web geekytheory.com
 */
public class Rectangle {
    int side1, side2;
    public Rectangle(int side1, int side2) {
        this.side1 = side1;
        this.side2 = side2;
    }
    public int area() {
        return this.side1*this.side2;
    }
}

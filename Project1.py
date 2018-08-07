//La clase Circle tendrá el siguiente código:
package geometry;
/**
 * @author Mario Pérez Esteso <mario@geekytheory.com>
 * @web geekytheory.com
 */
public class Circle {
    int radius;
    public Circle(int radius) {
        this.radius = radius;
    }
    public float area() {
        return (float) (Math.PI*this.radius*this.radius);
    }
}

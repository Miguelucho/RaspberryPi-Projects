La clase principal Geometry tendrá el siguiente código:
package geometry;
/**
 * @author Mario Pérez Esteso <mario@geekytheory.com>
 * @web geekytheory.com
 */
public class Geometry {

    public static void main(String[] args) {
        // Triangle parameters
        int base = 5, height = 3;
        // Rectangle parameters
        int side1 = 4, side2 = 2;
        // Circle parameter
        int radius = 6;

        System.out.println("I am going to create 3 objects (Triangle, Circle and Rectangle) and print their areas");
        // Triangle
        Triangle tri = new Triangle(base, height);
        System.out.println("Triangle area: " + tri.area());
        // Circle
        Circle cir = new Circle(radius);
        System.out.println("Circle area: " + cir.area());
        // Rectangle
        Rectangle rect = new Rectangle(side1, side2);
        System.out.println("Rectangle area: " + rect.area());
    }
}

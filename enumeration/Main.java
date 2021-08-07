package enumeration;

/**
 * @author kuntiarso
 * @since August 7th, 2021
 */
public class Main {

    protected enum Color {
        RED("red"), GREEN("green"), BLUE("blue");

        private String value;

        Color(String value) {
            this.value = value;
        }
    }

    public static void main(String[] args) {

        for (Color color: Color.values()) {
            System.out.println(String.format("Color name: %s", color.name()));
            System.out.println(String.format("Color ordinal: %s", color.ordinal()));
            System.out.println(String.format("Color value: %s", color.value));
        }

    }
}
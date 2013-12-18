package week1;

/**
 * Created with IntelliJ IDEA.
 * User: nuria
 * Date: 9/16/13
 * Time: 10:56 PM
 * To change this template use File | Settings | File Templates.
 */
public class DogTest {


    public static void main(String args[]) {

        Dog d1 = new Dog("pepito");

        DogTest.changeDogName(d1);
        System.out.println(d1.getName());

    }

    public static void changeDogName(Dog d) {
        d.setName("juanito");
    }


}

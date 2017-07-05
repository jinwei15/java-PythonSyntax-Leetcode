package personproject;

import java.text.SimpleDateFormat;
import java.util.Date;
import java.util.Scanner;

public class PersonProject {

    static Scanner kb = new Scanner(System.in);

    public static void main(String[] args) {

        Person[] people = new Person[5];
        for (int i = 0; i <= 4; i++) {
            people[i] = dataEntryNewPerson();
        }

        // Display all people:  name and age only
        // write some code here
        bubbleSort(people);
        for (int i = 0; i <= 4; i++) {
            System.out.println(people[i].toString());
        }
    }







    public static Person dataEntryNewPerson() {
        System.out.println("Enter details of person");
        System.out.print("Enter name:");
        String n = kb.nextLine();
        System.out.print("Enter gender (M/F):");
        String g = kb.nextLine();
        System.out.print("Enter address:");
        String a = kb.nextLine();
        System.out.print("Enter the date of birth (DD MM YYYY): ");
        Date dob = inputDate();
        Person p = new Person(n, g, a, dob);
        return p;
    }






    public static void swapNames(Person x, Person y) {
        String temp;
        temp = x.getName();
        x.setName(y.getName());
        y.setName(temp);
    }





    public static Date inputDate() {
        Date d = new Date();

        String s = kb.nextLine();
        SimpleDateFormat df = new SimpleDateFormat("d M y");
        try {
            d = df.parse(s);
        } catch (Exception e) {
            System.out.println("Input is not a date");
        };
        return d;
    }






    private static void bubbleSort(Person[] pArray) {
        int n = pArray.length;
        Person temp = null;
        for (int i = 0; i < n; i++) {
            for (int j = 1; j < (n - i); j++) {
                if ((pArray[j - 1].getName().compareTo(pArray[j].getName()) > 0)) {
                    temp = pArray[j - 1];
                    pArray[j - 1] = pArray[j];
                    pArray[j] = temp;
                }
            }
        }
    }

}

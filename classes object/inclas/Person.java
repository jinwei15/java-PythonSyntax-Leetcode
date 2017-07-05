package personproject;

import java.util.Date;

public class Person {

    public static int lastId = 0;

    private String name;
    private String gender;
    private String address;
    private int idNumber;
    private Date dateOfBirth;



                                                    //constructor method with no arguments
    public Person() {
        address = "";
    }





                                               //constructor method with 3 String, 1 Date arguments
    public Person(String name, String gender, String address, Date d) {
        super();
        this.name = name;
        this.gender = gender;
        this.address = address;
        this.dateOfBirth = d;
        lastId++;
        this.idNumber = lastId;
    }

    public String getName() {
        return name;
    }

    public void setName(String n) {
        this.name = n;
    }

    public String getGender() {
        return gender;
    }

    public void setGender(String g) {
        this.gender = g;
    }

    public String getAddress() {
        return address;
    }

    public void setAddress(String a) {
        this.address = a;
    }

    public Date getDateOfBirth() {
        return dateOfBirth;
    }

    public void setDateOfBirth(Date d) {
        this.dateOfBirth = d;
    }
    




    

    public String toString() {
        return "Person [name=" + name + ", gender=" + gender + ", DOB=" + dateOfBirth
                + ", address=" + address + ", idNumber=" + idNumber + "]";
    }
    
                                                    // return the person's age in years
    public int age(){
        int a = 0;
                                                    //  finish coding this method
        
        return a;
    }








    public boolean isHomeless() {
        if (address.length() == 0) {
            return true;
        } else {
            return false;
        }
    }

                           // check if two Person objects have similiar attribute values
                         // Ignore case when comparing attributes
    public boolean isSimiliarTo(Person peep) {
        boolean areTheyEqual = true;
        if (!this.address.equalsIgnoreCase(peep.address)) {
            areTheyEqual = false;
        }
        if (!this.name.equalsIgnoreCase(peep.name)) {
            areTheyEqual = false;
        }
        if (!this.gender.equalsIgnoreCase(peep.gender)) {
            areTheyEqual = false;
        }
        return areTheyEqual;
    }



    public boolean equals(Person p) {
        if ((this.idNumber == p.idNumber) && (this.address.equals(p.address)) && (this.name.equals(p.name)) && (this.gender.equals(p.gender))) {
            return true;
        } else {
            return false;
        }
    }



    public static int numberOfPeople() {
        return lastId;
    }

}

package moneyproject;

// objects of this class store exact money amounts by storing the dollar
// and cent component separately as integers.
public class Money {

    int dollar;    // 1 dollar = 100 cents
    int cents;

    public Money(int dollar, int cents) {
        this.dollar = dollar;
        this.cents = cents;
    }





    // Add another Money object to this Money object; return a new Money object
    public Money add(Money m) {
        int d = this.dollar + m.dollar;
        int c = this.cents + m.cents;
        if (c > 99) {
            c = c - 100;
            d = d + 1;
        }
        return new Money(d, c);
    }






    // Substract another Money object from this Money object; return a new Money object
    public Money subtract(Money m) {
        int d = this.dollar - m.dollar;
        int c = this.cents - m.cents;
        if (c < 0) {
            c = c + 100;
            d = d - 1;
        }
        return new Money(d, c);
    }







    // Multiply another Money object to this Money object; return a new Money object
    public Money multiply(Money m) {
        int d = 0;
        int c = 0;

        // add more code
        return new Money(d, c);
    }







    // Divide another Money object into this Money object; return a new Money object
    public Money divide(Money m) {
        int d = 0;
        int c = 0;

        // add more code
        return new Money(d, c);
    }








    // check if another Money object is equal to this Money object 
    public Boolean equals(Money x) {
        if ((this.dollar == x.dollar) && (this.cents == x.cents)) {
            return true;
        } else {
            return false;
        }
    }






    public String toString() {
        String s = "$";
        s = s + Integer.toString(this.dollar);
        s = s + ".";
        if (this.cents < 10) {
            s = s + "0";
        }
        s = s + Integer.toString(this.cents);
        return s;
    }

}

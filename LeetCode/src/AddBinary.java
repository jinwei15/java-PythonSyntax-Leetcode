/**
 * 
 */

/**
 * @author jinweizhang
 *
 */
public class AddBinary {

	/**
	 * @param args
	 */
	public static void main(String[] args) {
		// TODO Auto-generated method stub
		SolutionAddBinary aa = new SolutionAddBinary();
		String a= "10100000100100110110010000010101111011011001101110111111111101000000101111001110001111100001101";
		String b="110101001011101110001111100110001010100001101011101010000011011011001011101111001100000011011110011";

		System.out.println(aa.addBinary(a, b));
		
	}

}


class SolutionAddBinary {
    public String addBinary(String a, String b) {
        long number0 = Long.parseLong(a, 2);
        long number1 = Long.parseLong(b, 2);

        return  Long.toBinaryString(number0 + number1); 
    }
}
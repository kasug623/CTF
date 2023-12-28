import java.net.URLDecoder;
import java.util.Base64;
import java.io.UnsupportedEncodingException;

class Solver {
    public static void main(String args[]) {
        Solver solver = new Solver();
        solver.displayFlag();
    }

    public String base64Decode(byte[] input) {
        byte[] byteArray = Base64.getDecoder().decode(input);
        String result = new String(byteArray);
        return result;

    }

    public String urlDecode(byte[] input) {
        StringBuffer buf = new StringBuffer();

        for ( int i = 0; i < input.length; i+=3)
        {
            String a = String.valueOf((char)input[i+1]) + String.valueOf((char)input[i+2]);
            int decimalValue = Integer.parseInt(a, 16);
            char asciiChar = (char) decimalValue;
            buf.append(asciiChar);
        }

        return buf.toString();
    }

    public void displayFlag() {
        String encryptedFlag = "JTYzJTMwJTZlJTc2JTMzJTcyJTc0JTMxJTZlJTY3JTVm"
                                + "JTY2JTcyJTMwJTZkJTVmJTYyJTYxJTM1JTY1JTVmJTM2"
                                + "JTM0JTVmJTY1JTMzJTMxJTM1JTMyJTYyJTY2JTM0";
        System.out.println("encrypted flag is : " + encryptedFlag);

        String decodedFlag1 = base64Decode(encryptedFlag.getBytes());
        String decodedFlag2 = urlDecode(decodedFlag1.getBytes());

        byte[] flag = decodedFlag2.getBytes();

        System.out.print("flag is: picoCTF{");
        for (byte c : flag) {
            System.out.print((char)c);
        }
        System.out.println("}");
    }
}

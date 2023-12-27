import java.util.*;

class Solver {
    public static void main(String args[]) {
        Solver solver = new Solver();
        solver.displayFlag();
    }

    public void displayFlag() {
        String encryptedFlag = "jU5t_a_sna_3lpm18g947_u_4_m9r54f";
        System.out.println("encrypted flag is : " + encryptedFlag);

        char[] flag = new char[32];

        int i;
        for (i=0; i<8; i++) {
            flag[i] = encryptedFlag.charAt(i);
        }
        for (; i<16; i++) {
            flag[23-i] = encryptedFlag.charAt(i);
        }
        for (; i<32; i+=2) {
            flag[46-i] = encryptedFlag.charAt(i);
        }
        for (i=31; i>=17; i-=2) {
            flag[i] = encryptedFlag.charAt(i);
        }

        System.out.print("flag is: picoCTF{");
        for (char c : flag) {
            System.out.print(c);
        }
        System.out.println("}");
    }
}

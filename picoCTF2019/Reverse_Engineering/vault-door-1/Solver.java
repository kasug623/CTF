import java.util.*;

class Solver {
    public static void main(String args[]) {
        Solver solver = new Solver();
        solver.displayFlag();
    }

    public void displayFlag() {
        char[] flag = new char[32];
        flag[0]  = 'd';
        flag[29] = '9';
        flag[4]  = 'r';
        flag[2]  = '5';
        flag[23] = 'r';
        flag[3]  = 'c';
        flag[17] = '4';
        flag[1]  = '3';
        flag[7]  = 'b';
        flag[10] = '_';
        flag[5]  = '4';
        flag[9]  = '3';
        flag[11] = 't';
        flag[15] = 'c';
        flag[8]  = 'l';
        flag[12] = 'H';
        flag[20] = 'c';
        flag[14] = '_';
        flag[6]  = 'm';
        flag[24] = '5';
        flag[18] = 'r';
        flag[13] = '3';
        flag[19] = '4';
        flag[21] = 'T';
        flag[16] = 'H';
        flag[27] = '5';
        flag[30] = '2';
        flag[25] = '_';
        flag[22] = '3';
        flag[28] = '0';
        flag[26] = '7';
        flag[31] = 'e';

        // Print the contents of the char array
        System.out.print("flag is: picoCTF{");
        for (char c : flag) {
            System.out.print(c);
        }
        System.out.println("}");
    }
}

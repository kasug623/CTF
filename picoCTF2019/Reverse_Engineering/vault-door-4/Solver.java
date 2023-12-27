class Solver {
    public static void main(String args[]) {
        Solver solver = new Solver();
        solver.displayFlag();
    }

    public void displayFlag() {
        String encryptedFlag = "jU5t_a_sna_3lpm18g947_u_4_m9r54f";
        System.out.println("encrypted flag is : " + encryptedFlag);

        byte[] flag = {
            106 , 85  , 53  , 116 , 95  , 52  , 95  , 98  ,
            0x55, 0x6e, 0x43, 0x68, 0x5f, 0x30, 0x66, 0x5f,
            0142, 0131, 0164, 063 , 0163, 0137, 070 , 0146,
            '4' , 'a' , '6' , 'c' , 'b' , 'f' , '3' , 'b' ,
        };

        System.out.print("flag is: picoCTF{");
        for (byte c : flag) {
            System.out.print((char)c);
        }
        System.out.println("}");
    }
}

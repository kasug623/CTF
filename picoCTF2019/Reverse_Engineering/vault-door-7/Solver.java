class Solver {
    public static void main(String args[]) {
        Solver solver = new Solver();
        solver.displayFlag();
    }

    public String singleBruteForce(int x){
        for(int b1 = -127; b1 <= 128; b1++)
        {
            for(int b2 = -127; b2 <= 128; b2++)
            {
                for(int b3 = -127; b3 <= 128; b3++)
                {
                    for(int b4 = -127; b4 <= 128; b4++)
                    {
                        int candidate = b1 << 24
                                        | b2 << 16
                                        | b3 << 8
                                        | b4;
                        if(candidate == x)
                        {
                            return String.valueOf((char)b1)
                                     + String.valueOf((char)b2)
                                     + String.valueOf((char)b3)
                                     + String.valueOf((char)b4);
                        }
                    }
                }
            }
        }
        return "--FAIL--";
    }

    public void displayFlag() {
        int[] xs = {1096770097, 1952395366, 1600270708, 1601398833, 1716808014, 1734304867, 942695730, 942748212};
        System.out.print("flag is: picoCTF{");
        for (int x : xs) {
            System.out.print(singleBruteForce(x));
        }
        System.out.println("}");
    }
}

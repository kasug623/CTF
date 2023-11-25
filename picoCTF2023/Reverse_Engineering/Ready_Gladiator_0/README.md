# Memo
1. first try  
    imp.red  
    ```
    ;redcode
    ;name Imp Ex
    ;assert 1
    mov 0, 1
    end
    ```
    connect to server  
    ```bash
    $ nc saturn.picoctf.net 53527 < imp.red
    ;redcode
    ;name Imp Ex
    ;assert 1
    mov 0, 1
    end
    Submit your warrior: (enter 'end' when done)

    Warrior1:
    ;redcode
    ;name Imp Ex
    ;assert 1
    mov 0, 1
    end

    Rounds: 100
    Warrior 1 wins: 0
    Warrior 2 wins: 0
    Ties: 100
    Try again. Your warrior (warrior 1) must lose all rounds, no ties.
    ```
2. second try  
    imp.red  
    ```
    ;redcode
    ;name Imp Ex
    ;assert 1
    mov 0, 2
    end
    ```
    connect to server  
    ```bash
    $ nc saturn.picoctf.net 53527 < imp.red
    ;redcode
    ;name Imp Ex
    ;assert 1
    mov 0, 2
    end
    Submit your warrior: (enter 'end' when done)

    Warrior1:
    ;redcode
    ;name Imp Ex
    ;assert 1
    mov 0, 2
    end

    Rounds: 100
    Warrior 1 wins: 0
    Warrior 2 wins: 100
    Ties: 0
    You did it!
    picoCTF{h3r0_t0_z3r0_4m1r1gh7_f1e207c4}
    ```
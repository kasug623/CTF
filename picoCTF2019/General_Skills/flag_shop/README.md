# Memo
1. analyze  
focus on a range og integer.  
    - int() : -2147483647 ~ 2147483647

    - initial balance
    ```
    Balance: 1100
    ```
    - target
    ```c
    int total_cost = 0;
    total_cost = 900*number_flags;
    printf("\nThe final cost is: %d\n", total_cost);
    if(total_cost <= account_balance){
        account_balance = account_balance - total_cost;
        printf("\nYour current balance after transaction: %d\n\n", account_balance);
    }
    ```
    2147483647 / 900 = 2386092.9411111  

    - investigate a input around "2386092"  
account_balance : 1100(100 0100 1100)  

input : 2386092 (10 0100 0110 1000 1010 1100)  
input : 2386093 (10 0100 0110 1000 1010 1101)  
input : 2386094 (10 0100 0110 1000 1010 1110)  
input : 2386095 (10 0100 0110 1000 1010 1111)  

total_cost : 2147482800 (0111 1111 1111 1111 1111 1100 1011 0000)  
total_cost : 2147483700 (1000 0000 0000 0000 0000 0000 0011 0100)  
total_cost : 2147484600 (1000 0000 0000 0000 0000 0011 1011 1000)  
total_cost : 2147485500 (1000 0000 0000 0000 0000 0111 0011 1100)  

account_balance - total_cost
= 100 0100 1100 - 0111 1111 1111 1111 1111 1100 1011 0000
= 100 0100 1100 + 1000 0000 0000 0000 0000 0011 0101 0000

account_balance - total_cost
= 100 0100 1100 - 1000 0000 0000 0000 0000 0000 0011 0100
= 100 0100 1100 + 0111 1111 1111 1111 1111 1111 1100 1100

account_balance - total_cost
= 100 0100 1100 - 1000 0000 0000 0000 0000 0011 1011 1000
= 100 0100 1100 + 0111 1111 1111 1111 1111 1100 0100 1000

account_balance - total_cost
= 100 0100 1100 - 1000 0000 0000 0000 0000 0111 0011 1100
= 100 0100 1100 + 0111 1111 1111 1111 1111 1000 1100 0100


input : 2386092 (0b 10 0100 0110 1000 1010 1100)
```
These knockoff Flags cost 900 each, enter desired quantity
2386092

The final cost is: 2147482800
Not enough funds to complete purchase
```
input : 2386093 (0b 10 0100 0110 1000 1010 1101)
```
These knockoff Flags cost 900 each, enter desired quantity
2386093

The final cost is: -2147483596

Your current balance after transaction: -2147482600
```
input : 2386094 (10 0100 0110 1000 1010 1110)
```
These knockoff Flags cost 900 each, enter desired quantity
2386094

The final cost is: -2147482696

Your current balance after transaction: -2147483500
```
input : 2386095 (10 0100 0110 1000 1010 1111)
```
These knockoff Flags cost 900 each, enter desired quantity
2386095

The final cost is: -2147481796

Your current balance after transaction: 2147482896
```
Then I got enough money.

2. buy
```
1. Defintely not the flag Flag
2. 1337 Flag
2
1337 flags cost 100000 dollars, and we only have 1 in stock
Enter 1 to buy one1
YOUR FLAG IS: picoCTF{m0n3y_bag5_68d16363}
```
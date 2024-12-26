def find_factorial(n):
    if n ==1 or n == 0:
        return 1;
    else:
        return n*find_factorial(n-1)

fact = int(input("Enter a number that you want to find factorial:"))
print(f"That number you enter is this {fact} and the factoial of this number is this {find_factorial(fact)}")
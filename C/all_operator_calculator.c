#include <stdio.h>
int main()
{
    int a, b;
    printf("Enter the first:  ");
    scanf("%d", &a);
    
    printf("Enter the second number:  ");
    scanf("%d", &b);

    printf("The sum of the inputs is ", a+b);
    printf("The product of the inputs is ", a*b);
    printf("The quotient upon a divided by b is ", a/b);
    printf("The difference of the inputs is ", a-b);

    return 0;
}

#include <stdio.h>

int main()
{
 int numbers[] = {5, 5, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1};
 int n = sizeof(numbers) / sizeof(numbers[0]);

 float sum = 0;
 for (int i = 0; i < n; i++)
   sum += numbers[i];

 float avg = sum / n;

 printf("The total of the added numbers is: %f\n", sum);
 printf("The average value of the numbers added up is: %f\n", avg);
}

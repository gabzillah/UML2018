/*****************************************************************
** Name: Gabrielle Jameson
** Functions:  calculate_simple_interest && calculate_compound_interest
**
** Description:  Simple Interest is the amount of interest
**               calculated by using the formula:
**
**               interest = (P * R * T)
**
**               where P is the principle, r is the rate, and t
**               is the time of the investment
**
**               This function will return the simple interest
**               calculated based upon it being passed the principle,
**               rate, and time.
**
** Parameters:   Principle - The original principal to start with
**               Rate      - The rate of interest.  If you wanted
**                           9.5 percent it would be passed as 0.095
**               Time      - The time in years
**
** Returns:      Interest  - The amount of simple and compund interest earned
**
********************************************************************/
#include<stdio.h>
#include<math.h>

float calculate_simple_interest (float principle, float rate, float time)
{
 float interest;
 interest = principle * rate * time;
 return interest;
} /* end Calculate_Simple_Interest */

float calculate_compound_interest(float principle, float rate, float time)
{
  float compound_interest;
  compound_interest = principle * pow((1 + rate/100), time);
  return compound_interest;
} /* end calculate_compound_interest */

int main (void)
{
 float interest; /* The interest earned over a period of time */
 float compound_interest; /* The compund interest earned over a period of time */
 float principle; /* The amount being invested */
 float rate;  /* The interest rate earned */
 float time; /* The years of the investment */

 /* Initialize the interest and compund interest values */
 interest = 0;
 compound_interest = 0;

 /* Enter values needed to determine simple and compund interest*/
 printf ("\nEnter your principle value: ");
 scanf ("%f", &principle);

 printf ("\nEnter the rate: For example 9.5 percent would be .095: ");
 scanf ("%f", &rate);

 printf ("\nEnter the period of time of your investment: (In years)");
 scanf ("%f", &time);

 interest = calculate_simple_interest (principle, rate, time);
 compound_interest = calculate_compound_interest (principle, rate, time);

 /* print the simple and compound interest earned to the screen */
printf("\n\nThe total simple interest earned is: $%8.2f\n", interest);
printf("\n\nThe total compound interest earned is: $%8.2f\n", compound_interest);


 return (0); /* indicate successful completion */


} /* end main */

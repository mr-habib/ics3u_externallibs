# IS3U External Libs

Your goal for this assignment is to use the [datetime](https://docs.python.org/3/library/datetime.html) library in order to create a "Days Until" counter.

The user will `input()` a date in the format we always use in class (Eg. mm/dd/yyyy) and the program will either output "That's past already" (Or something to that nature) or the number of days until the inputted date with a nice message to boot.

You will do this by writing a function called `calc_days_until(date_string)` and having this method return the number of days until that date, or -1 if the date happens before today's date. Then you will call the function, and, depending on the output of the function, print the appropriate message.

## Example Interaction
Note: This interaction was updated on 03/08/2020, so date outputs will adjust accordingly.
```
>> Enter a date: 03/10/2021
That's in 2 days
>> Enter a date: 06/10/2020
That's past already
```

You do not need to provide a while loop.
If you have any questions, please let me know

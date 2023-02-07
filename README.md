# SportsReferencePrompt

1. Packages 'pandas' and 'json' were imported.
2. The json file was read and stored as the variable 'dict'.
3. A function was created to read the dictionary and create a table using the pandas package. The function will allow the table to be assigned to an external variable.
4. A 'teams' variable was created by taking the dictionary keys - this is a list of all the team names.
5. A data frame was created and the team names were used as column names and in the index. Having the team names in the index makes it easier to input win values later
6. The for loop iterates over the dictionary and will input the win values using team names in the column and index.
7. The index of the data frame was named 'Tms'.
8. The index was then removed and used as a column in the data frame.
9. The example table had the team names as the last row of the table - a 'last_row' list was created by taking the column names of the data frame to append to the end of the data frame.
10. The last row was appended to the data frame.
11. The NaN values were replaced with '--'.
12. The function will then return the data frame

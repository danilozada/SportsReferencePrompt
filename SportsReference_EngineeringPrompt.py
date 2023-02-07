# Import packages
import pandas as pd
import json

# Read json file
with open('SportsReference_Prompt.json', 'r') as json_file:
    dict = json.load(json_file)

## Create function for dictionary
def table_func(dict):
    # Get individual team names
    teams = dict.keys()

    # Create empty data frame
    df = pd.DataFrame(index=teams, columns = teams)

    # Fill data frame with wins from each team
    for k in dict:
        for v in dict[k]:
            for y in dict[k][v]:
                if y == 'W':
                    df.loc[v,k] = dict[k][v][y]

    # Name index
    df.index.name = 'Tms'

    # Remove teams from index and add to the table
    df.reset_index(inplace = True)

    # Append the team names as the last row in the data frame
    last_row = list(df.columns)

    df.loc[len(df)] = last_row

    # Replace NaN values with '--'

    df.fillna('--', inplace = True)

    return df

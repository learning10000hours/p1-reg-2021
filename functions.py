import pandas as pd

def read_file_to_df(file_name, area):
    mylines = [] 
    schools = pd.DataFrame(columns=["Schools", "Area", "Address"])

    with open(file_name, 'r') as file:
        for line in file:
            mylines.append(line.rstrip()

    filtered = list(filter(None, mylines))

    for i in range(len(filtered)):
        if(filtered[i] == area):
            schools.loc[i, 'School'] = filtered[i-1]
            schools.loc[i, 'Address'] = filtered[i+1]
            schools.loc[i, 'Area'] = filtered[i]
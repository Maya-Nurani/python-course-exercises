#draft:


def funcDup():
    print("func dup")
    print(dataset)
    DFRow = pd.DataFrame(dataset, columns=['x', 'y'])
    #duplicateDFRow = (dataset['x'].isin(dataset['y'])).values
    duplicateDFRow = DFRow.where(DFRow['x']==DFRow['y'])
    print(duplicateDFRow.notna())
    return duplicateDFRow



print("The duplicates between Y and Z are: \n {0}".format(funcDup()))


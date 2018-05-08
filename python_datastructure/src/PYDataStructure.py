from collections import Counter

class DataStructure:
    def __init__(self):
        print("***********************PYTHON Data Structure************************", '\n')

    def mostcommonwordindict(self):
        items =['black', 'blue', 'black', 'white', 'pink', 'red', 'red', 'blue', 'pink']
        print("Item in Dict :", items)
        count = Counter(items).most_common(items.__len__())
        print("Most Common Words in Dictionary : ", count, '\n')

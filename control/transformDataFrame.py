import pandas as pd

class transfomDataFrame:
    def transform(self, data):
        header = data[0]
        values = data[1]

        dataTransformed = pd.DataFrame(values, columns=header)

        return dataTransformed
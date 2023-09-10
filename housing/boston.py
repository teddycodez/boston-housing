def regg(params:list):
    import pandas as pd
    import numpy as np
    from pathlib import Path
    
    BASE_DIR = Path(__file__).resolve().parent.parent
    df = pd.read_csv(BASE_DIR / "assets\data\housing.csv", delim_whitespace=True, header=None)
    col_name = ["CRIM", "ZN", "INDUS", "CHAS", "NOX", "RM", "AGE", "DIS", "RAD", "TAX", "PTRATIO", "B", "LSTAT", "MEDV"]
    df.columns = col_name
    X = df.drop(["MEDV"], axis=1)
    y = df["MEDV"].values
    from xgboost import XGBRegressor
    reg = XGBRegressor()
    reg.fit(X, y)
    return reg.predict(np.array([np.array(params)]))

# print(regg([1, 2, 3, 4, 5, 6, 7, 9, 8, 1, 12, 13, 14]))
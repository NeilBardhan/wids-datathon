import pandas as pd
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split

def x_y_split(df, col_target="", aligned=True):
    """[summary]

    Args:
        df ([type]): [description]
        col_target ([type]): [description]
    """
    if not aligned:
        if col_target:
            X = df[[x for x in df.columns if x != col_target]]
            y = df[[col_target]]
            return X, y
        else:
            print("col_target not provided")
    else:
        X = df.iloc[:, :-1]
        y = df.iloc[:, -1]
        return X, y


def train_val_split(X, y, val_size=0.25, seed=42):
    """[summary]

    Args:
        X ([type]): [description]
        y ([type]): [description]
        val_size (float, optional): [description]. Defaults to 0.25.
        random_seed (int, optional): [description]. Defaults to 42.
    """
    return train_test_split(X, y, test_size=val_size, random_state=seed)

def encoding(df, cols_categorical):
    """[summary]

    Args:
        df ([type]): [description]
        cols_categorical ([type]): [description]
    """
    # le = LabelEncoder()

    # for i in cols_categorical:
    #     df[i] = le.fit_transform(df[i])

    df = pd.get_dummies(data=df, columns=cols_categorical)
    return df
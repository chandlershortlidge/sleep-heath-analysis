def clean_sleep_disorder(df):
    # fills NaN values with "None"
    df["Sleep Disorder"] = df["Sleep Disorder"].fillna("None")
    return df

def lowercase_columns(df):
    df.columns = df.columns.str.lower()
    return df

def add_underscore(df):
    df.columns = df.columns.str.replace(" ", "_")
    return df
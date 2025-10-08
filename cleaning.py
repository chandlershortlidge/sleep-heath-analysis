def clean_sleep_disorder(df):
    # fills NaN values with "None"
    df["Sleep Disorder"] = df["Sleep Disorder"].fillna("None")
    return df

def lowercase_columns(df):
    # turns columns into lowercase
    df.columns = df.columns.str.lower()
    return df

def add_underscore(df):
    # replaces whitespace with underscore in column names
    df.columns = df.columns.str.replace(" ", "_")
    return df

def rename_columns(df):
    # rename columns
    df = df.rename(columns={
    "quality_of_sleep": "sleep_quality",
    "sleep_duration": "sleep_hours",
    "heart_rate": "rhr",
    "physical_activity_level": "activity_min_per_day",
    "person_id": "id" 
    "death_rate100k__age_group_age_standardized__sex_both_sexes__cause_cardiovascular_diseases": "death_rate"
})
    return df

def remove_duplicates(df):
    # removes duplicates
    df = df.drop_duplicates()
    return df

def standardize_bmi_category(df):
    df['bmi_category'] = df['bmi_category'].replace('Normal Weight', 'Normal')
    return df

def clean_data(df):
    df = clean_sleep_disorder(df)
    df = lowercase_columns(df)
    df = add_underscore(df)
    df = rename_columns(df)
    df = remove_duplicates(df)
    df = standardize_bmi_category(df)
    return df

def rename_cvd_columns(df):
    # rename columns
    df = df.rename(columns={
    "entity": "country",
    "death_rate100k__age_group_age_standardized__sex_both_sexes__cause_cardiovascular_diseases": "death_rate"
})
    return df
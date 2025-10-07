def create_bp_columns(df):
    bp = df["blood_pressure"].str.split("/")
    s = bp.str[0]
    d = bp.str[1]
    s = s.astype(int)
    d = d.astype(int)
    df["systolic"] = s
    df["diastolic"] = d
    return df 


def bp_category(row):
    s, d = row["systolic"], row["diastolic"]
    
    if s >= 180 or d >= 120:
        return "Hypertensive Crisis"
    elif s >= 140 or d >= 90:
        return "High (Stage 2)"
    elif s >= 130 or d >= 80:
        return "High (Stage 1)"
    elif s >= 120 and d < 80:
        return "Elevated"
    else:
        return "Normal"


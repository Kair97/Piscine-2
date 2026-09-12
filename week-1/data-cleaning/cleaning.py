import numpy as np
import pandas as pd

# Exercise 0: Environment and libraries
print(pd.__version__)

csv_content = """name,email,age,signup_date,spend
Alice ,alice@example.com,25,2023-01-15,100.50
BOB,BOB@example.com,30,2023/02/10,200.00
carol,carol@example.com,?,2023-03-22,0.0
Alice ,alice@example.com,25,2023-01-15,100.50
Dave,dave@example.com,40,March 1 2023,
Eve,eve@example.com,35,2023-05-08,350.75
,ghost@example.com,28,2023-06-17,0.0
Frank,frank@example.com,?,2023-07-04,
Grace,,33,,175.25
henry,henry@example.com,200,2023-09-12,500.00
"""

with open("signups.csv", "w") as f:
    f.write(csv_content)

df = pd.read_csv("signups.csv")
print(df)

# Exercise 1: Missing values
print(df.isna().sum())
print(df[df.isna().any(axis=1)])
print(df.dropna().shape)
print(df.dropna(subset=["name"]).shape)

filled = df.fillna({"spend": 0.0, "name": "unknown"})
print(filled[["name", "spend"]])

# Exercise 2: Duplicates
print(df.duplicated().sum())
print(df[df.duplicated()])
print(df.drop_duplicates().shape)
print(df[df.duplicated(subset="email", keep=False)])
print(df.drop_duplicates(subset="email", keep="last").shape)

# Exercise 3: Dtype conversions
print(df.dtypes)

df["age"] = pd.to_numeric(df["age"], errors="coerce")
print(df["age"])

df.loc[df["age"] > 100, "age"] = np.nan
print(df["age"].max())

s = pd.Series(["10", "20", "bad", "30"])
print(pd.to_numeric(s, errors="coerce").tolist())
try:
    s.astype(int)
except ValueError as e:
    print("ValueError:", str(e)[:30])

# Exercise 4: String cleaning
df["name"] = df["name"].str.strip().str.lower()
print(df["name"])

df["name"] = df["name"].str.title()
print(df["name"].tolist())

print(df[df["email"].str.contains("alice", na=False)])

df["email_domain"] = df["email"].str.split("@").str[1]
print(df[["email", "email_domain"]])

df["email"] = df["email"].str.lower()
print(df["email"].head(3))

# Exercise 5: Datetime parsing
df["signup_date"] = pd.to_datetime(df["signup_date"], errors="coerce")
print(df["signup_date"])

df["signup_year"] = df["signup_date"].dt.year
df["signup_month"] = df["signup_date"].dt.month
df["signup_day_name"] = df["signup_date"].dt.day_name()
print(df[["signup_date", "signup_year", "signup_month", "signup_day_name"]])

print(df.sort_values("signup_date")[["name", "signup_date"]])

mask = (df["signup_date"] >= "2023-03-01") & (df["signup_date"] <= "2023-03-31")
print(df.loc[mask, ["name", "signup_date"]])

# Exercise 6: Cleanup pipeline
df = pd.read_csv("signups.csv")


def clean_signups(df: pd.DataFrame) -> pd.DataFrame:
    cleaned = (
        df
        .drop_duplicates()
        .assign(
            age=lambda d: pd.to_numeric(d["age"], errors="coerce").where(lambda x: x <= 100),
            signup_date=lambda d: pd.to_datetime(d["signup_date"], errors="coerce"),
            name=lambda d: d["name"].str.strip().str.lower().str.title(),
            email=lambda d: d["email"].str.lower(),
        )
        .dropna(subset=["name", "email", "signup_date"])
        .reset_index(drop=True)
    )
    return cleaned


clean = clean_signups(df)
print(clean)
print(clean.dtypes)
print(f"input rows: {len(df)} output rows: {len(clean)} dropped: {len(df) - len(clean)}")

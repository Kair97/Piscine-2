import numpy as np
import pandas as pd

DATA_URL = "https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv"


def load(url: str = DATA_URL) -> pd.DataFrame:
    df = pd.read_csv(url)
    return df


def inspect(df: pd.DataFrame) -> None:
    print(df.shape)
    print(df.dtypes)
    print(df.isna().sum())
    print(df["Sex"].value_counts())
    print(df["Pclass"].value_counts())
    print(df["Embarked"].value_counts())


def clean_titanic(df: pd.DataFrame) -> pd.DataFrame:
    median_age = df["Age"].median()

    cleaned = (
        df
        .drop(columns=["Cabin", "Ticket"])
        .dropna(subset=["Embarked"])
        .copy()
    )
    cleaned["Age"] = cleaned["Age"].fillna(median_age)
    cleaned["Sex"] = cleaned["Sex"].astype("category")
    cleaned["Embarked"] = cleaned["Embarked"].astype("category")
    cleaned = cleaned.reset_index(drop=True)
    return cleaned


def engineer_features(df: pd.DataFrame) -> pd.DataFrame:
    featured = df.copy()
    featured["FamilySize"] = featured["SibSp"] + featured["Parch"] + 1
    featured["IsAlone"] = (featured["FamilySize"] == 1).astype(int)
    featured["AgeBand"] = pd.cut(
        featured["Age"],
        bins=[0, 12, 18, 35, 60, 100],
        labels=["Child", "Teen", "Adult", "Senior", "Elder"],
    )
    featured["FareBand"] = pd.qcut(
        featured["Fare"],
        q=4,
        labels=["Low", "Mid", "High", "VeryHigh"],
    )
    return featured


def analyze(df: pd.DataFrame) -> None:
    print(f"Overall survival rate: {df['Survived'].mean():.4f}")
    print("\nPer-sex survival rate:")
    print(df.groupby("Sex", observed=True)["Survived"].mean().round(4))

    print("\nPer-class survival rate:")
    print(df.groupby("Pclass", observed=True)["Survived"].mean().round(4))

    print("\nPer-(sex, class) survival:")
    sex_class = df.groupby(["Sex", "Pclass"], observed=True).agg(
        survival_rate=("Survived", "mean"),
        n=("Survived", "size"),
    )
    print(sex_class.round(4))

    print("\nPer-AgeBand survival:")
    print(df.groupby("AgeBand", observed=True)["Survived"].mean().round(4))

    print("\nPer-IsAlone survival:")
    print(df.groupby("IsAlone", observed=True)["Survived"].mean().round(4))


def merge_with_ports(df: pd.DataFrame) -> pd.DataFrame:
    ports = pd.DataFrame({
        "Embarked": ["S", "C", "Q"],
        "PortName": ["Southampton", "Cherbourg", "Queenstown"],
        "Country": ["England", "France", "Ireland"],
    })
    ports["Embarked"] = ports["Embarked"].astype(df["Embarked"].dtype)
    merged = pd.merge(df, ports, on="Embarked", how="left")
    return merged


def main() -> None:
    # 1. Load and inspect
    df = load()
    inspect(df)

    # 2. Clean
    cleaned = clean_titanic(df)

    # 3. Engineer features
    featured = engineer_features(cleaned)
    print(featured["AgeBand"].value_counts())
    print(featured["FareBand"].value_counts())
    print(featured["IsAlone"].value_counts(normalize=True).round(4))

    # 4. Survival analysis
    analyze(featured)

    # 5. Join with ports
    merged = merge_with_ports(cleaned)
    print(merged.shape)

    port_stats = merged.groupby("PortName", observed=True).agg(
        survival_rate=("Survived", "mean"),
        n=("Survived", "size"),
    )
    print(port_stats.round(4))

    pivot = merged.pivot_table(
        index="Country",
        columns="Sex",
        values="Survived",
        aggfunc="mean",
        observed=True,
    )
    print(pivot.round(4))


if __name__ == "__main__":
    main()

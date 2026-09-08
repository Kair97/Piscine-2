import numpy as np
import pandas as pd

# Exercise 0: Environment and libraries
print(pd.__version__)
print(np.__version__)

# Exercise 1: Series
s_list = pd.Series([10, 20, 30, 40, 50])
s_array = pd.Series(np.array([1.5, 2.5, 3.5]))
s_dict = pd.Series({"a": 100, "b": 200, "c": 300})

print(s_list)
print(s_array)
print(s_dict)

print(s_list.index)
print(s_list.values)
print(s_list.dtype)
print(s_list.name)

s_list.name = "counts"
print(s_list)

print(s_dict["b"])
print(s_dict[["a", "c"]])

# Exercise 2: DataFrame creation
data = {
    "name": ["Alice", "Bob", "Carol", "David", "Eve"],
    "department": ["Engineering", "Sales", "Engineering", "Marketing", "Sales"],
    "salary": [85000, 60000, 95000, 70000, 65000],
    "years": [3, 7, 5, 2, 4],
    "remote": [True, False, True, False, True],
}
df = pd.DataFrame(data)
print(df)

records = [
    {"name": "Alice", "department": "Engineering", "salary": 85000, "years": 3, "remote": True},
    {"name": "Bob", "department": "Sales", "salary": 60000, "years": 7, "remote": False},
    {"name": "Carol", "department": "Engineering", "salary": 95000, "years": 5, "remote": True},
    {"name": "David", "department": "Marketing", "salary": 70000, "years": 2, "remote": False},
    {"name": "Eve", "department": "Sales", "salary": 65000, "years": 4, "remote": True},
]
df_from_records = pd.DataFrame(records)
print(df.equals(df_from_records))

df.to_csv("employees.csv", index=False)
df_loaded = pd.read_csv("employees.csv")
print(df_loaded)

df.to_csv("employees.csv")
df_unnamed = pd.read_csv("employees.csv")
print(df_unnamed.columns)

df.to_csv("employees.csv", index=False)

# Exercise 3: Inspecting a DataFrame
print(df.shape)
print(df.columns)
print(df.dtypes)
print(len(df))

print(df.head(3))
print(df.tail(2))

df.info()

print(df.describe())
print(df.describe(include="all").columns)

# Exercise 4: Column selection
print(df["salary"])
print(df[["salary"]])
print(df[["name", "salary"]])

print(df["salary"].sum())
print(df["salary"].mean())
print(df["salary"].max())
print(df["salary"].min())

df["salary_k"] = df["salary"] / 1000
print(df)

# Exercise 5: Row selection with loc and iloc
print(df.iloc[0])
print(df.loc[0])

print(df.iloc[1:4])
print(df.loc[1:3])

print(df.iloc[2, 0])
print(df.loc[2, "name"])

print(df.loc[0:2, ["name", "salary"]])

# Exercise 6: Indexes
df_named = df.set_index("name")
print(df_named)

print(df_named.loc["Carol"])

df_reset = df_named.reset_index()
print(df_reset.columns)

print(df.rename(columns={"years": "tenure"}).columns)

print(df_named.rename_axis("employee_name").index.name)

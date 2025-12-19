import pandas as pd
from sklearn.metrics import adjusted_rand_score, adjusted_mutual_info_score


if __name__ == "__main__":
    # Load the partitioned data
    df = pd.read_csv("devoir_4/output.csv", sep=";")

    print(df.head())
    familles = df["famille"].values
    se = set(familles)
    print(se)
    s = ["0,05", "0,5", "1", "2"]
    col_names = [f"Modularity Class_{s[i]}" for i in range(4)]
    communities = [df[col].values for col in col_names]
    print(col_names)
    print(communities[0])

    for score in [adjusted_rand_score, adjusted_mutual_info_score]:
        for comm, col in zip(communities, col_names):
            s = score(familles, comm)
            print(f"{str(score)} of {col}: {s}")

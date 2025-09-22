import pandas as pd

def get(term):

    df = pd.read_csv("backend/data.csv")
    return tuple(df.loc[df["word"]==term]["definition"])

# class Definition:

#     def __init__(self, term):
#         self.term = term

#     def get(self):
#         df = pd.read_csv("data.csv")
#         return tuple(df.loc[df["word"]==self.term]["definition"])

# def main():
#     d = Definition("acid")
#     print(d.get())

# if __name__=="__main__":
#     main()

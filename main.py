import pandas as pd

def pandasExe():
    #
    # s1 = pd.Series(['a', 'b', 'c'], index=[1, 2, 3])
    # print(s1)
    #
    # s2 = pd.Series({1:"abc", 2:"edf"})
    # print(s2)

    # df1 = pd.DataFrame([['a', 'A'], ['b', 'B'], ['c', 'C'], ['d', 'D']], columns=['low', 'upper'])
    # print(df1)
    # print(df1.columns)
    # print(df1.index)
    #
    # df2 = pd.DataFrame({"low":['a', 'b', 'c'], "upper":['A', 'B', 'C']})
    # print(df2)
    # print(df2.columns)
    # print(df2.index)

    df3 = pd.read_excel(r"/Users/xsun/Downloads/OriginalOrgnizationAdminHeadInfo_TEST.xlsx", usecols=[1, 3]);
    print(df3, "\n")



if __name__ == '__main__':
    pandasExe()


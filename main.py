import pandas as pd
import glob
import os.path

def printKBs(df):
    for val in df['KB'].unique():
        df_kb = df.query(f'KB == @val')
        print("-" * 30 + "KB for installation" + "-" * 30 + "\n")
        print(df_kb[['Hostname', 'KB', 'CVE Description']].to_string(index=False), "\n")
def readReportFile():
    folder_path = r'/Users/xsun/Downloads'
    file_type = '/*csv'
    files = glob.glob(folder_path + file_type)

    max_file = max(files, key=os.path.getctime)
    return max_file

def pandasExe():
    pd.set_option('display.max_colwidth', None)
    reportFile = readReportFile()
    df = pd.read_csv(reportFile)
    df = df[~df["Hostname"].isin(['RISE-PRPDEVSQL', 'RISE-RPTPRESQL', 'RISE-EXRDEVSQL'])]
    df[['Install', 'KB']] = df['Remediation Details'].str.split(r':', expand=True)
    #print(df.info(), "\n")

    df_critical = df.query('Severity == "CRITICAL"')
    df_high = df.query('Severity == "HIGH"')
    print("#" * 30 + " Critical Vulnerability " + "#" * 30 + "\n")
    printKBs(df_critical)
    print("#" * 30 + " High Vulnerability " + "#" * 30 + "\n")
    printKBs(df_high)

if __name__ == '__main__':
    pandasExe()


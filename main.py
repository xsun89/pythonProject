import pandas as pd
import glob
import os.path
import requests
import json
import re

def getKBInfo(url):
    urlList = url.split('=')
    lastStr = urlList[-1].rstrip("\n")
    kbNumber = lastStr[-7:]
    page = requests.get("https://support.microsoft.com/app/content/api/content/help/en-us/" + kbNumber)
    print(page.content)
    site_json = json.loads(page.content)
    return re.sub('\W+', ' ', str(site_json["details"]["heading"]))

def printKBs(df, file_object):
    for val in df['KB'].unique():
        df_kb = df.query(f'KB == @val')
        kbInfo = getKBInfo(df_kb["Remediation Links"].to_string(index=False))
        file_object.write("<h2>" + kbInfo + " for installation</h2>" + '\n')
        _html = df_kb[['Hostname', 'KB', 'CVE Description', 'Remediation Links']].to_html(index=False)
        file_object.write(_html)

def readReportFile():
    folder_path = r'.'
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
    file_object = open("data.html", "w")
    df_critical = df.query('Severity == "CRITICAL"')
    df_high = df.query('Severity == "HIGH"')

    file_object.write("<h1>Critical Vulnerability</h1>" + '\n')
    printKBs(df_critical, file_object)
    file_object.write("<h1>High Vulnerability</h1>" + '\n')
    printKBs(df_high, file_object)
    file_object.close()


if __name__ == '__main__':
    pandasExe()


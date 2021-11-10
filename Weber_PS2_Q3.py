# ### Question 3

# a
# Read data from cohorts of interest and create cohort columns
df2011 = pd.read_sas("datasets/DEMO_G.XPT")
df2011['cohort'] = 2011
df2013 = pd.read_sas("datasets/DEMO_H.XPT")
df2013['cohort'] = 2013
df2015 = pd.read_sas("datasets/DEMO_I.XPT")
df2015['cohort'] = 2015
df2017 = pd.read_sas("datasets/DEMO_J.XPT")
df2017['cohort'] = 2017
# Create df with columns of interest
df_demo = df2011.append(df2013).append(df2015).append(df2017)
df_demo = df_demo[['SEQN', 'RIAGENDR', 'RIDAGEYR', 'RIDRETH3', 'DMDEDUC2', 'DMDMARTL',
       'RIDSTATR', 'SDMVPSU', 'SDMVSTRA', 'WTMEC2YR', 'WTINT2YR', 'cohort']]
# Change column names
df_demo.rename(columns={'SEQN' : "id", 'RIAGENDR' : "gender", 'RIDAGEYR' : "age", 'RIDRETH3' : "race", 
                   'DMDEDUC2' : "education", 'DMDMARTL' : "marital status",
                   'RIDSTATR' : "interview status", 'SDMVPSU' : "pseudo-psu", 
                   'SDMVSTRA' : "pseudo-stratum", 'WTMEC2YR' : "interviewed and mec examined", 
                   'WTINT2YR' : "interviewed"}, inplace=True)
# Change dtypes to appropriate types
df_demo = df_demo.fillna(-1)
df_demo = df_demo.astype({'id' : 'int64', 'age' : 'int64', 'race' : 'int64', 
                'marital status' : 'int64', 'education': 'int64', 'interview status' : 'int64', 
                'pseudo-psu' : 'int64', 'pseudo-stratum' : 'int64'})
df_demo = df_demo.astype({'gender' : 'category', 'race' : 'category', 'education' : 'category', 
                          'marital status' : 'category', 'interview status' : 'category'})
df_demo.to_pickle("./demographic.pkl")

# b
# Read data from cohorts of interest and create cohort columns
df2011 = pd.read_sas("datasets/OHXDEN_G.XPT")
df2011['cohort'] = 2011
df2013 = pd.read_sas("datasets/OHXDEN_H.XPT")
df2013['cohort'] = 2013
df2015 = pd.read_sas("datasets/OHXDEN_I.XPT")
df2015['cohort'] = 2015
df2017 = pd.read_sas("datasets/OHXDEN_J.XPT")
df2017['cohort'] = 2017
df_dent = df2011.append(df2013).append(df2015).append(df2017)

# +
# Create df with columns of interest
colnames = list(df_dent.columns)
newcols = []
for name in colnames:
    if re.search("OHX[0-9]+TC", name) is not None or re.search("OHX[0-9]+CTC", name) is not None:
        newcols.append(name)
newcols.insert(0, "SEQN")
newcols.insert(1, "OHDDESTS")
newcols.append("cohort")
df_dent = df_dent[newcols]

# Define new column names using regex
namedict = {"SEQN" : "id", "OHDDESTS" : "status"}
numcols = len(newcols)
for col in newcols[2:numcols-1]:
    if re.search("OHX[0-9]+TC", col) is not None:
        num = re.findall(r'\d+', col)
        namedict[col] = "tooth count " + num[0]
    else:
        num = re.findall(r'\d+', col)
        namedict[col] = "coronal cavity " + num[0]
df_dent.rename(columns=namedict, inplace=True)
df_dent = df_dent.fillna(-1)

# Change dtypes to appropriate types
typedict = {}
for col in list(df_dent.columns):
    typedict[col] = "int64"
    if re.search("coronal cavity", col) is not None:
        typedict[col] = "category"
df_dent = df_dent.astype(typedict)

for col in list(df_dent.columns):
    typedict[col] = "category"
typedict["id"] = "int64"
typedict["cohort"] = "int64"
df_dent = df_dent.astype(typedict)
df_dent.to_pickle("./dentition.pkl")
# -

# c Number of cases in each df
print("Cases in first df:", df_demo.shape[0])
print("Cases in second df:", df_dent.shape[0])
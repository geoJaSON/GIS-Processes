#%%
import pandas as pd
import smartsheet
#%% import txt file into pandas dataframe
txt = r"C:\Users\M3ECHJJJ\Downloads\ssmigrate.txt"
df = pd.read_csv(txt, sep=',')
# %%
df['id']=''
df['ktoken']=''
df['htoken']=''
df['ntoken']=''
df['name']=''



# %%
token = "xqVcW9af3YEoeEvFLDw1UlwNaxjHKNTfNslfC"
smartsheet_client = smartsheet.Smartsheet(token)
response = smartsheet_client.Sheets.list_sheets()
sheets = response.data

#%%
for i in sheets:
    #get index of df where permalink matches i.permalink
    idx = df[df['permalink'] == i.permalink].index

        #update df.id at idx with i.id
    df.at[idx, 'id'] = i.id
        #update df.token at idx with token
    df.at[idx, 'htoken'] = token
    df.at[idx, 'name'] = i.name

# %%
df[df['permalink'] == i.permalink]
# %%
idx
# %%
for i in sheets:
    print(df[df['permalink'] == i.permalink].index)
# %%
df2.to_clipboard(excel=True, sep=',')
# %%
df2.to_csv(rr"C:\Users\M3ECHJJJ\Downloads\ssmigrate.csv")
# %%
df['jtoken']=''
# %%
df.to_csv('C:\\Users\\M3ECHJJJ\\Downloads\\ssmigrate.csv')
# %%

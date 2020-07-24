import pandas as pd
ds=pd.read_csv("C:/Users/seeth/Downloads/6th sem/EC/data.csv")
data=ds
data['Calories'].fillna(data['Calories'].median(),inplace=True)
data['Move_m_count'].fillna(data['Move_m_count'].mode(),inplace=True)
data['Min_speed'].fillna(data['Min_speed'].median(),inplace=True)
data['Max_speed'].fillna(data['Max_speed'].median(),inplace=True)
data['Inactive'].fillna(data['Inactive'].mean(),inplace=True)
data['Distance'].fillna(data['Distance'].median(),inplace=True)
data['Avg_speed'].fillna(data['Avg_speed'].median(),inplace=True)
data['Step_count'].fillna(data['Step_count'].mean(),inplace=True)
bi=[0,3000,5000,9000,18000]
for i in range(0,251):
    if(int(data.loc[i,['Distance']])==0):
        data.loc[i,['Distance']]=data['Distance'].mean()
data['Walk']=pd.cut(data.Distance,bi,labels=["Ver Low","Below Normal","Normal","Good"])
data['bmi']=pd.DataFrame(data['Weight'])
for i in range(0,251):
    a=int(data.loc[i,['Weight']])
    b=pow(int(data.loc[i,['Height']]),2)
    c=(a/b)*10000
    data.loc[i,['bmi']]=c
bi=[0,18.5,24.9,29.9,35]
data['bmi_cdn']=pd.cut(data.bmi,bi,labels=["Under Weight","Normal","Over Weight","Obese"])
data.to_csv('ds.csv')

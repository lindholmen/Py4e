import pandas as pd

def tax(s):
    ss = s - 3500
    if ss <= 0:
        return 0
    elif ss < 1500:
        return ss * 0.03
    elif ss < 4500:
        return ss * 0.1 - 105
    elif ss < 9000:
        return ss * 0.2 - 555
    elif ss < 35000:
        return ss * 0.25 - 1005
    elif ss < 55000:
        return ss * 0.3 - 2755
    elif ss < 80000:
        return ss * 0.35 - 5505
    else:
        return ss * 0.45 - 13505
            
df = pd.read_excel('salary.xlsx', sheet_name = 0)
ts = []
for s in df['工资']:
    ts.append(tax(s))
print(ts)
df['税'] = ts

out = pd.ExcelWriter('salary_and_tax.xls')
df.to_excel(out)
out.save()

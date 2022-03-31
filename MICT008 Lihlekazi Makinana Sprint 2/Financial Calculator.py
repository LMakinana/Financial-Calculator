import math as pd

print ("Case 1")
initial_deposit = float(input("initial amount for Case 1 (R): "))
yearly_topup = float(input("Amount increase for Case 1 (R): "))
print ('')

print ("Case 2")
initial_deposit_2 = float(input("initial amount for Case 2 (R): "))
yearly_topup_2 = float(input("Amount increase for Case 2 (R): "))
print ('')

interest_rate = float(input("interest rate (e.g. 4x = 1.04): "))
print ('')
no_of_yr = int(input("Duration (years): "))

#case 1
data = [[0, initial_deposit]]
df = pd.dataFrame(data, columns = ['Year', 'Case1'])

for i in range(no_of_yr):
    next_yr_total = round (((df.iloc[-1,1] * interest_rate) + yearly_topup), 2)
    year = df.iloc[-1,0]=1
    df = df.append(pd.Series([year, next_yr_total], index=df.columns), ingnore_index=True)

#case 2 
data_2 = [initial_deposit_2]
df2 = pd.DataFrame(data_2, columns = ['Case2'])

for i in range(no_of_yr):
    next_yr_total_2 = round (((df.iloc[-1,1] * interest_rate) + yearly_topup_2), 2)
    df = df.append(pd.Series([year, next_yr_total_2], index=df.columns), ingnore_index=True)

result = pd.concat([df, df2], axis=1, sort=False)

print('')
print("Case 1, End of duration: R" + str(result.iloc[-1,1]))
print("Case 2, End of duration: R" + str(result.iloc[-1,2]))
print('')
print('====================')

graph = result.set_index('Year').plot(figsize=(7.5), grid=True)
graph.st_ylim(0)

#to save graph as a picture file
#fig = graph.get_figure()
#fig.savefig("output_plot.png")





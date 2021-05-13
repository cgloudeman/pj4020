import contenders as c
import csv

start_dates = []
for year in range(1977,2021): 
    if year == 2012: # Lockout year adjustment 66 GP
        start_dates.append(str(year) + '-04-06')
    elif year == 1999: # Lockout adjustment 50 GP
        pass
    else:
        start_dates.append(str(year) + '-02-06')
 
master_list = []      
for date in start_dates:
    print('Working on season: ' + date[:4] + '...')
    cons = c.contender(date)
    contenders_list = [int(date[:4])]
    for key in cons:
        if cons[key]:
            contenders_list.append(key)
    print(str(len(contenders_list)-1) + ' teams in season ' + date[:4])
    master_list.append(contenders_list)

titles = ['Season', 'Team_1', 'Team_2', 'Team_3', 'Team_4', 'Team_5', 'Team_6', 
          'Team_7', 'Team_8']
master_list.insert(0, titles)


with open("out.csv", "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerows(master_list)
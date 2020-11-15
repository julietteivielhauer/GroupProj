#try except, open/read file & create a list of lists for records
fname = 'Records.csv'
try:
    fhand = open(fname, 'r')
except FileNotFoundError:
    print('File cannot be opened: ', fname)
    quit()
records = list()
for line in fhand:
    stripped_lines = line.strip()
    record_line = stripped_lines.split(",")
    records.append(record_line)

'''
#create class for records
class Records():
    def __init__(record, region, country, item_type, sales_channel, oder_priority, order_date, order_id, ship_date, units_sold, unit_price, unit_cost, total_revenue, total_cost, total_profit):
        record.region = region
        record.country = country
        record.item_type = item_type
        record.sales_channel = sales_channel
        record.oder_priority = oder_priority
        record.order_date = order_date
        record.order_id = order_id
        record.ship_date = ship_date
        record.units_sold = units_sold
        record.unit_price = unit_price
        record.unit_cost = unit_cost
        record.total_revenue = total_revenue
        record.total_cost = total_cost
        record.total_profit = total_profit
    def get_total_profit(record):
        return record.total_profit
    def get_order_id(record):
        return record.order_id
#initialize new class list
all_records = []
for i in range(1, len(records)):
    record = Records(records[i][0],records[i][1],records[i][2],records[i][3],records[i][4],records[i][5],records[i][6],records[i][7],records[i][8],records[i][9],records[i][10],records[i][11],records[i][12],records[i][13])
    all_records.append(record)
'''
records.pop(0)
#formatting for statistics
print("ORDER STATISTICS")
print("******************************************************************")
for record in records:
    highest_profit = 0
    tprofit = float(record[:][13])
    if tprofit>highest_profit:
        highest_profit = tprofit
print("The max profit is: $", highest_profit)
'''
#loop to find the highest total profit
for record in all_records:
    highest_profit = 0
    tprofit = float(record.get_total_profit())
    if tprofit>highest_profit:
        highest_profit = tprofit
print("The max profit is: $", highest_profit)
'''

'''             
#print stats
#record with highest total profit
#record 14 in each list of lists is total profit
i = 1
for record in records:
    profits = list()
    for i in range(1, (len(records))):
        profits.append(float(records[i][13]))
print(max(profits))
#for record in range(len(records)):
#    highest_profit = 0
#    i=1
#    if (float(records[i][13]))>highest_profit:
#        highest_profit=records[i][13]
#        i+=1
#print("The max profit is: $",highest_profit)
'''

import matplotlib.pyplot as plt
dates = ['10-03-16', '10-04-16', '10-05-16', '10-06-16', '10-07-16']
open_price = [774.25, 776.030029, 779.309998, 779.969971, 779.659973]
high_price = [776.065002, 778.710022, 782.970032, 785.899975, 779.759975]
low_price = [769.5, 772.890015, 775.650024, 775.539978, 775.075]
close_price = [772.559998, 776.429993, 783.409973, 775.889975, 775.080017]
plt.plot(dates, open_price, label='Open')
plt.plot(dates, high_price, label='High')
plt.plot(dates, low_price, label='Low')
plt.plot(dates, close_price, label='Close')
plt.xlabel('Date')
plt.ylabel('Price')
plt.title('Alphabet Inc. Financial Data')
plt.legend()

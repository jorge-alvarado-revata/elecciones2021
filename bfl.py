import math
import numpy as np
# adaptacion de test de la ley de Benford's Law
# codigo original en 
# https://github.com/eleprocha/Benford-s-Law_python_code/blob/master/code

#Benford 1d
BENFORD = [30.1, 17.6, 12.5, 9.7, 7.9, 6.7, 5.8, 5.1, 4.6]

#Benford 2d
BENFORD2 = [11.96, 11.38, 10.88, 10.43, 10.03, 9.66, 9.34, 9.03, 8.76, 8.5]

def count_first_digit(df, data_str):#TAKE AS AN ARGUMENT A STR-COLUMN NAME
    data_count = {}
    for i in range(1,10):
        data_count[i] = 0

    mask=df[data_str]>1.
    data=list(df[mask][data_str])
    for i in range(len(data)):
        while int(data[i])>9:
            data[i]=data[i]/10
    first_digits=[int(x) for x in sorted(data)]
    unique=(set(first_digits))#a list with unique values of first_digit list
    for i in unique:
        count=first_digits.count(i)
        data_count[i]=count
    total_count=sum(data_count.values())
    lsunique = list(unique)
    ldata_count = [x for x in data_count.values()]
    data_percentage=[(i/total_count)*100 for i in ldata_count]
    return  (lsunique, total_count, ldata_count, data_percentage)
    #return lsunique, data_count, data_percentage

def count_second_digit(df, data_str):#TAKE AS AN ARGUMENT A STR-COLUMN NAME
    data_count = {}
    for i in range(0,10):
        data_count[i] = 0

    data=[str(x) for x in df[data_str].tolist()]
    newdata = []
    for x in data:
        if len(x)>=2:
            newdata.append(int(x[1]))
    second_digits=[x for x in sorted(newdata)]
    unique=(set(second_digits))#a list with unique values of first_digit list
    for i in unique:
        count=second_digits.count(i)
        data_count[i]=count
    total_count=sum(data_count.values())
    lsunique = list(unique)
    ldata_count = [x for x in data_count.values()]
    data_percentage=[(i/total_count)*100 for i in ldata_count]
    return  (lsunique, total_count, ldata_count, data_percentage)
    #return lsunique, data_count, data_percentage

def get_expected_counts(total_count, lsunique):

    """Return list of expected Benford's Law counts for total sample count."""
    
    return [round(p * total_count / 100) for p in BENFORD]

def get_expected_counts2(total_count, lsunique):

    """Return list of expected Benford's Law counts for total sample count."""
    
    return [round(p * total_count / 100) for p in BENFORD2]


def chi_square_test(data_count,expected_counts):

    """Return boolean on chi-square test (8 degrees of freedom & P-val=0.05)."""

    chi_square_stat = 0  # chi square test statistic

    for data, expected in zip(data_count,expected_counts):

        chi_square = math.pow(data - expected, 2)

        chi_square_stat += chi_square / expected

    print("\nChi-squared Test Statistic = {:.3f}".format(chi_square_stat))

    print("Critical value at a P-value of 0.05 is 15.51.")    

    return chi_square_stat < 15.51


def chi_square_test2(data_count,expected_counts):

    """Return boolean on chi-square test (9 degrees of freedom & P-val=0.05)."""

    chi_square_stat = 0  # chi square test statistic

    for data, expected in zip(data_count,expected_counts):

        chi_square = math.pow(data - expected, 2)

        chi_square_stat += chi_square / expected

    print("\nChi-squared Test Statistic = {:.3f}".format(chi_square_stat))

    print("Critical value at a P-value of 0.05 is 16.92.")    

    return chi_square_stat < 16.92

def bar_chart(plt, data_pct):

    """Make bar chart of observed vs expected 1st digit frequency in percent."""
    fig, ax = plt.subplots()
    index = [i + 1 for i in range(len(data_pct))]  # 1st digits for x-axis # text for labels, title and ticks
    fig.canvas.set_window_title('Percentage First Digits')
    ax.set_title('Data vs. Benford Values', fontsize=15)
    ax.set_ylabel('Frequency (%)', fontsize=16)
    ax.set_xticks(index)
    ax.set_xticklabels(index, fontsize=14)
    # build bars    
    rects = ax.bar(index, data_pct, width=0.95, color='black', label='Data')
    # attach a text label above each bar displaying its height
    for rect in rects:
        height = rect.get_height()
        ax.text(rect.get_x() + rect.get_width()/2, height,'{:0.1f}'.format(height), ha='center', va='bottom', fontsize=13)
    # plot Benford values as red dots
    ax.scatter(index, BENFORD, s=150, c='red', zorder=2, label='Benford')
    # Hide the right and top spines & add legend
    ax.spines['right'].set_visible(False)
    ax.spines['top'].set_visible(False)
    ax.legend(prop={'size':15}, frameon=False)
    plt.show()
    
    
    #2nd_bar_chart
    labels=list(data_pct)
    width = 0.35 
    x = np.arange(0,len(data_pct),1) # the label locations
    width = 0.35  # the width of the bars
    fig, ax = plt.subplots()
    rects1 = ax.bar(x - width, data_pct, width=0.95, color='black', label='Data')
    rects2 = ax.bar(x + width, BENFORD,width,label='Benford')
    # Add some text for labels, title and custom x-axis tick labels, etc.
    ax.set_ylabel('Frequency (%)', fontsize=16)
    ax.set_title('Benford')
    ax.set_xticks(x)
    ax.legend()
    plt.show()


def bar_chart2(plt, data_pct):

    """Make bar chart of observed vs expected 1st digit frequency in percent."""
    fig, ax = plt.subplots()
    index = [i + 1 for i in range(len(data_pct))]  # 1st digits for x-axis # text for labels, title and ticks
    fig.canvas.set_window_title('Percentage First Digits')
    ax.set_title('Data vs. Benford Values', fontsize=15)
    ax.set_ylabel('Frequency (%)', fontsize=16)
    ax.set_xticks(index)
    ax.set_xticklabels(index, fontsize=14)
    # build bars    
    rects = ax.bar(index, data_pct, width=0.95, color='black', label='Data')
    # attach a text label above each bar displaying its height
    for rect in rects:
        height = rect.get_height()
        ax.text(rect.get_x() + rect.get_width()/2, height,'{:0.1f}'.format(height), ha='center', va='bottom', fontsize=13)
    # plot Benford values as red dots
    ax.scatter(index, BENFORD2, s=150, c='red', zorder=2, label='Benford')
    # Hide the right and top spines & add legend
    ax.spines['right'].set_visible(False)
    ax.spines['top'].set_visible(False)
    ax.legend(prop={'size':15}, frameon=False)
    plt.show()
    
    
    #2nd_bar_chart
    labels=list(data_pct)
    width = 0.35 
    x = np.arange(0,len(data_pct),1) # the label locations
    width = 0.35  # the width of the bars
    fig, ax = plt.subplots()
    rects1 = ax.bar(x - width, data_pct, width=0.95, color='black', label='Data')
    rects2 = ax.bar(x + width, BENFORD2,width,label='Benford')
    # Add some text for labels, title and custom x-axis tick labels, etc.
    ax.set_ylabel('Frequency (%)', fontsize=16)
    ax.set_title('Benford')
    ax.set_xticks(x)
    ax.legend()
    plt.show()
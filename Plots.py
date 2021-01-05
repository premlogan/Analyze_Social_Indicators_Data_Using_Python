##############################################################################
#                Socio- Economic Indicators Portal                           #
##############################################################################
import matplotlib.pyplot as plt
import seaborn as sns

a = ['China']
# Function Name: indicator_plot
# it takes Parameters: a, label and z 
#a which is the name of the country 
# z is the dataframe with time series values for an indicator
# label is the label for the graph 
# it returns a plot for the indicator and country 
def indicator_plot(a,label, z):
    b = ''.join(a)
    plot_1 = sns.lineplot(z.index.astype(int),z[b],label=str(b))
    plot_1.set(xlabel="Years", ylabel = label)
    plt.show()
    return plot_1

# Function Name: indicator_plot
# it takes Parameters: a, label and one
# a contains the names of the countries 
# label specifies the y label for the plot 
# one specifies the dataframe that speicifies one indicator for multiple countries  
# this function returns the plot for countries by the specified indicator 

def compare_plot(a,label, one):
    for country in a:
        plot_1 = sns.lineplot(one.index.astype(int),one[country],label=str(country))
        plot_1.set(xlabel="Years", ylabel = label)
    plt.show()
    return plot_1

# Function name is analyze plot
# it take four parameters a, c, label_list and ind
# a is the name of the country 
# c is a predefined list of index values with 1,2 values for analyze_plot
# label_list specifies the y lable 
#ind is a list of two dataframes having data for two indicators for one country 
# This function returns a plot showing correlation between the specified indicator for a country 
def analyze_plot(a, c, label_list, ind):
    b = ''.join(a)
    column_1 = ind[c[0]-1][b]
    column_2 = ind[c[1]-1][b]
    correlation = column_1.corr(column_2)
    correlation = round(correlation,3)
    plt.annotate('Correlation = ' + str(correlation), xy=(0.5,0.1), xycoords='axes fraction')
    plot_2 = sns.regplot(ind[c[0]-1][b],ind[c[1]-1][b])
    plot_2.set(xlabel = label_list[0], ylabel = label_list[1])
    plt.title(b)
    plt.show()
    return plot_2
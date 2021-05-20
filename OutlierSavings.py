#---------------------------------------------------OutlierSavings.py---------------------------------------------------#
'''
Importing modules:
-statistics (st)
-random (rd)
-pandas (pd)
-plotly.figure_factory (ff)
-plotly.express (px)
-plotly.graph_objects (go)
-seaborn (sns)
-matplotlib (plt)
-time (tm)
'''
import statistics as st
import random as rd
import pandas as pd 
import plotly.figure_factory as ff
import plotly.express as px
import plotly.graph_objects as go
import seaborn as sns
import matplotlib.pyplot as plt
import time as tm


#Defining a function to abstract the stipulated data and return a new dataset
def AbstractGivenData(df_arg,df_section_arg,label_arg):

  abstract_data=input("Should the data be abstracted?:(:-Yes or No)")

  #Requesting the user wether to abstract the data or not
  #Case-1
  if(abstract_data=="yes" or abstract_data=="Yes"):
    comparitive_value_method=input("Should the value be greater or lesser or equal?:(:-Greater,Lesser,Equal)")

    #Verifying the method of comparison with the user
    #Case-1
    if(comparitive_value_method=="Greater" or comparitive_value_method=="greater"):
      value_param=input("Choose value:")
      df_loc_greater=df_arg.loc[df_arg[df_section_arg]>float(value_param)]
      CreateBoxAndScatterPlot(df_loc_greater,df_section_arg,label_arg)

    #Case-2
    elif(comparitive_value_method=="Lesser" or comparitive_value_method=="lesser"):
      value_param=input("Choose value:")
      df_loc_lesser=df_arg.loc[df_arg[df_section_arg]<float(value_param)]
      CreateBoxAndScatterPlot(df_loc_lesser,df_section_arg,label_arg)

    #Case-3
    elif(comparitive_value_method=="Equal" or comparitive_value_method=="equal"):
      value_param=input("Choose value:")
      df_loc_equal=df_arg.loc[df_arg[df_section_arg]==float(value_param)]
      CreateBoxAndScatterPlot(df_loc_equal,df_section_arg,label_arg)

  #Case-2
  else:
    CreateBoxAndScatterPlot(df_arg,df_section_arg,label_arg) 


#Defining a function to calculate the mean,median and standard deviations of the original data
def CalculateMeanMedianAndStandardDeviationAndCreateOriginalPlotOfData(list_arg,label_arg,modification_arg):

  param_mean=st.mean(list_arg)
  param_median=st.median(list_arg)
  param_st_dev=st.stdev(list_arg)

  st_dev_1_start,st_dev_1_end=param_mean-(1*param_st_dev),param_mean+(1*param_st_dev)
  st_dev_2_start,st_dev_2_end=param_mean-(2*param_st_dev),param_mean+(2*param_st_dev)
  st_dev_3_start,st_dev_3_end=param_mean-(3*param_st_dev),param_mean+(3*param_st_dev)

  percentage_list_1=[value_a for value_a in list_arg if st_dev_1_start<value_a and value_a<st_dev_1_end]
  percentage_list_2=[value_b for value_b in list_arg if st_dev_2_start<value_b and value_b<st_dev_2_end]
  percentage_list_3=[value_c for value_c in list_arg if st_dev_3_start<value_c and value_c<st_dev_3_end]

  percentage_1=(len(percentage_list_1*100))/len(list_arg)
  percentage_2=(len(percentage_list_2*100))/len(list_arg)
  percentage_3=(len(percentage_list_3*100))/len(list_arg)

  CreateNormalDistributionGraph(st_dev_1_start,st_dev_1_end,st_dev_2_start,st_dev_2_end,st_dev_3_start,st_dev_3_end,percentage_1,percentage_2,percentage_3,param_mean,param_median,param_st_dev,list_arg,label_arg,modification_arg)


#Defininng a function to create a normal distribution graph for the orginal data
def CreateNormalDistributionGraph(st_dev_1_arg,st_dev_2_arg,st_dev_3_arg,st_dev_4_arg,st_dev_5_arg,st_dev_6_arg,percentage_1_arg,percentage_2_arg,percentage_3_arg,param_mean_arg,param_median_arg,param_st_dev_arg,list_arg,label_arg,modification_arg):
  
  print("Generating distribution graph for Original Data...")
  tm.sleep(1.3)
  print("Graph generated")

  param_graph=ff.create_distplot([list_arg],["{}:{} ({})".format(label_arg,"Original Data",modification_arg)],show_hist=False)

  param_graph.add_trace(go.Scatter(x=[param_mean_arg,param_mean_arg],y=[0,max(param_graph["data"][0]["y"])],mode="lines",name="Mean Value"))

  param_graph.add_trace(go.Scatter(x=[st_dev_1_arg,st_dev_1_arg],y=[0,max(param_graph["data"][0]["y"])],mode="lines",name="Standard Deviation 1"))
  param_graph.add_trace(go.Scatter(x=[st_dev_2_arg,st_dev_2_arg],y=[0,max(param_graph["data"][0]["y"])],mode="lines",name="Standard Deviation 1"))
  param_graph.add_trace(go.Scatter(x=[st_dev_3_arg,st_dev_3_arg],y=[0,max(param_graph["data"][0]["y"])],mode="lines",name="Standard Deviation 2"))
  param_graph.add_trace(go.Scatter(x=[st_dev_4_arg,st_dev_4_arg],y=[0,max(param_graph["data"][0]["y"])],mode="lines",name="Standard Deviation 2"))
  param_graph.add_trace(go.Scatter(x=[st_dev_5_arg,st_dev_5_arg],y=[0,max(param_graph["data"][0]["y"])],mode="lines",name="Standard Deviation 3"))
  param_graph.add_trace(go.Scatter(x=[st_dev_6_arg,st_dev_6_arg],y=[0,max(param_graph["data"][0]["y"])],mode="lines",name="Standard Deviation 3"))

  param_graph.update_layout(title="{}:{} ({})".format(label_arg,"Original Data",modification_arg))

  param_graph.show()

  print("The mean of the data (of {}) is {}".format(label_arg,round(param_mean_arg,2)))
  print("The median of the data (of {}) is {}".format(label_arg,round(param_median_arg,2)))
  print("The standard deviation of the data (of {}) is {}".format(label_arg,round(param_st_dev_arg,2)))

  print("{}% of the data lies within the first standard deviation".format(round(percentage_1_arg,2)))
  print("{}% of the data lies within the second standard deviation".format(round(percentage_2_arg),2))
  print("{}% of the data lies within the third standard deviation".format(round(percentage_3_arg,2)))

  #Verifying whether the data follows normal distribution or not
  #Case-1
  if( percentage_1_arg<67 or percentage_1_arg>69.8 or percentage_2_arg<95 or percentage_2_arg>96.5 or percentage_3_arg<98.5 or percentage_3_arg>100 ):
    print("The data does not follow normal distribution")

  #Case-2
  else:
    print("The data follows normal distribution") 

  CalculateSampleValuesAndCreateSampleDistributionGraph(list_arg,label_arg,modification_arg)


#Defining a function to calculate the mean,median and standard deviations and to create a normal distribution graph for the sample data
def CalculateSampleValuesAndCreateSampleDistributionGraph(list_arg,label_arg,modification_arg):

  final_list=[]

  for loop in range(1000):
    mean_list=[]

    for value in range(100):

      rd_index=rd.randint(0,(len(list_arg)-1))
      mean_list.append(list_arg[rd_index])

    mean_list_mean=st.mean(mean_list)
    final_list.append(mean_list_mean)  

  param_mean=st.mean(final_list)
  param_median=st.median(final_list)
  param_st_dev=st.stdev(final_list)

  st_dev_1_start,st_dev_1_end=param_mean-(1*param_st_dev),param_mean+(1*param_st_dev)
  st_dev_2_start,st_dev_2_end=param_mean-(2*param_st_dev),param_mean+(2*param_st_dev)
  st_dev_3_start,st_dev_3_end=param_mean-(3*param_st_dev),param_mean+(3*param_st_dev)

  percentage_list_1=[value_a for value_a in final_list if st_dev_1_start<value_a and value_a<st_dev_1_end]
  percentage_list_2=[value_b for value_b in final_list if st_dev_2_start<value_b and value_b<st_dev_2_end]
  percentage_list_3=[value_c for value_c in final_list if st_dev_3_start<value_c and value_c<st_dev_3_end]

  percentage_1=(len(percentage_list_1*100))/len(final_list)
  percentage_2=(len(percentage_list_2*100))/len(final_list)
  percentage_3=(len(percentage_list_3*100))/len(final_list)

  print("Generating distribution graph for Original Data...")
  tm.sleep(1.3)
  print("Graph generated")

  param_graph=ff.create_distplot([final_list],["{}:{} ({})".format(label_arg,"Sample Data",modification_arg)],show_hist=False,curve_type="normal")

  param_graph.add_trace(go.Scatter(x=[param_mean,param_mean],y=[0,max(param_graph["data"][0]["y"])],mode="lines",name="Mean Value"))  
  
  param_graph.add_trace(go.Scatter(x=[st_dev_1_start,st_dev_1_start],y=[0,max(param_graph["data"][0]["y"])],mode="lines",name="Standard Deviation 1"))
  param_graph.add_trace(go.Scatter(x=[st_dev_2_start,st_dev_2_start],y=[0,max(param_graph["data"][0]["y"])],mode="lines",name="Standard Deviation 2"))
  param_graph.add_trace(go.Scatter(x=[st_dev_3_start,st_dev_3_start],y=[0,max(param_graph["data"][0]["y"])],mode="lines",name="Standard Deviation 3"))

  param_graph.add_trace(go.Scatter(x=[st_dev_1_end,st_dev_1_end],y=[0,max(param_graph["data"][0]["y"])],mode="lines",name="Standard Deviation 1"))
  param_graph.add_trace(go.Scatter(x=[st_dev_2_end,st_dev_2_end],y=[0,max(param_graph["data"][0]["y"])],mode="lines",name="Standard Deviation 2"))
  param_graph.add_trace(go.Scatter(x=[st_dev_3_end,st_dev_3_end],y=[0,max(param_graph["data"][0]["y"])],mode="lines",name="Standard Deviation 3"))

  param_graph.update_layout(title="{}:{} ({})".format(label_arg,"Sample Data",modification_arg))
  
  param_graph.show()

  print("The mean of the data (of {}) is {}".format(label_arg,round(param_mean,2)))
  print("The median of the data (of {}) is {}".format(label_arg,round(param_median,2)))
  print("The standard deviation of the data (of {}) is {}".format(label_arg,round(param_st_dev,2)))

  print("{}% of the data lies within the first standard deviation".format(round(percentage_1,2)))
  print("{}% of the data lies within the second standard deviation".format(round(percentage_2),2))
  print("{}% of the data lies within the third standard deviation".format(round(percentage_3,2)))

  if( percentage_1<=67 or percentage_1>=69.8 or percentage_2<=95 or percentage_2>=96.5 or percentage_3<=98.5 or percentage_3>=100 ):
    print("The data does not follow normal distribution")

  else:
    print("The data follows normal distribution")
      

#Defining a function to create a box plot and scatter graph from the stipulated data
def CreateBoxAndScatterPlot(df_arg,df_section_arg,label_arg):

  print("Generating box plot...")
  tm.sleep(1.3)
  print("Box Plot Generated")

  sns_data=sns.boxplot(data=df_arg,x=df_arg[df_section_arg])
  plt.title("{}:-Box Plot".format(label_arg))
  plt.show()

  axis_list=["Unusable_Element","Quantity Saved","Age"]
  axis_count=0

  x_axis="None"
  y_axis="None"

  print("Generating scatter graph...")
  tm.sleep(2.3)

  for axis in axis_list[1:]:
    axis_count+=1
    print(str(axis_count)+":"+axis)

  axis_input=int(input("Please enter the field to be allocated to the x-axis of the scatter graph:"))  
  axis_choice=axis_list[axis_input]

  #Verifying the user's input
  #Case-1
  if(axis_input==1):
    x_axis="quant_saved"
    y_axis="age"
   
  #Case-2 
  elif(axis_input==2):
    x_axis="age"
    y_axis="quant_saved"  

  df_quantile_3=df_arg[df_section_arg].quantile(0.75)
  df_quantile_1=df_arg[df_section_arg].quantile(0.25)
  IQR=df_quantile_3-df_quantile_1
  upper_whisker=df_quantile_3+(1.5*IQR)

  df_abstracted=df[df[df_section_arg]<upper_whisker]
  df_abstracted_list=df_abstracted[df_section_arg].tolist()
  df_list=df[df_section_arg].tolist()

  print("Scatter Graph Generated.")

  scatter_graph=px.scatter(df_arg,x=x_axis,y=y_axis,title="{}:-Scatter Graph".format(label_arg))

  #Verifying that which axis is the data required to be displayed for the distribution graphs
  if(df_section_arg==x_axis):
    scatter_graph.update_layout(shapes=[dict(type="line",x0=upper_whisker,x1=upper_whisker,y0=0,y1=max(scatter_graph["data"][0]["y"]))])

  elif(df_section_arg==y_axis):  
    scatter_graph.update_layout(shapes=[dict(type="line",y0=upper_whisker,y1=upper_whisker,x0=0,x1=max(scatter_graph["data"][0]["x"]))])

  scatter_graph.show()

  print("The first quantile of the data is {}".format(round(df_quantile_1,2)))
  print("The third quantile of the data is {}".format(round(df_quantile_3,2)))
  print("The IQR(InterQuantileRange) of the range is {}".format(round(IQR,2)))
  print("Calculating uppper whisker...")
  print("The upper whisker is {}".format(round(upper_whisker,2)))

  print("Displaying the data with outliers...")
  CalculateMeanMedianAndStandardDeviationAndCreateOriginalPlotOfData(df_list,label_arg,"With Outliers")

  print("Displaying the data without outliers...")
  CalculateMeanMedianAndStandardDeviationAndCreateOriginalPlotOfData(df_abstracted_list,label_arg,"Without Outliers")

  print("Thank You for using OutlierSavings.py")



df=pd.read_csv("data.csv")


print("Welcome to OutlierSavings.py. We provide data of a particular city's savings data with and without outliers.")
tm.sleep(2.3)

view_information=input("View information on outliers?(:-Yes or No)")

#Assessing the users input on viewing information about outliers
#Case-1
if(view_information=="Yes" or view_information=="yes"):
  print("What are outliers?")
  tm.sleep(2.9)

  print("Outliers are datapoints of a dataset that occur at disproportionate boundaries, isolated from most of the datapoints.")
  tm.sleep(3.0)

  print("Why do we need to remove outliers?")
  tm.sleep(2.5)

  print("Outliers often affect the performance of the whole dataset. For instance, the mean value of the dataset might vary drastically due to outliers.")
  tm.sleep(5.0)

  print("Sometimes outliers also damage the equilibrium of the normal distribution attained by the sample data.")
  tm.sleep(3.5)

  print("Hence, in order to facilitate distribution of hihger efficiency, removal of outliers is integral.")
  tm.sleep(3.9)

  print("How to identify an outlier?")
  tm.sleep(2.5)

  print("Outliers can be at extreme minimums and maximums, both of which can be identified using the InterQuartileRange Method(IQR)")
  tm.sleep(2.3)

  print("The method implies the first and third quantiles in its usage. The difference of latter and former produces the IQR")
  tm.sleep(3.4)

  print("Outliers at low extremes can be found by comapring all the values to the result of the formula-[1st quantile-(IQR*1.5)]. Values lower than the aforementioned are deemed -low outliers-")
  tm.sleep(2.3)

  print("Outliers at low extremes can be found by comapring all the values to the result of the formula-[3rd quantile+(IQR*1.5)]. Values lower than the aforementioned are deemed -low outliers-")
  tm.sleep(2.3)

  print("To find more about the IQR Method visit 'https://en.wikipedia.org/wiki/Interquartile_range#:~:text=In%20descriptive%20statistics%2C%20the%20interquartile,IQR%20is%20the%20first%20quartile'")
  tm.sleep(1.2)

  print("Loading list...")
  tm.sleep(2.3)

field_choice_list=["Unusable_Element","Quantity Saved","Age"]
field_choice_count=0

for field_choice in field_choice_list[1:]:
  field_choice_count+=1
  print(str(field_choice_count)+":"+field_choice)

field_choice=int(input("Please enter the index of the statistic desired to compare with and without outliers:")) 
field_choice_choice=field_choice_list[field_choice] 

#Assessing the user's input about the statistic chosen to display and abstract outliers from
#Case-1
if(field_choice==1):
  AbstractGivenData(df,"quant_saved","Quantity Saved")
 
#Case-2
elif(field_choice==2):
  AbstractGivenData(df,"age","Age")

#---------------------------------------------------OutlierSavings.py---------------------------------------------------#
  

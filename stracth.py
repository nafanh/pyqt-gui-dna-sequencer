<<<<<<< HEAD
import pandas as pd



# def size(df,length,ranges_list):
#     # Asks user input for template size
#     # original = int(input('Please enter the template size: '))
#     # Adjusts the peak number in relation to template size
#
#     # Polymer length list. Ex: [27mer,28mer,29mer]
#     #length = []
#
#     # Nested list for the ranges of the difference ranges for each polymer.
#     # Ex: For 27mer: [[300,400]]. Where 300 is lower bound and 400 is upper bound
#     #ranges_list = []
#
#     # Creates a dictionary for polymer length and difference ranges
#     # Ex: {27mer:[300,400],28mer"[450,500]}
#     ranges_dict = {}
#
#     # Loop appends each polymer as the key and the range list as the value
#     for i in range(len(ranges_list)):
#         ranges_dict[length[i]] = ranges_list[i]
#     # print(ranges_dict)
#
#     # Takes difference values to list
#     diff_list = df['Diff'].astype(float).tolist()
#
#     # Gets the keys of the dictionary which are the polymer sizes
#     ranges_keys = list(ranges_dict.keys())
#     # print(ranges_keys)
#     final_length_list = []
#     # print(diff_list)
#
#     # Parses the differences (internal std - sample) and checks to see
#     # If within a certain range. If it is, then it is appends the key(size)
#     # to final_length_list
#     for j in diff_list:
#         for i in range(len(ranges_keys)):
#             # Gets the value of ranges. Ex: [300,400]
#             width = ranges_dict[ranges_keys[i]]
#             # print(ranges_dict[ranges_keys[i]])
#
#             # Takes lower bound
#             low = width[0]
#             # Takes upper bound
#             high = width[-1]
#             # If the difference is in between these bounds, then
#             # append the size to the final_length_list
#             if j >= low and j < high:
#                 final_length_list.append(ranges_keys[i])
#
#     # print(final_length_list)
#     # Creates a new column in the dataframe for the size of each sample run
#     df["Size"] = final_length_list
#
#     return df

# polymer_list = ['27mer','28mer']
# # ranges_list = [[110,111],[111,113]]
#
# ranges_list = "[110:111],[111:113]"
# a = ranges_list.split(',')
# final_list = []
# for x in a:
#     new_x = x.strip('[]')
#     num_list = new_x.split(':')
#     for i in range(len(num_list)):
#         num_list[i] = float(num_list[i])
#     final_list.append(num_list)
#
# print(a)
# print(final_list)
#
#
#

# Function that creates the table containing area values for each polymer
def table(df):
    # Creates sorted set with time values (unique values only)
    df_time = list(set(df['Time'].tolist()))
    df_time.sort()

    # Creates sorted set with size values (unique values only)
    df_size = list(set(df['Size'].tolist()))
    df_size.sort(key=natural_keys)

    # print(df_size)
    # n = pd.DataFrame(columns = df_size)
    # headings = df_size
    # headings.append('Total')
    # for i in range(len(df_size)-1):
    #     headings.append(str(df_size[i]) + '/' + headings[len(headings)-1-i])
    # n = pd.DataFrame(df_time,columns=['Time'])
    #  for i in range(len(headings)):
    #      n[headings[i]] = np.nan
    # n.set_index('Time',inplace=True)

    area_list = df['Area'].tolist()
    time_list = df['Time'].astype(float).tolist()
    # time_dict = {'time':time_list}

    # Creates dictionary where time and size are keys. Value is area
    size_list = df['Size'].tolist()

    # Creates tuple of time,size pairs
    # This tuple will eventually be the key values for the dictionary
    two_keys = list(zip(time_list, size_list))
    # print(two_keys)

    new_dict = {}

    # Creates new empty dataframe with time values as index
    n = pd.DataFrame()
    n.index.name = 'Time'

    for size in df_size:
        n[size] = ""
    # print(n)
    # Appends area to dictionary containing the time and size keys
    # Ex: {(0.05 sec,27mer),34000, (0.10 sec, 27mer), 20000}
    for i in range(len(two_keys)):
        new_dict[two_keys[i]] = area_list[i]

    # Parses the dictionary and creates a new column in the table
    # for area. Locates the time and size and inputs the area for that
    # those values into the dataframe
    for key in two_keys:
        time = key[0]
        size = key[1]
        n.loc[time, size] = int(new_dict[key])
    #     print(n)
    # print(new_dict)
    # print(len(new_dict))
    # print('This is the table for fractional area vs. size. Please analyze to see if you want to delete outliers.')
    # print('-----------------------------------------------------------------------------')
    # print(n)
    #
    # #Creates new columns containing the area of each polymer/total
    # remove_datapt_quest = input('Do you want to delete a polymer? If so, please enter ''y'', else enter in ''n'': ')
    # while remove_datapt_quest == 'y' or remove_datapt_quest == 'Y':
    #     remove_datapt = input('Please enter the polymer name you want to delete (ex: 24mer): ')
    #     del n[remove_datapt]
    #     remove_datapt_quest= input('Any more polymers you want to delete? Please enter y for yes and n for no: ')
    # #Creates new columns containing the area of each polymer/total
    # n['Total'] = n.sum(axis=1)
    # headers_list = n.columns.values.tolist()
    # for i in range(len(headers_list)-1):
    #     divide_name = headers_list[i] + '/' + headers_list[-1]
    #     n[divide_name] = n.iloc[:,i] / n.iloc[:,len(headers_list)-1]
    #
    # Sorts table by time and fill 'NaN' values with '0'
    n.sort_index(inplace=True)
    n = n.fillna(0)
    n['Total'] = n.sum(axis=1)
    headers_list = n.columns.values.tolist()
    # print(headers_list)
    for i in range(len(headers_list) - 1):
        divide_name = headers_list[i] + '/' + headers_list[-1]
        n[divide_name] = n.iloc[:, i] / n.iloc[:, len(headers_list) - 1]
    # n = n.fillna(0)
    print('This is the table for fractional area vs. size. Please analyze to see if you want to delete outliers.')
    print('-----------------------------------------------------------------------------')
    print(n)

    remove_datapt_quest = input('Do you want to delete a polymer? If so, please enter ''y'', else enter in ''n'': ')
    while remove_datapt_quest == 'y' or remove_datapt_quest == 'Y':
        remove_datapt = input('Please enter the polymer name you want to delete (ex: 24mer): ')
        del n[remove_datapt]
        del n[remove_datapt + '/Total']
        headers_list.remove(remove_datapt)
        # headers_list.remove(remove_datapt + '/Total')
        n['Total'] = 0
        n['Total'] = n.iloc[:, :int(len(n.columns) / 2)].sum(axis=1)
        remove_datapt_quest = input('Any more polymers you want to delete? Please enter y for yes and n for no: ')
    for i in range(len(headers_list) - 1):
        divide_name = headers_list[i] + '/' + headers_list[-1]
        n[divide_name] = n.iloc[:, i] / n.iloc[:, len(headers_list) - 1]
    # Sorts table by time and fill 'NaN' values with '0'
    n = n.fillna(0)

    # Exports non-concentration fixed data. Gives the fractional area for
    # Each polymer and the time points
    # export_before_conc = n.to_csv('Export_data_Before_concfix.csv',sep=',')
    return n







































# def size(df):
#     # Asks user input for template size
#     # original = int(input('Please enter the template size: '))
#     # Adjusts the peak number in relation to template size
#
#     # Polymer length list. Ex: [27mer,28mer,29mer]
#     length = []
#
#     # Nested list for the ranges of the difference ranges for each polymer.
#     # Ex: For 27mer: [[300,400]]. Where 300 is lower bound and 400 is upper bound
#     ranges_list = []
#
#     # Prompts user for difference bounds for each polymer
#     print("Please enter the diff bounds for each polymer.Ex: 27mer/300-400")
#     addit = 'y'
#
#     # # Loop for multiple polymers
#     # while addit == 'y' or addit == 'Y':
#     #     # Creates temporary list to be added to the ranges_list
#     #     # Resets everytime the loop is run
#     #     temp = []
#     #     polymer = input("Enter polymer (ex:27mer): ")
#     #     while True:
#     #         if 'mer' not in polymer:
#     #             polymer = input("Invalid polymer name, please try again: ")
#     #         else:
#     #             break
#     #     length.append(polymer)
#     #     while True:
#     #         try:
#     #             low_r = float(input("Enter lower bound of diff (lower bound is inclusive): "))
#     #             upper_r = float(input("Enter upper bound of diff (upper bound is exclusive): "))
#     #             temp.append(low_r)
#     #             temp.append(upper_r)
#     #             # Adds nested list of lower and upper bounds to list
#     #             ranges_list.append(temp)
#     #             break
#     #
#     #         # In case integer not entered for bounds. Catch exception
#     #         except ValueError:
#     #             print("Lower or upper bounds not valid. Please try again.")
#     #     addit = input("Are there any more? Input 'y' for yes and 'n' to end: ")
#
#     # ranges_list2 = sorted(ranges_list, key=lambda x: int("".join([i for i in x if i.isdigit()])))
#
#     # Creates a dictionary for polymer length and difference ranges
#     # Ex: {27mer:[300,400],28mer"[450,500]}
#     ranges_dict = {}
#
#     # Loop appends each polymer as the key and the range list as the value
#     for i in range(len(ranges_list)):
#         ranges_dict[length[i]] = ranges_list[i]
#     # print(ranges_dict)
#
#     # Takes difference values to list
#     diff_list = df['Diff'].astype(float).tolist()
#
#     # Gets the keys of the dictionary which are the polymer sizes
#     ranges_keys = list(ranges_dict.keys())
#     # print(ranges_keys)
#     final_length_list = []
#     # print(diff_list)
#
#     # Parses the differences (internal std - sample) and checks to see
#     # If within a certain range. If it is, then it is appends the key(size)
#     # to final_length_list
#     for j in diff_list:
#         for i in range(len(ranges_keys)):
#             # Gets the value of ranges. Ex: [300,400]
#             width = ranges_dict[ranges_keys[i]]
#             # print(ranges_dict[ranges_keys[i]])
#
#             # Takes lower bound
#             low = width[0]
#             # Takes upper bound
#             high = width[-1]
#             # If the difference is in between these bounds, then
#             # append the size to the final_length_list
#             if j >= low and j < high:
#                 final_length_list.append(ranges_keys[i])
#
#     # print(final_length_list)
#     # Creates a new column in the dataframe for the size of each sample run
#     df["Size"] = final_length_list
#
#     return df

#
# def table(df):
#     # Creates sorted set with time values (unique values only)
#     df_time = list(set(df['Time'].tolist()))
#     df_time.sort()
#
#     # Creates sorted set with size values (unique values only)
#     df_size = list(set(df['Size'].tolist()))
#     df_size.sort(key=natural_keys)
#
#     # print(df_size)
#     # n = pd.DataFrame(columns = df_size)
#     # headings = df_size
#     # headings.append('Total')
#     # for i in range(len(df_size)-1):
#     #     headings.append(str(df_size[i]) + '/' + headings[len(headings)-1-i])
#     # n = pd.DataFrame(df_time,columns=['Time'])
#     #  for i in range(len(headings)):
#     #      n[headings[i]] = np.nan
#     # n.set_index('Time',inplace=True)
#
#     area_list = df['Area'].tolist()
#     time_list = df['Time'].astype(float).tolist()
#     # time_dict = {'time':time_list}
#
#     # Creates dictionary where time and size are keys. Value is area
#     size_list = df['Size'].tolist()
#
#     # Creates tuple of time,size pairs
#     # This tuple will eventually be the key values for the dictionary
#     two_keys = list(zip(time_list, size_list))
#     # print(two_keys)
#
#     new_dict = {}
#
#     # Creates new empty dataframe with time values as index
#     n = pd.DataFrame()
#     n.index.name = 'Time'
#
#     for size in df_size:
#         n[size] = ""
#     # print(n)
#     # Appends area to dictionary containing the time and size keys
#     # Ex: {(0.05 sec,27mer),34000, (0.10 sec, 27mer), 20000}
#     for i in range(len(two_keys)):
#         new_dict[two_keys[i]] = area_list[i]
#
#     # Parses the dictionary and creates a new column in the table
#     # for area. Locates the time and size and inputs the area for that
#     # those values into the dataframe
#     for key in two_keys:
#         time = key[0]
#         size = key[1]
#         n.loc[time, size] = int(new_dict[key])
#     #     print(n)
#     # print(new_dict)
#     # print(len(new_dict))
#     # print('This is the table for fractional area vs. size. Please analyze to see if you want to delete outliers.')
#     # print('-----------------------------------------------------------------------------')
#     # print(n)
#     #
#     # #Creates new columns containing the area of each polymer/total
#     # remove_datapt_quest = input('Do you want to delete a polymer? If so, please enter ''y'', else enter in ''n'': ')
#     # while remove_datapt_quest == 'y' or remove_datapt_quest == 'Y':
#     #     remove_datapt = input('Please enter the polymer name you want to delete (ex: 24mer): ')
#     #     del n[remove_datapt]
#     #     remove_datapt_quest= input('Any more polymers you want to delete? Please enter y for yes and n for no: ')
#     # #Creates new columns containing the area of each polymer/total
#     # n['Total'] = n.sum(axis=1)
#     # headers_list = n.columns.values.tolist()
#     # for i in range(len(headers_list)-1):
#     #     divide_name = headers_list[i] + '/' + headers_list[-1]
#     #     n[divide_name] = n.iloc[:,i] / n.iloc[:,len(headers_list)-1]
#     #
#     # Sorts table by time and fill 'NaN' values with '0'
#     n.sort_index(inplace=True)
#     n = n.fillna(0)
#     n['Total'] = n.sum(axis=1)
#     headers_list = n.columns.values.tolist()
#     # print(headers_list)
#     for i in range(len(headers_list) - 1):
#         divide_name = headers_list[i] + '/' + headers_list[-1]
#         n[divide_name] = n.iloc[:, i] / n.iloc[:, len(headers_list) - 1]
#     # n = n.fillna(0)
#     print('This is the table for fractional area vs. size. Please analyze to see if you want to delete outliers.')
#     print('-----------------------------------------------------------------------------')
#     print(n)
#
#     remove_datapt_quest = input('Do you want to delete a polymer? If so, please enter ''y'', else enter in ''n'': ')
#     while remove_datapt_quest == 'y' or remove_datapt_quest == 'Y':
#         remove_datapt = input('Please enter the polymer name you want to delete (ex: 24mer): ')
#         del n[remove_datapt]
#         del n[remove_datapt + '/Total']
#         headers_list.remove(remove_datapt)
#         # headers_list.remove(remove_datapt + '/Total')
#         n['Total'] = 0
#         n['Total'] = n.iloc[:, :int(len(n.columns) / 2)].sum(axis=1)
#         remove_datapt_quest = input('Any more polymers you want to delete? Please enter y for yes and n for no: ')
#     for i in range(len(headers_list) - 1):
#         divide_name = headers_list[i] + '/' + headers_list[-1]
#         n[divide_name] = n.iloc[:, i] / n.iloc[:, len(headers_list) - 1]
#     # Sorts table by time and fill 'NaN' values with '0'
#     n = n.fillna(0)
#
#     # Exports non-concentration fixed data. Gives the fractional area for
#     # Each polymer and the time points
#     # export_before_conc = n.to_csv('Export_data_Before_concfix.csv',sep=',')
#     return n


a = '27mer,28mer'
b = a.split(',')
print(b)
=======
import pandas as pd
import numpy as np

a = {'a':[1,2,3], 'b' : [18,2,121]}

df = pd.DataFrame(a)
print(df)

print()

a = df['b'].tolist()
a.sort()
df_a = pd.DataFrame(a,columns=['Diff'])
#a.sort_values(by=['b'])

print(a)
print(df_a)
>>>>>>> 14dd7a7d363abd73c3382bddcb4bbae63a207333

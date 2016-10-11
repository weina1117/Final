__author__ = 'weinaguo'
import matplotlib.pyplot as plt
import numpy as np

# This function reads the contents of file input and prints the contents to the output
def load_data_from_file(input):
    try:
        file = open(input, 'r')
        lines = file.readlines()
        lines = np.array(lines)
        print('Load file successfully!\n')
        print('The first ten lines are:\n')
        for i in range(10):
            print(lines[i])
        nrow = len(lines)
        data_array = []
        for record in lines:
            data_array.append(record.split(','))
        ncol = len(data_array[0])
        data_array = np.array(data_array)
        extracted = data_array[:, 0:2]
        ret = extracted.copy()
        print('Number of records is {0:d}'.format(ret.shape[0]))
        unique_names = np.unique(extracted[:,0])
        print('Number of unique names is {0:d}'.format(unique_names.size))
        return ret, ncol, nrow
    except IOError:
        print('File is not existing')
        quit()


def extract_sex_data(data):
    males, females = [], []
    for i in range(data.shape[0]):
        if data[i, 1] == 'M':
            males.append(data[i])
        else:
            females.append(data[i])
    males = np.array(males)
    females = np.array(females)
    males_writer = open('males_1880.txt', 'w')
    females_writer = open('females_1880.txt', 'w')
    for i in range(males.shape[0]):
        males_writer.write('{0:s},{1:s}\n'.format(males[i, 0], males[i, 1]))
    for i in range(females.shape[0]):
        females_writer.write('{0:s},{1:s}\n'.format(females[i, 0], females[i, 1]))
    males_writer.close()
    females_writer.close()
    print('Sex\t Total number of births in 1880\n')
    print('F\t{0:d}'.format(females.shape[0]))
    print('M\t{0:d}'.format(males.shape[0]))
    return males, females, males.shape[0], females.shape[0]


def extract_names_start_with(females, start_letter):
    positions, selected_names = [], []
    selected_names_writer = open('selected_names.txt', 'w')
    for i in range(females.shape[0]):
        if females[i, 0][0] == start_letter:
            positions.append(i)
            selected_names = females[i]
            selected_names_writer.write('{0:s},{1:s}\n'.format(females[i,0], females[i,1]))
    selected_names_writer.close()
    rows = [i for i in range(females.shape[0])]
    zeros = [0] * len(rows)
    szeros = [0] * len(positions)
    plt.hlines(0,1,len(rows))  # Draw a horizontal line
    plt.xlim(0,len(rows))
    ax1 = plt.axes(frameon=False)
    ax1.axes.get_yaxis().set_visible(False)
    plt.plot(rows, zeros, 'ro')
    plt.plot(positions, szeros, 'b*')
    plt.show()


def Extract_names_start_with_gt_threshold(females, threshold_value, start_letter):
    positions, selected_names = [], []
    selected_names_writer = open('selected_names_filtered.txt', 'w')
    for i in range(females.shape[0]):
        if females[i, 0][0] == start_letter and i > threshold_value:
            positions.append(i)
            selected_names = females[i]
            selected_names_writer.write('{0:s},{1:s}\n'.format(females[i,0], females[i,1]))
    selected_names_writer.close()
    rows = [i for i in range(females.shape[0])]
    zeros = [0] * len(rows)
    szeros = [0] * len(positions)
    plt.hlines(0,1,len(rows))  # Draw a horizontal line
    plt.xlim(0,len(rows))
    ax1 = plt.axes(frameon=False)
    ax1.axes.get_yaxis().set_visible(False)
    plt.plot(rows, zeros, 'ro')
    plt.plot(positions, szeros, 'b*')
    plt.show()


def __main__():
    data, ncol, nrow = load_data_from_file('yob1880.txt')
    males, females, num_males, num_females = extract_sex_data(data)
    extract_names_start_with(females, 'N')
    Extract_names_start_with_gt_threshold(females, 200, 'N')

__main__()
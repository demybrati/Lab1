import subprocess
import csv

def read_csv(file_name):

    x = []
    y = []
    with open(file_name, 'r') as file:
        reader = csv.reader(file)
        next(reader)  # skip header
        for row in reader:
            #make sure there are no empty values in the rows
            if row[0] and row[1]:  #pass only if both columns have values
                x.append(float(row[0]))  #first column
                y.append(float(row[1]))  #second column
    return x, y


def main():
    #read CSV file
    file_name = 'data_table.csv'
    x, y = read_csv(file_name)
    
    #convert data into strings to pass to the C program
    x_str = "[" + " ".join(map(str, x)) + "]"
    y_str = "[" + " ".join(map(str, y)) + "]"
    
    #call C program using subprocess
    result = subprocess.run(
        ['./part3_calc_cov_and_var.out', x_str, y_str], 
        capture_output=True, text=True
    )
    
    #print the output result
    print(result.stdout.strip())

if __name__ == '__main__':
    main()


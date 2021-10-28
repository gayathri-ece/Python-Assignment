# Importing the packages Pandas, Numpy, logging and os

import pandas as pd
import numpy as np
import logging
import os

# Creating Class named Student
logging.basicConfig(format='%(asctime)s - %(message)s', level=logging.INFO)
class Student:

    # Defining Constructor for Student Class

    def __init__(self,file,total_per_each):
        self.file=file
        self.total_per_each=total_per_each

    # Defining Method To add Percentage Column

    def add_percentage(self):
     
        # Reading Excel file and storing in a dataframe
   
        df=pd.read_excel(self.file)
        subject_count=0
        
        # Counting number of Subjects

        for i in df.columns:
            if('Marks' in i):
                subject_count+=1

        # Counting number of records

        l=len(df)

        # Using For loop, Calculating the percentage and appending the result of each student into list d
 
        d=[]
        for i in range(l):
            d.append((df.loc[i,'Marks1']+df.loc[i,'Marks2']+df.loc[i,'Marks3']+df.loc[i,'Marks4']+df.loc[i,'Marks5'])/(self.total_per_each*subject_count)*100)
 
        # Adding Percentage Column to Data Frame

        df['Percentage']=d
        logging.info("Successfully Added Percentage Column\n")
     
        # Converting the Data Frame to CSV File using to_csv function

        df.to_csv('marks.csv')

        # Returning True so as to print that Percentages have been added successfuly

        return(True)


if __name__=="__main__":

    # Taking File name and Total marks per each subject as string and integer input
    
    filename=input('Enter Filename : ')

    # Logging Error if file name is not excel format and prompting user to enter filename till it is excel format

    while(os.path.isfile(filename)==False) or ('.xlsx' not in filename):
         if(os.path.isfile(filename)==False and '.xlsx' not in filename):
             logging.error('Error : File not found and Excel format file is only supported\n')
         elif(os.path.isfile(filename)==False):
             logging.error('Error : File not found\n')
         elif('.xlsx' not in filename):
             logging.error('Error : Excel format file is only supported\n')
         filename=input("Enter File Name : ")   
    logging.info("Filename is {} Accepted\n".format(filename))

    # Taking Total marks per each subject as float input
    q=True
    while(q or total_per_each <= 0.0):
        try:
            total_per_each=float(input('Enter Marks per each Subject : '))
        except:
            logging.error('Error : Total marks of each Subject cannot be String\n')
        else:
             if(total_per_each <= 0.0):
                 logging.error('Error : Total marks of each Subject cannot be negative or zero\n')
             else:
                 q=False
    logging.info("Total Marks entered = {} is Accepted\n".format(total_per_each))


    # Passing file name and total marks per each subject as    

    s=Student(filename,total_per_each)
    d1=s.add_percentage()
    if(d1):
        logging.info("Successfully created CSV file with Percentage Column added\n")

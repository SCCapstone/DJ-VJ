## Interpreter Class
The duty of this class is to return the file path that satified the condions stored within the dataframe. The drawback of this class it will return the first file that passes the conditions.

### creating_master_frame:
Returns a newly organized dataframe to use later within the code

### search_panda_data:
`search_panda_data` will set the current values of  `self.curr_pitch,self.curr_tempo,self.cur_time` to be equal to the current pitch, tempo, and time. 
As the dataframe iterates through each row within iteslf, it will check to see which file is best suites the to be returned based on the current inputs

## Helper Functions 

### iterate_master_frame:
Iterates through the original dataframe. If the file within the original dataframe is not inside the new dataframe, that file along with the conditions will be added to the new dataframe

### nested_iteration:
if the file already exist in the new dataframe, it will return one as a flag that indicates this information does not need to be within the dataframe does not need to be added again

### created_master_frame:
This function will be grab every data related towards the file name and place it on a single row

### compare
Compares the current value along with the value stored within the table.  If there is a match, the compare function will return the file path. If there was no match, it will return 1 as a reprsentation of a flag of an error. 

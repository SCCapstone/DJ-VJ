## Class Interpreter
The duty of this class is return a the correct file from the dataframe                                                       based on the the inputs givin

The drawback of this class is that the function works first come first serve based on the conitions                 that are met from the dataframe

### search_panda_data:

`Line 43`: 
The `iterate_master_frame` is a helper function that creates the new dataframe                                  that will be used in the class

           Old Data Frame:
           File_Name     Sign    Pitch   Tempo   Time
           File1         >       30      None    None
           File2         <       None    60      None

           New Data Frame:
           File_Path     Pitch_Com   Pitch   Tempo_Com   Tempo   Time_Com    Time
           File1         >           30      <           60      None        None

`Line 45`: 
Iteration of master data frame 

`Line47-123`: 
The top level if statements will check to see if there are any                                                                    current values inside and of the current values. if the condition is                                                                  true, The `compare` function that can be located on line `line 125`, will return the file path of the specific row if the comapartive operater is true. If it is not true, the function will return one (In this code the one will be used as a flag for error). This practice will continue on other cells found on the row to make sure the best match was found. If there was a flag for error found for on the visited row, the program will go to the next index, else it would return the file path value to the main

### Helper Function

`compare`:
The `compare` function wull take in the current value in question, comaparotor operator, and the value found in table that enables the exection. If the compare between the current value and the value within the table it true, the function will return the file path of the cell

`iterate_master_frame`:
The `iterate_master_frame` is a helper function that                                                                           takes in the dataframe created from the gui.py class and                                                                     organizes the data into a new dataframe ex:

            Old Data Frame:
            File_Name     Sign    Pitch   Tempo   Time
            File1         >       30      None    None
            File1         <       None    60      None

            New Data Frame:
            File_Path     Pitch_Com   Pitch   Tempo_Com   Tempo   Time_Com    Time
            File1         >           30      <           60      None        None
                
`create_master_frame`:
The `create_master_frame` works with the `iterate_master_frame` to create the new dataframe. The function will take in a file path and the old data frame. using the global variable found within the if statements, every time the file path is true it will store the data it found within the cells to merge in the master dataframe.


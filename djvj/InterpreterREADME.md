## Class Interpreter
The duty of this class is return a the correct file path from the dataframe based on the the inputs givin. The drawback of this class is that the function works first come first serve based on the conitions that are met from the dataframe

### `creating_master_frame:`
`creating_master_frame` returns the newly created master frame from the `iterate_master_frame` function

### `search_panda_data`:
`search_panda_data` iterates through the dataframe and returns the file path that best fit the current conditions that are being activaly given 

## Helper Function

### `compare`:
The `compare` function wull take in the current value in question, comaparotor operator, and the value found in table that enables the exection. If the compare between the current value and the value within the table it true, the function will return the file path of the cell

### `iterate_master_frame`:
The `iterate_master_frame` is a helper function that takes in the dataframe created from the gui.py class and                                                                     organizes the data into a new dataframe ex:

            Old Data Frame:
            File_Name     Sign    Pitch   Tempo   Time
            File1         >       30      None    None
            File1         <       None    60      None

            New Data Frame:
            File_Path     Pitch_Com   Pitch   Tempo_Com   Tempo   Time_Com    Time
            File1         >           30      <           60      None        None
                
### `create_master_frame`:
The `create_master_frame` works with the `iterate_master_frame` to create the new dataframe. The function will take in a file path and the old data frame. using the global variable found within the if statements, every time the file path is true it will store the data it found within the cells to merge in the master dataframe.

### `nested_iteration`:
This function is called within the `iterate_master_frame`  to check to see if the row that is being visited from the old dataframe is not already inside the new dataframe that is being populated. If the row matches a row within the new dataframe, it will not be added

## Future Plans
The future plans of the this class will be to set rangs for each video that is within load show. This will decrease the chances of shows being prioritize based on first come first serve through the conditions given. The drawback of this implementation is a video added with multliple ranges. The table below gives an example of what the dataframe will look with the implementation. Looking at the columns that are before `Pitch2`,  in order to access `File1`, the current pitch will have to be greater than 300 and less than 400. 

        Data Frame From GUI:
        File_name       Sign1   Pitch1  Sign2   Pitch2  Sign3   Tempo1   Sign4  Tempo   Sign5   Time1   Sign6   Time2
        File1           >       300     <       400     <       300     None    None    None    None    None    None

Requirements:
* Gui will need the user to specify to the user what range should the video be activated on
* Add tables to data frame that represent to new values coming from the Gui
* Add conditions for the new colmns to the `search_panda_data`

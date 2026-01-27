import os.path


def write_file(working_directory, file_path, content):


    try:
        working_dir_abs = os.path.abspath(working_directory)

        target_file_path = os.path.normpath(os.path.join(working_dir_abs, file_path))

        valid_file_path = os.path.commonpath([working_dir_abs, target_file_path]) == working_dir_abs

        parent_dir_name = os.path.dirname(target_file_path)

        if not valid_file_path:
            return f'Error: Cannot write to "{file_path}" as it is outside the permitted working directory'

        if os.path.isdir(target_file_path):
            return f'Error: Cannot write to "{file_path}" as it is a directory'
        
           

        #print(F"FILE PATH - {file_path}")    
        print(f"WORKING DIR - {working_dir_abs}")
        #print(F"TARGET FILE PATH - {target_file_path}")
        #print(F"VALID FILE PATH - {valid_file_path}")
        print(F"PARENT DIR NAME - {parent_dir_name}")
        


        os.makedirs(parent_dir_name,exist_ok=True)

        with open(target_file_path, "w") as f:
            f.write(content)
            
        return f'Successfully wrote to "{file_path}" ({len(content)} characters written)'

        

    except Exception as e:
        return f"Error: {e}"
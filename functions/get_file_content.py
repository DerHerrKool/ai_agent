import os.path
from config import MAX_CHARS


def get_file_content(working_directory, file_path):
    
    try:
        working_dir_abs = os.path.abspath(working_directory)

        target_file_path = os.path.normpath(os.path.join(working_dir_abs, file_path))

        valid_file_path = os.path.commonpath([working_dir_abs, target_file_path]) == working_dir_abs

        if not valid_file_path:
            return f'Error: Cannot read "{file_path}" as it is outside the permitted working directory'

        if not os.path.isfile(target_file_path):
            return f'Error: File not found or is not a regular file: "{file_path}"'
        
        #print(F"FILE PATH - {file_path}")
        #print(f"WORKING DIR - {working_dir_abs}")
        #print(F"TARGET FILE PATH - {target_file_path}")
        #print(F"VALID FILE PATH - {valid_file_path}")
        
        with open(target_file_path, "r") as f:
            file_content_string = f.read(MAX_CHARS)
            if f.read(1):
                file_content_string += f'\n[...File "{file_path}" truncated at {MAX_CHARS} characters]'
            
            return file_content_string

        

    except Exception as e:
        return f"Error: {e}"
    



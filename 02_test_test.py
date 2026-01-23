import os.path


def get_file_content(working_directory, file_path):
    

    working_dir_abs = os.path.abspath(working_directory)

    target_file_path = os.path.normpath(os.path.join(working_dir_abs, file_path))

    valid_file_path = os.path.commonpath([working_dir_abs, target_file_path]) == working_dir_abs

        
    print(f"WORKING DIR - {working_dir_abs}")
    print(F"TARGET FILE PATH - {target_file_path}")
    print(F"VALID FILE PATH - {valid_file_path}")
        
    if not valid_file_path:
        return f'Error: Cannot read "{file_path}" as it is outside the permitted working directory'

    if not os.path.isfile(target_file_path):
        return f'Error: File not found or is not a regular file: "{file_path}"'
        

print(get_file_content("calculator", "lorem.txt"))







        
        

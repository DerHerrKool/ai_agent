import os.path

def get_files_info(working_directory, directory="."):

    working_dir_abs = os.path.abspath(working_directory)

    target_dir = os.path.normpath(os.path.join(working_dir_abs, directory))

    valid_target_dir = os.path.commonpath([working_dir_abs, target_dir]) == working_dir_abs



    if not valid_target_dir:
        f'Error: Cannot list "{directory}" as it is outside the permitted working directory'

    if not os.path.isdir(directory):
        f'Error: "{directory}" is not a directory'

    
    #print(f"WORKING DIR - {working_dir_abs}")
    #print(F"TARGET DIR - {target_dir}")
    
    #print(f"DIR LIST - {os.listdir(target_dir)}")

    dir_items = os.listdir(target_dir)
    #print(f"DIR ITEMS - {dir_items}")


    for item in dir_items:
        #print(f"ITEM IN TARGET DIR - {item}")

        item_path = os.path.join(target_dir, item)
        #print(f"THIS IS ITEM PATH - {item_path}")
        
        is_file = os.path.isfile(item_path)
        is_dir = os.path.isdir(item_path)
        file_size = os.path.getsize(item_path)
        
        #print(f"ITEM IS FILE - {is_file}")
        #print(f"ITEM IS DIR - {is_dir}")
        #print(f"SIZE - {file_size}")


        print(f"- {item}: file_size={file_size} bytes, is_dir={is_dir}")

       


#get_files_info("calculator", "pkg")

#get_files_info("calculator", ".")

get_files_info("calculator", "/bin")

#get_files_info("calculator", "../")
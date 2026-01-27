import os.path
import subprocess



def run_python_file(working_directory, file_path, args=None):

    try:
        working_dir_abs = os.path.abspath(working_directory)

        target_file_path = os.path.normpath(os.path.join(working_dir_abs, file_path))

        valid_file_path = os.path.commonpath([working_dir_abs, target_file_path]) == working_dir_abs

        parent_dir_name = os.path.dirname(target_file_path)

        if not valid_file_path:
            return f'Error: Cannot execute "{file_path}" as it is outside the permitted working directory'

        if not os.path.isfile(target_file_path):
            return f'Error: "{file_path}" does not exist or is not a regular file'
        
        if not target_file_path.endswith(".py"):
            return f'Error: "{file_path}" is not a Python file'  


        if os.path.isdir(target_file_path):
            return f'Error: Cannot write to "{file_path}" as it is a directory'
        

        command = ["python", target_file_path]

        if args != None:
            command.extend(args)

        executed_command = subprocess.run(
            command, 
            cwd=working_dir_abs,
            capture_output=True, 
            timeout=30, text=True
        )
        
        output_string = []
        
        if executed_command.returncode != 0:
            output_string.append(f"Process exited with code {executed_command.returncode}")

        if not executed_command.stdout and not executed_command.stderr:
            output_string.append("No output produced")

        if executed_command.stdout:
            output_string.append("STDOUT:\n" + executed_command.stdout)

        if executed_command.stderr:
            output_string.append("STDERR:\n" + executed_command.stderr)

        return "\n".join(output_string)


    except Exception as e:
        return f"Error: executing Python file: {e}"
import os
import re

'''
SCONSTRUCT file interesting lines
config.version = Version(
major=15,
minor=0,
point=6,
patch=0
)
''' 

'''
VERSION file interesting line
ADLMSDK_VERSION_POINT=6
'''

# Function to update the build number in file
def updateBuildNum(file_name: str):

    # Defining the path of the directory containing the files to be updated
    file_dir_path = os.path.join(os.environ.get("SourcePath"),"develop","global","src")

    # Change file permissions for owner, group, others
    try:
        os.chmod(os.path.join(file_dir_path,file_name), 0o755)
    
    except FileNotFoundError:
        print(f"file \"{file_name}\" was not found")
        return
    except Exception as e:
        print(f"An unexpected error has occurred when opening file \"{file_name}\": {e}")
        return

    # Reading the file and editing the value in a temp file
    try:
        with open(os.path.join(file_dir_path,file_name),'r') as original_file,\
            open(os.path.join(file_dir_path,"temp"),'w') as temp_file:

            content = original_file.read()

            if file_name == "SConstruct":
                updated_content = re.sub("point\=[\d]+", "point=" + os.environ.get("BuildNum"), content)
            elif file_name == "VERSION":
                updated_content = re.sub("ADLMSDK_VERSION_POINT=[\d]+", "ADLMSDK_VERSION_POINT="+os.environ.get("BuildNum"), content)
            else:
                print("Invalid file name")
                return

            temp_file.write(updated_content)

    except PermissionError:
        print(f"You do not have permission to read the file \"{file_name}\"")
        return
    except Exception as e:
        print(f"An unexpected error has occurred when updating the file \"{file_name}\": {e}")
        return

    # Replacing the original file with the temp file
    os.replace(os.path.join(file_dir_path,"temp"), os.path.join(file_dir_path,file_name))

def main():
    updateBuildNum("SConstruct")
    updateBuildNum("VERSION")

main()
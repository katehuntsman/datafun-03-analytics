
# Import modules
import pathlib
import time
import utils_huntsman

###############################
# Declare global variables
###############################

# Create a project path object
project_path = pathlib.Path.cwd()

# Create a project data path object
data_path = project_path.joinpath('data')

# Create the data path if it doesn't exist, otherwise do nothing
data_path.mkdir(exist_ok=True)

#####################################
# This function generates folders for a given range (e.g., years).
# Pass in an int for the first year
# Pass in an int for the last year
#####################################

def create_folders_for_range(start_year: int, end_year: int) -> None:
    for year in range(start_year, end_year + 1):
        year_folder = data_path/str(year)
        year_folder.mkdir(exist_ok=True)
        print(f"FUNCTION CALLED: create_folders_for_range with start_year={start_year} and end_year={end_year}")

#####################################
# This function creates folders from a list of names.
# Pass in a list of folder names 
####################################

def create_folders_from_list(folder_list: list, to_lowercase: bool = False, remove_spaces: bool = False) -> None:
    for folder_name in folder_list:
        if to_lowercase:
            folder_name = folder_name.lower()
        if remove_spaces:
            folder_name = folder_name.replace(" ", "_")
        folder_path = data_path/folder_name
        folder_path.mkdir(exist_ok=True)
        print(f"FUNCTION CALLED: create_folders_from_list with '{folder_name}'")

#####################################
# Define Function 3. List Comprehension: Create a function to create prefixed folders by transforming a list of names and combining each with a prefix (e.g., "data-").
# Pass in a list of folder names
# Pass in a prefix (e.g. 'data-') to add to each
#####################################

def create_prefixed_folders(folder_list: list, prefix: str) -> None:
    for folder_name in folder_list:
        # Create the full folder name with prefix
        folder_path = data_path / f"{prefix}-{folder_name}"
        folder_path.mkdir(exist_ok=True)
        print(f"Created folder: {folder_path}")

#####################################
# Define Function 4. While Loop: Write a function to create folders periodically (e.g., one folder every 5 seconds).
# Pass in the wait time in seconds
#####################################

def create_folders_periodically(folder_count: int, duration_seconds: int) -> None:
        for per in range (folder_count):
            folder_path = data_path/f"folder_{per}"
            folder_path.mkdir(exist_ok=True)
            print(f"Created folder: {per}")
            time.sleep(duration_seconds)

#####################################
# Define a main() function for this module.
#####################################

def main() -> None:
    ''' Main function to demonstrate module capabilities. '''

    # Start of main execution
    print("#####################################")
    print("# Starting execution of main()")
    print("#####################################\n")

    # Print get_byline() from imported module
    print(f"Byline: {utils_huntsman.get_byline()}")

    # Call function 1 to create folders for a range (e.g., years)
    create_folders_for_range(start_year=2020, end_year=2023)

    # Call function 2 to create folders given a list
    folder_names = ['data-csv', 'data-excel', 'data-json']
    create_folders_from_list(folder_names)

    # Call function 3 to create folders using a prefix
    folder_names = ['csv', 'excel', 'json']
    prefix = 'data-'
    create_prefixed_folders(folder_names, prefix)

    # Call function 4 to create folders periodically using while loop
    duration_seconds:int=5
    create_folders_periodically(folder_count=3, duration_seconds=5)

    # Define a list of regions and create folders with transformations
    regions = [
        "North America", 
        "South America", 
        "Europe", 
        "Asia", 
        "Africa", 
        "Oceania", 
        "Middle East"
    ]
    create_folders_from_list(regions, to_lowercase=True, remove_spaces=True)

    # End of main execution
    print("\n#####################################")
    print("# Completed execution of main()")
    print("#####################################")

#####################################
# Conditional Execution
#####################################

if __name__ == '__main__':
    main()
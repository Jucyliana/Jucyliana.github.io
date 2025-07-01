import os

def clean_profile_json(file_path):
    print(f"  -> Cleaning file: {file_path}")
    with open(file_path, 'r', encoding='utf-8') as f:
        lines = f.readlines()

    new_lines = []
    skip_indices = set()

    # Find lines to remove
    for i, line in enumerate(lines):
        stripped = line.lstrip()
        if stripped.startswith('"totalCost":'):
            print(f"    - Found 'Type' line to remove at line {i+1}: {line.strip()}")
            skip_indices.add(i)
            # Remove trailing comma from previous line
            if i > 0:
                prev_line = lines[i - 1].rstrip()
                if prev_line.endswith(','):
                    print(f"    - Removing comma from previous line {i}: {lines[i - 1].strip()}")
                    lines[i - 1] = prev_line[:-1] + '\n'

    # Build new lines excluding marked ones
    for i, line in enumerate(lines):
        if i not in skip_indices:
            new_lines.append(line)

    # Overwrite the same file
    with open(file_path, 'w', encoding='utf-8') as f:
        f.writelines(new_lines)
    print(f"  -> Finished cleaning {file_path}\n")


def process_all_subfolders(root_folder):
    print(f"Scanning root folder: {root_folder}\n")
    for dirpath, dirnames, filenames in os.walk(root_folder):
        print(f"Checking folder: {dirpath}")
        if 'units.json' in filenames:
            file_path = os.path.join(dirpath, 'units.json')
            clean_profile_json(file_path)
        else:
            print("  -> No profiles.json found in this folder.\n")

# Example usage:
# Replace with your root folder path
process_all_subfolders('C:/Users/User/AppData/LocalLow/Greenfeet/WarhallTest/WDS/WAP')

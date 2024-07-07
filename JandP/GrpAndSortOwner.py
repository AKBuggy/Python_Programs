def groupAndSortOwners(file_and_owner):
    owner_files = {}
    for file, owner in file_and_owner.items():
        if owner in owner_files:
            owner_files[owner].append(file)
        else:
            owner_files[owner] = [file]
    for files_list in owner_files.values():
        files_list.sort()
    return owner_files


def main():
    file_and_owner = {}
    size = int(input("Enter the size of the dictionary: "))
    for i in range(size):
        name = input("Enter owner's name: ")
        file = input("Enter file name: ")
        if file_and_owner.get(file):
            print("File name already exists. Please enter a different file name.")
            continue
        file_and_owner[file.lower()] = name
    result = groupAndSortOwners(file_and_owner)
    print(result)


if __name__ == "__main__":
    main()

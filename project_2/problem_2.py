import os

# Recursive DFS sollution
def find_files(suffix, path):
    results = []
    def helper_recursively(suffix, path):
        if os.path.exists(path) == False:
            return
        isDirectory = os.path.isdir(path)
        files = os.listdir(path)
        for f in files:
            file_path = os.path.join(path, f)
            if os.path.isfile(file_path):
                if suffix in f:
                    results.append(file_path)
            else:
                helper_recursively(suffix, file_path)
    helper_recursively(suffix, path)
    return results

test_results1 = find_files('.c','./testdir')
print(test_results1)
test_results1 = find_files('.h','./testdir')
print(test_results1)
test_results1 = find_files('.c','./testdir/subdir3')
print(test_results1)
# wrong input
test_results1 = find_files('.c','./nonexitdirectory')
print(test_results1)


# Iterative DFS solution
def find_files_iter(suffix, path):
    if os.path.exists(path) == False:
            return []
    results = []
    queue = list(map( lambda x: os.path.join(path, x) ,os.listdir(path)))
    while len(queue) > 0:
        curr_path = queue.pop(0)
        isDirectory = os.path.isdir(curr_path)
        if isDirectory == True:
            sub_queue = list(map(lambda x: os.path.join(curr_path, x), os.listdir(curr_path)))
            # insted of extend Inserting at start of queue will make DFS
            #  commented queue.extend(sub_queue) will also work 
            # However it will append subdirectory resources at then end
            while sub_queue:
                queue.insert(0, sub_queue.pop())
            # queue.extend(sub_queue)
        else:
            if suffix in curr_path:
                results.append(curr_path)

    return results

test_results2 = find_files_iter('.c','./nonexitdirectory')
print(test_results2)

test_results2 = find_files_iter('.c','./testdir')
print(test_results2)

test_results2 = find_files_iter('.h','./testdir')
print(test_results2)
test_results2 = find_files_iter('.c','./testdir/subdir3')
print(test_results2)

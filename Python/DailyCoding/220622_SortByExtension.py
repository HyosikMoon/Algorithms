from typing import List

def sort_by_ext(files: List[str]) -> List[str]:
    results = {}
    files.sort()

    for i, f in enumerate(files):
        # '.' once
        if f.count('.') == 1 and ('config' not in f):
            fileIndex = f.index('.')
            [name, ext] = f.split('.')
            if ext == '': results[i] = ''
            elif name == '': results[i] = ''
            else: results[i] = ext

        # 'config'
        if ('config' in f): results[i] = ''

        # '.' twice
        if f.count('.') >= 2:
            elements = f.split('.')
            ext = elements[-1]
            results[i] = ext

    # Sort results according to the extensions
    sortedIndex = sorted(results, key=lambda x: results[x])
    output = []
    for i in sortedIndex:
        output.append(files[i])

    return output

print(sort_by_ext(['1.cad', '1.bat', '1.aa', '.bat']))
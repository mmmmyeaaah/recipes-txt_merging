def count(file_text):
    with open(file_text, encoding = 'utf-8') as file:
        count = 0
        for line in file:
            count +=1
    return count


def txt_merging(list_files):
    dict_count = {}

    for file_txt in list_files:
        dict_count[file_txt] = count(file_txt)
    
    sorted_value = sorted(dict_count.values())
    sorted_dict = {}

    for i in sorted_value:
        for k in dict_count.keys():
            if dict_count[k] == i:
                sorted_dict[k] = dict_count[k]
    
    with open('file_mrg.txt', 'a', encoding = 'utf-8') as file_mrg:
        for file_txt in sorted_dict:
            with open(file_txt, encoding = 'utf-8') as file:
                file_mrg.write(file_txt)
                file_mrg.write('\n')
                file_mrg.write(str(sorted_dict[file_txt]))
                file_mrg.write('\n')
                file_mrg.write(file.read())
                file_mrg.write('\n')









txt_merging(['file1.txt', 'file2.txt', 'file3.txt'])      
 

              
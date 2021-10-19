import pinyin
file_name="NWPU-VR-AR-PPT大纲.md"
file_name_write="AlphabetSort-NWPU-VR-AR-PPT大纲.md"

file_content=open(file_name, "r")
lines=file_content.readlines()
new_lines=[]
for line in lines:
    if len(line)<1:
        pass
    else:
        cur_line=line.strip()
        cur_pinyin=''
        if len(cur_line)<3:
            pass
        elif cur_line[:2]=="* ":
            cur_pinyin=pinyin.get(cur_line[2:][0][0])

        new_lines.append((cur_pinyin, cur_line[2:]))
file_content.close()
new_lines=sorted(new_lines)
# print(len(new_lines))
print(new_lines[:10])


file_write=open(file_name_write, "w")
write_content=""
for line in new_lines:
    write_content+=line[1]+"\n"
file_write.write(write_content)
file_write.close()




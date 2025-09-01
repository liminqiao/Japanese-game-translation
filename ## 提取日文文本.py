import re
import os

file_dir = r"D:\blgame_and_tool\game\揺蕩う刻 （リマスター版）\GameMaterial\itazura_dsm_decrypt"
out_dir = r"D:\blgame_and_tool\game\揺蕩う刻 （リマスター版）\GameMaterial\itazura_dsm_decrypt_finish"

file_names = os.listdir(file_dir)

# 提取日文文本
jump_pattern = r'\[jump.*\]'  # 匹配包含[jump ...]的行
pattern1 = r'[\u3040-\u309F\u30A0-\u30FF\u4E00-\u9FFF、。！？「」【】［］（）～]+'  # 判断是否含日文字符
pattern2 = r'[\u3040-\u309F\u30A0-\u30FF\u4E00-\u9FFFＡ-Ｚａ-ｚA-Za-z0-9\uFF10-\uFF19、。！？「」『』【】［］（）～〜:…―]'

# 确保输出文件夹存在
if not os.path.exists(out_dir):
    os.makedirs(out_dir)

def Extract_Japanese_text(file_path, out_path):
    # 读取文件内容
    with open(file_path, 'r', encoding='utf-8') as file:
        lines = file.readlines()
    
    # 提取日文文本
    japanese_lines = []
    for line in lines:
        if re.search(jump_pattern, line):  # 跳过含有[jump...]的行
            continue
        
        line = line.replace("[r]", ":")  # 替换[r]为冒号
        
        # 检查是否包含日文字符（使用pattern1）
        if re.search(pattern1, line):
            # 提取日文文本（使用pattern2）
            extracted_text = re.findall(pattern2, line)
            if extracted_text:
                # 将匹配的部分合并为一个字符串
                combined_text = ''.join(extracted_text)
                japanese_lines.append(combined_text)
                print(combined_text)  # 输出提取的文本
    
    # 如果有提取的日文文本，写入输出文件
    if japanese_lines:
        with open(out_path, 'w', encoding='utf-8') as out_file:
            out_file.writelines([line + '\n' for line in japanese_lines])
        print(f"File saved: {out_path}")
    else:
        print(f"No Japanese text extracted from: {file_path}")

# 处理所有文件
for file_name in file_names:
    file_path = os.path.join(file_dir, file_name)
    out_path = os.path.join(out_dir, file_name)
    Extract_Japanese_text(file_path, out_path)

print('Processing complete.')

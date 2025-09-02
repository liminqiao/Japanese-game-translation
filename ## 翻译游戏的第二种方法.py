## 翻译游戏
import re
import os

# 文件路径（请根据需要修改路径）
jp_file_dir = r'D:\blgame_and_tool\game\test\test1\2'  # 日文文本文件
ch_file_dir = r'D:\blgame_and_tool\game\test\test1\3'  # 中文翻译文本文件
original_file_dir = r'D:\blgame_and_tool\game\test\test1\1'  # 原始游戏文本文件
output_file_dir = r'd:\blgame_and_tool\game\test\test1'  # 输出替换后的文本文件

# 替换函数，替换对话中的:为[r]
def replace_colon_with_r(lines):
    return [line.replace(":", "[r]") for line in lines]

# 构建日文→中文的映射字典
def create_translation_dict(jp_lines, ch_lines):
    translation_dict = {}
    for jp, ch in zip(jp_lines, ch_lines):
        jp = jp.strip()
        ch = ch.strip()
        if jp and ch:
            if "[r]" in jp and "[r]" in ch:
                translation_dict[jp] = ch
            elif "[r]" not in jp and "[r]" not in ch:
                translation_dict[jp] = ch
    return translation_dict

# 替换函数
def replace_japanese_with_chinese(text_lines, translations):
    updated = []
    for line in text_lines:
        for jp, ch in translations.items():
            line = re.sub(re.escape(jp), ch, line)
        updated.append(line)
    return updated

# 获取文件列表并进行批量处理
file_names = os.listdir(original_file_dir)

for file_name in file_names:
    jp_file_path = os.path.join(jp_file_dir, file_name)
    ch_file_path = os.path.join(ch_file_dir, file_name)
    original_file_path = os.path.join(original_file_dir, file_name)
    output_file_path = os.path.join(output_file_dir, file_name)

    # 读取并处理日文文件
    with open(jp_file_path, 'r', encoding='utf-8') as f:
        jp_lines = f.readlines()
        jp_lines = replace_colon_with_r(jp_lines)
    
    # 读取并处理中文文件
    with open(ch_file_path, 'r', encoding='utf-8') as f:
        ch_lines = f.readlines()
        ch_lines = replace_colon_with_r(ch_lines)

    # 读取原始文件
    with open(original_file_path, 'r', encoding='utf-8') as f:
        original_lines = f.readlines()

    # 创建翻译字典
    translation_dict = create_translation_dict(jp_lines, ch_lines)

    # 执行替换操作
    updated_lines = replace_japanese_with_chinese(original_lines, translation_dict)

    # 保存替换后的文件
    with open(output_file_path, 'w', encoding='utf-8') as f:
        f.writelines(updated_lines)

    print(f"替换完成！输出文件路径: {output_file_path}")

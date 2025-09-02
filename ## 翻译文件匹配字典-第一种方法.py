## 翻译文件匹配字典
import re
import os

# 现在将目录作为参数传递，而不是硬编码
jp_file_dir = r"D:\blgame_and_tool\game\揺蕩う刻 （リマスター版）\GameMaterial\itazura_dsm_decrypt_finish"
ch_file_dir = r"D:\blgame_and_tool\game\揺蕩う刻 （リマスター版）\GameMaterial\itazura_dsm_decrypt_translate"
original_file_dir = r"D:\blgame_and_tool\game\揺蕩う刻 （リマスター版）\GameMaterial\itazura_dsm_decrypt"
output_file_dir = r"D:\blgame_and_tool\game\揺蕩う刻 （リマスター版）\GameMaterial\itazura_dsm_decrypt-translate-updata"

os.makedirs(output_file_dir,exist_ok= True)


def mapping_between_Japanese_Chinese(jp_file_path,ch_file_path,original_file_path,output_file_path):
# 读取日文文本
    with open(jp_file_path, 'r', encoding='utf-8') as jp_file:
    # 读取文件并同时处理替换和去除空白字符
        jp_lines = [line.replace(":", "[r]").strip() for line in jp_file]


# 读取中文翻译文本
    with open(ch_file_path, 'r', encoding='utf-8') as ch_file:
        ch_lines = [line.replace(":", "[r]").strip() for line in ch_file]
    print(f"jp_lines: {len(jp_lines)}")
    print(f"ch_lines: {len(ch_lines)}")
    
    # 使用 zip 遍历日文和中文行
    translation_dict = dict(zip(jp_lines, ch_lines))
    #     # 将翻译字典写入输出文件（每行一对键值对）
    # with open(output_file_path, 'w', encoding='utf-8') as output_file:
    #     for jp_text, ch_text in translation_dict.items():
    #         output_file.write(f"{jp_text} -> {ch_text}\n")

    with open(original_file_path, 'r', encoding='utf-8') as original_file:
        original_content = original_file.read()
    for jp_text, ch_text in translation_dict.items():
        original_content = re.sub(re.escape(jp_text), ch_text, original_content)
    with open(output_file_path, 'w', encoding='utf-8') as output_file:
        output_file.write(original_content)
    print("替换完成，结果已保存到：", output_file_path)    

# 读取日文和中文翻译文件
file_names = os.listdir(original_file_dir)
for file_name in file_names:
    jp_file_path = os.path.join(jp_file_dir,file_name)
    ch_file_path = os.path.join(ch_file_dir,file_name)
    original_file_path = os.path.join(original_file_dir,file_name)
    output_file_path = os.path.join(output_file_dir,file_name)
    mapping_between_Japanese_Chinese(jp_file_path,ch_file_path,original_file_path,output_file_path)

print("a")





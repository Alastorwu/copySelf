import os
import shutil
import random




# 生成随机字符串
def random_string(length):
    return ''.join(random.choices("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789,.;:()[]{}\"\'\\ \t\n#%!!(MISSING)=><+-*/", k=length))

# 随机替换字符串中的1到3个字符
def random_replace(s):
    n = random.randint(1, 3)
    indices = random.sample(range(len(s)), n)
    for i in indices:
        s = s[:i] + random_string(1) + s[i+1:]
    return s

# 复制文件到新目录并执行
def copy_and_execute(filename):
    compiled = 'compiled'
    try:     
        encoding = "utf-8"
        
        # 构造新目录路径
        new_dir = os.path.join(current_dir, compiled)
        # 如果新目录不存在，则创建
        if not os.path.exists(new_dir):
            os.makedirs(new_dir)
        # 构造新文件路径
        new_filename = os.path.join(new_dir, os.path.basename(filename))
        # 复制文件到新目录
        shutil.copyfile(filename, new_filename)
        # 读取文件内容
        with open(filename, 'r', encoding=encoding) as f:
            content = f.read()
        # 随机替换字符串中的1到3个字符
        new_content = random_replace(content)
        # 将修改后的内容写入文件
        with open(new_filename, 'w', encoding=encoding) as f:
            print(new_content, file=f)
        os.system('python -m py_compile ' + new_filename)
        with open(new_filename, 'w', encoding=encoding) as f:
                    print(new_content, file=f)
        os.system('python ' + new_filename )
    except Exception as e:
        print(e)
    
       


# 测试
while True:

    try:     
        # 获取当前脚本所在目录
        current_dir = os.path.dirname(os.path.realpath(__file__))
        copy_and_execute(__file__)
    except Exception as e:
        print(e)

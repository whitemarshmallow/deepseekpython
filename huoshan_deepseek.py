# -*- coding: utf-8 -*-

# import codecs
import os
import sys
import codecs

# from fontTools.encodings import codecs
from volcenginesdkarkruntime import Ark

def main():

    # 设置输出为UTF-8编码
    # sys.stdout = codecs.getwriter('utf-8')(sys.stdout)
    # 设置输出为UTF-8编码
    sys.stdout = sys.stdout.detach()
    sys.stdout = codecs.getwriter('utf-8')(sys.stdout)

    # 检查参数是否合法
    if len(sys.argv) < 2:
        print("Error: 缺少问题参数")
        sys.exit(1)

    # 从命令行参数获取问题内容
    user_content = sys.argv[1]

    try:
        client = Ark(api_key=os.environ.get("ARK_API_KEY"))
        completion = client.chat.completions.create(
            model="ep-20250214153853-99qsw",
            messages=[
                {"role": "user", "content": user_content}
            ]
        )
        # 直接输出结果内容
        print(completion.choices[0].message.content)

    except Exception as e:
        print(f"Error: {str(e)}")
        sys.exit(2)


if __name__ == "__main__":
    main()





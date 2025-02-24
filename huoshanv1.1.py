import os
import sys
from volcenginesdkarkruntime import Ark

def get_deepseek_response(query):
    # 从环境变量中读取 API Key
    client = Ark(api_key=os.environ.get("ARK_API_KEY"))
    try:
        # 使用 DeepSeek 接口进行调用
        completion = client.chat.completions.create(
            model="ep-20250214153853-99qsw",  # 替换为实际的接入点ID
            messages=[{"role": "user", "content": query}]
        )
        # 返回结果
        return completion.choices[0].message
    except Exception as e:
        return f"Error occurred while calling DeepSeek API: {str(e)}"

if __name__ == "__main__":
    # 从命令行参数获取查询文本
    if len(sys.argv) < 2:
        print("Usage: python huoshanv1.1.py <query>")
        sys.exit(1)

    query = sys.argv[1]

    # 调用 DeepSeek API 获取结果
    result = get_deepseek_response(query)

    # 输出结果，强制以 UTF-8 编码输出
    sys.stdout.buffer.write(result.encode('utf-8'))

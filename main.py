import google.generativeai as genai
import config  

# 1. 配置 API
genai.configure(api_key=config.GEMINI_API_KEY)
model = genai.GenerativeModel('gemini-1.5-flash')

# 2. 定义一个你想测试的 Prompt（以后可以从你的 README 里复制过来）
my_prompt = "你现在是一个幽默的代码教练，请用三句话鼓励一个刚开始学 GitHub 的新手。"

# 3. 运行并打印结果
print("正在连接 Gemini...\n")
response = model.generate_content(my_prompt)
print(f"Gemini 说：\n{response.text}")

from  dotenv import load_dotenv # type: ignore
load_dotenv()
from openai import OpenAI
import time

client = OpenAI()

thread_id = "thread_ASW07mbTGURl6qoQi63bOnm8"  # 조금 전 생성한  thread의 ID를 사용합니다.

thread_messages = client.beta.threads.messages.list(thread_id)
message_contents = thread_messages.data
for data in thread_messages.data:
    print(f'<{data.role}>')
    for content in data.content:
        print(content.text.value)
        print('------')


### 첫번째
# <user>
# I need to solve the equation `3x + 11 = 14`. Can you help me?
# ------

### 두번째
# <assistant>
# The solution to the equation \(3x + 11 = 14\) is \(x = 1\).
# ------
# <assistant>
# Certainly! Let's solve the equation \(3x + 11 = 14\).

# First, we will isolate \(x\) by performing operations on both sides of the equation. Here's how you do it step-by-step:

# 1. Subtract 11 from both sides to eliminate the constant term on the left side.
# 2. Divide both sides by 3 to solve for \(x\).

# Let me calculate that for you.
# ------
# <user>
# I need to solve the equation `3x + 11 = 14`. Can you help me?
# ------
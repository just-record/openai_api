# Function calling 연습

## 함수

```python
def equipment_control(
    equipment: str,
    action: str,
):
    equipment_action = f'I Turned {action} {equipment}.'
    print(equipment_action)
    return equipment_action
```

## `main.py`

사용자의 상태나 요청을 파악하여 적절한 장비를 상황에 맞게 제어하는 함수를 호출

질문:

- 더워 (It is hot)
- 드라마가 보고 싶어 (I want to watch a drama)
- 이제 잘거야 (I'm going to sleep)
- 세종대황은 어떤 곡을 작곡했어? (What song did King Sejong compose?)
- 음악의 아버지는 누구야? (Who is the father of music?)

결과:

- 적절한 장비를 제어하여 사용자의 요청에 맞게 처리합니다.
- 장비 제어와 관계 없는 질의는 질의에 맞는 답변을 합니다.

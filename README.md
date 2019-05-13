# 42maru QA Engine API Client for Python

1. [**Install**](./#install)
2. [**Insert Data**](./#insert-data)
3. [**Inquiry**](./#inquiry)

## Install

```bash
pip3.6 install --extra-index-url http://ec2-13-125-248-226.ap-northeast-2.compute.amazonaws.com/simple --trusted-host ec2-13-125-248-226.ap-northeast-2.compute.amazonaws.com -r ./requirements_private.txt
```

sample requirements\_private.txt

```text
f2maru-qa==0.0.1
```

## Insert data

```python
from f2maru_qa.client import Client

app_code = "143e6a1a2384405ebdd98d8174c4080f"
api_key = "938214eb094c432b8f893bbdc8732a26"
client = Client(app_code, api_key)

result = client.bulk_insert(json.load(open('sample.json')))
print("bulk insert result is {}".format(result))
```

sample.json

```javascript
[
  {
    "title": "사레 들린 백종원, 큰 충격 받은 조보아... 경악스럽다",
    "content": "철없는 자영업자들을 보고 있노라니 속이 답답했다. 재밌자고 보는 예능 프로그램인데, 남는 건 혈압뿐인 듯하다. SBS <백종원의 골목식당>의 고로케집 사장과 피자집 사장 이야기다.입으로는 절박하다고 말하지만, 그들의 행동에는 여전히 정체불명의 여유가 넘친다. 포방터 시장의 돈가스집 사장처럼 폭삭 망해본 경험이 없기 때문일까? 그래서 삶의 무게를 제대로 느껴보지 못한 걸까? 절실함이 전혀 없는 그들의 태도가 이젠 불편하기까지 하다."
  },
  {
    "title": "'복수돌' 조보아-곽동연, 끝나지 않은 '외사랑 투샷'",
    "content": "설송고 교사 손수정역을, 복수에게 애증과 열등감을 가진 설송고 이사장 오세호 역을 맡았다. 극중 두 사람은 복수와 삼각관계 구도를 형성, 설송고의 시스템과 로맨스에서 팽팽하게 대립하며 극의 긴장감을 증폭시키고 있다."
  },
  {
    "title": "조보아 나이에 관심 증폭…‘복수돌’ 유승호와 연상연하",
    "content": "상대역인 유승호는 1993년생으로 올해 27세가 됐다. 두 사람은 2살 차로 '복수가 돌아왔다'에서 인상 깊은 연기를 보여주고 있다."
  }
]
```

## Inquiry

```python
from f2maru_qa.client import Client

app_code = "143e6a1a2384405ebdd98d8174c4080f"
api_key = "938214eb094c432b8f893bbdc8732a26"
client = Client(app_code, api_key)

res = client.inquiry("유승호 나이는?")
pprint(res)
```


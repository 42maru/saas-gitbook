---
description: >-
  이 문서에는 ${Platform} 활용 필수적인 계정 및 ${app} 생성 방법을 다루고 있습니다. 또한 선택저인 기능인 SDK 설치 방법에
  대해서 기술하고 있습니다.
---

# Getting Started

## Required

${platform} 의 검색 서비스를 이용하기 위해서는 계정 및 ${app} 을 생성해야 합니다.

### Step 1 : Sign Up

-- Home 화면 구현이 아직 안됨

### Step 2 : Create an App

최초로 계정 정보를 등록하신 후 접하게 되는 아래 화면을 통해 새로운 ${APP} 에 대한 정보를 등록할 수 있습니다. ${Platform} 의 모든 기능들은 ${APP} 단위로 구분되어 있기 때문에 ${APP} 간에 공유되거나 영향을 주지 않습니다. 이를 활용하여 사용자는 다양한 설정값과 데이터에 기반해서  ${Platform} 기능들을 활용하는 것이 가능합니다.

* 애플리케이션 이름 : ${APP} 이름
* 애플리케이션 설정 언어 : 검색엔진이 받아들이게  ${query} 의 언어
* 임계값 : 검색엔진 ${query}를 바탕으로 찾은 ${answer}를 정답으로 인정하기 위한 최소 ${validity}. 이 점수 미만의 정답은 ${noanswer} 를 반환하게 됩니다.

{% hint style="info" %}
애플리케이션 언어는 한국어와 English 로 설정 가능합니다.
{% endhint %}

![](.gitbook/assets/image%20%283%29.png)

## Optional : Installation SDK

### Python

```text
$ pip install ~~~
```

## Next Steps

계정 및 ${app} 이 생성 되었다면 각각의 검색서비스를 이용하실 수 있으며 방은 아래 문서에 기재되어 있습니다.

{% page-ref page="search-service/usd-mrc/" %}

{% page-ref page="search-service/usd-nlp.md" %}


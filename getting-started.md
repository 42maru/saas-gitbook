---
description: '이 문서에서는 ${platform} 이용 전 필수 준비과정과 선택적 준비과정을 설명하고 있습니다.'
---

# Getting Started

## Required

${platform} 의 검색 서비스를 이용하기 위해서는 계정 및 ${app} 을 생성해야 합니다.

### Step 1 : Sign Up

-- Home 화면 구현이 아직 안됨

### Step 2 : Create an App

최초로 계정 정보를 등록하신 후 접하게 되는 아래 화면에서 새로운 ${APP} 을 생성하실 수 있습니다. ${Platform} 의 모든 기능들은 ${APP} 단위로 구분되어 있기 때문에 ${APP} 은 서로 정보를 공유하거나 영향을 주지 않습니다. 따라서 사용자는 다양한 설정값과 데이터로 만들어진 여러 개의 ${APP}을 운영하는 것이 가능합니다.

* 애플리케이션 이름 : ${APP} 이름
* 애플리케이션 설정 언어 : ${APP} 은 이곳에서 설정한 언어를 앞으로 들어올 ${query} 의 언어라고 인지합니다.
* 임계값 : 임계값은 ${platform}의 검색엔진이 ${answer}를 찾은 후 해당 ${answer}이 신뢰할 만한 ${answer} 확인하기 위한 기준 값 입니다. 앞으로 들어올 ${query}에 대해서 검색엔진이 찾아낸 정답의 ${t}
* 검색엔진 ${query}를 바탕으로 찾은 ${answer}를 정답으로 인정하기 위한 최소 ${validity}. 이 점수 미만의 정답은 ${noanswer} 를 반환하게 됩니다.

{% hint style="info" %}
애플리케이션 언어는 한국어와 English 로 설정 가능합니다.
{% endhint %}

![](.gitbook/assets/image%20%288%29.png)

### Step 3 : authentication

${App} 을 생성하게 되면 ${platform} 의 기능 대부분을 사용하실 수 있습니다. 하지만 API 나 SDK 를 통하여   
${platform} 의 기능을 사용하시려면 ${App}의 Application Code 값과 API Key 값이 필요합니다. 이 값들은 Setting 탭에서 확인하실 수 있습니다.

![http://alpha.42maru.com/applications/{app\_code}/settings](.gitbook/assets/image%20%284%29.png)



## Optional : Installation SDK

### Python

```text
$ pip install ~~~
```

## Next Steps

계정 및 ${app} 이 생성 되었다면 각각의 검색서비스를 이용하실 수 있으며 방법은 아래 문서들에 기재되어 있습니다.

{% page-ref page="search-service/usd-mrc/" %}

{% page-ref page="search-service/usd-nlp.md" %}


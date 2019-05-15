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
* 임계값 : 임계값은 검색엔진 성능의 엄격함을 나타냅니다. 검색엔진이 ${query} 를 전달받으면 우선 ${answer}이 될만한 후보군들을 찾아냅니다. 그리고 각 후보가 ${answer}에 적절한지 점수를 매깁니다. 최종적으로 검색엔진은 임계값 이상의 점수를 가진 후보군 중 가장 높은 점수의 후보군을  ${answer}로 사용자에게 전달합니다. 만약 모든 후보군이 임계값에 미치지 못한다면 검색엔진은 ${noanswer} 로 판단합니다.

{% hint style="info" %}
애플리케이션 언어는 한국어와 English 로 설정 가능합니다.
{% endhint %}

{% hint style="warning" %}
임계값을 지나치게 낮게 설정한다면 잘못된 ${query} 에 대해서도 ${answer} 를 찾아내서 반환하게 됩니다. 반면 임계값이 지나치게 높으면 ${answer} 판단이 엄격해지게 되어 많은 ${query} 에 대해서 ${noanswer}로 판단합니다. 따라서 임계값을 수정하면서 Test 를 거쳐 적절한 임계값을  설정하기를 권장드립니다. 
{% endhint %}

![](.gitbook/assets/image%20%289%29.png)

### Step 3 : authentication

${App} 을 생성하게 되면 ${platform} 의 기능 대부분을 사용하실 수 있습니다. 하지만 API 나 SDK 를 통하여   
${platform} 의 기능을 사용하시려면 ${App}의 Application Code 값과 API Key 값이 필요합니다. 이 값들은 Setting 탭에서 확인하실 수 있습니다.

![http://alpha.42maru.com/applications/{app\_code}/settings](.gitbook/assets/image%20%285%29.png)



## Optional : Installation SDK

### Python

```text
$ pip install ~~~
```

## Next Steps

계정 및 ${app} 이 생성 되었다면 각각의 검색서비스를 이용하실 수 있으며 방법은 아래 문서들에 기재되어 있습니다.

{% page-ref page="search-service/usd-mrc/" %}

{% page-ref page="search-service/usd-nlp.md" %}


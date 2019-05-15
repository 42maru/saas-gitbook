---
description: '이 문서에는 ${MRC} 검색엔진에 ${passage}  데이터를 등록하는 방법이 기술되어 있습니다.'
---

# Insert Data

## Browser

Browser 상에서 ${passage} 문서 추가는 Documents 화면에서 가능합니다.

![](../../.gitbook/assets/image%20%285%29.png)

그 다음 File Upload 버튼을 누르시면 파일은 업로드 하실 수 있습니다.

{% hint style="info" %}
json, excel 형식의 파일을 지원합니다.
{% endhint %}

![](../../.gitbook/assets/image%20%286%29.png)

## SDK



{% api-method method="post" host="https://13.209.5.247" path="/api/application/documents/bulk" %}
{% api-method-summary %}
API
{% endapi-method-summary %}

{% api-method-description %}

{% endapi-method-description %}

{% api-method-spec %}
{% api-method-request %}
{% api-method-headers %}
{% api-method-parameter name="X-PLATFORM42-APP-ID" type="string" required=true %}
${app} 식벽을 위한 id 
{% endapi-method-parameter %}

{% api-method-parameter name="X-PLATFORM42-API-KEY" type="string" required=true %}
${app} 정보 조회의 권환 획득을 위한 key  
{% endapi-method-parameter %}
{% endapi-method-headers %}

{% api-method-body-parameters %}
{% api-method-parameter name="" type="array" required=true %}

{% endapi-method-parameter %}
{% endapi-method-body-parameters %}
{% endapi-method-request %}

{% api-method-response %}
{% api-method-response-example httpCode=200 %}
{% api-method-response-example-description %}

{% endapi-method-response-example-description %}

```

```
{% endapi-method-response-example %}
{% endapi-method-response %}
{% endapi-method-spec %}
{% endapi-method %}



${MRC }검색 엔진에 전달할 ${query}








---
description: '${MRC} 를 사용하기 위해서는 먼저 ${passage} 데이터를 업로드 하셔야 합니다.'
---

# Insert Data

### Browser

Browser 상에서 ${passage} 문서 추가는 Documents 화면에서 가능합니다.

![](../../.gitbook/assets/image.png)

그 다음 File Upload 버튼을 클릭 하시면 새로운 창이 팝업되며 이곳에서 drag&drop 으로 파일을 업로드 하실 수 있습니다.

{% hint style="info" %}
json, excel 형식의 파일을 지원합니다.
{% endhint %}

![](../../.gitbook/assets/image%20%2810%29.png)

### SDK



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
${app} 의 ID 값
{% endapi-method-parameter %}

{% api-method-parameter name="X-PLATFORM42-API-KEY" type="string" required=true %}
${app} 의 접근권한을 가진 Key 값
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
ㅁㄴㅇㄹㅁㄴㅇㄹ
```
{% endapi-method-response-example %}
{% endapi-method-response %}
{% endapi-method-spec %}
{% endapi-method %}












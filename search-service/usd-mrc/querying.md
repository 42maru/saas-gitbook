---
description: '이 문서에는 ${MRC} 검색엔진에 ${query} 를 전달해서 ${answer} 를 받는 방법이 기술되어 있습니다.'
---

# Querying

## Browser

## SDK



{% api-method method="get" host="https://13.209.5.247" path="/api/broker/answer" %}
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
{% api-method-parameter name="query" type="string" required=false %}
${MRC }검색 엔진에 전달할 ${query}
{% endapi-method-parameter %}

{% api-method-parameter name="debug" type="string" required=false %}
??
{% endapi-method-parameter %}

{% api-method-parameter name="count" type="string" required=true %}
검색엔진이 찾아낸 ${answer} 후보 중 상위 몇 개의 ${answer} 를 받을 것인지에 대한 설정
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










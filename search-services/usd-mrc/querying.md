---
description: MRC 검색엔진은 업로드 된 문서를 바탕으로 질문의 정답을 찾아냅니다.
---

# Querying

## Browser

Simulation 메뉴로 이동합니다. 그리고 텍스트 박스\(Questions\) 안에 질문 입력합니다.

![http://alpha.42maru.com/applications/{app\_code}/mrc/simulation](../../.gitbook/assets/image-6.png)

질문을 입력 하셨다면 정답과 검색된 문서를 확인하실 수 있습니다. 정답은 신뢰도 값에 의해서 내림차순 정렬됩니다.

> 정답과 함께 나타난 값\(ex.0.996\) 은 해당 정답에 대한 신뢰도를 의미합니다.

![](../../.gitbook/assets/image-7.png)

{% api-method method="get" host="http://alpha.42maru.com" path="/api/broker/answer" %}
{% api-method-summary %}
Get MRC result
{% endapi-method-summary %}

{% api-method-description %}
질문에 해당하는 정답을 반환합니한다.
{% endapi-method-description %}

{% api-method-spec %}
{% api-method-request %}
{% api-method-headers %}
{% api-method-parameter name="X-PLATFORM42-APP-ID" type="string" required=true %}
app의 id
{% endapi-method-parameter %}

{% api-method-parameter name="X-PLATFORM42-API-KEY" type="string" required=true %}
app의 접근권한을 가진 Key
{% endapi-method-parameter %}
{% endapi-method-headers %}

{% api-method-body-parameters %}
{% api-method-parameter name="query" type="string" required=true %}
MRC검색 엔진에 전달할 질문
{% endapi-method-parameter %}

{% api-method-parameter name="debug" type="boolean" required=false %}
true로 설정 시 검색 결과를 자세히 확인할 수 있다.
{% endapi-method-parameter %}

{% api-method-parameter name="count" type="integer" required=false %}
응답으로 받을 정답 상위 후보군의 개수
{% endapi-method-parameter %}
{% endapi-method-body-parameters %}
{% endapi-method-request %}

{% api-method-response %}
{% api-method-response-example httpCode=200 %}
{% api-method-response-example-description %}

{% endapi-method-response-example-description %}

```yaml
{
    "data": {
        "answer": [
            "절충장군전라좌도수군절도사",
            "위인",
            "장군"
        ]
    }
}
```
{% endapi-method-response-example %}

{% api-method-response-example httpCode=400 %}
{% api-method-response-example-description %}

{% endapi-method-response-example-description %}

```text

```
{% endapi-method-response-example %}
{% endapi-method-response %}
{% endapi-method-spec %}
{% endapi-method %}


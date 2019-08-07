---
description: MRC 를 사용하기 위해서는 먼저 문서 데이터를 업로드 하셔야 합니다.
---

# Upload passage

## Browser

문서 추가는 Documents 화면에서 가능합니다.

![](../../.gitbook/assets/image.png)

그 다음 File Upload 버튼을 클릭 하시면 새로운 창이 팝업되며 이곳에서 드래그 앤 드롭으로 파일을 업로드 하실 수 있습니다.

{% hint style="info" %}
json, excel 형식의 파일을 지원합니다.
{% endhint %}

![](../../.gitbook/assets/image-11.png)



{% api-method method="post" host="http://alpha.42maru.com" path="/api/application/documents" %}
{% api-method-summary %}
Upload a passage
{% endapi-method-summary %}

{% api-method-description %}
 하나의 문서를 업로드 한다.
{% endapi-method-description %}

{% api-method-spec %}
{% api-method-request %}
{% api-method-headers %}
{% api-method-parameter name="X-PLATFORM42-APP-ID" type="string" required=true %}
app의 id
{% endapi-method-parameter %}

{% api-method-parameter name="X-PLATFORM42-API-KEY" type="string" required=true %}
app의 접근권한을 가진 key
{% endapi-method-parameter %}
{% endapi-method-headers %}
{% endapi-method-request %}

{% api-method-response %}
{% api-method-response-example httpCode=200 %}
{% api-method-response-example-description %}

{% endapi-method-response-example-description %}

```yaml
{
    "data": {
        "id": 3044702,
        "doc_id": 337842,
        "application_id": 24,
        "title": "제한 효소",
        "content": "몇 종류의 제한 효소를 이용하여 목표 DNA 와 반응을 시키면, 각각의 제한 효소가 특정한 염기서열 을 인식해 DNA 를 절단하므로, 특정한 제한 효소 작용자리가 상대적으로 어느 위치인지 알 수 있다. 이를 이용하여 유전자 지도를 작성한다.",
        "deleted": false,
        "created_at": "2019-08-07T02:27:54",
        "updated_at": null
    }
}
```
{% endapi-method-response-example %}

{% api-method-response-example httpCode=400 %}
{% api-method-response-example-description %}

{% endapi-method-response-example-description %}

```

```
{% endapi-method-response-example %}
{% endapi-method-response %}
{% endapi-method-spec %}
{% endapi-method %}

Body parameters

{% hint style="info" %}
content는 필수정보 입니다.
{% endhint %}

```yaml
{
    "doc_id": 337842,
    "title": "제한 효소",
    "content": "몇 종류의 제한 효소를 이용하여 목표 DNA 와 반응을 시키면, 각각의 제한 효소가 특정한 염기서열 을 인식해 DNA 를 절단하므로, 특정한 제한 효소 작용자리가 상대적으로 어느 위치인지 알 수 있다. 이를 이용하여 유전자 지도를 작성한다."
}
```

{% api-method method="post" host="http://alpha.42maru.com" path="/api/application/documents/bulk" %}
{% api-method-summary %}
Upload many passages
{% endapi-method-summary %}

{% api-method-description %}
 여러개의 문서를 업로드 한다.
{% endapi-method-description %}

{% api-method-spec %}
{% api-method-request %}
{% api-method-headers %}
{% api-method-parameter name="X-PLATFORM42-APP-ID" type="string" required=true %}
app의 ID
{% endapi-method-parameter %}

{% api-method-parameter name="X-PLATFORM42-API-KEY" type="string" required=true %}
app 의 접근권한을 가진 Key
{% endapi-method-parameter %}
{% endapi-method-headers %}
{% endapi-method-request %}

{% api-method-response %}
{% api-method-response-example httpCode=200 %}
{% api-method-response-example-description %}

{% endapi-method-response-example-description %}

```yaml
{
    "data": {}
}
```
{% endapi-method-response-example %}

{% api-method-response-example httpCode=400 %}
{% api-method-response-example-description %}

{% endapi-method-response-example-description %}

```

```
{% endapi-method-response-example %}
{% endapi-method-response %}
{% endapi-method-spec %}
{% endapi-method %}

Body Parameters

{% hint style="info" %}
content는 필수정보 입니다.
{% endhint %}

```yaml
[
    {
        "doc_id": 337842,
        "title": "제한 효소",
        "content": "몇 종류의 제한 효소를 이용하여 목표 DNA 와 반응을 시키면, 각각의 제한 효소가 특정한 염기서열 을 인식해 DNA 를 절단하므로, 특정한 제한 효소 작용자리가 상대적으로 어느 위치인지 알 수 있다. 이를 이용하여 유전자 지도를 작성한다."
    },
    {
        "doc_id": 337842,
        "title": "제한 효소",
        "content": "사람의 DNA 중 유용한 물질을 생산하는 부분을 제한 효소로 절단하여 조각을 대장균 의 플라스미드 DNA 에 연결한다. 형질전환 된 플라스미드를 대장균 에 삽입하여, 짧은 시간에 유용한 물질을 대량 생산한다."
    },
    {
        "doc_id": 1758246,
        "title": "윤정일 (배우)",
        "content": "--중앙대학교 연극학과\r\n"
    },
    {
        "doc_id": 1758246,
        "title": "윤정일 (배우)",
        "content": "--《 심장박동조작극 》 (2017년) - 승빈 역\r\n--《 양치기들 》 (2016년) - 영민 역\r\n--《 동주 》 (2016년) - 조선유학생 2 역\r\n"
    }
]
```


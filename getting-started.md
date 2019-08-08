---
description: '${platform}을 이용하기 위해서는 몇 가지 과정이 필요합니다.'
---

# Getting Started

## Required

${platform} 의 검색 서비스를 이용하기 위해서는 계정과 애플리케이션을 생성해야 합니다.

### Step 1 : 회원가입 

회원가입이 필요한 경우, '로그인' '페이지 하단에 위치한 \[Sign up for an account\] 버튼을 클릭하여 '회원가입' 페이지로 이동 후 계정을 생성합니다.

![](.gitbook/assets/2_sign-up.jpg)

![](.gitbook/assets/2_sign-up-2%20%281%29.jpg)

### Step 2 : 애플리케이션 생성

#### 계정 생성

회원가입 후 접하게 되는 'Create application' 화면에서 새로운 애플리케이션을 생성할 수 있습니다.

![](.gitbook/assets/3_create-app.jpg)

* **Name** : 애플리케이션의 이름을 설정합니다.
* **Documents language** : 검색 대상이 되는 문서의 언어를 설정합니다. 애플리케이션은 이곳에서 선택된 언어를 문서의 언어와 사용자가 입력한 질문 언어로 인식합니다. 현재까지 Korean, English, Deutsch 총 3개의 언어를 지원하며, 한 애플리케이션 당 언어 한 개를 선택할 수 있습니다. 애플리케이션 생성 시에만 Document language 선택이 가능하고 애플리케이션 생성을 완료한 후에는 이 설정을 변경할 수 없습니다. 따라서, 다른 언어로 변경하고 싶을 경우 새로운 애플리케이션을 생성해야 합니다.
* **Threshold** : 답변 여부를 결정하는 기준값입니다. Threshold을 너무 낮게 설정하면 정밀도\(Precision\)가 떨어질 수 있고, Threshold을 너무 높게 설정하면 재현율\(Recall\)이 떨어질 수 있습니다. 따라서, Test를 거쳐 적절한 Threshold를 설정하기를 권장드립니다. 
* **Regions** : 서버를 생성할 지역을 설정합니다. 실제 서비스가 나가는 지역과 가까운 지역을 선택합니다. 애플리케이션의 데이터를 여러 지역의 서버에 저장할 수 있습니다. 모든 API 요청은 응답속도가 더 빠른 서버로 라우팅 됩니다.

{% hint style="success" %}
사용자는 다양한 설정값과 데이터로 만들어진 여러 개의 애플리케이션을 동시에 운영할 수 있습니다. ${Platform}의 계정관리 기능을 제외한 모든 기능들은 애플리케이션 단위로 구분됩니다. 애플리케이션은 서로 독립적이며 한 애플리케이션의 변화가 다른 애플리케이션에 영향을 주지 않습니다.
{% endhint %}

#### 애플리케이션 추가 생성

애플리케이션을 추가하고 싶다면 다음의 단계를 통해 쉽게 생성할 수 있습니다.

1. 메뉴 네비게이션 바의 상단에서 \[Current app\]을 클릭합니다.
2. 드롭다운 메뉴 내  \[New Application\]를 클릭하면 'Create application' 페이지로 전환됩니다.
3. 'Create application' 페이지에서 주어진 항목을 모두 설정하고 \[Save\]를 클릭하면 애플리케이션이 생성됩니다.

![](.gitbook/assets/4_add-app.jpg)

### Step 3 : 인증키 확인

애플리케이션을 생성하게 되면 ${platform}의 기능 대부분을 사용할 수 있습니다. API와 SDK를 사용할 때는 app의 Application Code 값과 API Key 값이 필요합니다.

**Application Code 값, API Key 값 확인**

이 값들은 화면 좌측 메뉴 네비게이션 바 하단에 위치한 'Settings' 메뉴에 들어가서 확인할 수 있습니다.

![http://alpha.42maru.com/applications/{app\_code}/settings](.gitbook/assets/image-5.png)

* **Application Information**: 애플리케이션 정보를 확인, 변경, 삭제할 수 있습니다.
* **Application Code**: ****API를 사용할 때 애플리케이션을 식별하는 데 사용되는 키 값을 확인할 수 있습니다.
* **API Key**: Admin API, Monitoring API, Search QA API를 호출할 때 필요한 키 값을 확인, 변경할 수 있습니다. 
* **IP Blacklist**: API에 접근 금지가 필요한 IP를 등록, 수정, 삭제할 수 있습니다. 
* **Regions**: 애플리케이션의 데이터를 저장할 서버의 위치를 확인, 변경할 수 있습니다.  

## Optional : Installation SDK

### Python

```text
$ pip install ~~~
```

## Next Steps

계정 및 app이 생성 되었다면 ${platform} 의 기능들을 정삭적으로 이용하실 수 있습니다.

### Search Services

{% page-ref page="search-services/usd-mrc/" %}

### Features

{% page-ref page="features/usd-mrc.md" %}

{% page-ref page="features/log.md" %}

{% page-ref page="features/static/" %}

{% page-ref page="features/frequently.md" %}

{% page-ref page="features/simulation.md" %}

{% page-ref page="features/api.md" %}

{% page-ref page="features/app.md" %}

### Additional Resources

{% page-ref page="additional-resources/untitled.md" %}

{% page-ref page="additional-resources/glossary.md" %}

{% page-ref page="additional-resources/security.md" %}

{% page-ref page="additional-resources/usd-mrc.md" %}

{% page-ref page="additional-resources/troubleshooting.md" %}


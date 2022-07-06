---
layout: post
title: "[회고] 성능 측정의 필요성 - 성능 테스트 자동화 플랫폼 개발기 (1)"
summary: "성능 테스트 자동화 플랫폼 개발 회고, 성능 측정의 필요성"
thumbnail: "https://media.giphy.com/media/l2Je6xTnSDh4dmA4o/giphy.gif"
category: dev
tags: [retrospective, performance-test-automation]
comments: true
date: 2022-07-06 19:11:00
lastmod: 2022-07-06 19:11:00
series: performance-test-automation
sitemap: 
  changefreq: daily
  priority: 1.0
---
# 성능 측정의 필요성

![weredoomed](https://media.giphy.com/media/l2Je6xTnSDh4dmA4o/giphy.gif)

2021년 8월 9일 [이파피루스](https://www.epapyrus.com)에 입사 후 벌써 다음달이면 입사 1년차를 바라보고있습니다.

그동안 제가 진행했던 가장 큰 프로젝트인 `PdfGateway` 차세대 버전 출시가 얼추 마무리되고 제품을 검증하기 위한 테스트가 내부적으로 진행되었습니다.

10만건, 100만건의 변환 작업을 투입하고 오류가 발생하지는 않는지, 병목이 발생하지는 않는지 검증했고 안정적으로 부하를 견딘다고 판단했고 제품을 출시하게 되었습니다.

## 그래서, 뭐가 더 좋아진건데요?

![](https://media.giphy.com/media/4GIcsQJorDZOU/giphy.gif)
> 내부적으로 구현이 깔끔해졌다. 복잡한 데이터베이스 의존성을 단순하게 변경했다. 락에 의한 병목을 최소화 했다. 등등…
>

더 나아졌을거라는 느낌은 있었지만 **이를 확실하게 보여줄만한 자료**는 없었습니다.

그 때 일부 고객들이 **제품의 성능 측정 자료**를 요구했고, 그런 준비가 되어있지 않았던 우리는 부랴부랴 지표를 만들어내기 시작했습니다.

# 무엇을 성능의 지표로 삼을것인가?

일단 만들긴 해야겠는데, `PdfGateway`의 성능이란 무엇이고 `어떻게` 측정할 수 있을까에 대한 고민을 하게되었습니다.

> `PdfGateway`의 가장 주요한 기능은 **문서변환**!
>

따라서 `PdfGateway`는 동일한 파일에 대한 변환 과정에서 변환 시작 부터 변환 완료 까지의 **시간**이 성능의 지표가 될 것이라고 생각했습니다.

## 고객의 관심사

고객은 우리의 제품이 어떻게 구현되었고, 어디에서 병목이 발생하는지에 대해서는 크게 관심을 두지 않습니다.

그저 **문서 변환에 얼마나 걸리는지**가 주된 관심사일 것이라고 생각했습니다.

## 우리의 관심사

개발자인 우리는 우리의 제품이 **어디에서 병목이 발생하는지**, 기능 추가 이후 **성능 저하는 없는지**에 대한 **꾸준한 검증**이 필요했습니다.

## 일단 고객이 먼저다

![](https://media.giphy.com/media/3o6Mbe90zhQaXhWSw8/giphy.gif)

기업을 상대로 제품을 판매하는 B2B 회사인 만큼, 우리 회사의 타겟은 고객이 최우선이였습니다.

따라서 일단 **고객이 원하는 지표를 생성하는 프로토타입**을 만들어보자가 첫번째 과제였습니다.

# 프로토타입 개발

![](https://media.giphy.com/media/hbd8nlok7kqnS/giphy.gif)

첫번째 프로토타입은 `PgPerformanceTester`라는 프로젝트였습니다.

파일 서버에 변환 테스트 대상 파일들을 확장자, 크기별로 준비해놓고

아래와 같은 지표를 설정했습니다.

- 해당 파일들에 대해 1, 2, 4, 8, 16회 동시변환 시 시간이 얼마나 걸리는지
- 이 속도라면 1시간동안 얼마나 변환될지
- 하루에 몇개나 변환할 수 있을지

그리고 코드를 작성했습니다…

> 데이터 생성되는걸 보는것만이 유일한 목표였기 때문에...  
> 근본 언어인 C언어 스타일로 개발했습니다.
>
> .  
> .  
> .
>   
> ![](https://media.giphy.com/media/Zd0EmHgMwPvJfCuypE/giphy.gif)
> ~~메인_함수님만_믿습니다.jpg~~
>
>
> ![trash-code](https://github.com/outstanding1301/outstanding1301.github.io/blob/master/imgs/dev/2022-07-06-performance-test-automation-1/trash-code.png?raw=true)
>

`PdfGateway`는 배치프로그램이기 때문에, 변환 결과를 Http 응답으로 주지 않습니다.

그 대신 요청시 `callbackUri`를 body로 보내고, 변환 완료 시 해당 `callbackUri`로 변환 결과를 `POST` 요청하는  비동기 방식입니다.

따라서 callback 요청을 처리할 서버가 필요했습니다…

## 알고 계셨나요? 자바에는 내장 HttpServer가 있답니다~

> [com.sun.net.httpserver.HttpServer](https://docs.oracle.com/javase/8/docs/jre/api/net/httpserver/spec/com/sun/net/httpserver/HttpServer.html)

```java
private void startHttpServer() {
  new Thread(() -> {
    try {
      this.server = HttpServer.create(new InetSocketAddress(8081), 0);
      this.server.createContext("/callback", exchange -> {
        PgResult pgResult =
          gson.fromJson(new InputStreamReader(exchange.getRequestBody()), PgResult.class);
        Optional.ofNullable(unitSent.get(pgResult.getId()))
                .ifPresent(testUnit -> testUnit.getResult().complete(pgResult));
        String res = "ok";
        exchange.sendResponseHeaders(200, res.length());
        OutputStream os = exchange.getResponseBody();
        os.write(res.getBytes());
        os.close();
      });
    } catch (IOException e) { throw new RuntimeException(e); }
    this.server.start();
  }).start();
}
```

> ![](https://media.giphy.com/media/l2JdT331SygGYI4wg/giphy.gif)  
> 
> 그냥 스프링을 쓰는게 더 좋았을텐데…

처음 써본 `HttpServer`로 아주 간단한 callback 서버를 만들어서 테스트를 진행했습니다..

그 결과는…

## 매번 다른 변환시간

> 아까는 1초 걸렸는데 이번엔 3초 걸리네
>

테스트 대상 **서버 환경**에 따라 변환에 걸리는 시간 차이가 많이 벌어졌습니다.

어차피 한번 쓰고 버릴 프로그램이라 다시 만들기는 귀찮고, 해야할 다른 일은 많고…

<br>
<br>

![](https://media.giphy.com/media/xp5APxhshrOTPjGBWQ/giphy.gif)
<br>
**그냥 여러번 돌려서 통계를 내자!**

## 어쨌든 목표 달성 😄

![](https://media.giphy.com/media/3orieZOr8fdbGbNmTK/giphy.gif)

우여곡절 끝에 부랴부랴 만들어진 산출물…

> 만나서 반가웠고 다신 보지말자 :)
>
>
> ![report](https://github.com/outstanding1301/outstanding1301.github.io/blob/master/imgs/dev/2022-07-06-performance-test-automation-1/report.png?raw=true)
>

매번 성능 측정이 필요할때마다 이걸 계속 수동으로 반복해야한다니…

[처음 만든 사람](https://namu.wiki/w/%EB%82%98(%EC%9D%B8%EC%B9%AD%EB%8C%80%EB%AA%85%EC%82%AC))이 앞으로도 계속 문서작업을 해야하지 않을까? 하는 생각이 들었습니다.

동시에 목표 또한 생겼습니다.

> **성능 측정 자동화**가 필요하겠다. 

팀장님과 몇번의 대화 그리고 회의 끝에 **성능 테스트 자동화 플랫폼 개발**이라는 과제가 저에게 주어졌습니다.

# 어떻게 만들것인가?

![](https://media.giphy.com/media/3ohs7KViF6rA4aan5u/giphy.gif)

그건 다음에 알아보죠~ 😊

---
layout: post
title: "[Java] 트위치 후원 알림 API (Twip, Toonation API)"
summary: "트윕과 투네이션의 후원 알림을 받아올 수 있는 Java API를 만들어봤습니다."
thumbnail: "https://camo.githubusercontent.com/be236b497b774e34606403d363620dacb54a61d8dbe17028bfe06cd51ccf0b65/68747470733a2f2f6d656469612e67697068792e636f6d2f6d656469612f336f726966316573496e56546468614e736b2f67697068792e676966"
category: dev
tags: [java, rxjava, twitch]
comments: true
date: 2021-01-15 23:18:19
lastmod: 2021-01-15 23:18:19
sitemap: 
  changefreq: daily
  priority: 1.0
---

# 💸 Donation Alert API

오늘은 [내가 만든 트위치 후원 알림 API](https://github.com/outstanding1301/donation-alert-api)를 소개하려고 한다.  
정확히 말하자면, [Twip](http://twip.kr/)과 [Toonation](https://toon.at/)의 Alertbox 알림을 받아올 수 있는 API이다.  

### 😎 왜 만들게 되었나!  

오래 알고지내는 [한 마인크래프트 유튜버](https://www.youtube.com/user/koyeyu)가 혹시 트윕 후원 내용을 마인크래프트로 보여줄 수 없냐고 물어봐서 만들게 되었다.

> <iframe width="560" height="315" src="https://www.youtube-nocookie.com/embed/ma5XgTHeCyg" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
>    
> 그리고 이렇게 쓰였다.  
> 참고로 이 영상의 0:45초에 나오는 **염료**가 마인크래프트 평행세계의 나다.

그래서.. 사실 만든지는 1년정도 됐다.  

그러다가 며칠 전 Twip의 1.1.60 패치 이후에 플러그인을 손 볼 일이 생겼다.  
오랜만에 보니까 참 감회가 새로웠는데, 이 도네이션 파싱(?) 기능만 따로 API로 만들어두면 누군가 유용하게 쓸 수 있지 않을까? 라는 생각이 들었다.

그래서 이것저것 떼어내고, 쓰기 쉽게 바꾸고... 하다보니 완성했다!

다 완성하고 나니 다른 라이브러리들처럼 깔끔하게 dependencies에 한 줄만 추가해서 사용할 수 있으면 얼마나 좋을까? 라는 생각을 하게되었고  

운 좋게도 나는 예전에 Jitpack이라는 것을 사용해봤으므로 Jitpack을 사용해서 아름답게 배포했다. (그냥 repository만 추가하면 된다.)  

## 🤔 어떻게 만들었나?
먼저 크롬의 개발자 도구로 Alertbox 위젯이 어떤 주소로 웹소켓에 연결하는지, 어떤 이벤트를 수신하는지 등을 살펴봤다.  

트윕은 [socket.io](https://github.com/socketio/socket.io-client-java), 투네이션은 WebSocket([okhttp](https://github.com/square/okhttp))을 사용해서 서로 다른 두 가지를 모두 써볼 수 있었다.  
(물론 클라이언트만, 그리고 okhttp는 socket.io에 내장되어있다.)  

그리고 [RxJava](https://github.com/ReactiveX/RxJava)라는 멋쟁이들에게만 허용된 라이브러리를 사용했다.  
웹소켓에 연결하고, 후원 발생 시 구독한 Observer들에게 이벤트를 전달한다!  

웹소켓을 통해 주고받는 메시지는 당연하게도 JSON 형식이라, [json-simple](https://mvnrepository.com/artifact/com.googlecode.json-simple/json-simple) 라이브러리를 사용했다.  
(마인크래프트의 bukkit이 json-simple을 내장하고 있기 때문에, 처음 만들때부터 json-simple을 사용하고 있었다.)  

우선은 내가 필요한 기능들만 구현해 놨는데, 누군가가 필요로 한다면 더 나아가서 Twip과 Toonation의 전체 기능에 대한 API로 확장 시켜보는 것도 재밌을 것 같다.

<hr>

## ✨ 소개합니다. Donation Alert API

[Twip](http://twip.kr/), [Toonation](https://toon.at/)의 후원 알림(Alertbox)을 받아올 수 있는 RxJava 기반 Java API  

![so much money](https://media.giphy.com/media/3orif1esInVTdhaNsk/giphy.gif)

> [outstandingboy/DonationAlertAPI](https://github.com/outstanding1301/donation-alert-api)  

----

# 🚀 Start
## Gradle (use [Jitpack](https://jitpack.io/))
```gradle
repositories {
    ...
    maven { url 'https://jitpack.io' }
}

dependencies {
    ...
    compile 'com.github.outstanding1301:donation-alert-api:1.0.0'
}
```

## Twip
```java
// Twip Alertbox URL의 마지막 https://twip.kr/widgets/alertbox/<YOUR_TWIP_KEY> 부분을 입력하세요.
Twip twip = new Twip("YOUR_TWIP_KEY");

// 메시지를 구독합니다.
// 연결 알림, 에러 등의 String 메시지를 처리하는 핸들러를 인자로 사용합니다. 
twip.subscribeMessage(s -> System.out.println(s));

// 도네이션 알림을 구독합니다.
// Donation 객체를 처리하는 핸들러를 인자로 사용합니다.
twip.subscribeDonation(donation -> {
    System.out.println("[Twip] "+donation.getNickName()+"님이 "+donation.getAmount()+"원을 후원했습니다.");
    System.out.println("후원 내용: "+donation.getComment());
});
```

## Toonation
```java
// Toonation Alertbox URL의 마지막 https://toon.at/widget/alertbox/<YOUR_TOONATION_KEY> 부분을 입력하세요.
Toonation toonation = new Toonation("YOUR_TOONATION_KEY");

// 메시지를 구독합니다.
// 연결 알림, 에러 등의 String 메시지를 처리하는 핸들러를 인자로 사용합니다. 
toonation.subscribeMessage(s -> System.out.println(s));

// 도네이션 알림을 구독합니다.
// Donation 객체를 처리하는 핸들러를 인자로 사용합니다.
toonation.subscribeDonation(donation -> {
    System.out.println("[Toonation] "+donation.getNickName()+"님이 "+donation.getAmount()+"원을 후원했습니다.");
    System.out.println("후원 내용: "+donation.getComment());
});
```

# 📃 Docs

## Donation

| 식별자 | 타입 | 설명 |
|:---:|:---:|:---:|
| id | String | 후원자 ID |
| nickname | String | 후원자 닉네임 |
| comment | String | 후원 내용 |
| amount | Integer | 후원 금액 |

<br>

## Platform (Twip, Toonation)

| 식별자 | 타입 | 설명 |
|:---:|:---:|:---:|
| subscribeDonation(Consumer<Donation> onNext) | void | 후원 알림 구독 |
| subscribeMessage(Consumer<String> onNext) | void | API 메시지 구독 |
| close() | void | 연결 종료 |
| getDonationObservable() | Subject<Donation> | 후원 알림 Subject 객체 반환 |
| getMessageObservable() | Subject<String> | API 메시지 Subject 객체 반환 |

# 💉 Dependencies
```gradle
implementation 'io.socket:socket.io-client:1.0.0'
implementation  'io.reactivex.rxjava2:rxjava:2.1.16'
implementation 'org.jsoup:jsoup:1.13.1'
implementation 'com.googlecode.json-simple:json-simple:1.1.1'
```
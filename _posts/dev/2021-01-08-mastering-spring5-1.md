---
layout: post
title: "[Spring] 왜 스프링 프레임워크를 사용할까? (Spring vs EJB, JavaEE)"
summary: "스프링 프레임워크의 특징 및 장점을 정리했습니다."
category: dev
tags: [spring]
comments: true
---
# ☘️ 왜 스프링 프레임워크를 사용할까?

## 📚 시리즈 - 스프링 5.0
1. [왜 스프링 프레임워크를 사용할까? (Spring vs EJB, JavaEE)](https://outstanding1301.github.io/dev/2021/01/08/mastering-spring5-1/)
2. [스프링 프레임워크의 주요 모듈들](https://outstanding1301.github.io/dev/2021/01/09/mastering-spring5-2/)
3. [DI(Dependency Injection, 의존성 주입)와 IoC(Inversion of Control, 제어 반전)](https://outstanding1301.github.io/dev/2021/01/11/di-and-ioc/)

----

## ⚽︎ 목표
본격적으로 스프링 프레임워크를 공부하기 전에, 왜 스프링이 좋은것인지 발전과정과 함께 살펴보자.

## 1. 스프링 프레임워크는 왜 생겼는가?
`스프링 프레임워크 1.0`은 2004년 3월에 릴리스됐다.  
스프링이 처음 나올 당시, 자바로 엔터프라이즈 애플리케이션을 개발하는 가장 일반적인 방법은 `EJB(Enterprise Java Beans)`를 사용하는 것이였다.  

### 그러나 EJB에는 단점이 있었다.
1. 단위 테스트가 어렵다.
2. 불필요한 메서드를 구현해야 한다.
3. 예외 처리가 번거롭다.
4. 배포가 불편하다.

### ☄️ 그 때 혜성과 같이 등장한 스프링 프레임워크
사람들은 왜 스프링 프레임워크에 열광했을까?? (지금까지도..)  

스프링 프레임워크가 중요한 이유는 다음과 같다.  
1. 단순화된 단위 테스팅
2. 복잡한 코드의 감소
3. 아키텍처의 유연성
4. 변화하는 시대를 선도

### 1. 단순화된 단위 테스팅  
> EJB는 단위테스트가 어렵다.

정확히 말하자면, EJB 컨테이너 외부에서 실행 하는 것이 어려웠다.  
그러므로 테스트를 위해서 반드시 컨테이너에 배포해야했다.  

그러나 스프링 프레임워크는 **의존성 주입(Dependency Injection, DI)** 이라는 개념을 도입했다.

#### 의존성 주입(Dependency Injection, DI)
> 간단히 말하자면, 사용할 도구를 외부에서 지정해 주는 것이다.  
> DI에 대해서는 나중에 자세히 알아보자!  
> [임시 링크](https://ko.wikipedia.org/wiki/%EC%9D%98%EC%A1%B4%EC%84%B1_%EC%A3%BC%EC%9E%85)

의존성 주입을 도입하면서, 단위 테스트를 위해 전체 애플리케이션을 배포할 필요가 없게 됐다.  
단위 테스트 간소화의 이점은 다음과 같다.
- 생산성 향상  
- 빠른 결함 발견 -> 수정 비용이 적음
- **지속적인 통합(Continuous Integration, CI)** 시 자동화된 단위 테스트로 향후 결함을 예방

### 2. 복잡한 코드의 감소
자바로 데이터베이스 연동을 해 본 사람이라면 이런 코드를 한번 쯤은 작성 해 보았을 것이다.

```java
Connection con = null;
PreparedStatement stmt = null;

String sql = /* INSERT 문 */;

try {
    con = DriverManager.getConnection(DB_URL, DB_ID, DB_PW);
    stmt = con.prepareStatement(sql);
    stmt.setInt(1, id);
    stmt.setString(2, someValue);
    stmt.execute();
}
catch (Exception e) {
    e.printStackTrace();
}
finally {
    try {
        if (stmt != null) stmt.close();
        if (con != null) con.close();
    }
    catch (Exception e) {
        e.printStackTrace();
    }
}
```

이런 코드를 SQL 마다 작성해야 한다...

하지만 스프링 프레임워크의 Spring JDBC를 사용하면 다음과 같이 사용할 수 있다.

```java
String sql = /* INSERT 문 */;
jdbcTemplate.update(sql, id, someValue);
```

![말도 안돼...](https://media.giphy.com/media/CH0fzClj8QCDS/giphy.gif)

> 모든 메서드에서 예외 처리를 구현하는 대신,  
> 중앙 집중식 예외 처리를 수행하고 **관점 지향 프로그래밍(Aspect Oriented Programming, AOP)**을 사용해 주입할 수 있다고 한다.
>   
> 나중에 자세히 알아보자!


### 3. 아키텍처의 유연성

유연하다는 것은 무엇일까?  

> ~~유연한 사고, 남탓하지 않기~~

스프링 프레임워크는 `모듈 방식`이다.  
스프링 코어 모듈 위에 독립적인 모듈을 올려 완성한다.  

#### 🧐 모듈?
모듈화 디자인이란, 한 시스템을 여러 개의 기능적 구성요소(모듈)들을 조합함으로써 완성하도록 한 설계를 말한다.

> by [나무위키(~~꺼라~~)](https://namu.wiki/w/%EB%AA%A8%EB%93%88#s-1)

> 예를 들어, `옷을 입는 것`을 생각해보자.  
> 특히 `모자, 상의, 하의, 신발`만 선택한다고 했을 때  
> 우리는 다양한 조합을 생각할 수 있다.  
>  
> 각각의 모자, 상의, 하의, 신발들을 `모듈`이라고 생각해보자!  
>  
> 어떠한 `기능`(우리 예시에서는 `옷입기`)을 완성하는데 우리는 다양한 `모듈`(`옷`)을 선택할 수 있다.

사실 [정확한 정의(wikipedia)](https://ko.wikipedia.org/wiki/%EB%AA%A8%EB%93%88_(%ED%94%84%EB%A1%9C%EA%B7%B8%EB%9E%98%EB%B0%8D))와는 거리가 멀다.  

하지만 내가 무엇을 말하고 싶은건지 이해해줬으면 한다.

#### 🤔 스프링 프레임워크는 그 자체로 완벽하지 않다.
이게 무슨말인가 싶겠지만, 앞서 모듈을 언급했듯이

스프링 프레임워크는 스프링 애플리케이션의 서로 다른 부분들 간의 결합을 줄이고 (모듈화를 통해), 이를 테스트할 수 있게 만드는 것에 중점을 두면서 **사용자가 선택한 프레임워크와의 통합을 제공한다**

이는 아키텍처에 융통성이 있다는 것이며, 여러분은 **원하는 기능 구현을 위해 프레임워크를 자유롭게 선택할 수 있다.**

> 즉, 스프링 프레임워크는 `옷을 입힐` `마네킹`이고,  
> 여러분들이 선택하는 여러가지 도구(`모듈`)들이 `옷`이다.

### 4. 변화하는 시대를 선도

스프링은 트렌드를 ~~Java EE보다~~ 빠르게 반영한다.
> 책에서 예로든 것들은 어노테이션, 캐싱 API, 배치 애플리케이션 스펙, 마이크로서비스 아키텍처가 있는데,  
> 결론은 JavaEE보다 빠르게 지원했다 이므로, 굳이 정리 안했다.

## 📕 마무리
왜 스프링 프레임워크를 사용하는가?
> 기존 자바기반의 다른(EJB, JavaEE) 프레임워크들 보다  
> **테스트하기 쉽고**, **사용하기 간단하며**, **유연한 아키텍처를 가졌고**, **트렌드를 잘 반영**하기 때문이다.

다음에는 스프링의 주요 모듈들과 스프링 프로젝트에 대해 정리해보겠다.

## 🚀 참고
- [스프링 5.0 마스터 : 스프링 부트, 스프링 클라우드, 마이크로서비스, 리액티브, 코틀린까지](http://www.yes24.com/Product/Goods/62950195)
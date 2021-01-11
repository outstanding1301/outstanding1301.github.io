---
layout: post
title: "[Spring] 스프링 프레임워크의 주요 모듈들을 알아보자"
summary: "코어, 횡단 관심, 웹, 비즈니스, 데이터로 구성된 스프링 프레임워크의 주요 모듈들을 정리했습니다."
category: dev
tags: [spring]
comments: true
---
<!-- ![이미지](https://github.com/outstanding1301/outstanding1301.github.io/blob/master/imgs/spring/2021-01-09-mastering-spring5-2/이미지파일?raw=true) -->
# ☘️ 스프링 프레임워크의 주요 모듈들

## 📚 시리즈 - 스프링 5.0
1. [왜 스프링 프레임워크를 사용할까? (Spring vs EJB, JavaEE)](https://outstanding1301.github.io/spring/2021/01/08/mastering-spring5-1/)
2. [스프링 프레임워크의 주요 모듈들](https://outstanding1301.github.io/spring/2021/01/09/mastering-spring5-2/)

----

## ⚽︎ 목표
스프링 프레임워크의 주요 모듈들을 살펴보자

## 🤔 스프링 모듈?
[지난 번 포스트](https://outstanding1301.github.io/spring/2021/01/08/mastering-spring5-1/#3-%EC%95%84%ED%82%A4%ED%85%8D%EC%B2%98%EC%9D%98-%EC%9C%A0%EC%97%B0%EC%84%B1) 에서 공부했듯이 스프링 프레임워크의 모듈성은 스프링이 인기있는 이유 중 하나다.  
이번에는 스프링 프레임워크의 주요 모듈들에 대해 살펴보도록 하겠다.

----

![모듈](https://github.com/outstanding1301/outstanding1301.github.io/blob/master/imgs/spring/2021-01-09-mastering-spring5-2/modules.png?raw=true)


1. 스프링 코어 컨테이너 (Spring Core Container)
2. 횡단 관심 (Crosscutting Concerns)
3. 웹 (WEB)
4. 비즈니스 (Business)
5. 데이터 (Data)

하나씩 살펴보자.

## 1. 스프링 코어 컨테이너 (Spring Core Container)

스프링 코어 컨테이너는 
- `DI (Dependency Injection, 의존성 주입)`  
- `IoC (Inversion of Control, 제어 역전) 컨테이너`  
- `Application Context (애플리케이션 컨텍스트)`  

의 핵심 기능을 제공한다.  

### 💉 DI (Dependency Injection, 의존성 주입)
> 의존성을 외부에서(주로 IoC 컨테이너가) 지정해 주는 것  

### ⏳ IoC (Inversion of Control, 제어 역전)
> 프로그래머가 작성한 프로그램이 프레임워크의 제어를 받게 되는 소프트웨어 디자인 패턴  

### 🏭 IoC 컨테이너
> 객체의 생성, 의존성을 관리하는 컨테이너  

### 🐣 빈 (Bean)
> Spring IoC Container가 관리하는 자바 객체  
> 스프링이 제어권을 가지고 직접 생성하며 관계를 부여하는 오브젝트

### 🐔 빈 팩토리 (Bean Factory)
> 빈을 생성하고 관계를 설정하는등의 제어를 담당하는 IoC 오브젝트

### 🐓 애플리케이션 컨텍스트 (Application Context)
> 애플리케이션 전반에 걸쳐 모든 구성요소의 제어 작업을 담당하는 IoC 엔진, 일종의 빈 팩토리라고 볼 수 있다.  
> ApplicationContext 인터페이스는 BeanFactory 인터페이스를 상속한다.

|  | 모듈/아티팩트 | 사용 |
| :----: | :----: | :----: |
| Core | spring-core  | 다른 스프링 모듈이 사용하는 유틸리티 |
| Beans | spring-beans  | 스프링 빈 지원, 의존성 주입을 제공한다. 빈 팩토리(BeanFactory)의 구현을 포함한다. |
| Context | spring-context  | 빈 팩토리를 상속하는 애플리케이션 컨텍스트를 구현하고 리소스 로드 및 국제화 지원을 제공한다. |
| SpEL | spring-expression  | EL(Expression Language, 표현 언어)을 확장하고 빈 속성 및 접근, 처리를 위한 언어를 제공한다. |

----

## 2. 횡단 관심 (Crosscutting Concerns)

> ![횡단 관심](https://img1.daumcdn.net/thumb/R720x0.q80/?scode=mtistory2&fname=http%3A%2F%2Fcfile29.uf.tistory.com%2Fimage%2F99E908435BB6A833358353)  
> `AOP(Aspect Oriented Programming, 관점지향 프로그래밍)` 에서  
> `핵심적인 기능 (Core Concerns)` 외에 중간중간 삽입되어야 할 기능들을 `횡단 관심 (Crosscutting Concerns)` 이라고 한다.  
>   
> ![Crosscutting Concerns](https://miro.medium.com/max/620/1*M1A80NOT8WXWKZzxbBf67A.jpeg)  
> 예를 들어서, 로깅, 보안, 예외처리, 모니터링 등이 대표적인 횡단 관심이다.



횡단 관심은 로깅 및 보안과 같은 모든 애플리케이션 레이어에 적용할 수 있다.  
AOP는 일반적으로 횡단 관심을 구현하는 데 사용된다.  
단위 테스트와 통합 테스트는 모든 레이어에 적용될 수 있으므로 횡단 관심 카테고리에 적합하다.  

|  | 모듈/아티팩트 | 사용 |
| :----: | :----: | :----: |
| AOP | spring-aop  | `AOP(Aspect Oriented Programming, 관점지향 프로그래밍)`에 대한 기본적인 기능을 제공한다. |
| Aspect | spring-aspects  | 인기있는 AOP 프레임워크인 `AspectJ`와의 통합을 제공한다. |
| Instrument | spring-instrument  | 기본적인 instrumentation을 제공한다. <br> `(Byte Code Instrumentation: 런타임이나 로딩 때 클래스의 바이트코드를 변경하는 것)` |
| Test | spring-test  | 단위 및 통합 테스트에 대한 기본적인 기능을 제공한다. |

----

## 3. 웹 (WEB)

스프링은 다른 대중적인 웹 프레임워크들(ex. [Apache Struts](https://struts.apache.org/))과의 훌륭한 통합을 제공하는 것 외에도 자체 MVC 프레임워크인 `Spring MVC`를 제공한다.  

|  | 모듈/아티팩트 | 사용 |
| :----: | :----: | :----: |
| Web | spring-web  | 멀티파트 파일 업로드와 같은 `기본 웹 기능`을 제공한다. `다른 웹 프레임워크와의 통합`을 제공한다. |
| Servlet | spring-webmvc  | 자체 MVC 프레임워크를 제공한다. Spring MVC, REST 웹 서비스를 구현을 포함한다. |
| WebSocket | spring-websocket  | 웹 소켓을 지원한다. |
| Portlet | spring-webmvc-portlet  | 포틀릿 환경에서 사용할 MVC 구현을 제공한다. |

----

## 4. 비즈니스 (Business)

비즈니스 레이어는 애플리케이션의 `비즈니스 로직을 실행`하는 데 초점을 맞춘다.  
스프링에서는 비즈니스 로직을 `POJO (Plain Old Java Object)`로 구현한다.  

> 🤔 POJO..?
> 
> 순수한 자바 객체를 의미한다.  
> 다시 말해, 어떤 클래스를 확장(extends)하거나, 인터페이스를 구현(implements)하거나, 어노테이션(Annotation)을 포함할 필요가 없는 객체이다..

|  | 모듈/아티팩트 | 사용 |
| :----: | :----: | :----: |
| Transaction | spring-tx | 선언적 트랜잭션 관리를 제공한다. |

----

## 5. 데이터 (Data)

데이터 레이어는 일반적으로 데이터베이스 및 외부 인터페이스와 상호작용한다.  

|  | 모듈/아티팩트 | 사용 |
| :----: | :----: | :----: |
| JDBC (Java Database Connectivity) | spring-jdbc | JDBC 추상화를 제공한다. 이 모듈의 이점에 대해서는 [이전 포스트](https://outstanding1301.github.io/spring/2021/01/08/mastering-spring5-1/#2-%EB%B3%B5%EC%9E%A1%ED%95%9C-%EC%BD%94%EB%93%9C%EC%9D%98-%EA%B0%90%EC%86%8C)에서 잠깐 언급했다. |
| ORM (Object Relational Mapping) | spring-orm | JPA (Java Persistence API), JDO (Java Data Objects), Hibernate와 같은<br>ORM API를 위한 통합레이어를 제공한다. |
| OXM (Object XML Mapping) | spring-oxm | JAXB, Castor, XMLBeans, JiBX, XStream과 같은<br>Object/XML 매핑을 지원한다. |
| Messaging | spring-messaging | 메시지 기반 애플리케이션을 작성할 수 있는 기능을 제공한다. |
| JMS (Java Message Service) | spring-jms | 메시지 생산(Producing)과 소비(Consuming)를 위한 기능을 제공한다.<br>Spring Framework 4.1 부터는 spring-messaging과의 통합을 제공한다. |

----


## 📕 마무리

책에서 설명이 부실한 부분은 직접 찾아가면서 내용을 채웠다.  
스프링의 주요 모듈들이 어떤 기능들을 제공하는지 짚고 다음 단계로 넘어가면 될 것 같다.  

크게 `코어`, `횡단 관심`, `웹`, `비즈니스`, `데이터` 계층으로 나뉘고, 각각의 역할을 간단히 정리해보자  
- 코어 : `DI`, `IoC`에 대한 핵심 기능 제공 (`Bean`, `Bean Factory`, `Application Context`)
- 횡단 관심 : `AOP`에서 핵심기능 외에 중간중간 삽입되어야 할 기능들
- 웹 : 웹 서비스를 위한 기능들
- 비즈니스 : 비즈니스 로직을 실행, 선언적 트랜잭션 관리
- 데이터 : 데이터베이스 및 외부 인터페이스와의 상호작용


다음에는 스프링의 핵심 기능 중 하나인 `DI (Dependency Injection, 의존성 주입)` 에 대해 자세하게 알아보자.

----

## 🚀 참고
- [스프링 5.0 마스터 : 스프링 부트, 스프링 클라우드, 마이크로서비스, 리액티브, 코틀린까지](http://www.yes24.com/Product/Goods/62950195)
- [스프링 application context](https://derekpark.tistory.com/81)
- [Cross-cutting concerns for an Enterprise Application](https://medium.com/techmonks/cross-cutting-concerns-for-an-enterprise-application-ef9884e6bed3)
- [핵심기능과 부가기능](https://codedragon.tistory.com/m/7912?category=81876)
- [[Spring] Java Spring 기본](https://wordbe.tistory.com/entry/Spring-Java-Spring-%EA%B8%B0%EB%B3%B8)
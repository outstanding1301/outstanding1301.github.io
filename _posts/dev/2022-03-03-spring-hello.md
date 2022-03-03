---
layout: post
title: "[Spring] 스프링의 시작, 옳게된 객체지향이란 무엇인가에 대해 알아보자 (SOLID)"
summary: "객체지향의 특징과 좋은 객체지향 설계를 위한 SOLID원칙, 빈, 컨테이너, 그리고 스프링이 나오기까지"
thumbnail: "https://media.giphy.com/media/zfUrjBQDP2EntP8pVz/giphy.gif"
category: dev
tags: [spring]
comments: true
date: 2022-03-03 23:08:00
lastmod: 2022-03-03 23:08:00
series: spring
sitemap: 
  changefreq: daily
  priority: 1.0
---
# 스프링, 너 누구야!

![spring](https://media.giphy.com/media/zfUrjBQDP2EntP8pVz/giphy.gif)

> 스프링의 시작, 옳게된 객체지향이란 무엇인가에 대해 알아보자

## 객체 지향적(Object Oriented)인 것

 `객체 지향적`인 것은 무엇일까요?

`객체 지향 프로그래밍`은 프로그램을 명령어의 목록으로 보는 시각에서 벗어나, 프로그램은 여러 개의 독립적인 `객체`들의 모임이며, 이들간의 `협력`과 `상호작용`을 통해 메시지를 주고받고, 데이터를 처리하는 것으로 보는 관점입니다.

객체 지향에는 크게 4가지의 특징이 있습니다.

1. 추상화 - 불필요한 부분은 생략하고 객체의 속성 중 가장 중요한 것에만 중점을 두어 간소화하는 것 -> 객체의 공통적인 속성과 기능을 중심으로 추상화
	> ex) 송인걸, 유도곤, 김현수는 공통적으로 이름, 나이, 성별이라는 속성을 가지며, 걷기, 먹기, 일하기 등의 행위(기능)을 가진 `사람`으로 추상화 가능
2. 캡슐화 - 객체의 공통적인 속성(필드)과 행위(메소드)를 가지는 하나의 클래스로 묶는 것
	> ex) 송인걸, 유도곤, 김현수의 이름, 나이, 성별 속성과 걷기, 먹기, 일하기 기능을 하나의 `사람` 이라는 클래스에서 동작하도록 캡슐화
3. 상속 - 이미 정의된 상위 클래스(부모 클래스)의 모든 속성과 연산을 하위 클래스가 물려받는 것
	> ex) `사람`은 `동물`의 나이, 성별 속성과 걷기, 먹기 행위를 물려받을 수 있음, 만약 `고양이`라는 새로운 클래스를 생성한다면, `고양이` 역시 `동물`의 속성과 행위를 물려받을 수 있음
4. 다형성 - 서로 다른 클래스의 객체가 같은 메시지를 받았을 때 각자의 방식으로 동작하는 능력
	> ex) `사람`과 `고양이`의 `인사` 라는 행위는 각각 "안녕하세요", 또는 "야옹"과 같이 다르게 동작

이러한 객체 지향적인 프로그램은 유연하고, 변경하기 쉬워 대규모 소프트웨어 개발에 사용하기 좋습니다.

### 객체지향을 실생활에 비유해보자

![notebook](https://media.giphy.com/media/l2JhBhnPWzrp11LBC/giphy.gif)


`배우`와 `역할`에 대해서 생각해봅시다.

예를 들어, 영화 `노트북`의 주인공 `노아 캘훈`, `앨리슨 해밀튼`은 `역할`입니다.  
`노아 캘훈`은 `라이언 고슬링`이, `앨리슨 해밀튼`은 `레이첼 맥아담스`가 배역을 맡았습니다.  

만약 `라이언 고슬링`이 개인적인 사정으로 영화 촬영을 할 수 없게 된다면 `노아 캘훈`이라는 역할을 수정해야 할까요?  

아니죠, 역할은 그대로, 배우만 교체하면 됩니다. 

이 때 `역할`을 `인터페이스`, `배우`를 그 인터페이스를 구현하는 `클래스`라고 생각해보십시오.  

왜 객체지향이 유연하고 변경하기 쉬운지 이해하실 수 있을 것입니다.


## 좋은 객체지향 설계의 5가지 원칙 (SOLID)

그럼 객체지향이라고 다 좋은 객체지향이냐, 그건 또 아닙니다.

"좋은" 객체지향에 대해 클린코드의 저자 로버트 마틴이 정리한 원칙이 있습니다.
- `SRP (Single Responsibility Principle)`: 단일 책임 원칙
	- 하나의 클래스는 하나의 책임만 가져야 한다.
- `OCP (Open/Closed Principle)`: 개방-폐쇄 원칙
	- 소프트웨어 요소는 확장에는 열려있으나 변경에는 닫혀 있어야 한다.
		- 소스코드를 변경하지 않고, 구현 객체를 변경할 수 있어야한다.
		- 이를 위해 객체를 생성하고, 연관관계를 맺어주는 `별도의 무언가`가 필요하다..
- `LSP (Liskov Substitution Principle)`: 리스코프 치환 원칙
	- 객체는 프로그램의 정확성을 깨뜨리지 않으면서 하위 타입의 인스턴스로 바꿀 수 있어야 한다. (하위 타입의 클래스는 인터페이스의 규약을 모두 지켜야한다.)
- `ISP (Interface Segregation Principle)`: 인터페이스 분리 원칙
	- 범용 인터페이스 하나보다 특화된 여러개의 인터페이스로 분리하는 것이 낫다.
		> ex) 자동차 인터페이스 -> 액셀 인터페이스, 핸들 인터페이스, 브레이크 인터페이스, 변속 인터페이스...
		- 이렇게 분리하면 변속 기어를 수동, 자동으로 변경해도 액셀과 핸들, 브레이크에는 영향을 주지 않을 수 있음 
- `DIP (Dependency Inversion Principle)`: 의존관계 역전 원칙
	- 구현체가 아닌 추상화에 의존해야 한다.
	- 구현 클래스에 의존하지 말고 인터페이스에 의존하라는 말이다.
	- 그러나 어쨌든 우린 구현 클래스를 통해 인스턴스를 생성해야한다...   
	  어떻게 해야 구현 클래스가 아닌 인터페이스에 의존할 수 있을까? `별도의 무언가`가 필요하다...

일반적으로 객체지향의 다형성만으로는 OCP, DIP를 지킬 수 없습니다. `별도의 무언가`의 도움이 필요합니다.


## 빈(Bean)과 컨테이너(Container)

![bean](https://media.giphy.com/media/Rf4c7JZUHdse7AzQbM/giphy.gif)


일반적으로, 우리는 클래스의 인스턴스가 필요할 때 생성자를 호출하여 인스턴스를 생성합니다. 더 나아가, 오로지 하나의 인스턴스만 존재하여 재사용할 수 있도록 싱글톤패턴으로 구현하기도 합니다.

그러나 만약에 우리가 직접 인스턴스를 생성하지 않고, 해당 인스턴스를 생성하기 위해 필요한 모든 의존성들을 자동으로 생성해주고, 라이프사이클까지 관리해주는 무언가가 있다면 얼마나 좋을까요? 

이렇게 하면 그저 인터페이스를 통해 필요한 객체를 접근해서 쓸 수 있고 OCP, DIP 원칙을 지킬 수 있을텐데요...

이 때 우리가 필요한 객체를 생성하고 관리해주는 것의 개념을 `컨테이너(Container)`, 컨테이너에 의해 관리되는 객체를 `빈(Bean)` 이라고 합니다.

이러한 개념이 구현되어 아주 오랫동안 엔터프라이즈급 웹애플리케이션 시장을 점유했던 `EJB (Enterprise Java Beans)` 라는 프레임워크가 있습니다.

EJB는 `EJB 컨테이너`라는 것으로 빈을 관리했는데, 이를 사용하기 위해 필요한 상속 및 구현이 많아 비즈니스 로직에 집중하기 어려웠다고 합니다.

또한 `객체지향적이지 않고`, `특정 환경이나 기술에 종속적이며`, `객체는 컨테이너 안에서만 동작 가능`하여 `테스트하기 어려운 (불가능에 가까운)` 등 매우 생산성이 떨어지는 단점이 있었습니다.

## 스프링

> 추운 겨울이 지나고 봄이 찾아왔읍니다.

객체지향적이고, 특정 환경이나 기술에 종속적이지 않으며, 객체가 컨테이너 밖에서도 동작 가능하고, 테스트 하기 쉬운 프레임워크가 있다면 얼마나 좋을까요...


`스프링` : ![thatsme](https://media.giphy.com/media/LMWG4e8WfVWspCxJR7/giphy.gif)


스프링은 `의존성 주입: DI (Dependency Injection)`라는 기술로 OCP, DIP를 가능하게 했습니다.

또한 `순수 자바 객체: POJO (Plain Old Java Object)`를 빈으로 관리하는 `DI 컨테이너`와 함께 봄이 찾아왔읍니다...

다음 이 시간에는 스프링의 DI 개념, 컨테이너, 빈을 알아보며 `벚꽃놀이`를 즐기도록 하겠습니다.



그럼 이만,,,


![sakura](https://media.giphy.com/media/FWtVYDHIxgGgE/giphy.gif)

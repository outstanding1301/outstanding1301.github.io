---
layout: post
title: "[Java] 1. 자바의 입출력과 변수"
summary: "자바의 입출력과 변수에 대해 알아보자"
thumbnail: "https://media.giphy.com/media/citBl9yPwnUOs/giphy.gif"
category: dev
tags: [java, java-lecture]
comments: true
date: 2022-06-15 19:18:00
lastmod: 2022-06-15 19:18:00
series: java-lecture
sitemap: 
  changefreq: daily
  priority: 1.0
---
# 자바의 입출력과 변수

## 입출력 (I/O)
### 표준 스트림
- `input` (stdin) - 0
- `output` (stdout) - 1
- `error` (stderr) - 2

### 입력 (Input)
- `System.in` 스트림 사용
- `Scanner를` 사용해서 스트림으로 입력된 값을 받음
```java
Scanner scanner = new Scanner(System.in);
String oneWord = scanner.next();
String oneLine = scanner.nextLine();
int oneInteger = scanner.nextInt();
```

### 출력 (Output)
- `System.out` 스트림 사용 (에러 출력을 위해서는 `System.err`)
```java
System.out.print("Hello "); // 출력 후 개행하지않음
System.out.println("World"); // 출력 후 개행
System.out.printf("%d %s\n", 1, "안녕"); // 문자열 포맷팅 (String formatting)
```


## 변수 (Variable)
### 원시 타입 (Primitive Type) - 8개
> 실제 데이터 값을 저장  
> 소문자로 시작 (int, char, short …)  

- 문자형 (문자 하나 표현 a, b, c, d, …) 
	> **한글을 표현할 수 있음**  
	> C의 경우 `char`는 1바이트의 크기를 가지지만  
	> Java는 Unicode를 사용하여 **2바이트**의 크기를 가짐  
	- `char` : 2 Bytes -> ASCII
- 정수형 (-붙은 자연수, 0, 자연수)
	- `byte`: 1 Bytes (8bits)
	- `short` : 2 Bytes
	- `int` : 4 Bytes
	- `long` : 8 Bytes
- 실수형 (소수점이 포함된 수, -붙은, 0)
	- `float` : 4 Bytes
	- `double` : 8 Bytes
- 논리형 - true, false 값을 가짐
	- `boolean` : 1 Bytes

### 레퍼런스 타입 (Reference Type)
> 객체의 주소를 참조  
> 
> 원시타입을 제외한 모든 타입  
> 대문자로 시작 (String, Object, Integer …)  
> 모두 `Object를` 상속받음, `null` 값을 가질 수 있음  
- 문자열 : `String`
- 원시타입의 `Wrapper` 클래스들
	- char : `Character` (16 Bytes)
	- byte : `Byte` (16 Bytes)
	- short : `Short` (16 Bytes)
	- int : `Integer` (16 Bytes)
	- long : `Long` (24.5 Bytes)
	- float : `Float` (16 Bytes)
	- double : `Double` (24.5 Bytes)
	- boolean : `Boolean` (16 Bytes)

### 원시타입 VS 레퍼런스 타입
- 원시타입이 레퍼런스보다 속도가 빠름
- 원시타입이 레퍼런스보다 메모리를 적게먹음
- 레퍼런스는 다양한 원시 타입들로 구성됨

## 예제
> 정수 두개를 입력받아 더하여 출력하는 프로그램  
```java
Scanner scanner = new Scanner(System.in);
int a, b;
a = scanner.nextInt();
b = scanner.nextInt();
System.out.printf("%d + %d = %d\n", a, b, a + b);
```

## 참고
- [JAVA String.format() - 문자열 형식 지정](https://velog.io/@yu-jin-song/JAVA-%EB%AC%B8%EC%9E%90%EC%97%B4-%ED%98%95%EC%8B%9D-%EC%A7%80%EC%A0%95)
- [원시타입, 참조타입(Primitive Type, Reference Type)](https://velog.io/@gillog/%EC%9B%90%EC%8B%9C%ED%83%80%EC%9E%85-%EC%B0%B8%EC%A1%B0%ED%83%80%EC%9E%85Primitive-Type-Reference-Type)

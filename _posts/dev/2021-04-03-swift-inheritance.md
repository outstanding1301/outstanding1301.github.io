---
layout: post
title: "[Swift] 상속 (Inheritance)"
summary: "스위프트의 상속"
thumbnail: "https://developer.apple.com/assets/elements/icons/swift/swift-256x256.png"
category: dev
tags: [swift]
comments: true
date: 2021-04-03 20:23:49
lastmod: 2021-04-03 20:23:49
sitemap: 
  changefreq: daily
  priority: 1.0
---
# 상속

`기반클래스`: 아무것도 상속받지 않은 클래스

### 서브클래싱

```swift
class SomeSuperclass {
	var a = 0
}

class SomeSubclass: SomeSuperclass {
	var b = 1
}

let someSubclass = SomeSubclass()
someSubclass.a // SomeSuperclass의 프로퍼티
someSubclass.b // SomeSubclass의 프로퍼티
```

### 오버라이딩

#### 메소드 오버라이드

메소드 선언 앞에 `override` 키워드를 붙임
```swift
class Vehicle {
	func makeNoise() {
		print("빵빵")
	}
}

class Bicycle: Vehicle  {
	override func makeNoise() {
		print("따르릉")
	}
}

let bicycle = Bicycle()
bicycle.makeNoise() // 따르릉
```

#### 프로퍼티 오버라이드

```swift
class Vehicle {
	var speed = 0.0
	var description: String {
		return "속도: \(speed) km/h"
	}
}

class Bicycle: Vehicle  {
	var gear = 1
	override var description: String {
		return "\(super.description), 기어: \(gear)"
	}
}

let bicycle = Bicycle()
bicycle.speed = 30.0
bicycle.gear = 3
bicycle.description // 속도: 30.0 km/h, 기어: 3
```
### 오버라이드 방지

`final` 키워드로 선언

```swift
class Vehicle {
	final func makeNoise() {
		print("빵빵")
	}
}

class Bicycle: Vehicle  {
	override func makeNoise() { // 컴파일 시 에러 발생
		print("따르릉")
	}
}
```
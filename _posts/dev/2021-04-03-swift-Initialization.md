---
layout: post
title: "[Swift] 초기화 (Initialization)"
summary: "스위프트의 초기화, 프로퍼티의 초기 값 설정 단계, 이니셜라이저를 정의"
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
# 초기화

프로퍼티의 초기 값 설정 단계, 이니셜라이저를 정의

> 스위프트의 `이니셜라이저`는 다른 언어의 `생성자`와 비슷한 역할

### 이니셜라이저

`init` 키워드 사용

```swift
class SomeClass {
	var someProperty: Int
	var propertyWithDefaultValue = 1 // 선언과 동시에 초기화
	
	// 파라미터가 없는 이니셜라이저
	init() {
		someProperty = 1
	} // let someClass = SomeClass()
	
	// 파라미터가 있는 이니셜라이저
	init(someProperty: Int) {
		self.someProperty = someProperty
	} // let someClass = SomeClass(someProperty: 10)
	
	// 같은 타입의 파라미터로 오버로딩 (이름으로 구분)
	init(propertyWithDefaultValue: Int) {
		self.propertyWithDefaultValue = propertyWithDefaultValue
	} // let someClass = SomeClass(propertyWithDefaultValue: 10)
	
	// 인자 레이블이 없는 이니셜라이저 파라미터
	init(_ value: Int) {
		self.someProperty = value
	} // let someClass = SomeClass(10)
}
```

### 편리한 초기자

`convenience` 키워드 사용, 일반적인 `init` 초기자 (지정 초기자) 보다 먼저 호출됨

```swift
class Food {
	var name: String
	init(name: String) {
		self.name = name
	}
	convenience init() {
		self.init(name: "default")
	}
}
```

슈퍼클래스에서의 편리한 초기자 오버라이딩

```swift
class Meat: Food {
	var quantity: Int
	init(name: String, quantity: Int) {
		self.quantity = quantity
		super.name = name
	}
	override convenience init(name: String) {
		self.init(name: name, quantity: 1)
	}
}
```

이렇게 하면 3가지의 형태로 인스턴스 생성 가능
```swift
1. let meat = Meat() // name: default, quantity: 1
2. let meat = Meat(name: "소고기") // name: 소고기, quantity: 1
3. let meat = Meat(name: "소고기", quantity: 3) // name: 소고기, quantity: 3
```

### 실패 가능한 초기자

`init?` 키워드 사용, `nil`을 반환하여 인스턴스의 값이 `nil`이 됨

```swift
struct Animal {
	let species: String
	init?(species: String) {
		if species.isEmpty { return nil }
		self.species = species
	}
}
```

### 필수 초기자

모든 서브클래스에서 반드시 구현해야 하는 초기자, `required` 키워드를 붙여줌

```swift
class SomeClass {
	required init() {
		...
	}
}

class SomeSubclass: SomeClass {
	required init() {
		...
	}
}
```

### 클로저를 이용한 기본 프로퍼티 값 설정
```swift
struct Gugudan {
	let values: [Int] = {
		var tempValues = [Int]()
		for i in 1..9 {
			for j in 1..9 {
				tempValues.append(i * j)
			}
		}
		return tempValues
	}()
	
	subscript(i: Int, j: Int) {
		return values[(i-1)*9 + (j-1)]
	}
}
```

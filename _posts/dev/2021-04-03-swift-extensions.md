---
layout: post
title: "[Swift] 익스텐션 (Extensions)"
summary: "열거형, 클래스, 구조체를 그 타입 안에서 다시 정의할 수 있음"
thumbnail: "https://developer.apple.com/assets/elements/icons/swift/swift-256x256.png"
category: dev
tags: [swift]
comments: true
date: 2021-04-03 20:30:49
lastmod: 2021-04-03 20:30:49
series: swift
sitemap: 
  changefreq: daily
  priority: 1.0
---
# 익스텐션

클래스, 구조체, 열거형 혹은 프로토콜 타입에 **기능을 추가**할 수 있다.

- 계산된 인스턴스 프로퍼티와 계산된 타입 프로퍼티의 추가
- 인스턴스 메소드와 타입 메소드의 추가
- 새로운 이니셜라이저 제공
- 서브스크립트 정의
- 중첩 타입의 선언과 사용
- 특정 프로토콜을 따르는 타입 만들기

> 익스텐션은 타입에 새 기능을 추가할 수 있지만, **오버라이드는 할 수 없다.**


### 익스텐션 문법

`extension` 키워드를 사용해 선언한다.

```swift
extension SomeType {
    ...
}
```

하나 이상의 프로토콜을 따르도록 확장할 수 있다.
```swift
extension SomeType: SomeProtocol, AnotherProtocol {
    ...
}
```

### 계산된 프로퍼티

익스텐션을 이용해 존재하는 타입에 `인스턴스 프로퍼티와 타입 프로퍼티`를 추가할 수 있다.

```swift
extension Double {
    var km: Double { return self 1_000.0 }
    var m: Double { return self }
    var cm: Double { return self / 100.0 }
    var mm: Double { return self / 1_000.0 }
    var ft: Double { return self / 3.28084 }
}

let oneInch = 25.4.mm
print("1인치는 \(oneInch) 미터 입니다.")

let threeFeet = 3.ft
print("3피트는 \(threeFeet) 미터 입니다.")
```

### 이니셜라이저

익스텐션을 이용해 존재하는 타입에 새로운 `이니셜라이저`를 추가할 수 있다.

```swift
struct Size {
    var width = 0.0, height = 0.0
}

struct Point {
    var x = 0.0, y = 0.0
}

struct Rect {
    var origin = Point()
    var size = Size()
}
```

```swift
extension Rect {
    init(center: Point, size: Size) {
        let originX = center.x - (size.width / 2)
        let originY = center.y - (size.height / 2)
        self.init(origin: Point(x: originX, y: originY), size: size)
    }
}

let centerRect = Rect(center: Point(x: 4.0, y: 4.0),
                      size: Size(width: 3.0, height: 3.0))
```

### 메소드

익스텐션을 이용해 존재하는 타입에 인스턴스 메소드나 타입 메소드를 추가할 수 있다.

```swift
extension Int {
    func repetitions(task: () -> Void) {
        for _ in 0..<self {
            task()
        }
    }
}

3.repetitions {
    print("Hello!")
}

// Hello!
// Hello!
// Hello!
```

### 변경 가능한 인스턴스 메소드

익스텐션에서 추가된 인스턴스 메소드는 인스턴스 자신(self)을 변경할 수 있다.

```swift
extension Int {
    mutating func square() {
        self = self * self
    }
}
var someInt = 3
someInt.square()

// someInt의 값은 9가 됨
```

### 서브스크립트

익스텐션을 이용해 존재하는 타입에 새로운 서브스크립트를 추가할 수 있다.

```swift
extension Int {
    subscript(digitIndex: Int) -> Int {
        var decimalBase = 1
        for _ in 0..<digitIndex {
            decimalBase *= 10
        }
        return (self / decimalBase) % 10
    }
}
746381295[0] // 5
746381295[1] // 9
746381295[2] // 2
746381295[8] // 7
```

### 중첩 타입

익스텐션을 이용해 존재하는 클래스, 구조체, 열거형에 중첩 타입을 추가할 수 있다.

```swift
extension Int {
    enum Kind: Character {
        case negative = "-", zero = "0", positive = "+"
    }
    var kind: Kind {
        switch self {
        case 0:
            return .zero
        case let x where x > 0:
            return .positive
        default:
            return .negative
        }
    }
}

1.kind.rawValue // +
0.kind.rawValue // 0
-1.kind.rawValue // -


```
---
layout: post
title: "[Swift] 프로토콜 (Protocols)"
summary: "특정 기능 수행에 필수적인 요소를 정의한 청사진"
thumbnail: "https://developer.apple.com/assets/elements/icons/swift/swift-256x256.png"
category: dev
tags: [swift]
comments: true
date: 2021-04-03 20:31:49
lastmod: 2021-04-03 20:31:49
series: swift
sitemap: 
  changefreq: daily
  priority: 1.0
---
# 프로토콜

특정 기능 수행에 필수적인 요소를 정의한 청사진.  
프로토콜을 만족시키는 타입을 `프로토콜을 따른다(conform)`고 말한다.  
프로토콜에 필수 구현을 추가하거나 추가적인 기능을 더하기 위해 프로토콜을 `확장(extend)`할 수 있다.  

> 자바의 interface와 유사하다.

### 프로토콜 문법

`protocol` 키워드를 사용하여 정의

```swift
protocol SomeProtocol {
    ...
}
```

프로토콜을 따르는 타입을 정의하기 위해서 상속처럼 표현한다.

```swift
class SomeClass: SomeProtocol, AnotherProtocol {
    ...
}
```

서브클래싱인 경우 슈퍼클래스를 프로토콜 앞에 적어준다.

```swift
class SomeClass: SomeSuperclass, FirstProtocol, AnotherProtocol {
    // class definition goes here
}
```

### 프로퍼티 요구사항

프로토콜에서는 프로퍼티가 저장된 프로퍼티인지 계산된 프로퍼티인지 명시하지 않는다.  
하지만 프로퍼티의 `이름`과 `타입` 그리고 `gettable, settable` 한지는 명시한다.  
필수 프로퍼티는 항상 `var`로 선언해야한다.

```swift
protocol SomeProtocol {
    var mustBeSettable: Int { get set }
    var doesNotNeedToBeSettable: Int { get }
}
```

타입 프로퍼티는 `static` 키워드를 적어 선언한다.

```swift
protocol AnotherProtocol {
    static var someTypeProperty: Int { get set }
}
```

### 메소드 요구사항

타입 메소드

```swift
protocol SomeProtocol {
    static func someTypeMethod()
}
```

인스턴스 메소드

```swift
protocol RandomNumberGenerator {
    func random() -> Double
}
```

### 변경 가능한 메소드 요구사항

```swift
protocol Togglable {
    mutating func toggle()
}
```

```swift
enum ToggleSwitch: Togglable {
    case off, on
    mutating func toggle() {
        switch self {
        case .off:
            self = .on
        case .on:
            self = .off
        }
    }
}
var lightSwitch = ToggleSwitch.off
lightSwitch.toggle()
```

### 초기자 요구사항

```swift
protocol SomeProtocol {
    init(someParameter: Int)
}
```

프로토콜에서 특정 이니셜라이저가 필요했다고 명시했기 때문에 구현에서 `required` 키워드를 붙여줘야 한다.

```swift
class SomeClass: SomeProtocol {
    required init(someParameter: Int) {
        ...
    }
}
```

### 타입으로써의 프로토콜

타입 사용이 허용되는 모든 곳에 프로토콜을 사용할 수 있다. (자바의 interface 처럼)

- 함수, 메소드, 이니셜라이저의 파라미터 타입 혹은 리턴 타입
- 상수, 변수, 프로퍼티의 타입
- 컨테이너인 배열, 사전 등의 아이템 타입

```swift
protocol RandomNumberGenerator {
    func random() -> Double
}

class LinearCongruentialGenerator: RandomNumberGenerator {
    var lastRandom = 42.0
    let m = 139968.0
    let a = 3877.0
    let c = 29573.0
    func random() -> Double {
        lastRandom = ((lastRandom a + c).truncatingRemainder(dividingBy:m))
        return lastRandom / m
    }
}

class Dice {
    let sides: Int
    let generator: RandomNumberGenerator
    init(sides: Int, generator: RandomNumberGenerator) {
        self.sides = sides
        self.generator = generator
    }
    func roll() -> Int {
        return Int(generator.random() Double(sides)) + 1
    }
}

var d6 = Dice(sides: 6, generator: LinearCongruentialGenerator())
for _ in 1...5 {
    print("주사위의 눈: \(d6.roll())")
}
```

### 위임

클래스 혹은 구조체 인스턴스에 특정 행위에 대한 책임을 넘길 수 있게 해주는 디자인 패턴

```swift
protocol DiceGame {
    var dice: Dice { get }
    func play()
}
protocol DiceGameDelegate: AnyObject {
    func gameDidStart(_ game: DiceGame)
    func game(_ game: DiceGame, diceRoll: Int)
    func gameDidEnd(_ game: DiceGame)
}
```

```swift
class OddEven: DiceGame {
    let dice = Dice(sides: 6, generator: LinearCongruentialGenerator())
    weak var delegate: DiceGameDelegate?
    func play() {
        delegate?.gameDidStart(self)
        delegate?.game(self, diceRoll: dice.roll())
        delegate?.gameDidEnd(self)
    }
}
```

### 익스텐션을 이용해 프로토콜 따르게 하기

이미 존재하는 타입에 새 프로토콜을 따르게 하기 위해 익스텐션을 사용할 수 있다.

```swift
protocol TextRepresentable {
    var textualDescription: String { get }
}

extension Dice: TextRepresentable {
    var textualDescription: String {
        return "\(sides)면체 주사위"
    }
}

let d12 = Dice(sides: 12, generator: LinearCongruentialGenerator())
print(d12.textualDescription) // 12면체 주사위
```

#### 조건적으로 프로토콜 따르기

`where` 절을 사용하여 Array의 원소들이 특정 프로토콜을 따르는 경우에만 프로토콜을 따르도록 할 수 있다.

```swift
extension Array: TextRepresentable where Element: TextRepresentable {
    var textualDescription: String {
        let itemsAsText = self.map { $0.textualDescription }
        return "[" + itemsAsText.joined(separator: ", ") + "]"
    }
}

let d6 = Dice(sides: 12, generator: LinearCongruentialGenerator())
let d12 = Dice(sides: 12, generator: LinearCongruentialGenerator())

let dices = [d6, d12]
print(dices.textualDescription) // [6면체 주사위, 12면체 주사위]
```

#### 익스텐션을 이용해 프로토콜을 따른다고 선언하기

이미 프로토콜의 모든 조건을 만족하지만 프로토콜을 따른다는 선언을 하지 않은 경우  
빈 익스텐션으로 선언할 수 있다.

```swift
struct Hamster {
    var name: String
    var textualDescription: String {
        return "A hamster named \(name)"
    }
}
extension Hamster: TextRepresentable {}
// textualDescription이 구현되어 있으므로 TextRepresentable 프로토콜을 따를 수 있다.
```

### 프로토콜 상속

프로토콜도 프로토콜을 상속할 수 있다.

```swift
protocol InheritingProtocol: SomeProtocol, AnotherProtocol {
    ...
}
```

### 클래스 전용 프로토콜

클래스 전용 프로토콜인 경우 프로토콜에 `AnyObject`를 추가한다.

```swift
protocol SomeClassOnlyProtocol: AnyObject, SomeInheritedProtocol {
    ...
}
```

### 선택적 프로토콜 요구조건

`@objc` 키워드를 사용하여 필수 구현이 아닌 선택적 구현 조건을 정의할 수 있다.  
프로토콜 앞에 `@objc` 키워드를 붙이고, 함수나 프로퍼티에 `@objc`와 `optional` 키워드를 붙인다.  
`@objc` 프로토콜은 `클래스 타입`에서만 사용할 수 있다.

```swift
@objc protocol CounterDataSource {
    @objc optional func increment(forCount count: Int) -> Int
    @objc optional var fixedIncrement: Int { get }
}

class Counter {
    var count = 0
    var dataSource: CounterDataSource?
    func increment() {
        // dataSource의 increment 메소드가 구현되어있지 않을 수 있기 때문에 옵셔널 체이닝을 이용한다.
        if let amount = dataSource?.increment?(forCount: count) {
            count += amount
        // dataSource의 fixedIncrement 프로퍼티가 구현되어있지 않을 수 있기 때문에 옵셔널 체이닝을 이용한다.
        } else if let amount = dataSource?.fixedIncrement {
            count += amount
        }
    }
}
```

### 프로토콜 익스텐션

익스텐션을 이용해 프로토콜을 확장할 수 있다.

```swift
extension RandomNumberGenerator {
    func randomBool() -> Bool {
        // 이미 정의된 random 메소드를 사용하여 randomBool() 메소드를 추가
        return random() > 0.5
    }
}
```
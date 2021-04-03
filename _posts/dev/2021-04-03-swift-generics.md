---
layout: post
title: "[Swift] 지네릭 (Generics)"
summary: "지네릭은 더 유연하고 재사용 가능한 함수와 타입의 코드를 작성하는 것을 가능하게 해준다"
thumbnail: "https://developer.apple.com/assets/elements/icons/swift/swift-256x256.png"
category: dev
tags: [swift]
comments: true
date: 2021-04-03 20:32:49
lastmod: 2021-04-03 20:32:49
series: swift
sitemap: 
  changefreq: daily
  priority: 1.0
---
# 지네릭

지네릭은 더 `유연`하고 `재사용 가능`한 함수와 타입의 코드를 작성하는 것을 가능하게 해준다.

### 지네릭 함수

```swift
func swapTwoValues<T>(_ a: inout T, _ b: inout T) {
    let tmp = a
    a = b
    b = tmp
}

var someIntA = 1
var someIntB = 2
swapToValues(&someIntA, &someIntB) // someIntA = 2, someIntB = 1

var someStringA = "Hello"
var someStringB = "World"
swapToValues(&someStringA, &someStringB) // someStringA = World, someStringB = Hello
```

### 지네릭 타입

지네릭을 이용하여 스택 자료구조를 구현하면 다음과 같다.

```swift
struct Stack<Element> {
    var items = [Element]()
    mutating func push(_ item: Element) {
        items.append(item)
    }
    mutating func pop() -> Element {
        return items.removeLast()
    }
}

var stackOfStrings = Stack<String>()
stackOfStrings.push("a")
stackOfStrings.push("b")
stackOfStrings.push("c")
stackOfStrings.push("d")
```

### 지네릭 타입의 확장

익스텐션을 이용해 지네릭 타입을 확장할 수 있다.

```swift
extension Stack {
    var topItem: Element? {
        return items.isEmpty ? nil : items[items.count - 1]
    }
}

if let topItem = stackOfStrings.topItem {
    print("스택의 최상단 아이템: \(topItem).")
}
```

### 타입 제한

지네릭 타입이 특정 타입을 따르도록 제한할 수 있다.

아래 예제에서는, T가 `Equatable` 프로토콜을 따르는 경우에만 사용할 수 있다. 

> `Equatable` 프로토콜:  
> == 연산자를 정의하는 프로토콜

```swift
func findIndex<T: Equatable>(of valueToFind: T, in array:[T]) -> Int? {
    for (index, value) in array.enumerated() {
        if value == valueToFind {
            return index
        }
    }
    return nil
}

let doubleIndex = findIndex(of: 9.3, in: [3.14159, 0.1, 0.25]) // 옵셔널, nil
let stringIndex = findIndex(of: "Andrea", in: ["Mike", "Malcolm", "Andrea"]) // 옵셔널, 2
```

### 연관 타입

특정 타입을 동적으로 지정해 사용할 수 있다.  
`associatedtype` 키워드를 사용한다.

```swift
protocol Container {
    associatedtype Item
    mutating func append(_ item: Item)
    var count: Int { get }
    subscript(i: Int) -> Item { get }
}
```

```swift
struct IntStack: Container {
    var items = [Int]()
    mutating func push(_ item: Int) {
        items.append(item)
    }
    mutating func pop() -> Int {
        return items.removeLast()
    }
    // typealias를 사용해 Item의 별칭을 지정한다.
    typealias Item = Int
    mutating func append(_ item: Int) {
        self.push(item)
    }
    var count: Int {
        return items.count
    }
    subscript(i: Int) -> Int {
        return items[i]
    }
}
```

```swift
struct Stack<Element>: Container {
    var items = [Element]()
    mutating func push(_ item: Element) {
        items.append(item)
    }
    mutating func pop() -> Element {
        return items.removeLast()
    }

    mutating func append(_ item: Element) {
        self.push(item)
    }
    var count: Int {
        return items.count
    }
    subscript(i: Int) -> Element {
        return items[i]
    }
}
```

#### 연관 타입에 제약 조건 추가

```swift
protocol Container {
    associatedtype Item: Equatable // 제약 조건
    mutating func append(_ item: Item)
    var count: Int { get }
    subscript(i: Int) -> Item { get }
}
```

익스텐션을 사용하여 제약조건을 추가할 수 있다.  
아래의 예제는 Suffix가 SuffixableContainer프로토콜을 따르고 Item타입이 반드시 Container의 Item타입이어야 한다는 제약조건이다.

```swift
protocol SuffixableContainer: Container {
    associatedtype Suffix: SuffixableContainer where Suffix.Item == Item
    func suffix(_ size: Int) -> Suffix
}
```

```swift
extension Stack: SuffixableContainer {
    func suffix(_ size: Int) -> Stack { 
        var result = Stack()
        for index in (count-size)..<count {
            result.append(self[index])
        }
        return result
    }
    // Inferred that Suffix is Stack.
}
var stackOfInts = Stack<Int>() 
stackOfInts.append(10)
stackOfInts.append(20)
stackOfInts.append(30)
let suffix = stackOfInts.suffix(2) // 20, 30
```

또는 다음과 같이 사용할 수 있다.

```swift
extension IntStack: SuffixableContainer {
    func suffix(_ size: Int) -> Stack<Int> { 
        var result = Stack<Int>()
        for index in (count-size)..<count {
            result.append(self[index])
        }
        return result
    }
}
```

### 지네릭의 Where 절

`where` 절을 사용하여 지네릭의 제약조건을 자세하게 설정할 수 있다.

```swift
func allItemsMatch<C1: Container, C2: Container>
    (_ someContainer: C1, _ anotherContainer: C2) -> Bool 
    where C1.Item == C2.Item, C1.Item: Equatable { // C1의 Item과 C2의 Item 타입은 같아야 하고, C1의 Item은 Equatable 프로토콜을 따라야한다.
        if someContainer.count != anotherContainer.count {
            return false
        }

        for i in 0..<someContainer.count {
            if someContainer[i] != anotherContainer[i] {
                return false
            }
        }
        
        return true
}
```

### Where 절을 포함하는 지네릭의 익스텐션

```swift
extension Stack where Element: Equatable { // Element가 Equatable을 따르는지
    func isTop(_ item: Element) -> Bool {
        guard let topItem = items.last else {
            return false
        }
        return topItem == item
    }
}

struct NotEquatable { }
var notEquatableStack = Stack<NotEquatable>()
let notEquatableValue = NotEquatable()
notEquatableStack.push(notEquatableValue)
notEquatableStack.isTop(notEquatableValue)  // Error
```

```swift
extension Container where Item == Double { // Item이 Double인지
    func average() -> Double {
        var sum = 0.0
        for index in 0..<count {
            sum += self[index]
        }
        return sum / Double(count)
    }
}
print([1260.0, 1200.0, 98.6, 37.0].average())
// Prints "648.9"
```

### 지네릭의 연관 타입에 where절 적용

```swift
protocol Container {
    associatedtype Item
    mutating func append(_ item: Item)
    var count: Int { get }
    subscript(i: Int) -> Item { get }

    associatedtype Iterator: IteratorProtocol where Iterator.Element == Item
    func makeIterator() -> Iterator
}

protocol ComparableContainer: Container where Item: Comparable { }
```

### 지네릭 서브스크립트

지네릭 서브스크립트에도 조건을 걸 수 있다.

```swift
extension Container {
    subscript<Indices: Sequence>(indices: Indices) -> [Item]
        where Indices.Iterator.Element == Int { // Indices가 Sequence 타입을 따라야 하며, Iterator의 Element가 Int여야함
            var result = [Item]()
            for index in indices {
                result.append(self[index])
            }
            return result
    }
}
```
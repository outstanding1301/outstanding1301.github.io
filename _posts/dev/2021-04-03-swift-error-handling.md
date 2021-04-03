---
layout: post
title: "[Swift] 에러 처리 (Error Handling)"
summary: "Swift에서는 런타임 에러 발생 시 처리를 위해 에러의 발생(throwing), 감지(catching), 증식(propagation), 조작(manipulating)을 지원하는 일급 클래스를 제공"
thumbnail: "https://developer.apple.com/assets/elements/icons/swift/swift-256x256.png"
category: dev
tags: [swift]
comments: true
date: 2021-04-03 20:28:49
lastmod: 2021-04-03 20:28:49
sitemap: 
  changefreq: daily
  priority: 1.0
---
# 에러 처리

Swift에서는 런타임 에러 발생 시 처리를 위해 에러의 `발생(throwing)`, `감지(catching)`, `증식(propagation)`, `조작(manipulating)`을 지원하는 일급 클래스를 제공

주로 Error 프로토콜을 상속받은 열거형으로 정의

```swift
enum VendingMachineError: Error {
	case invalidSelection
	case insufficientFunds(coinsNeeded: Int)
	case outOfStock
}

throw VendingMachineError.insufficientFunds(coinsNeeded: 5)
```

### 에러 발생

`throws` 키워드를 사용해 어떤 함수, 메소드가 에러를 발생 시킬 수 있다는 것을 명시,   
`throws` 키워드는 리턴 타입 표시 기호인 `->` 전에 적음
```swift
func canThrowErrors() throws -> String
func cannotThrowErrors() -> String
```

> 오직 throwing function 만이 에러를 발생시킬 수 있음.


```swift
struct Item {
    var price: Int
    var count: Int
}

class VendingMachine {
    var inventory = [
        "빼빼로": Item(price: 12, count: 7),
        "꼬북칩": Item(price: 10, count: 0),
        "포카칩": Item(price: 7, count: 11)
    ]
    var coinsDeposited = 0

    func vend(_ name: String) throws {
        guard let item = inventory[name] else {
            throw VendingMachineError.invalidSelection // 에러 발생
        }

        guard item.count > 0 else {
            throw VendingMachineError.outOfStock // 에러 발생 
        }

        guard item.price <= coinsDeposited else {
            throw VendingMachineError.insufficientFunds(coinsNeeded: item.price - coinsDeposited) // 에러 발생
        }

        coinsDeposited -= item.price

        var newItem = item
        newItem.count -= 1
        inventory[name] = newItem

        print("Dispensing \(name)")
    }
}
```

### 에러 처리

do-catch를 이용해 에러를 처리하는 코드 블럭을 작성할 수 있다.  

일반적으로 다음과 같이 사용한다.

```swift
do {
	try expression
	statements
} catch pattern1 {
	statements
} catch pattern2 where condition {
	statements
} catch {
	statements
}
```


```swift
var vendingMachine = VendingMachine()
vendingMachine.coinsDeposited = 8
do {
    try vendingMachine.vend("꼬북칩")
    print("꼬북칩을 구매했다.")
} catch VendingMachineError.invalidSelection {
    print("그런 과자는 없습니다.")
} catch VendingMachineError.outOfStock {
    print("재고가 없습니다.")
} catch VendingMachineError.insufficientFunds(let coinsNeeded) {
    print("돈이 부족합니다. \(coinsNeeded) 개의 동전을 더 넣으세요.")
} catch {
    print("알 수 없는 에러: \(error).")
}
// 재고가 없습니다. 출력
```

### 에러를 옵셔널 값으로 변환하기

`try?` 구문을 사용해 에러를 옵셔널 값으로 변환할 수 있다.  
`try?` 표현 내에서 에러 발생 시 그 표현의 값은 `nil`이 된다.

```swift
func someFunction() throws -> Int {
	...
}

// try? 구문 사용
let x = try? someFunction()

// do - catch 구문 사용
let y = Int?
do {
	y = try somFunction()
} catch {
	y = nil
}

```

위 두 가지 표현은 동일한 결과를 반환함

### 에러 발생 중지

함수나 메소드에서 에러가 발생하지 않을 것이라고 확신하는 경우 `try!`를 사용할 수 있음

```swift
let x = try! someFunction()
```

### 정리 액션 기술

`defer` 구문을 이용해 함수가 종료된 후 구문을 수행할 수 있음

```swift
func proccessFile(filename: String) throws {
	if exists(filename){
		let file = open(filename)
		defer {
			close(file)
		}
		~~~
		// 스코프의 마지막에 defer 구문이 실행됨, close(file)
	}
}
```
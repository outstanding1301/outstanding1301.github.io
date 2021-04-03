---
layout: post
title: "[Swift] 옵셔널 체이닝 (Optional Chaining)"
summary: "nil일 수도 있는 프로퍼티나 메소드 그리고 서브스크립트에 질의(query)를 하는 과정"
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
# 옵셔널 체이닝

`nil`일 수도 있는 프로퍼티나 메소드 그리고 서브스크립트에 `질의(query)`를 하는 과정  
만약 옵셔널이 값을 가지고 있다면 값을 반환하고, 값이 nil이면 nil을 반환함

### 강제 언래핑(`!`)의 대체로서의 옵셔널 체이닝(`?`)

강제 언래핑 시 그 값이 없으면 런타임 에러가 발생하지만, **옵셔널 체이닝을 사용하면 런타임 에러 대신 `nil`이 반환**  
옵셔널 체이닝의 값은 항상 `옵셔널 값`


```swift
class  Person  {
	var residence:  Residence?
}

class  Residence  {
	var numberOfRooms =  1
}
```

```swift
let person = Person()

// 강제 언래핑
let roomCount = person.residence!.numberOfRooms // 런타임 에러 발생

// 옵셔널 체이닝
if let roomCount = person.residence?.numberOfRooms {
	print("person의 집엔 방이 \(roomCount)개가 있다.")
} else {
	print("person은 집이 없다.")
}
// person은 집이 없다. 출력
```

```swift
let person = Person()
person.residence = Residence()

// 옵셔널 체이닝
if let roomCount = person.residence?.numberOfRooms {
	print("person의 집엔 방이 \(roomCount)개가 있다.")
} else {
	print("person은 집이 없다.")
}
// person의 집엔 방이 1개가 있다. 출력
```

### 옵셔널 체이닝을 통한 프로퍼티의 접근

```swift
let person = Person()
person.residence?.numberOfRooms = 2 // residence가 nill이기 때문에 아예 실행되지 않음
```
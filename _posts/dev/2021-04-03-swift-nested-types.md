---
layout: post
title: "[Swift] 중첩 타입 (Nested Types)"
summary: "열거형, 클래스, 구조체를 그 타입 안에서 다시 정의할 수 있음"
thumbnail: "https://developer.apple.com/assets/elements/icons/swift/swift-256x256.png"
category: dev
tags: [swift]
comments: true
date: 2021-04-03 20:29:49
lastmod: 2021-04-03 20:29:49
series: swift
sitemap: 
  changefreq: daily
  priority: 1.0
---
# 중첩 타입

`열거형, 클래스, 구조체`를 `열거형, 클래스, 구조체` 안에서 정의할 수 있음  
한글로 번역하면 이상한데, nested의 의미를 생각하면 이해하기 편함  
`Inner Class`를 생각하면 됨

```swift
struct BlackjackCard {
    
    // struct 안에서 enum 정의
    enum Suit: Character {
        case spades = "♠", hearts = "♡", diamonds = "♢", clubs = "♣"
    }

    // struct 안에서 enum 정의
    enum Rank: Int {
        case two = 2, three, four, five, six, seven, eight, nine, ten
        case jack, queen, king, ace
        
        // enum 안에서 struct 정의
        struct Values {
            let first: Int, second: Int?
        }
        var values: Values {
            switch self {
                case .ace:
                    return Values(first: 1, second: 11)
                case .jack, .queen, .king:
                    return Values(first: 10, second: nil)
                default:
                    return Values(first: self.rawValue, second: nil)
            }
        }
    }

    let rank: Rank, suit: Suit
    var description: String {
        var output = "suit is \(suit.rawValue),"
        output += " value is \(rank.values.first)"
        if let second = rank.values.second {
            output += " or \(second)"
        }
        return output
    }
 }
```

### 중첩 타입의 언급

중첩 타입을 선언 밖에서 사용하려면 선언된 곳의 시작부터 끝까지 적어줘야 함

```swift
let heartsSymbol = BlackjackCard.Suit.hearts.rawValue
// heartsSymbol is "♡"
```
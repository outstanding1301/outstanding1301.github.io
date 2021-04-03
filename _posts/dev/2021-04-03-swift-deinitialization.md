---
layout: post
title: "[Swift] 초기화 해지 (Deinitialization)"
summary: "클래스 인스턴스가 소멸되기 직전에 호출"
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
# 초기화 해지

클래스 인스턴스가 소멸되기 직전에 호출, `deinit` 키워드를 사용  
클래스 당 오직 하나의 디이셜라이저만 선언 가능, 파라미터를 받을 수 없음

```swift
class Player {
	var name: String
	init(_ name: String) {
		self.name = name
		print("플레이어 \(name) 생성됨")
	}
	deinit() {
		print("플레이어 \(name) 소멸됨")	
	}
}

var player = Player("test") // 플레이어 test 생성됨
player = nil // 플레이어 test 소멸됨
```
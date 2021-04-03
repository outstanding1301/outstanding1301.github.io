---
layout: post
title: "[Swift] 서브스크립트 (Subscript)"
summary: "콜렉션, 리스트, 시퀀스 등 집합의 특정 멤버 엘리먼트에 간단하게 접근할 수 있는 문법"
thumbnail: "https://developer.apple.com/assets/elements/icons/swift/swift-256x256.png"
category: dev
tags: [swift]
comments: true
date: 2021-04-03 20:23:49
lastmod: 2021-04-03 20:23:49
series: swift
sitemap: 
  changefreq: daily
  priority: 1.0
---
# 서브스크립트

콜렉션, 리스트, 시퀀스 등 **집합의 특정 멤버 엘리먼트에 간단하게 접근**할 수 있는 문법

### 문법
```swift
// 기본 사용법
subscript(index:  Int)  ->  Int  {
	get  {
		return ~ // 적절한 반환 값
	}
	set(newValue)  {
	// 적절한 set 액션
	}
}

// 읽기 전용 (get은 생략)
subscript(index:  Int)  ->  Int  {
	return ~ // 적절한 반환 값
}

// 호출
someInstance[index] = newValue // 서브스크립트의 set 호출
print(someInstance[index]) // 서브스크립트의 get 호출
```
---
layout: post
title: "[Swift] 타입캐스팅 (Type Casting)"
summary: "인스턴스의 타입을 확인하거나 인스턴스를 같은 계층에 있는 다른 superclass나 subclass로 취급하는 방법"
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
# 타입캐스팅

인스턴스의 타입을 확인하거나 인스턴스를 같은 계층에 있는 다른 superclass나 subclass로 취급하는 방법.  
`is` 와 `as` 두 연산자를 사용함

```swift
class MediaItem {
    var name: String
    init(name: String) {
        self.name = name
    }
}
```

```swift
class Movie: MediaItem {
    var director: String
    init(name: String, director: String) {
        self.director = director
        super.init(name: name)
    }
}

class Song: MediaItem {
    var artist: String
    init(name: String, artist: String) {
        self.artist = artist
        super.init(name: name)
    }
}
```

```swift
let library = [
    Movie(name: "비포 선라이즈", director: "리처드 링클레이터"),
    Song(name: "Slow Dancing In The Dark", artist: "Joji"),
    Movie(name: "그린북", director: "피터 패럴리"),
    Song(name: "HIGHEST IN THE ROOM", artist: "Travis Scott"),
    Song(name: "시공간", artist: "기리보이")
]

// 이 배열의 타입은 [MediaItem]으로 추론됨
```

### 타입 확인 `is`

인스턴스의 타입을 확인할 수 있음. 자바로 치면 instanceof

```swift
var movieCount = 0
var songCount = 0

for item in library {
    if item is Movie {
        movieCount += 1
    } else if item is Song {
        songCount += 1
    }
}

print("\(movieCount) 개의 영화와 \(songCount) 개의 음악이 있습니다.")
```

### 다운캐스팅 `as?`, `as!`

특정 타입이 맞는지 확신할 수 없을 때 `as?`
특정 타입이라는 것이 확실한 경우에 `as!`

```swift
for item in library {
    if let movie = item as? Movie {
        print("영화: \(movie.name), 감독. \(movie.director)")
    } else if let song = item as? Song {
        print("음악: \(song.name), 아티스트 \(song.artist)")
    }
}
```
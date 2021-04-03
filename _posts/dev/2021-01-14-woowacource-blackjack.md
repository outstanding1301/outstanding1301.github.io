---
layout: post
title: "[Java] 우아한 테크코스 - 블랙잭"
summary: "우아한 테크코스의 프리코스-블랙잭을 구현하면서 정리한 글입니다."
thumbnail: "https://media.giphy.com/media/xU9TT471DTGJq/giphy.gif"
category: dev
tags: [java, woowacource]
comments: true
date: 2021-01-14 18:46:24
lastmod: 2021-01-14 18:46:24
sitemap: 
  changefreq: daily
  priority: 1.0
---
<!-- ![이미지](https://github.com/outstanding1301/outstanding1301.github.io/blob/master/imgs/dev/2021-01-14-woowacource-blackjack/이미지파일?raw=true) -->

우아한 테크코스의 [프리코스-블랙잭](https://github.com/outstanding1301/java-blackjack-precourse)을 구현하면서 정리한 글입니다.  

## 요구사항
- 블랙잭 게임을 진행하는 프로그램을 구현한다. 블랙잭 게임은 딜러와 플레이어 중 카드의 합이 21 또는 21에 가장 가까운 숫자를 가지는 쪽이 이기는 게임이다.
- 플레이어는 게임을 시작할 때 배팅 금액을 정해야 한다. 카드의 숫자 계산은 카드 숫자를 기본으로 하며, 예외로 Ace는 1 또는 11로 계산할 수 있으며, King, Queen, Jack은 각각 10으로 계산한다.
- 게임을 시작하면 플레이어는 두 장의 카드를 지급 받으며, 두 장의 카드 숫자를 합쳐 21을 초과하지 않으면서 21에 가깝게 만들면 이긴다. 21을 넘지 않을 경우 원한다면 얼마든지 카드를 계속 뽑을 수 있다. 단, 카드를 추가로 뽑아 21을 초과할 경우 배팅 금액을 모두 잃게 된다.
- 처음 두 장의 카드 합이 21일 경우 블랙잭이 되면 베팅 금액의 1.5 배를 딜러에게 받는다. 딜러와 플레이어가 모두 동시에 블랙잭인 경우 플레이어는 베팅한 금액을 돌려받는다.
- 딜러는 처음에 받은 2장의 합계가 16이하이면 반드시 1장의 카드를 추가로 받아야 하고, 17점 이상이면 추가로 받을 수 없다. 딜러가 21을 초과하면 그 시점까지 남아 있던 플레이어들은 가지고 있는 패에 상관 없이 승리해 베팅 금액을 받는다.

> [우아한테크코스 프리코스 Week 3. 블랙잭](https://hotheadfactory.com/?p=1677) 을 참고했습니다.


<br>

## 🎱 프로그래밍 요구사항
- 자바 코드 컨벤션을 지키면서 프로그래밍한다.
  - 기본적으로 [Google Java Style Guide](https://google.github.io/styleguide/javaguide.html)을 원칙으로 한다.
  - 단, 들여쓰기는 '2 spaces'가 아닌 '4 spaces'로 한다.
- indent(인덴트, 들여쓰기) depth를 **1까지만 허용**한다.
- 3항 연산자를 쓰지 않는다.
- 함수(또는 메소드)가 한 가지 일만 하도록 최대한 작게 만들어라.
- 프로그래밍 요구사항에서 별도로 변경 불가 안내가 없는 경우 파일 수정과 패키지 이동을 자유롭게 할 수 있다.
- 예외 상황 시 에러 문구를 출력해야 한다. 단, 에러 문구는 `[ERROR]` 로 시작해야 한다.
- 함수(또는 메소드)의 길이가 **10라인**을 넘어가지 않도록 구현한다.
  - 함수(또는 메소드)가 한 가지 일만 잘 하도록 구현한다.
- else 예약어를 쓰지 않는다.
- 생성자와 접근 제어자를 건드리지 않는다.

## 😎 나의 요구사항
- 가능하면 Setter, Getter를 사용하지 않는다.
- TDD 기반으로 개발한다. (공부한 내용 블로깅 하기)
- MVC 패턴으로 개발한다.

<br>

----

# 요구사항 분석

요구사항을 간단하게 정리해보았다.

- 구성 요소
  - 블랙잭 게임
    - 딜러
    - 플레이어
    - 카드
      - Ace는 1 또는 11로 계산
      - J, Q, K는 각각 10으로 계산
- 게임 흐름
  - 시작 시
    - 플레이어
      1. 배팅 금액을 정함
      2. 2장의 카드를 지급 받음
  - 게임 진행 중
    - 카드의 합이 21을 넘지 않을 경우 계속 카드를 더 뽑을 수 있음 (`힛, hit`)
    - 21이 넘으면(`버스트, burst`) 즉시 패배
    - 본인의 패에 만족하는 경우 차례를 마칠 수 있음 (`스탠드, stand`)
    - 딜러
      - 16 이하면 무조건 히트, 17 이상이면 무조건 스테이
  - 승리 조건
    - 카드의 합이 21 또는 21에 가장 가까운 숫자를 가지는 쪽이 이김
  - 보상
    - `버스트, burst`인 경우 -> 0배
    - 첫 2장이 21인 경우 -> 1.5배
    - 그 외 승리할 경우 -> 2배

# 0. 프로젝트 구조

초기 프로젝트 구조는 아래와 같다.

```
.
|-- main
|   `-- java
|       `-- domain
|           |-- card
|           |   |-- Card.java
|           |   |-- CardFactory.java
|           |   |-- Symbol.java
|           |   `-- Type.java
|           |-- user
|               |-- Dealer.java
|               `-- Player.java
`-- test
    `-- java
        `-- domain
            `-- card
                `-- CardFactoryTest.java
```


## 1. repository 추가

repository 패키지를 생성하고 PlayerRepository 인터페이스를 추가했다.

```java
package domain.repository;

import domain.user.Player;

import java.util.List;

public interface PlayerRepository {
    List<Player> getPlayers();
    void addPlayer(Player player);
}

```

그리고 PlayerRepositoryImpl 클래스를 구현하였다.

```java
package domain.repository;

import domain.user.Player;

import java.util.ArrayList;
import java.util.List;

public class PlayerRepositoryImpl implements PlayerRepository {
    private List<Player> players;

    public PlayerRepositoryImpl() {
        players = new ArrayList<>();
    }

    @Override
    public List<Player> getPlayers() {
        return players;
    }

    @Override
    public void addPlayer(Player player) {
        players.add(player);
    }
}
```

그리고 테스트 코드를 작성했다.
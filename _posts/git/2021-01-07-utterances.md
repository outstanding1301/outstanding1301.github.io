---
layout: post
title: "[Github] 블로그에 댓글 기능 추가하기 (ft. Utterances)"
category: git
tags: [git, blog, github, jekyll, comment, utterances]
comments: true
---

# ✏️ 댓글 기능을 추가하자!

블로그 커스터마이징이 어느정도 마무리 되어가고 있다.  
따로 포스팅은 안했지만 포스트의 오른쪽을 보면 목차가 보일 것이다.  

[allejo/jekyll-toc](https://github.com/allejo/jekyll-toc)을 이용해서 구현했는데 나중에 기회가 된다면 포스팅 해보겠다.  

아무튼, 댓글 기능을 추가해보려고 하는데 Jekyll 기반의 블로그의 대부분은 [Disqus](https://disqus.com/)를 사용하는 것 같다.  

### 😨 그러나 Disqus에는 **치명적인** 문제점이 있다.
1. Disqus는 무겁다.
2. 무료 라이센스로 사용하는 경우 광고가 붙는다.

무겁고 광고가 붙는다니... 도저히 용서할 수가 없었다.

그래서 다른 대안을 찾던 중 [Utterances](https://utteranc.es/) 라는 것을 발견하게 되었다.

## ✨ Utterances
![Utternace 뜻](https://github.com/outstanding1301/outstanding1301.github.io/blob/master/imgs/git/2021-01-07-utterances/utterance.png?raw=true)

뭐.. 이런 뜻이 있다고 한다. 

`Utterances`를 사용하면 Github 저장소의 Issue로 댓글을 관리할 수 있다.  

개발 블로그 특성상, 내 블로그에 접근하는 사람들은 Github 계정이 있을 가능성이 높으니까 사용하기 좋을 것 같다.  

또 이슈가 등록되면 Slack 메세지가 오게 하거나, 메일이 오게 하는 등 설정이 가능하므로 댓글 알림 기능까지 쉽게 구현 가능하다.

### 😏 그럼 이제 본격적으로 써보자
#### 1. 설치
먼저 Github App에서 [Utterances](https://github.com/apps/utterances)를 설치해야한다.


![설치 페이지](https://github.com/outstanding1301/outstanding1301.github.io/blob/master/imgs/git/2021-01-07-utterances/install-1.png?raw=true)

> [설치 페이지](https://github.com/apps/utterances)에 접속하면 다음과 같이 나온다.  
> 이미 설치한 경우 Configure버튼이 보이는데, 여러분들에게는 Install 버튼이 보일것이다.


Install 버튼을 누르면 저장소를 선택하는 화면이 나온다.

![저장소 선택](https://github.com/outstanding1301/outstanding1301.github.io/blob/master/imgs/git/2021-01-07-utterances/install-2.png?raw=true)

> 댓글을 이슈로 관리할 저장소를 선택하면 된다.  

나는 블로그 저장소를 private로 설정해놨기 때문에 [댓글 관리를 위한 public 저장소](https://github.com/outstanding1301/blog-comments)를 새로 만들었다.

Install 버튼을 눌러 설치를 완료하자.

#### 2. 설정
설치가 완료되면 설정 페이지로 이동한다.  
설정 페이지에서 저장소를 설정해주자.

![저장소 설정](https://github.com/outstanding1301/outstanding1301.github.io/blob/master/imgs/git/2021-01-07-utterances/config-1.png?raw=true)

> repo에 `계정명/저장소이름` 을 입력하면 된다.

그 다음은 블로그 포스트와 이슈 매핑 방법에 대한 설정이다.

![이슈 매핑](https://github.com/outstanding1301/outstanding1301.github.io/blob/master/imgs/git/2021-01-07-utterances/config-2.png?raw=true)

> 블로그 글 경로를 이슈의 제목으로 설정하기로 했다.  
> 글의 제목은 빈번히 수정되어도 파일명은 수정하지 않을 것이기 때문이다.

![이슈 라벨](https://github.com/outstanding1301/outstanding1301.github.io/blob/master/imgs/git/2021-01-07-utterances/config-3.png?raw=true)

> 이슈 라벨과 테마 설정이다.  
> 굳이 설정할 필요는 없지만 구분을 위해 댓글 이슈에는 comments를 붙이도록 설정했다.  
> (오로지 댓글만을 위한 저장소이기 때문에 구분할 이유는 없긴하다..)

![스크립트](https://github.com/outstanding1301/outstanding1301.github.io/blob/master/imgs/git/2021-01-07-utterances/config-4.png?raw=true)
> 다 입력하면 이런 스크립트가 나온다.  
> 복사해서 _layout/post.html 에 추가할 것이다.

#### 3. _layout/post.html에 추가
지금 사용하고 있는 테마는 기본적으로 disqus를 사용하도록 되어있다.  
우리는 disqus가 필요 없으므로, 관련 코드들을 모두 주석시키자

![주석](https://github.com/outstanding1301/outstanding1301.github.io/blob/master/imgs/git/2021-01-07-utterances/post-1.png?raw=true)

이제 그 위치에 복사한 Utterances 스크립트를 추가하자.

![스크립트 추가](https://github.com/outstanding1301/outstanding1301.github.io/blob/master/imgs/git/2021-01-07-utterances/post-2.png?raw=true)

이제 Github 저장소에 push 하면 끝이다.

#### 4. Github 저장소에 push
```bash
git add _layout/post.html
git commit -m "feat(comment): disqus제거하고 utterances추가"
git push origin master
```
> 커밋 메시지는 각자 방식대로 작성하자

## 🔎 이제 확인해보자

![댓글 등록](https://github.com/outstanding1301/outstanding1301.github.io/blob/master/imgs/git/2021-01-07-utterances/comment-1.png?raw=true)

> 잘된다. 마크다운도 된다. 짱이다...

![이슈](https://github.com/outstanding1301/outstanding1301.github.io/blob/master/imgs/git/2021-01-07-utterances/comment-2.png?raw=true)

> 이슈도가 새로 생성되었고, 이런식으로 댓글이 달린다.



![쩐다...](https://media.giphy.com/media/M33UV4NDvkTHa/giphy.gif)
> 정말 와우다..

## 🚀 참고

- [https://www.hahwul.com/2020/08/08/jekyll-utterances/](https://www.hahwul.com/2020/08/08/jekyll-utterances/)

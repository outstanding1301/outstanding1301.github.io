---
layout: post
title: "[Github] 구글 검색 엔진에 내 블로그 등록하기"
category: dev
tags: [git, blog, github, jekyll, seo]
comments: true
---

# 💻 구글 검색 엔진에 등록해보자

호기롭게 블로그를 만들었다. [첫 글](https://outstanding1301.github.io/git/2020/12/30/the-angularjs-commit-conventions/)도 작성했고...  
이제 내가 쓴 글을 확인하려고 구글 검색을 해보았다.

![안나온다...](https://github.com/outstanding1301/outstanding1301.github.io/blob/master/imgs/git/2021-01-07-google-search-engine/google-search.png?raw=true)
> 안나온다...

### 😨 왜 안나올까?  
검색 엔진이 내 블로그의 존재를 모르기 때문이다.  
그러므로 검색엔진에게 직접 내 블로그에 대해 알려줘야한다.

### 🧐 어떻게 알려주지...?

1. [Google Search Console](https://search.google.com/search-console/welcome?hl=ko&utm_source=wmx&utm_medium=deprecation-pane&utm_content=home) 에 `속성`을 추가하고 인증한다.
2. `sitemap.xml`을 작성 및 등록한다.
3. `robots.txt`를 작성한다.

## 1. Google Search Console 에 속성 추가 및 인증

![접속](https://github.com/outstanding1301/outstanding1301.github.io/blob/master/imgs/git/2021-01-07-google-search-engine/google-search-console-1.png?raw=true)
[Google Search Console](https://search.google.com/search-console/welcome?hl=ko&utm_source=wmx&utm_medium=deprecation-pane&utm_content=home) 에 접속하여 블로그 URL을 입력하자.  
왼쪽 도메인 입력으로 할 경우에는 DNS 레코드에 TXT를 추가해야하는데,  
우린 github.io를 이용하므로 이는 불가능하다.  

따라서 오른쪽 `URL 접두어`에 입력한다.

![인증파일 다운로드](https://github.com/outstanding1301/outstanding1301.github.io/blob/master/imgs/git/2021-01-07-google-search-engine/google-search-console-2.png?raw=true)

이제 `HTML 파일`을 다운로드 받아서 Github 저장소에 등록하면 된다.  
저장소의 루트 디렉토리에 저장하고 Github 저장소에 등록한다.  

```bash
git add [HTML 파일]
git commit -m "docs: google search console 인증 파일 추가"
git push origin master
```

이제 `확인` 버튼을 누르면 소유권이 인증 된다.  

![소유권 인증](https://github.com/outstanding1301/outstanding1301.github.io/blob/master/imgs/git/2021-01-07-google-search-engine/google-search-console-3.png?raw=true)

> 소유권이 인증되었다.

## 2. sitemap.xml 작성 및 등록
저장소의 루트 디렉토리에 `sitemap.xml` 파일을 생성한다.  
[이 파일의 내용](https://github.com/outstanding1301/outstanding1301.github.io/blob/master/sitemap.xml)을 붙여넣기 한다.

[🧐 참고한 글]([https://joelglovier.com/writing/sitemaps-for-jekyll-sites](https://joelglovier.com/writing/sitemaps-for-jekyll-sites))

> 반드시 1~2행의 `---`도 입력해야한다!

마찬가지로 Github 저장소에 등록해준다.

```bash
git add sitemap.xml
git commit -m "docs: sitemap.xml 추가"
git push origin master
```

[https://블로그주소/sitemap.xml](https://outstanding1301.github.io/sitemap.xml) 에 접속해 `sitemap.xml`이 정상적으로 등록되었는지 확인한다.

 이제 Google Search Console에 사이트맵을 제출하면 된다.

![사이트맵](https://github.com/outstanding1301/outstanding1301.github.io/blob/master/imgs/git/2021-01-07-google-search-engine/sitemap-1.png?raw=true)

[Google Search Console](https://search.google.com/search-console) 에서 아까 등록한 속성을 선택하고 Sitemaps 탭으로 이동한다.

![사이트맵 등록](https://github.com/outstanding1301/outstanding1301.github.io/blob/master/imgs/git/2021-01-07-google-search-engine/sitemap-2.png?raw=true)

사이트맵 URL 입력에 `sitemap.xml`을 입력하고 제출한다.

![등록성공](https://github.com/outstanding1301/outstanding1301.github.io/blob/master/imgs/git/2021-01-07-google-search-engine/sitemap-3.png?raw=true)
> 성공적으로 등록되었다!

## 3. robots.txt 작성
> `robots.txt`는 검색 엔진의 크롤러의 웹 문서 접근을 허가하거나 차단하기 위해 기술되는 문서이다.  
자세한 내용은 [로봇 배제 표준](https://ko.wikipedia.org/wiki/%EB%A1%9C%EB%B4%87_%EB%B0%B0%EC%A0%9C_%ED%91%9C%EC%A4%80)을 참고하자

일단은 모든 검색 엔진의 크롤러가 모든 문서에 접근하는 것을 허락할 것이다.

```
User-agent: *
Allow: /

Sitemap: http://outstanding1301.github.io/sitemap.xml
```

```sitemap.xml``` 의 경로도 명시해주었다.

마찬가지로 Github 저장소에 등록하자.

```bash
git add robots.txt
git commit -m "docs: robots.txt 추가"
git push origin master
```

## 🔎 이제 구글에 내 글을 검색해보자

아직 안나온다...  
완전히 등록되는데에 한 일주일 정도가 걸린다고 하니 천천히 기다려보자 :)

## 🚀 참고
- [https://wayhome25.github.io/etc/2017/02/20/google-search-sitemap-jekyll/](https://wayhome25.github.io/etc/2017/02/20/google-search-sitemap-jekyll/)
- [http://jinyongjeong.github.io/2017/01/13/blog_make_searched/](http://jinyongjeong.github.io/2017/01/13/blog_make_searched/)
- [https://joelglovier.com/writing/sitemaps-for-jekyll-sites](https://joelglovier.com/writing/sitemaps-for-jekyll-sites)
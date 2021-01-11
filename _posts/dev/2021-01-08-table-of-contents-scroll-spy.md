---
layout: post
title: "[Github] 블로그 포스트에 스크롤에 따른 목차(Table of Contents, TOC)를 띄우는 ScrollSpy 기능 구현하기"
category: dev
tags: [git, blog, github, jekyll]
comments: true
---

# ✨ 스크롤에 따른 목차를 띄우는 ScrollSpy 기능 구현하기

지난번에 약속한 대로, [allejo/jekyll-toc](https://github.com/allejo/jekyll-toc)을 이용해서 포스트 오른쪽에 목차를 띄우는 기능을 구현하는 방법을 포스팅하겠다.

## 🤔 뭘 한다고?

직접 보는게 이해하기 쉬울 것이다.
![이걸 구현할거다.](https://github.com/outstanding1301/outstanding1301.github.io/blob/master/imgs/git/2020-01-08-table-of-contents-scroll-spy/what.gif?raw=true)

이걸 구현할 것이다.  
처음엔 이걸 도대체 뭐라고 검색해야 나오는지 몰라서 이것저것 검색해봤는데  

이 글을 보고 있는 여러분들도 나와 같은 심정이였을 것 같다.  

[velog.io](https://velog.io/)의 포스트를 보고, 이 기능을 구현해야 겠다고 생각하게 됐다.

그래서 디자인도 거의 ~~유사~~동일하다..  

## 🔨 이제 만들어보자!

 이 기능을 구현하기 위한 과정은 크게 3단계로 나눌 수 있다.  

 1. _includes 디렉터리에 [toc.html](https://github.com/allejo/jekyll-toc/releases/download/v1.1.0/toc.html) 등록하기
 2. _layouts/post.html 파일 수정하기
 3. _scss/component/_post.scss 파일 수정하기

 테마에 따라 파일명은 다를 수 있지만, 결국 해야 하는 일은 같다.

### 1. _includes 디렉터리에 toc.html 등록하기

간단하다. 말 그대로 [toc.html](https://github.com/allejo/jekyll-toc/releases/download/v1.1.0/toc.html)를 _includes 디렉터리에 다운로드 하면 된다. ([클릭](https://github.com/allejo/jekyll-toc/releases/download/v1.1.0/toc.html)하면 바로 다운로드 됩니다.)

그리고 Github 저장소에 Push하자.

```bash
git add _includes/toc.html
git commit -m "docs(toc): toc.html 추가"
git push origin master
```

> 커밋 메시지 타입이 docs가 맞는지 확실하지는 않다... 아무튼 html 문서니까 docs로 했다.

### 2. _layouts/post.html 파일 수정하기

> 반드시 내가 작성한 코드대로 하는 것이 정답은 아니다.  
> 상당히 비효율적이고, 나중에 리팩토링이 필요한 코드라고 생각한다. 

#### 1. 본문이 들어가는 `<article>`을 수정한다.
{% raw %}
```html
<div class="post">
  <h1 class="post-title">{{ page.title }}</h1>
  <span class="post-date">{{ page.date | date_to_string }}</span>
  {% if page.tags %} | 
  {% for tag in page.tags %}
    <a href="{{ site.baseurl }}{{ site.tag_page }}#{{ tag | slugify }}" class="post-tag">{{ tag }}</a>
  {% endfor %}
  {% endif %}
  <article>
    <!-- 이 부분을 수정하면 된다. -->
    {{ content }}
  </article>
</div>
```
{% endraw %}


이 부분에서 `<article>...</article>` 부분을 아래와 같이 수정한다.

{% raw %}
```html
<article class="post-article">
    <div class="toc">
      <a href="#">&lt;맨 위로&gt;</a>
      {% include toc.html html=content %}
    </div>
    {{ content }}
  </article>
```
{% endraw %}

간단하게 설명하자면, article에 class를 추가해주었다.  
이는 스타일링을 위한 클래스가 아니라, `script에서 엘리먼트로 가져오기 위해` 추가한 것이다.

또, toc 클래스를 가지는 div 엘리먼트를 추가했다.  
안에는 아까 다운로드한 toc.html의 내용이 들어간다.

#### 2. 스크립트를 추가한다.

> 스크롤할 때마다 계속 반복하므로, 효율적이지 못한 것 같다.  
> 추후에 수정하도록 하겠다.

`_layouts/post.html`의 맨 아래에 아래 코드를 추가한다.

```html
<script>
  function getTOCNodes(master) {
    var nodes = Array.prototype.slice.call(master.getElementsByTagName("*"), 0);
    var tocNodes = nodes.filter(function(elem) {
        return elem.tagName == "A";
    });
    return tocNodes;
  }
  function getHeaderNodes(master) {
    var nodes = Array.prototype.slice.call(master.getElementsByTagName("*"), 0);
    var headerNodes = nodes.filter(function(elem) {
        return elem.tagName == "H1" || elem.tagName == "H2" || elem.tagName == "H3" || elem.tagName == "H4" || elem.tagName == "H5" || elem.tagName == "H6";
    });
    return headerNodes;
  }

  var title = document.getElementsByClassName("post-title")[0];
  var titleY = window.pageYOffset + title.getBoundingClientRect().top;
  
  var article = document.getElementsByClassName("post-article")[0];
  var articleY = window.pageYOffset + article.getBoundingClientRect().top;

  var toc = document.getElementsByClassName("toc")[0];

  var headerNodes = getHeaderNodes(article);
  var tocNodes = getTOCNodes(toc);

  var before = undefined;

  document.addEventListener('scroll', function(e) {
    if (window.scrollY >= articleY-60) {
      toc.style.cssText = "position: fixed; top: 60px;";
    }
    else {
      toc.style.cssText = "";
    }

    var current = headerNodes.filter(function(header) {
      var headerY = window.pageYOffset + header.getBoundingClientRect().top;
      return window.scrollY >= headerY - 60;
    });

    if (current.length > 0) {
      current = current[current.length-1];

      var currentA = tocNodes.filter(function(tocNode) {
        return tocNode.innerHTML == current.innerHTML;
      })
      
      currentA = currentA[0];
      if (currentA) {
        if (before == undefined) before = currentA;

        if (before != currentA) {
          before.classList.remove("toc-active");
          before = currentA;
        }

        currentA.classList.add("toc-active");
      }
      else {
        if (before) 
          before.classList.remove("toc-active");
      }
    }
    else {
      if (before) 
          before.classList.remove("toc-active");
    }

  }, false);
</script>
```

개선의 여지가 아~~~주 많이 보이는 코드이지만, 어쨌든 잘 동작한다.

간단하게 설명하자면, `scroll` 이벤트가 발생할 때 마다  
article의 `<h1~h6>`엘리먼트들의 위치와 스크롤 위치를 비교하면서  
현재 보고있는 부분에 해당하는 toc의 `<a>`태그의 스타일을 바꿔주는 스크립트이다.

놀랍게도 벌써 `_layouts/post.html` 파일 수정이 끝났다.

#### 3. Github 저장소에 Push하기


```bash
git add _layouts/post.html
git commit -m "feat(article): toc엘리먼트 및 스크립트 추가"
git push origin master
```

### 3. _scss/component/_post.scss 파일 수정하기

스타일을 아래와 같이 추가해준다.
```scss
.toc {
  position: absolute;
  right: 0px;
  width: 240px;
  color: $default;
  overflow-y: auto;
  overflow-x: hidden;
  padding-left: 0.75rem;
  padding-right: 0.75rem;
  padding-top: 0.25rem;
  padding-bottom: 0.25rem;
  margin-right: 0px;
  font-size: 0.7rem;
  border-left: 2px solid #e0d9e7;

  display: none;
  @media (min-width: 75em){
    width: 240px;
    display: block;
  }
  @media (min-width: 85em){
    width: 300px;
    display: block;
  }
  @media (min-width: 95em){
    width: 360px;
    display: block;
  }

  a.toc-active {
    font-weight: bold; 
    transition: all 0.125s ease-in 0s; 
    font-size: 0.75rem;
    color: #9075aa;
  }

  ul {
    list-style-type: none;
    margin-bottom: 0.1rem;
    padding-left: 0rem;
    li {
      padding-left: .5rem;
    }
  }

  a {
      color: $default;
      text-decoration: none;
  }
 
  a:hover {
     color:$theme-color;
  }
}
```

[velog.io](https://velog.io/)의 디자인과 최대한 비슷하게 만들어봤다.  

여러분들 취항에 따라서 각자 수정하면 되겠다.

그리고 Github 저장소에 Push하자.

```bash
git add _scss/component/_post.scss
git commit -m "style(toc): toc 스타일 추가"
git push origin master
```

## 😨 이게 다야..?

여러분들 입맛대로 수정해보시길 추천한다!  
내가 봐도 수정할 부분이 많으니, 각자 잘 수정해보자.  
아무리 생각해도 본인이 작성한 코드가 더 낫다 싶으면 댓글에 남겨줬으면 좋겠다.


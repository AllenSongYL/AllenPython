# jQuery

## 	介绍

jQuery 是一个 JavaScript 库。

### 	使用方法

使用方法在“<head>”引入jQuery文件：

```
<head>
    <script src="//code.jquery.com/jquery-1.11.3.min.js"></script>
	...
</head>
```

### 	 $

是著名的jQuery符号。实际上，jQuery把所有的功能全部封装在一个全局变量jQuery中，而$也是一个合法的变量名，它是变量jQuery的别名。

### jQuery对象和DOM对象之间互相转换

var jobject=$("#abc")      //jQuery对象

var DOMobject=jobject.get(0);    //假设存在，获取第一个DOM元素

var another=$(DOMobject)     //重新把DOM包装成jQuery对象

## 选择器

### 按id查找

‘<div id="abc">’

$('#abc')    

注意：id选择器以井号#开头，返回的对象是jQuery对象。（jQuery对象类似数组，它的每个元素都是引用了DOM节点的对象。如果id为abc的元素不存在，则返回[]）

### 按tag查找

var ps =$('p');      //返回所有'<p>'节点

ps.length;          //计算'<p>'节点数量

### 按class查找

class名称钱加一个 . 

var  a = $('.red');

例如： '<div class="red"></div>'   '<p class="green red"></p>'

### 按属性查找

var email = $('[name=email]');      //找出 '<??? name="email">'

var email = $('[name^=icon]');   //找出属性时name，并以icon开头的DOM

var email = $('[name$=icon]');   //找出属性时name，并以icon结尾的DOM

当属性包含空格等特殊字符时，需要用双引号括起来

### 组合查找

var emailinput = $('input[name=email]');

var tr=$('tr.red');     //找出'<tr class="red">'

### 多项选择器

$('p,div');     //把"<p>","<div>"都选出来

$(p.red,p.green);    //把'<p class="red">','<p class="green">'都选出来

要注意的是，选出来的元素是按照它们在HTML中出现的顺序排列的，而且不会有重复元素。例如，`<p class="red green">`不会被上面的`$('p.red,p.green')`选择两次。

### 层级选择器

层级之间用空格隔开

```
<!-- HTML结构 -->
<div class="testing">
    <ul class="lang">
        <li class="lang-javascript">JavaScript</li>
        <li class="lang-python">Python</li>
        <li class="lang-lua">Lua</li>
    </ul>
</div>
```

要选出JavaScript，可以用层级选择器：

```
$('ul.lang li.lang-javascript'); // [<li class="lang-javascript">JavaScript</li>]
$('div.testing li.lang-javascript'); // [<li class="lang-javascript">JavaScript</li>]
```

因为`<div>`和`<ul>`都是`<li>`的祖先节点，所以上面两种方式都可以选出相应的`<li>`节点。

要选择所有的`<li>`节点，用：

```
$('ul.lang li');
```

#### 子选择器

子选择器`$('parent>child')`类似层级选择器，但是限定了层级关系必须是父子关系，就是`<child>`节点必须是`<parent>`节点的直属子节点。还是以上面的例子：

```
$('ul.lang>li.lang-javascript'); // 可以选出[<li class="lang-javascript">JavaScript</li>]
$('div.testing>li.lang-javascript'); // [], 无法选出，因为<div>和<li>不构成父子关系
```

#### 过滤器

过滤器一般不单独使用，它通常附加在选择器上，帮助我们更精确地定位元素。观察过滤器的效果：

```
$('ul.lang li'); // 选出JavaScript、Python和Lua 3个节点

$('ul.lang li:first-child'); // 仅选出JavaScript
$('ul.lang li:last-child'); // 仅选出Lua
$('ul.lang li:nth-child(2)'); // 选出第N个元素，N从1开始
$('ul.lang li:nth-child(even)'); // 选出序号为偶数的元素
$('ul.lang li:nth-child(odd)'); // 选出序号为奇数的元素
```

### 表单相关

针对表单元素，jQuery还有一组特殊的选择器：

- `:input`：可以选择`<input>`，`<textarea>`，`<select>`和`<button>`；
- `:file`：可以选择`<input type="file">`，和`input[type=file]`一样；
- `:checkbox`：可以选择复选框，和`input[type=checkbox]`一样；
- `:radio`：可以选择单选框，和`input[type=radio]`一样；
- `:focus`：可以选择当前输入焦点的元素，例如把光标放到一个`<input>`上，用`$('input:focus')`就可以选出；
- `:checked`：选择当前勾上的单选框和复选框，用这个选择器可以立刻获得用户选择的项目，如`$('input[type=radio]:checked')`；
- `:enabled`：可以选择可以正常输入的`<input>`、`<select>` 等，也就是没有灰掉的输入；
- `:disabled`：和`:enabled`正好相反，选择那些不能输入的。

### 可见或隐藏选择器

```
$('div:visible'); // 所有可见的div
$('div:hidden'); // 所有隐藏的div
```

### 查找和过滤

#### 查找

通常情况下选择器可以直接定位到我们想要的元素，但是，当我们拿到一个jQuery对象后，还可以以这个对象为基准，进行查找和过滤。

最常见的查找是在某个节点的所有子节点中查找，使用`find()`方法，它本身又接收一个任意的选择器。例如如下的HTML结构：

```
<!-- HTML结构 -->
<ul class="lang">
    <li class="js dy">JavaScript</li>
    <li class="dy">Python</li>
    <li id="swift">Swift</li>
    <li class="dy">Scheme</li>
    <li name="haskell">Haskell</li>
</ul>
```

用`find()`查找：

```
var ul = $('ul.lang'); // 获得<ul>
var dy = ul.find('.dy'); // 获得JavaScript, Python, Scheme
var swf = ul.find('#swift'); // 获得Swift
var hsk = ul.find('[name=haskell]'); // 获得Haskell
```

如果要从当前节点开始向上查找，使用`parent()`方法：

```
var swf = $('#swift'); // 获得Swift
var parent = swf.parent(); // 获得Swift的上层节点<ul>
var a = swf.parent('.red'); // 获得Swift的上层节点<ul>，同时传入过滤条件。如果ul不符合条件，返回空jQuery对象
```

对于位于同一层级的节点，可以通过`next()`和`prev()`方法，例如：

当我们已经拿到`Swift`节点后：

```
var swift = $('#swift');

swift.next(); // Scheme
swift.next('[name=haskell]'); // 空的jQuery对象，因为Swift的下一个元素Scheme不符合条件[name=haskell]

swift.prev(); // Python
swift.prev('.dy'); // Python，因为Python同时符合过滤器条件.dy
```

#### 过滤

`filter()`方法可以过滤掉不符合选择器条件的节点：

```
var langs = $('ul.lang li'); // 拿到JavaScript, Python, Swift, Scheme和Haskell
var a = langs.filter('.dy'); // 拿到JavaScript, Python, Scheme
```

或者传入一个函数，要特别注意函数内部的`this`被绑定为DOM对象，不是jQuery对象：

```
var langs = $('ul.lang li'); // 拿到JavaScript, Python, Swift, Scheme和Haskell
langs.filter(function () {
    return this.innerHTML.indexOf('S') === 0; // 返回S开头的节点
}); // 拿到Swift, Scheme
```

`map()`方法把一个jQuery对象包含的若干DOM节点转化为其他对象：

```
var langs = $('ul.lang li'); // 拿到JavaScript, Python, Swift, Scheme和Haskell
var arr = langs.map(function () {
    return this.innerHTML;
}).get(); // 用get()拿到包含string的Array：['JavaScript', 'Python', 'Swift', 'Scheme', 'Haskell']
```

此外，一个jQuery对象如果包含了不止一个DOM节点，`first()`、`last()`和`slice()`方法可以返回一个新的jQuery对象，把不需要的DOM节点去掉：

```
var langs = $('ul.lang li'); // 拿到JavaScript, Python, Swift, Scheme和Haskell
var js = langs.first(); // JavaScript，相当于$('ul.lang li:first-child')
var haskell = langs.last(); // Haskell, 相当于$('ul.lang li:last-child')
var sub = langs.slice(2, 4); // Swift, Scheme, 参数和数组的slice()方法一致
```

## 操作DOM

### 修改节点文本和原始HTML文本

$('p').text();         //无参数调用text()是获取文本，传入参数就变成设置文本

$('p').html();      //获取原始html文本，和text用法相同

### 修改class属性

```
var div = $('#test-div');
div.hasClass('highlight'); 			// false， class是否包含highlight
div.addClass('highlight'); 			// 添加highlight这个class
div.removeClass('highlight'); 		// 删除highlight这个class
```

### 显示和隐藏DOM

```
var a = $('a[target=_blank]');
a.hide(); // 隐藏
a.show(); // 显示
```

### 修改DOM结构

#### 添加DOM

##### append()方法:添加到最后

```
var ul = $('#test-div>ul');
```

然后，调用`append()`传入HTML片段：

```
ul.append('<li><span>Haskell</span></li>');
```

除了接受字符串，`append()`还可以传入原始的DOM对象，jQuery对象和函数对象：

```
// 创建DOM对象:
var ps = document.createElement('li');
ps.innerHTML = '<span>Pascal</span>';
// 添加DOM对象:
ul.append(ps);

// 添加jQuery对象:
ul.append($('#scheme'));

// 添加函数对象:
ul.append(function (index, html) {
    return '<li><span>Language - ' + index + '</span></li>';
});
```

##### prepend()方法：添加到最前

 另外注意，如果要添加的DOM节点已经存在于HTML文档中，它会首先从文档移除，然后再添加，也就是说，用`append()`，你可以移动一个DOM节点。

如果要把新节点插入到指定位置，例如，JavaScript和Python之间，那么，可以先定位到JavaScript，然后用`after()`方法：

```
var js = $('#test-div>ul>li:first-child');
js.after('<li><span>Lua</span></li>');
```

也就是说，同级节点可以用`after()`或者`before()`方法。            

#### 删除节点

 remove() 方法

```
var li = $('#test-div>ul>li');
li.remove(); // 所有<li>全被删除               
```

### 事件

#### 事件语法

    $("p").click(function(){  
    	$(this).hide(); 
    });

#### 鼠标事件

- click: 鼠标单击时触发；
- dblclick：鼠标双击时触发；
- mouseenter：鼠标进入时触发；
- mouseleave：鼠标移出时触发；
- mousemove：鼠标在DOM内部移动时触发；
- hover：鼠标进入和退出时触发两个函数，相当于mouseenter加上mouseleave。

#### 键盘事件

键盘事件仅作用在当前焦点的DOM上，通常是`<input>`和`<textarea>`。

- keydown：键盘按下时触发；
- keyup：键盘松开时触发；
- keypress：按一次键后触发。

#### 其他事件

- focus：当DOM获得焦点时触发；

- blur：当DOM失去焦点时触发；

- change：当`<input>`、`<select>`或`<textarea>`的内容改变时触发；

- submit：当`<form>`提交时触发；

- ready：当页面被载入并且DOM树完成初始化后触发。

- 其中，`ready`仅作用于`document`对象。由于`ready`事件在DOM完成初始化后触发，且只触发一次，所以非常适合用来写其他的初始化代码。

  

  $(document).ready(function(){
       });        

  //这是为了防止文档在完全加载（就绪）之前运行 jQuery 代码。(入口函数)

## 修改CSS

### 格式

css('name','value')

```
var div = $('#test-div');
div.css('color');                    // '#000033', 获取CSS属性
div.css('color', '#336699');         // 设置CSS属性
div.css('color', '');                // 清除CSS属性
```

为了和JavaScript保持一致，CSS属性可以用`'background-color'`和`'backgroundColor'`两种格式。

`css()`方法将作用于DOM节点的`style`属性，具有最高优先级。

### 获取DOM信息

$(window).width();     //浏览器可是窗口的大小

$(window).height();

$(document).width();     //HTML文档的大小

$(document).height();

`attr()`和`removeAttr()`方法用于操作DOM节点的属性：

```
// <div id="test-div" name="Test" start="1">...</div>
var div = $('#test-div');
div.attr('data'); 				// undefined, 属性不存在
div.attr('name'); 				// 'Test'
div.attr('name', 'Hello'); 		 // div的name属性变为'Hello'
div.removeAttr('name'); 		// 删除name属性
div.attr('name'); 			    // undefined
```

`prop()`方法和`attr()`类似，但是HTML5规定有一种属性在DOM节点中可以没有值，只有出现与不出现两种，例如：

```
<input id="test-radio" type="radio" name="test" checked value="1">
```

等价于：

```
<input id="test-radio" type="radio" name="test" checked="checked" value="1">
```

`attr()`和`prop()`对于属性`checked`处理有所不同：

```
var radio = $('#test-radio');
radio.attr('checked'); // 'checked'
radio.prop('checked'); // true
```

`prop()`返回值更合理一些。不过，用`is()`方法判断更好：

```
var radio = $('#test-radio');
radio.is(':checked'); // true
```

类似的属性还有`selected`，处理时最好用`is(':selected')`。

### 操作表单

对于表单元素，jQuery对象统一提供`val()`方法获取和设置对应的`value`属性：

```
/*
    <input id="test-input" name="email" value="">
    <select id="test-select" name="city">
        <option value="BJ" selected>Beijing</option>
        <option value="SH">Shanghai</option>
        <option value="SZ">Shenzhen</option>
    </select>
    <textarea id="test-textarea">Hello</textarea>
*/
var
    input = $('#test-input'),
    select = $('#test-select'),
    textarea = $('#test-textarea');

input.val(); // 'test'
input.val('abc@example.com'); // 文本框的内容已变为abc@example.com

select.val(); // 'BJ'
select.val('SH'); // 选择框已变为Shanghai

textarea.val(); // 'Hello'
textarea.val('Hi'); // 文本区域已更新为'Hi'
```

## 其他

### 遍历jQuery和非jQuery对象

#### map

$.map() 和 .map() ：迭代。每当我们要基于jquery选择器中的所有匹配元素创建数组或串联字符串时使用。
$.map() 适用于普通的Javascript数组
.map()  适用于jQuery元素集合



```
<li id="a"></li>
<li id="b"></li>
<li id="c"></li>

<script>
var arr = [{
    id: "a",
    tagName: "li"
}, {
    id: "b",
    tagName: "li"
}, {
    id: "c",
    tagName: "li"
}];

// 返回 [ "a", "b", "c" ]
$( "li" ).map( function( index, element ) {
    return element.id;
}).get();

// 也返回 [ "a", "b", "c" ]
// Note that the value comes first with $.map
$.map( arr, function( value, index ) {
    return value.id;
});

</script>
```

## 参考手册

API查询


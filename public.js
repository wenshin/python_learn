/*
 * 获取页面元素，给元素绑定多个点击事件
 * 假设页面元素为 <div id="test" class="teststyle" name="test"></div>
 */

// 使用jQuery, 这会很简单

// 获取元素
var $div = $('#test');
// var $div = $('.teststyle');
// var $div = $('[name="test"]');

// 给元素绑定点击事件
$div.click(function () {
  // 点击事件1代码
});
$div.click(function () {
  // 点击事件2代码
});


// 获取元素
var div = document.getElementById('test');
// 通过class来获取元素
// var divs = document.getElementsByTagName('div');
// var div;
// for ( var i = 0; i < divs.length; i++ ) {
//   if ( divs[i].className === 'teststyle' ) {
//     div = divs[i];
//   }
// }
// 通过name属性来获取元素
// var div = document.getElementsByName('test')[0];

// 绑定事件
// 使用 div.onclick = function () {}; 可以吗？
div.addEventListener('click', function () {
  // 点击事件1代码
});
div.addEventListener('click', function () {
  // 点击事件2代码
});

// 这个看着也不比jQuery复杂嘛 = =!
// 但是等等！！在IE下不管用，怎么回事呢？
// 原来IE下使用的不是这个函数
if ( div.addEventListener ) {
  div.addEventListener('click', function () {
    // 点击事件1代码
  });
  div.addEventListener('click', function () {
    // 点击事件2代码
  });
}
if ( div.attachEvent ) {
  div.attachEvent('onclick', function () {
    // 点击事件1代码
  });
  div.attachEvent('onclick', function () {
    // 点击事件2代码
  });
}

// 提取公共代码
function bindEvent(obj, type, listener) {
  if ( div.addEventListener ) {
    obj.addEventListener(type, listener);
  }
  if ( div.attachEvent ) {
    div.attachEvent('on' + type, listener);
  }
}

bindEvent(div, 'click', function () {
  // 点击事件1代码
});
bindEvent(div, 'click', function () {
  // 点击事件2代码
});

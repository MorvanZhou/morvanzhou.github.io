---
description: 
youtube_id: 
youku_link: 
chapter: 1
title: 
date: 2016-11-3
---
* 学习资料:
  * [相关代码]()


<div class="video-container">
<iframe id="myVideo" class="myvideo" width="560" height="315" src="https://www.youtube.com/embed/R8LxK1Q_R8c?rel=0&autoplay=1" frameborder="0" allowfullscreen></iframe>
</div>

<button onclick="myFunction()" type="button" id="status">切换成 优酷 视频</button>

<script>
var vid = document.getElementById("myVideo");
var statusElement = document.getElementById("status");
var currentlyPlaying = 1;
var currentlPlayingTime

var src1 = "https://www.youtube.com/embed/R8LxK1Q_R8c?rel=0&autoplay=1";

var src2 = "http://player.youku.com/embed/XMTYyMjk2NDIwOA";

function myFunction() {
    currentlPlayingTime = vid.currentTime;
    if (currentlyPlaying === 1) {
        vid.src = src2;
        currentlyPlaying = 2;
        statusElement.innerText = '切换成 Youtube 视频';
    } else {
        vid.src = src1;
        currentlyPlaying = 1;
        statusElement.innerText = '切换成 优酷 视频';
    }
    vid.load();
    vid.addEventListener('loadedmetadata', function () {
        vid.currentTime = currentlPlayingTime;
    }, false);
}
</script>
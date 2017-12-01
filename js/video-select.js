function videoChinaIP(src) {
    if (window.XMLHttpRequest)
    {// code for IE7+, Firefox, Chrome, Opera, Safari
        var request = new XMLHttpRequest();
    }
    else
    {// code for IE6, IE5
        var request = new ActiveXObject("Microsoft.XMLHTTP");
    }
    request.open('GET', '//freegeoip.net/xml/');
    request.onreadystatechange = function() {
        if (request.readyState == 4 && request.status == 200) {
            var xmlDoc = request.responseXML;
            var root = xmlDoc.documentElement;
            var element = root.getElementsByTagName("CountryName");
            var country = element[0].firstChild.nodeValue;
            if (country == "China"){
                chooseVideo(src);
            }
        }
    }
    request.send(null);
}

function chooseVideo(src, src_name, vid)
{
    var velem = document.getElementById('videogfw');
    var vai = document.getElementById("video-alrt-info");

    // bilibili
    if (src_name == "bilibili") {
      if (src.includes("hdslb")) {
        velem.style.paddingBottom = "70%";
        vai.style.display = "block";
        if (vid.includes("&page=")) {
          var words = vid.split("&page=");
          var vid = words[0] +"/#page=" + words[1];
        }
        vai.innerHTML = '(Bilibili 无法播放? 请 <a href="https://www.bilibili.com/video/av' + vid + '" target="_blank" >点击这里</a> 跳转至B站内)';
      }
      else if (src.includes("bilibili")) {
        velem.style.paddingBottom = "58%";
        vai.style.display = "block";
        vai.innerHTML = '(Bilibili 无法播放? 请 <a href="https://www.bilibili.com/video/av' + vid +'" target="_blank" >点击这里</a> 跳转至B站内)';
      }
    }
    // youku
    else if (src_name == "youku") {
      velem.style.paddingBottom = "56.25%";
      velem.style.lineHeight = "0";
      velem.style.fontSize = "0";
      vai.style.display = "block";
      var aid = src.split("embed/")[1];
      vai.innerHTML = '(优酷无法播放? 请 <a href="http://v.youku.com/v_show/id_' + vid +'==.html" target="_blank" >点击这里</a> 跳转至优酷站内)';
    }

    else {  // youtube
      velem.style.paddingBottom = "56.25%";
      velem.style.lineHeight = "0";
      velem.style.fontSize = "0";
      if (vai) {
        vai.style.display = "none";
      }
    }


    if (src.includes("swf") && (!FlashDetect.installed)){
        $("#myVideo").remove();
        velem.style.paddingBottom = "0";
        velem.style.lineHeight = "90px";
        velem.style.textAlign = "center";
        velem.style.fontSize = "2.5em";
        velem.innerHTML = "您的浏览器不支持 Flash 播放器, <a href='https://www.bilibili.com/video/av" + vid +"' target='_blank'>点击这里</a> 查看视频";
    }
    else {
        var video = '<iframe id="myVideo" class="myvideo" width="560" height=315 src=' + src + ' frameborder="0" allowfullscreen></iframe>';
        $("#myVideo").remove();
        $("#videogfw").append(video);
    }

}
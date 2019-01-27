function getEmbeddedVideo(bilibili_src, bilibili_id, youtube_src, youtube_id, youku_src, youku_id) {
    if ((returnCitySN["cid"] != "710000") && (returnCitySN["cid"] == parseInt(Number(returnCitySN["cid"])))) {
        chooseVideo(bilibili_src, 'bilibili', bilibili_id);
    }
    else {
        chooseVideo(youtube_src, 'youtube', youtube_id);
    }


//    if (window.XMLHttpRequest)
//    {// code for IE7+, Firefox, Chrome, Opera, Safari
//        var request = new XMLHttpRequest();
//    }
//    else
//    {// code for IE6, IE5
//        var request = new ActiveXObject("Microsoft.XMLHTTP");
//    }
//    request.open('GET', '//ip-api.com/xml');
//    request.onreadystatechange = function() {
//      if (request.readyState == 4 && request.status == 200) {
//        var xmlDoc = request.responseXML;
//        var root = xmlDoc.documentElement;
//        var element = root.getElementsByTagName("countryCode");
//        var country = element[0].firstChild.nodeValue;
//        if (country == "CN"){
//          // alert('china');
//          chooseVideo(bilibili_src, 'bilibili', bilibili_id);
//        }
//        else {
//          // alert('overseas');
//          chooseVideo(youtube_src, 'youtube', youtube_id);
//          }
//
//      }
//    }
//    request.send(null);

}

function chooseVideo(src, src_name, vid)
// this function is not in here!!!!! find it in base.html
{
    var velem = document.getElementById('videogfw');
    var vai = document.getElementById("video-alrt-info");

    // bilibili
    if (src_name == "bilibili") {
      if (vai) {
          vai.style.display = "block";
          vai.innerHTML = '(Bilibili 无法播放? 请 <a href="https://www.bilibili.com/video/av' + String(vid) +'" target="_blank" >点击这里</a> 跳转至B站内)';
      }
      if (src.includes("hdslb")) {
        velem.style.paddingBottom = "70%";
      }
      else if (src.includes("bilibili")) {
        velem.style.paddingBottom = "72.5%";
      }
    }
    // youku
    else if (src_name == "youku") {
      velem.style.paddingBottom = "56.25%";
      velem.style.lineHeight = "0";
      velem.style.fontSize = "0";
      var aid = src.split("embed/")[1];
      if (vai) {
        vai.style.display = "block";
        vai.innerHTML = '(优酷无法播放? 请 <a href="http://v.youku.com/v_show/id_' + vid +'==.html" target="_blank" >点击这里</a> 跳转至优酷站内)';
      }
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
        velem.innerHTML = "您的浏览器不支持 Flash 播放器, 请前往<a href='https://www.bilibili.com/video/av" + vid +"' target='_blank'>B站内</a>观看或切换视频源";
    }
    else {
        var video = '<iframe id="myVideo" class="myvideo" width="560" height=315 src=' + src + ' frameborder="0" allowfullscreen></iframe>';
        $("#myVideo").remove();
        $("#videogfw").append(video);
    }
}



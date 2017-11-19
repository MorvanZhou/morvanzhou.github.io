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

function chooseVideo(src)
{
    var video = '<iframe id="myVideo" class="myvideo" width="560" height="315" src=' + src + ' frameborder="0" allowfullscreen></iframe>';
    $("#myVideo").remove();
    $("#videogfw").append(video);
}
/**
 * Created by Nan on 2015/4/14.
 */
$(function () {
    "use strict";

    //任务项
    var $sqlCheck = $('#sql-check'),
        $dbCompare = $('#db-compare'),
        $configCheck = $('#config-check'),
        $pausePointCheck = $('#pause-point-check'),
        $logMonitor = $('#log-monitor'),
        $checklist = $('#checklist'),
    //进度条
        $taskProgress = $('#task-progress'),
    //test按钮
        $testButton = $('#test-button'),
        $tableCheckButton = $('#table-check');


    var sum = 0,
        complete = 0,
        $id = $('#id');

    $sqlCheck.on('click', updateProgress);
    $dbCompare.on('click', updateProgress);
    $configCheck.on('click', updateProgress);
    $pausePointCheck.on('click', updateProgress);
    $logMonitor.on('click', updateProgress);
    $checklist.on('click', updateProgress);

    $testButton.on('click', showResult);
    $tableCheckButton.on('click', showTableCheck);

    var arrayObj = new Array();
    arrayObj.push($sqlCheck);
    arrayObj.push($dbCompare);
    arrayObj.push($configCheck);
    arrayObj.push($pausePointCheck);
    arrayObj.push($logMonitor);
    arrayObj.push($checklist);
    //alert($sqlCheck.attr("unchecked"));
    // alert($sqlCheck.attr('checked'));

    //updateProgress();
    init();
    updateProgress()

    function updateProgress(){
        //alert(arrayObj.length);
        sum = arrayObj.length;
        complete = 0;
        //遍历任务，计算已经完成的任务数量
        $.each(arrayObj, function(n, value){
            if (hasComplete(value) ){
                complete += 1;
            }
        });
        //计算任务完成度 更新进度条
        var percent = complete/sum * 100 + '%';
        $taskProgress.find('.progress-bar').width(percent);
    }

    function init() {
        //initItems();
    }

    function setItem(item, status){
        var item_temp;
        if(item.hasClass('switch')){
            if(item.has('.switch-on').length == 1){
                item_temp = item.find('switch-on switch-animate');
                item_temp.removeClass("switch-on");
                item_temp.addClass("switch-off switch-animate")
            }
            else if(item.has('.switch-off').length == 1){
                item_temp = item.find('switch-off switch-animate');
                item_temp.removeClass("switch-off");
                item_temp.addClass("switch-on switch-animate")
            }
        }
    }

    function hasComplete(item){
        if(item.hasClass('switch')){
            if(item.has('.switch-on').length == 1){
                return 1;
            }
            return 0;
        }
    }

    function showResult(){
        var res = "id=" + $id.text() + "&";
        //alert($id.text())
        $.each(arrayObj, function(n, value){
            //res += hasComplete(value) + " ";
            res += value.attr("id") + "=" + hasComplete(value) + "&";
        });
        //alert(res);
        $.ajax({
            type:"POST",
            url:"/test_ajax/",
            data: res + "csrfmiddlewaretoken="+ getCookie('csrftoken'),
            cache: false
            //success: function(result){
            //    alert("relegou");
            //    if (result == 1){
            //        alert("succeed");
            //    }
            //    else{
            //        alert("false");
            //    }
            //}
        });
    }

    function getCookie(name) {
        var cookieValue = null;
        if (document.cookie && document.cookie != '') {
            var cookies = document.cookie.split(';');
            for (var i = 0; i < cookies.length; i++) {
                var cookie = jQuery.trim(cookies[i]);
                if (cookie.substring(0, name.length + 1) == (name + '=')) {
                    cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                    break;
                }
            }
        }
        return cookieValue;
    }

    function showTableCheck(){
        //alert("lalal");
        var url = "/table_check?id=" + $id.text();
        var tableCheck = window.open(url,"info","width=270,height=300,left=800,top=300")
    }
});
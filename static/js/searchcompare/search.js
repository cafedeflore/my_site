var key = $("#keyword").val();

function search_by_keyword(keyword){
    var left = $("#baidu_iframe");
    var right = $("#sogou_iframe");

    var left_url = "https://www.baidu.com/s?wd=" + keyword;
    var right_url = "http://www.sogou.com/web?query=" + keyword;

    left[0]['src'] = left_url;
    right[0]['src'] = right_url;
}

function search_click(){
    var kw = $("#keyword");
    keyword = kw;
    search_by_keyword(kw.val());
}

function set_up(){
    //$("#keyword").val("ddd");
    var $button = $("#search_button");
    var $baidu_button = $("#baidu_button");
    var $sogou_button = $("#sogou_button");
    $button.on("click", search_click);
}

function likethis(choice){
    var data = {};
    data['keyword'] = $("#keyword").val();
    data['choice'] = choice;
    console.log(data);
    $.ajax({
        type: "POST",
        url: "/searchcompare/",
        data: data,
        success: function (data, status) {
            $("#commit_success_windows").fadeIn("normal").delay(1000).fadeOut();
        }
    });
}

window.onload = set_up;
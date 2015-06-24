function trim(str) { //删除左右两端的空格
    return str.replace(/(^\s*)|(\s*$)/g, "");
}

function show_details(id) {
    var $detail_win = $("#detailwin");
    getdetail(id);
    setpCenter($detail_win);
    $detail_win.fadeIn("slow");
    $detail_win.focus();
}

function setpCenter(pName) {

    var top = ($(window).height() - $(pName).height()) / 4;
    var left = ($(window).width() - $(pName).width()) / 2;
    var scrollTop = $(document).scrollTop();
    var scrollLeft = $(document).scrollLeft();
    $(pName).css({position: 'absolute', 'top': top + scrollTop, left: left + scrollLeft});
}

function close_detail() {
    $("#detailwin").fadeOut();
}

function init_data(data) {
    //var task_data = $.parseJSON(data);

    $("#id").find('td')[1].innerText = data['id'];

    var env_map = {'0': '大内测', '1': 'test for test', '2': '线上'};

    $("#env").find('td')[1].innerText = env_map[data['env']];
    $("#condition").find('td')[1].innerText = data['condition'];
    $("#details").find('td')[1].innerText = data['details'];
    $("#comment").find('td')[1].innerText = data['comment'];
}

function getdetail(id) {

    if (id != "") {
        $.ajax({
            type: "GET",
            url: "/dealtask/"+ id + "/",
            data: {id: id},
            async: false,
            success: function (data, status) {
                init_data(data)
            }
        });
    }

}
function set_up() {
    $("#detailwin").on('blur', close_detail);
}


function get_button_html_by_data(data){
    var id = data['id'];
    var content = "";
    content += "<button class=\"btn btn-sm btn-warning\" type=\"submit\" onclick=\"window.location.href='/dealtask/showpage?id="+id+"'\">修改</button>";
    content += "<button class=\"btn btn-sm btn-info\" type=\"submit\" onclick='show_details(" +id+ ")'>查看详情</button>";
    return content;
    //if data['is_resolved']
}

var deal_with_list = function deal_with_list(data, status){
    var $task_table = $("#task_table tbody");
    var newRow = "<tr><td>新行第一列</td><td>新行第二列</td><td>新行第三列</td><td>新行第四列</td><td>新行第五列</td></tr>";
    //$("#task_table tbody tr").(newRow);
    var item = ['id', 'env', 'condition', 'proposer', 'details', 'is_solved'];
    var env_map = {'0':'大内测', '1':'test for test', '2':'线上'};
    var solve_status = {'0':"未完成", '1':"完成"};
    if (status == 'success'){
        for (var i=0; i< data.length; ++i) {
            task = data[i];
            task['env'] = env_map[task['env']];
            task['is_solved'] = solve_status[task['is_solved']];
            newRow = "<tr>";
            for(var j = 0; j < item.length; ++j){
                newRow += "<td>" + task[item[j]] + "</td>";
            }

            //add the buttons
            newRow += "<td>" + get_button_html_by_data(task) + "</td>";

            newRow += "</tr>";
            console.log(data.length);
            console.log(task);
            $task_table.append(newRow);
        }
    }
    //console.log(status == 'success');
};

function load_task_list(){
    $.get('/dealtask/', deal_with_list);
    //$.ajax({
    //        type: "GET",
    //        url: "dealtask/",
    //        data: {},
    //        success: function (data, status) {
    //            init_data(data)
    //        }
    //});
}

window.onload = function () {
    set_up();
    load_task_list();
}

function trim(str) { //删除左右两端的空格
    return str.replace(/(^\s*)|(\s*$)/g, "");
}


function proposer_check() {
//alert("sb")
    var name = document.getElementsByName("proposer")[0]
    name.value = trim(name.value);
    var name_error = document.getElementsByName("proposer_error")[0]
    if (name.value.length == 0) {
        name_error.innerHTML = "<font color='red'>非法</font>";
        return false;
    }
    name_error.innerHTML = "";
    return true;

}

function system_check() {
    var name = document.getElementsByName("system")[0]
    if (name.value.length == 0) {
        document.getElementsByName("system_error")[0].innerHTML = "<font color='red'>非法</font>";
        return false;
    }
    document.getElementsByName("system_error")[0].innerHTML = "";
    return true;
}

function summit_task() {
//alert(proposer_check())
//return false;
    if ((proposer_check() && system_check()) != false) {
        var $id = $("input[name='id']");
        console.log($id.val());
        if ($id.val() != "") {
            $.ajax({
                type: "POST",
                url: ("/dealtask/" + $id.val() + "/"),
                data: $("#task_form").serialize(),
                async: false,
                success: function (data, status) {
                    //console.log("status");
                    window.location.href = '/dealtask/list/';
                }
            });
        } else {
            $.ajax({
                type: "POST",
                url: ("/dealtask/"),
                data: $("#task_form").serialize(),
                async: false,
                success: function (data, status) {
                    //console.log("status");
                    window.location.href = '/dealtask/list/';
                }
            });
        }
    }
    window.location.href = '/dealtask/list/';
    //} else {
    //    return false;
    //}
}

function init_data(data) {
    //console.log(data);

    $("#env").find('input').each(function (index, item) {
        if (item['value'] == data['env']) {
            item.setAttribute('checked', 'checked');
        }
        else {
            item.removeAttribute('checked');
        }
    });

    $("#proposer").val(data['proposer']);
    $("#system").val(data['system']);
    $("#details").val(data['details']);
    $("#condition").val(data['condition']);

//proposer
//alert(id);
}

function lalala() {

    var $id = $("input[name='id']");
    if ($id.val() != "") {
        $.ajax({
            type: "GET",
            url: "/dealtask/" + $id.val(),
            data: {},
            success: function (data, status) {
                init_data(data);
                //alert(status)
            }
        });
    }
    else {

    }

}
window.onload = lalala;


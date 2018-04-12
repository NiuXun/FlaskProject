type_select = function () {
    var selected = document.getElementById('type');
    if (selected.value == "服务器") {
        var result = document.getElementById('select_device_name');
    }else if (selected.value == "网络设备") {
        alert('这是网络设备');
    } else {
        alert('这是存储设备');
    }
};
jQuery(document).ready(function () {
    console.log('加载增加字段配置表单JS完毕');
    //  select2 Dom
    const scopeDom = jQuery('select#id_scope');
    const customDom = jQuery('input#id_is_custom');
    //  获取值的Dom
    const typeDom = jQuery('div.form-row.field-message_type');
    const valueDom = jQuery('div.form-row.field-value');

    //  初始化
    if (scopeDom.val() == '1') {
        typeDom.hide();
    } else {
        typeDom.show();
    }
    if (!customDom.prop("checked")) {
        valueDom.hide();
    } else {
        valueDom.show();
    }
    //  绑定字段类型修改form
    scopeDom.on('select2:select', e => {
        let data = e.params.data;
        console.log('字段类型更改', data);
        //  根据字段类型,隐藏多个值的提交
        if (data.id == '1') {
            typeDom.fadeOut(500);
        } else {
            typeDom.fadeIn(500);
        }
    })
    customDom.on('change', e => {
        var checkbox = e.target;
        console.log('字段类型更改', checkbox);
        //  根据字段类型,隐藏多个值的提交
        if (!checkbox.checked) {
            valueDom.fadeOut(500);
        } else {
            valueDom.fadeIn(500);
        }
    })
});
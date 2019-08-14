jQuery(document).ready(function () {
    console.log('加载增加字段配置表单JS完毕');

    //  select2 Dom
    const dictTypeDom = jQuery('select#id_type');
    //  获取多项字典值的页面link
    const dictMultiValFormPageLinkDom = jQuery('div#content-main ul.changeform-tabs li:nth(1)');
    //  获取单项字典值的Dom
    const dictSimpleDom = jQuery('div.form-row.field-dict_value');

    //  初始化
    if (dictTypeDom.val() == '1') {
        dictSimpleDom.fadeIn(500);
        dictMultiValFormPageLinkDom.fadeOut(500)
    } else {
        dictSimpleDom.fadeOut(500);
        dictMultiValFormPageLinkDom.fadeIn(500)
    }

    //  绑定字段类型修改form
    dictTypeDom.on('select2:select', e => {
        let data = e.params.data;
        console.log('字段类型更改', data);
        //  根据字段类型,隐藏多个值的提交
        if (data.id == 2) {
            dictSimpleDom.fadeOut(500);
            dictMultiValFormPageLinkDom.fadeIn(500)
        } else {
            dictSimpleDom.fadeIn(500);
            dictMultiValFormPageLinkDom.fadeOut(500)
        }
    })

});
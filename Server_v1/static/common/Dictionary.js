(function ($) {
    'use strict';
    var Dictionary = {
        test: function () {
            Dictionary.getAllDictionaryAjax(function (response) {
                var dropList = [];
                response.data[0].values.map(item => {
                    dropList.push({value: item.value, title: item.title})
                });
                Dictionary.pushDictionaryToSelectId('#id_type', dropList)
            })
        },
        getAllDictionaryAjax: function (callback) {
            return $.ajax('/ajax/dict/get_all_dict', {
                success: function (response) {
                    !!!callback || callback(response)
                }
            })
        },
        getDictionaryByCodeAjax: function (code_main, code_sub) {
            $.ajax('/ajax/dict/get_dict').success(response => {

            })
        },
        pushDictionaryToSelectId: function (selectId, data) {
            // 数据写入选择框
            if (data.length > 0) {
                // js 插值
                $('select' + selectId).children('option').remove();　　//删除下拉框下的选项
                for (var i = 0; i < data.length; i++) {
                    $('select' + selectId).append('<option value="' + data[i].value + '">' + data[i].title + '</option>')  // 依次增加选项
                }
            }
        }
    };
    window.Dictionary = Dictionary;
})(django.jQuery);
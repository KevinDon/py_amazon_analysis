jQuery(document).ready(function () {
    // 表单页显示隐藏相关输入内容
    if (!! jQuery('#cronjobmodel_form #id_type').val()){

        displayTimesInput(jQuery('#cronjobmodel_form #id_type').val())

        jQuery('#cronjobmodel_form #id_type').change(function(e){
            displayTimesInput(this.value)
        })
    }

    function displayTimesInput(type){
        if(type == 1){
            jQuery('.field-yr.field-hr').hide()
            jQuery('.field-mo.field-mi').hide()
            jQuery('.field-dy.field-se').hide()
            jQuery('.field-wk.field-dy_of_week').hide()
//            jQuery('.field-end_date').hide()
        }else if(type == 2){
            jQuery('.field-yr.field-hr').show()
            jQuery('.field-mo.field-mi').show()
            jQuery('.field-dy.field-se').show()
            jQuery('.field-wk.field-dy_of_week').show()
//            jQuery('.field-end_date').show()
        }
    }

});
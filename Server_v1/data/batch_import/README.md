### batch_import 数据批量导入运行说明

`运行目录`
batch_import 数据批量导入功能主要依赖于Django项目中的models实现ManyToMany关系数据的导入
运行脚本的目录需要在Django根目录中运行

`运行文件`
运行文件以csv与py脚本一对一存在,csv文件以batch为前缀,py脚本以import为前缀

`运行记录`
运行中打印成功执行的内容,运行结束后出现失败的次数并询问是否打印失败的记录

`失败记录`
失败的记录以log文件保存在脚本同级目录下,失败文件统一为failed.log(注意多次执行会覆盖)

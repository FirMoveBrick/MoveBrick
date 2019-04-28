phpstorm的cmd指令

    php think make:model index/User（通过命令行方式创建模型——一定要在文件根目录下创建）

    
模型的CURD操作
    
    CURD既数据的增删改查。在TP中提供的模型基类有以下方法
        增（add、addAll）
        删（delete）
        改（save）
        查（find[取出一条数据，返回一维数组]、select[取出多条数据，返回二 维数组]）   
    连贯方式
        where(),
        field(想要输出的字段),
        alias(指定具体表的别名),
        order,（指定具体某字段的排序方式）
        limit（限制具体的条数） 
    
    
    
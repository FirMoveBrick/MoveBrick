phpstorm的cmd指令

    php think make:model index/User（通过命令行方式创建模型——一定要在文件根目录下创建）
    SndVol 打开音量调节器
    
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
连表查询
    
    join方法指定具体的连表查询条件（连接方式，连接哪张数据表，连接字段）
    
TP使用原生查询

    1.Query：专门针对查询操作（select类型的SQL语句）。返回具体结果集
    2.Execute：专门针对写入操作（添加，修改，删除）使用。返回具体的受影响的行数
    使用方法  模型对象->Query/Execute($sql);
    
    
    
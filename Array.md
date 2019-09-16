## PHP数组常用方法
### 一维数组
### 多维数组
- array_column(array,column_key,index_key)
    > 返回值：返回一个数组，数组的值为输入数组中某个单一列的值
    
    | 参数     |  描述   |
    |       ---|  :---    |
    | array | 必需。指定要使用的多维数组（记录集）。|
    | column_key | 必需。需要返回值的列。可以是索引数组的列的整数索引，或者是关联数组的列的字符串键值。该参数也可以是 NULL，此时将返回整个数组（配合index_key 参数来重置数组键的时候，非常管用）。 |
    | index_key | 可选。作为返回数组的索引/键的列。|
    ```php
    $data1 = [
                ['route_dy_id'=>12345611,'describes'=>'假假按揭','create_time'=>1345234532],
                ['route_dy_id'=>123456,'describes'=>'假假法人三个人','create_time'=>1345234545],
            ];
    $arr = array_column($data1,'route_dy_id');
    ```

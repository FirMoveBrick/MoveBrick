## phpstorm的cmd指令
- php think make:model index/User
> （通过命令行方式创建模型——一定要在文件根目录下创建）
- `SndVol` 打开音量调节器

-----
 
## 模型的CURD操作
> CURD既数据的增删改查。在TP中提供的模型基类有以下方法
- 增（add、addAll）
- 删（delete）
- 改（save）     
- 查（find[取出一条数据，返回一维数组]、select[取出多条数据，返回二 维数组]）   
> 连贯方式
- where(),
- field(想要输出的字段),
- alias(指定具体表的别名),
- order,（指定具体某字段的排序方式）
- limit（限制具体的条数） 
> 连表查询
- join方法指定具体的连表查询条件（连接方式，连接哪张数据表，连接字段）
    
> TP使用原生查询
- Query：专门针对查询操作（select类型的SQL语句）。返回具体结果集
- Execute：专门针对写入操作（添加，修改，删除）使用。返回具体的受影响的行数
  >使用方法  模型对象->Query/Execute($sql);
 
---
   
## TP5模型关联
    
####1. 一对一关联： HAS_ONE	以及相对的	BELONGS_TO 
* hasOne方法有5个参数，依次分别是：
    > hasOne('关联模型名','关联外键','主键','别名定义','join类型')
* 关联操作都是基于（第一）模型的话,（第二）模型中并不需要定义关联方法
belongsTo 方法和 hasOne 一样，也有5个参数：
    > belongsTo('关联模型名','关联外键','关联模型主键','别名定义','join类型')
            
* 模型关联方法 
    ```php
    //	定义关联方法,在Model下定义
    public function profile()
    {
        //用户HASONE档案关联
        return $this->hasOne('Profile');
    }
    public function user()
    {								
        //档案BELONGSTO关联操作都基于profile方法时，直接使用
        return $this->belongsTo('User');				
    } 
    ```
1. 关联添加： 
2. 关联查询： 一对一的关联查询很简单，直接把关联对象当成属性来用即可
    >使用预载入查询来提高查询性能，对于一对一关联来说，只需要进行一次查 询即可获取关联对象数据。get方法使用第二个参数（关联模型方法名）就表示进行关联预载入查询    
    `$user	=	UserModel::get($id,'profile');`
3. 关联更新：
4. 关联删除：     
        
####2.一对多关联：HAS_MANY	以及相对的	BELONGS_TO 
    
* hasMany 的参数如下：
    > hasMany('关联模型名','关联外键','关联模型主键','别名定义')
    ```php
    public function books()
    {
        return $this->hasMany('Book');
    }
    ```        
        
              
1. 关联添加： 也可以批量增加数据
2. 关联查询： 可以直接调用模型的属性获取全部关联数据
    ```php
    public function read()
    {
       $user = UserModel::get(1);
       // 获取状态为1的关联数据
       $books = $user->books()->where('status',1)->select();
       dump($books);
       // 获取作者写的某本书
       $book = $user->books()->getByTitle('ThinkPHP5快速入门');
       dump($book);
    }
    ```     
3. 关联更新：
    ```php
    public function update($id)
    {
    $user = UserModel::get($id);
    $book = $user->books()->getByTitle('ThinkPHP5开发手册');
    $book->title = 'ThinkPHP5快速入门';
    $book->save();
    }
    ```

    
4. 关联删除：
    ```php
    //删除部分关联数据：
    $book = $user->books()->getByTitle('ThinkPHP5开发手册');
    $book->delete();
    //删除所有的关联数据：
    if($user->delete()){
    // 删除所有的关联数据
    $user->books()->delete();
    }
    ```
    
####3. 多对多关联：BELONGS_TO_MANY
    
## 模型输出

1. 输出数组: toArray 方法把模型对象输出为数组。
    > 模型对象->方法
    `$user->toArray()`
   
2. 隐藏属性:hidden方法在输出的时候隐藏某些属性  
    > //模型名->方法（[字段名称，字段名称，***]）
        
    `$user->hidden(['create_time','update_time'])->toArray()`
3. 指定属性:visible方法指定一些属性输出
    > 模型名->方法（[字段名称，字段名称，***]）
        
    `$user->visible(['id','nickname','email'])->toArray()`
4. 追加属性
    > 如果读取器定义了一些非数据库字段的读取，例如：
    ```php
    <?php
        namespace app\index\model;
        use think\Model;
        class User extends Model
        {
            // status修改器
            protected function getUserStatusAttr($value)
            {
            $status = [-1 => '删除', 0 => '禁用', 1 => '正常', 2 => '待审核'];
            return $status[$value];
            }
<<<<<<< HEAD
            
        
    三、多对多关联：BELONGS_TO_MANY
=======
        }
    ```
    >如果需要输出（字段名称） 属性数据的话，可以使用append 方法
    
    `$user->append(['user_status'])->toArray()`
5. 输出json:对于API 开发而言，经常需要返回JSON 格式的数据    
     > //模型名->方法（）
     
     `$user->toJson()`
         
* 模型输出例子：
    ```php
    // 读取用户数据并输出数组
    public function read($id = '')
    {
    //获取指定ID属性
    $user = UserModel::get($id);
    //输出数组
    dump($user->toArray());
    //隐藏属性
    dump($user->hidden(['create_time','update_time'])->toArray());
    //指定属性
    dump($user->visible(['id','nickname','email'])->toArray());
    //输出json
    echo $user->toJson();
    ```
    
>>>>>>> 98a409581aeae4aafe176784112c9a87aa048a56

    
        
        
    
    
    
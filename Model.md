## phpstorm的cmd指令
- php think make:model index/User
    > （通过命令行方式创建模型——一定要在文件根目录下创建）
- `SndVol` 打开音量调节器
- show create table well_set
    > 直接生成创建好表的SQL语句

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
    
- 一个用户会有多个角色，同时一个角色也会包含多个用户，这就是一个典型的多对多关联
- 多对多关联通常一定会有一个中间表，也称为枢纽表，所以需要创建一个用户角色的中间表
    > belongsToMany 的参数如下
    
    `belongsToMany('关联模型名','中间表名称','关联外键','关联模型主键','别名定义')`
    
    > 给模型添加多对多关联方法定义
    ```php
    // 定义多对多关联
    public function roles()
    {
    // 用户 BELONGS_TO_MANY 角色
    return $this->belongsToMany('Role', 'think_access');
    }
    ```
    > 对于枢纽表并不需要创建模型类，在多对多关联关系中，并不需要直接操作枢纽表。
    
1. 关联新增
    > 新增用户角色 并自动写入枢纽表
    
    `$user->roles()->save(['name' => 'editor', 'title' => '编辑']);`
    > 批量新增
       
    ```php
    $user->roles()->saveAll([
    ['name' => 'leader', 'title' => '领导'],
    ['name' => 'admin', 'title' => '管理员'],
    ]);
    ```
    > 由于该角色已经存在了，所以只需要使用attach 方法增加枢纽表的关联数据：
    
    `$user->roles()->attach($role);`
2. 关联删除
    > 使用detach 方法删除关联的枢纽表数据，但不会删除关联模型数据
    
    `$user->roles()->detach($role);`
    > 删除枢纽表的同时删除关联模型
    
    `$user->roles()->detach($role,true);`
3.关联查询  

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
        class User extends Model
        {
            // status修改器
            protected function getUserStatusAttr($value)
            {
            $status = [-1 => '删除', 0 => '禁用', 1 => '正常', 2 => '待审核'];
            return $status[$value];
            }
        }
    ```
   
   >如果需要输出（字段名称） 属性数据的话，可以使用append 方法
   
        `$user->append(['user_status'])->toArray()`
    
5. 输出json:对于API 开发而言，经常需要返回JSON 格式的数据    
     > //模型名->方法（）
     
     `$user->toJson()`
         
- 模型输出例子：
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
    
---

## 读取器和修改器
#### 读取器
- 读取器方法的命名规范是：
    > get + 属性名的驼峰命名+ Attr
- 给模型添加读取器的定义方法,读取器方法用于读取User模型的birthday属性的值，该方法会在读取birthday属性值的时候自动执行。
    ```php
    class User extends Model
    {
        // birthday读取器
        protected function getBirthdayAttr($birthday)
        {
            return date('Y-m-d', $birthday);
        }
    }
    ```
- 读取器方法使用了第二个参数，表示传入所有的属性数据
#### 修改器
- 修改器方法的命名规范是：
    > set + 属性名的驼峰命名+ Attr
- 给模型添加读取器的定义方法
    ```php
      // birthday修改器
      protected function setBirthdayAttr($value)
      {
          return strtotime($value);
      }
    ```
---
    
## 类型转换和自动完成
#### 类型转换

| ThinkPHP5.0 支持的转换类型包括： | 类型 |
| --------                 | :---:|
|   integer         | 整型 |
|  float | 浮点型|
|  boolean | 布尔型|
|  array | 数组|
|  json | JSON类型|
|  object | 对象|
|  datetime | 日期时间 |
|  timestamp | 时间戳（整形）|
|  serialize | 序列化 |
> 对于简单的数据格式转换之类的处理，设置类型转换比定义修改器和读取器更加方便。
- User 模型类中添加定义

    ```php
    class User extends Model
    {
      protected $dateFormat = 'Y/m/d';
      protected $type = [
      // 设置birthday为时间戳类型（整型）
      'birthday' => 'timestamp',
      ];
    }
    ```
    > 对于timestamp 和datetime 类型，如果不设置模型的dateFormat 属性，默认的日期显示格式为：
      Y-m-d H:i:s

#### 自动完成






    
        
        
    
    
    
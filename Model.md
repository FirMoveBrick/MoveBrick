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
连表查询
    
    join方法指定具体的连表查询条件（连接方式，连接哪张数据表，连接字段）
    
TP使用原生查询

    1.Query：专门针对查询操作（select类型的SQL语句）。返回具体结果集
    2.Execute：专门针对写入操作（添加，修改，删除）使用。返回具体的受影响的行数
    使用方法  模型对象->Query/Execute($sql);
    
TP5模型关联
    
    一、一对一关联： HAS_ONE	以及相对的	BELONGS_TO 
       hasOne方法有5个参数，依次分别是：
            hasOne('关联模型名','关联外键','主键','别名定义','join类型')
       如果你的关联操作都是基于 （第一） 模型的话， （第二） 模型中并不需要定义关联方法
       belongsTo 方法和 hasOne 一样，也有5个参数：
            belongsTo('关联模型名','关联外键','关联模型主键','别名定义','join类型')
            
       模型关联方法 
        //	定义关联方法,在Model下定义
        public	function	profile()
        {
        //	用户HAS	ONE档案关联
        return	$this->hasOne('Profile');
        }
        
        public	function	user()
        {								
        //	档案	BELONGS	TO	关联操作都基于profile方法时，直接使用
        return	$this->belongsTo('User');				
        } 
        
        关联添加： 
        关联查询： 一对一的关联查询很简单，直接把关联对象当成属性来用即可
        使用预载入查询来提高查询性能，对于一对一关联来说，只需要进行一次查 询即可获取关联对象数据
            	$user	=	UserModel::get($id,'**profile**');
            	//    get方法使用第二个参数（关联模型方法名）就表示进行关联预载入查询。
        关联更新：
        关联删除：     
        
        

    二、一对多关联：HAS_MANY	以及相对的	BELONGS_TO 
    
        hasMany 的参数如下：
        hasMany('关联模型名','关联外键','关联模型主键','别名定义')
        
        public function books()
            {
                return $this->hasMany('Book');
            }
        
    三、多对多关联：BELONGS_TO_MANY

    
        
        
    
    
    
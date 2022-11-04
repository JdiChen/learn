# learn

1.什么是封装

隐藏对象的属性和实现细节，仅对外公开接口，控制在程序中属性的读取和修改的访问级别。
封装途径
封装就是将抽象得到的数据和行为（或功能）相结合，形成一个有机的整体，也就是将数据与操作数据的源代码进行有机的结合，形成“类”，其中数据和函数都是类的成员。
封装的目的
增强安全性和简化编程，使用者不必了解具体的实现细节，而只是要通过外部接口，以特定的访问权限来使用类的成员。

2.为什么要使用封装
我们先来看一下未封装前的代码写法
3.写完运行后,提问不会这些怎么办-带出课程 python unittest部分
4.提出问题,
环境变更
协议变更
增加安全
5.怎么封装呢?
带出api object模式  将接口封装成一个整体,使得接口细节与业务流程相隔离
实现步骤
1.新建一个api对象类
2.从用例中找到公共变量作为类的属性
3.提取用例中的接口作为类的方法

6写封装APIOBJECT模式代码 写完后运行

带出要更换requeste框架的问题
7.继续封装BASEAPI  写一下封装步骤 运行

8.运行后,提出有什么可以继续优化?
配置文件,封装断言,封装工具,log等  带出课程
完成

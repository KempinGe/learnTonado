
use TORNADO;
create table tb_user_info(
    ui_user_id bigint unsigned auto_increment comment '用户ID',
    ui_user_name varchar(64) not null comment '用户名',
    ui_password varchar(128) not null comment '密码',
    ui_age int unsigned null comment '年龄',
    ui_gender tinyint  default 0  comment '性别',
    ui_phone char(11) not null comment '手机号码',
    ui_avatar varchar(128) null comment '头像',
    ui_isdel tinyint not null default 0 comment '是否已经注销',
    ui_craete_time datetime not null  default current_timestamp comment '注册时间',
    ui_update_time datetime not null  default current_timestamp on update current_timestamp comment '更新user的时间',
    primary key (ui_user_id),
    unique (ui_phone)
) engine=InnoDB default charset=utf8 comment '用户信息表';

create table tb_house_info(
    hi_house_id bigint unsigned auto_increment comment '房屋ID',
    hi_house_name varchar(64) not null comment '房屋名称',
    hi_house_use_id bigint unsigned not null comment '房东的ID',
    hi_house_price int unsigned not null comment '房屋价格',
    hi_house_address varchar(256) not null comment '房屋地址',
    hi_create_time datetime not null default current_timestamp comment '创建时间',
    hi_update_time datetime not null default current_timestamp on update current_timestamp comment '更新时间',
    primary key (hi_house_id),
    constraint foreign key (hi_house_use_id) references tb_user_info(ui_user_id)

)engine=InnoDB default charset=utf8 comment '房屋信息表';

create table tb_house_image(
    hi_img_id bigint unsigned  auto_increment comment '图片ID',
    hi_house_id bigint unsigned not null comment '图片所属房屋ID',
    hi_imag_url varchar(128) not null comment '图片链接',
    hi_create_time datetime not null default current_timestamp comment '创建时间',
    hi_update_time datetime not null default current_timestamp on update current_timestamp comment '更新时间',
    primary key (hi_img_id),
    constraint foreign key (hi_house_id) references tb_house_info(hi_house_id)

)engine=InnoDB default charset=utf8 comment '房屋图片表';

#unique 有保证字段唯一性 及 可为这个字段建立索引
#可以用show create table  ***** 来显示创建某张表时候的sql语句
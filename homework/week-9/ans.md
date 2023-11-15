# week9

## 9-3 
创建表
    
    CREATE TABLE `week_9`.`user` (
    `id` INT NOT NULL,
    `name` VARCHAR(45) NULL,
    `sex` VARCHAR(45) NULL,
    `age` INT NULL,
    `phone` INT NULL,
    PRIMARY KEY (`id`)
    );


插入数据
    
    INSERT INTO `week_9`.`user` (`id`, `name`, `sex`, `age`, `phone`) VALUES ('1', '张三', '男', '14', '223456');
    INSERT INTO `week_9`.`user` (`id`, `name`, `sex`, `age`, `phone`) VALUES ('2', '李四', '女', '18', '123452');
    INSERT INTO `week_9`.`user` (`id`, `name`, `sex`, `age`, `phone`) VALUES ('3', '王五', '男', '22', '124632');
    INSERT INTO `week_9`.`user` (`id`, `name`, `sex`, `age`, `phone`) VALUES ('4', '顾六', '女', '25', '125445');
    INSERT INTO `week_9`.`user` (`id`, `name`, `sex`, `age`, `phone`) VALUES ('5', '吴七', '男', '57', '342312');

## 9-4
查询年龄在20-30之内的
    
    SELECT *
    FROM user
    WHERE age between 20 and 30;

## 9-5
删除名字包含张的用户
    
    DELETE FROM user WHERE  name like '%张%';

## 9-6
计算平均年龄
    
    SELECT AVG(age) FROM user;

## 9-7
查询年龄在20-30，名字包含张，并按照年龄从大到小排
    
    SELECT *
    FROM user
    WHERE age between 20 and 30 and name like '%张%'
    order by age desc;

## 9-8
新建两张表
    
    CREATE TABLE `week_9`.`team` (
    `id` INT NOT NULL,
    `teamName` VARCHAR(45) NULL,
    PRIMARY KEY (`id`)
    );
    
    CREATE TABLE `week_9`.`score` (
    `id` INT NOT NULL,
    `teamid` INT NULL,
    `userid` INT NULL,
    `score` INT NULL,
    PRIMARY KEY (`id`)
    FOREIGN KEY (teamid) REFERENCES team(id)
    FOREIGN KEY (userid) REFERENCES user(id)
    );

## 9-9
查询ECNU的队伍中年龄小于20的用户
    
    SELECT user.*
    FROM user
    JOIN score ON user.id = score.userid
    JOIN team ON team.id = score.teamid
    WHERE team.teamName = 'ECNU' AND user.age < 20;

## 9-10
写出SQL语句,计算teamNameweiECNU的总分(假设score存在NULL值,NULL值默认为0加入计算)

    SELECT team.teamName, COALESCE(SUM(score.score), 0) AS totalScore
    FROM team
    LEFT JOIN score ON team.id = score.teamid
    WHERE team.teamName = 'ECNU'
    GROUP BY team.teamName;



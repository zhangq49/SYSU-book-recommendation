insert into book(name, imgUrl, isbn, author, press, doubanPoint, doubanRatesum,
bookDescription, authorDescription, sysuLibUrl, relevantBooks) values
('解忧杂货店', 'https://img1.doubanio.com/lpic/s27284878.jpg', '9787544270878',
'(日)东野圭吾', '南海出版公司', 8.6, 120000, 
'现代人内心流失的东西，这家杂货店能帮你找回——僻静的街道旁有一家杂货店，只要写下烦恼...',
'东野圭吾日本著名作家。1985年，《放学后..',
'http://202.116.64.108:8991/F/-?func=find-b&find_code=WRD&request=%E8%A7%A3%E5%BF%A7%E6%9D%82%E8%B4%A7%E5%BA%97&local_base=ZSU01',
'2,4'),

('嫌疑人X的献身', 'https://img3.doubanio.com/lpic/s4055190.jpg', '9787544245555',
'（日）东野圭吾 ', '南海出版公司', 9.0, 280000,
'百年一遇的数学天才石神，每', '东野圭吾，日本著名作家。1',
'http://202.116.64.108:8991/F/GV5VM4U9QA4B1PT9KXHEK5RBTLAXL51YU7MARECAY377NK5KJ3-21736?func=full-set-set&set_number=000604&set_entry=000002&format=999',
'1,3'),
('解忧杂货店3', 'https://img1.doubanio.com/lpic/s27284878.jpg', '9787544270878',
'(日)东野圭吾', '南海出版公司', 8.6, 270000, 
'现代人内心流失的东西，这家杂货店能帮你找回——僻静的街道旁有一家杂货店，只要写下烦恼...',
'东野圭吾日本著名作家。1985年，《放学后..',
'http://202.116.64.108:8991/F/-?func=find-b&find_code=WRD&request=%E8%A7%A3%E5%BF%A7%E6%9D%82%E8%B4%A7%E5%BA%97&local_base=ZSU01',
'2,4'),

('嫌疑人X的献身4', 'https://img3.doubanio.com/lpic/s4055190.jpg', '9787544245555',
'（日）东野圭吾 ', '南海出版公司', 9.0, 290000,
'百年一遇的数学天才石神，每', '东野圭吾，日本著名作家。1',
'http://202.116.64.108:8991/F/GV5VM4U9QA4B1PT9KXHEK5RBTLAXL51YU7MARECAY377NK5KJ3-21736?func=full-set-set&set_number=000604&set_entry=000002&format=999',
'1,3'),
('解忧杂货店5', 'https://img1.doubanio.com/lpic/s27284878.jpg', '9787544270878',
'(日)东野圭吾', '南海出版公司', 8.6, 110000, 
'现代人内心流失的东西，这家杂货店能帮你找回——僻静的街道旁有一家杂货店，只要写下烦恼...',
'东野圭吾日本著名作家。1985年，《放学后..',
'http://202.116.64.108:8991/F/-?func=find-b&find_code=WRD&request=%E8%A7%A3%E5%BF%A7%E6%9D%82%E8%B4%A7%E5%BA%97&local_base=ZSU01',
'2,4');


insert into user(token, recBooks) values
('olduser', '1,4'),
('newuser', NULL);

insert into bookLabel(name, useCount)
    values ('dygw', 3), ('label2', 1), ('label3', 2);

insert into labelOfBook(bookUid, bookLabelUid) 
    values(1, 1),         (1, 3),
          (2, 1), (2, 2), (2, 3),
          (3, 1);
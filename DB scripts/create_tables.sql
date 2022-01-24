create table label (
  class varchar(50) primary key not null,
  count int
  );
  
create table split (
  dataset varchar(10),
  class varchar(50),
  count int,
  foreign key (class)
    references label (class)
  );
  
create table image (
  image_name varchar(50) not null,
  image_location varchar(75) not null,
  class varchar(50),
  vehicle char(1) check (vehicle in ('Y','N')),
  non_vehicle char(1) check (non_vehicle in ('Y','N')),
  primary key (image_location, image_name),
  foreign key (class) 
	references label (class)
  );
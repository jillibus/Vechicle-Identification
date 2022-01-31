create table label (
	index serial primary key not null,
	class_name varchar(100)
);

create table image (
	index serial primary key not null,
	bbox_x1 int,
	bbox_y1 int,
	bbox_x2 int,
	bbox_y2 int,
	class	int,
	fname	varchar(150),
	foreign key (class)
		references label (index)
);

-- SEQUENCE: 
-- SEQUENCES for index columns

CREATE SEQUENCE image_index_seq;
ALTER SEQUENCE image_index_seq RESTART WITH 8144;

CREATE SEQUENCE label_index_seq;
ALTER SEQUENCE label_index_seq RESTART WITH 196;


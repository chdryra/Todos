--liquibase formatted sql

--changeset rizwan.choudrey:1
--comment: adding api calls table
create table api_calls (
    id serial primary key not null,
    api varchar(320) not null,
    dt timestamp not null DEFAULT NOW()
)
--rollback DROP TABLE api_calls;




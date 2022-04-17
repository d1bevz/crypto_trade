create schema public_data;
create schema market_data;

create user airflow with encrypted password 'airflow';

grant all privileges on database crypto_trade to airflow;


create table public_data.instruments_spot (
                                               inst_type text,
                                               inst_id text,
                                               uly text,
                                               category int8,
                                               base_ccy text,
                                               quote_ccy text,
                                               settle_ccy text,
                                               ct_val float8,
                                               ct_mult float8,
                                               ct_val_ccy text,
                                               opt_type text,
                                               stk float8,
                                               list_time timestamp,
                                               exp_time timestamp,
                                               lever float8,
                                               tick_sz float8,
                                               lot_sz float8,
                                               min_sz float8,
                                               ct_type text,
                                               alias text,
                                               state text,
                                               updated timestamp default now()
);

create table public_data.instruments_swap (
                                              inst_type text,
                                              inst_id text,
                                              uly text,
                                              category int8,
                                              base_ccy text,
                                              quote_ccy text,
                                              settle_ccy text,
                                              ct_val float8,
                                              ct_mult float8,
                                              ct_val_ccy text,
                                              opt_type text,
                                              stk float8,
                                              list_time timestamp,
                                              exp_time timestamp,
                                              lever float8,
                                              tick_sz float8,
                                              lot_sz float8,
                                              min_sz float8,
                                              ct_type text,
                                              alias text,
                                              state text,
                                              updated timestamp default now()
);

create table public_data.instruments_margin (
                                              inst_type text,
                                              inst_id text,
                                              uly text,
                                              category int8,
                                              base_ccy text,
                                              quote_ccy text,
                                              settle_ccy text,
                                              ct_val float8,
                                              ct_mult float8,
                                              ct_val_ccy text,
                                              opt_type text,
                                              stk float8,
                                              list_time timestamp,
                                              exp_time timestamp,
                                              lever float8,
                                              tick_sz float8,
                                              lot_sz float8,
                                              min_sz float8,
                                              ct_type text,
                                              alias text,
                                              state text,
                                              updated timestamp default now()
);

create view public_data.instruments as
select *
from public_data.instruments_spot
union all
select *
from public_data.instruments_swap
union all
select *
from public_data.instruments_margin;

create table crypto_trade.market_data.candlesticks_raw (
                                                           ticker text,
                                                           ts bigint,
                                                           open float8,
                                                           high float8,
                                                           low float8,
                                                           close float8,
                                                           vol float8,
                                                           vol_ccy float8,
                                                           updated timestamp default now()
);

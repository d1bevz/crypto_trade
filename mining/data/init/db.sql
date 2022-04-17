create schema crypto_trade;

create user punk with encrypted password 'decentralized';

grant all privileges on schema crypto_trade to punk;

create table crypto_trade.candlesticks_raw (
                                               ticker text,
                                               ts bigint,
                                               open float8,
                                               high float8,
                                               low float8,
                                               close float8,
                                               vol float8,
                                               volCcy float8,
                                               updated timestamp default now()
);

create table crypto_trade.instruments_spot (
                                               instType text,
                                               instId text,
                                               uly text,
                                               category int8,
                                               baseCcy text,
                                               quoteCcy text,
                                               settleCcy text,
                                               ctVal float8,
                                               ctMult float8,
                                               ctValCcy text,
                                               optType text,
                                               stk float8,
                                               listTime timestamp,
                                               expTime timestamp,
                                               lever float8,
                                               tickSz float8,
                                               lotSz float8,
                                               minSz float8,
                                               ctType text,
                                               alias text,
                                               state text,
                                               updated timestamp default now()
);

create table crypto_trade.instruments_swap (
                                                 instType text,
                                                 instId text,
                                                 uly text,
                                                 category int8,
                                                 baseCcy text,
                                                 quoteCcy text,
                                                 settleCcy text,
                                                 ctVal float8,
                                                 ctMult float8,
                                                 ctValCcy text,
                                                 optType text,
                                                 stk float8,
                                                 listTime timestamp,
                                                 expTime timestamp,
                                                 lever float8,
                                                 tickSz float8,
                                                 lotSz float8,
                                                 minSz float8,
                                                 ctType text,
                                                 alias text,
                                                 state text,
                                                 updated timestamp default now()
);

create table crypto_trade.instruments_margin (
                                                 instType text,
                                                 instId text,
                                                 uly text,
                                                 category int8,
                                                 baseCcy text,
                                                 quoteCcy text,
                                                 settleCcy text,
                                                 ctVal float8,
                                                 ctMult float8,
                                                 ctValCcy text,
                                                 optType text,
                                                 stk float8,
                                                 listTime timestamp,
                                                 expTime timestamp,
                                                 lever float8,
                                                 tickSz float8,
                                                 lotSz float8,
                                                 minSz float8,
                                                 ctType text,
                                                 alias text,
                                                 state text,
                                                 updated timestamp default now()
);

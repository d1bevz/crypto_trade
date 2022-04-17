create schema crypto_trade;

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
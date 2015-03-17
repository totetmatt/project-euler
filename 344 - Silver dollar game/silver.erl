-module(silver).
-export([test/1]).

test([s|_]) ->  1;
test([o|X]) ->  test(X).
test() ->  0.
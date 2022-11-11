taas: tail-as-a-service

(I know, but tac-pipe-grep-pipe-head-as-a-service just doesn't have the same ring to it.)

Assumptions I made, given the spec and what I know about logs:
 * "number of entries" means "newline-separated lines", in this context
 * number of entries applies *after* filtering, rather than before. I think this is the less-surprising behavior choice, but the spec doesn't spell it out
 * simple substring filtering is sufficient
 * "reasonably performant" means something like "in the same ballpark as grep"
 * we have no realistic way to know the encoding, so we'll be byte-oriented

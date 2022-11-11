# taas: tail-as-a-service

'taas' exposes the most recent lines from files in /var/log via a simple HTTP server on port 8080.

## usage

Requirements: python 3.10+ (expected to work with 3.8+, but below 3.10 is untested)

To run the server:

`./taas`

To get the contents of /var/log/syslog via the server:

`curl localhost:8080/syslog`

### parameters

#### l: maximum number of lines to return

To return only the 10 most recent lines from /var/log/syslog:

`curl localhost:8080/syslog?l=10`

#### search_string: only return lines containing the given string

To return the most recent lines from /var/log/syslog containing the string 'foo':

`curl localhost:8080/syslog?search_string=foo`

## assumptions

I made a few assumptions, given the spec and what I know about logs:
 * "number of entries" means "newline-separated lines", in this context
 * number of entries applies *after* filtering, rather than before. I think this is the less-surprising behavior choice, but the spec doesn't spell it out
 * simple substring filtering is sufficient
 * "reasonably performant" means something like "in the same ballpark as grep"
 * we have no realistic way to know the encodings of log files, so we'll be byte-oriented

## design

I think the "service" side of the design is pretty self-evident.

In terms of interacting with logs efficiently and nicely:
 * use of `mmap` lets me code as though I have the whole file in memory, leveraging the OS' page cache to ensure that the parts of the file I'm actively working on are available, without blowing up real memory usage.
 * use of python generators/iterators lets me code as though I have the whole list of reversed log lines in memory, leveraging iterator semantics to lazily load only the lines I actually access.
 * I made some effort to only *copy* the logfile bytes out of page cache once (when they're written to the output), but I'd need to check a few things to be 100% certain.
